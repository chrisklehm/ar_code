import io, re, os
from xml.etree import ElementTree

def soundSeq(sound_seq):
    sound_str = ''
    for s in sound_seq:
        sound_str += str(s)
    return sound_str

class Sound(object):
    def __init__(self, feat):
        self.features = {}
        for f in feat:
            f_name = f.attrib['name']
            if (f_name == 'symbol'):
                self.features[f_name] = f.text
            else:
                self.features[f_name] = int(f.text)

    def __str__(self):
        return self.features['symbol']

    def isVowel(self):
        return self.features['cons'] == 0

    def dist(self, b):
        sum = 0
        for k in self.features.keys():
            if (k == 'symbol'):
                pass
            else:
                sum += (int(self.features[k]) - int(b.features[k])) ^ 2
        return sum ** (0.5)


class Inventory(object):
    def __init__(self):
        self.sounds = set()
        file_name = 'sounds_and_features.xml'
        full_path = os.path.abspath(os.path.join("data", file_name))
        dom = ElementTree.parse(full_path)
        all_sounds = dom.findall('sound')
        for s in all_sounds:
            new_sound = Sound(s)
            self.sounds.add(new_sound)
        cons_features = set()
        vowel_features = set()
        for s in self.sounds:
            for k in s.features.keys():
                isCons = s.features['cons']
                if (k != 'symbol') and (k not in cons_features) and (k not in vowel_features):
                    if isCons:
                        cons_features.add(k)
                    else:
                        vowel_features.add(k)

    def getSound(self, sym):
        for s in self.sounds:
            if s.features['symbol'] == sym:
                return s

    def getSoundsSuchThat(self, property, value):
        return_sounds = set()
        for s in self.sounds:
            if (property not in s.features.keys()):
                pass
            elif (s.features[property] == value):
                return_sounds.add(s)
        return return_sounds


class ARPAtoIPA(object):
    def __init__(self):
        self.arpa_to_ipa = {}
        self.arpa_to_ipa[" "] = ['space', ' ']
        self.types = set(['vowel', 'cons', 'space','diph'])
        with io.open('data/arpa_to_ipa.txt', 'r', encoding='utf8') as infile:
            for line in infile:
                line = line.strip()
                line_list = line.split()
                if line_list[0] not in self.types:
                    raise Exception('Character must be either "v" (vowel) or "c" (consonant)')
                else:
                    self.arpa_to_ipa[line_list[1]] = [line_list[0],line_list[2]]
        infile.close()

    def getARPASansStress(self, arpa):
        return re.sub('\d', '', arpa)

    def getIPA(self, arpa: str):
        arpa_sans_stress = self.getARPASansStress(arpa)
        arpa_list = arpa_sans_stress.split()
        ipa = ''
        for i in arpa_list:
            ipa += self.arpa_to_ipa[i][1]  + " "
        ipa = ipa.strip()
        return ipa

    def getARPA(self, ipa: str):
        arpa = ''
        ipa_list = ipa.split()
        for i in ipa_list:
            arpa_chr = ''
            counter = 0
            for k in self.arpa_to_ipa.keys():
                if self.arpa_to_ipa[k][1] == i:
                    counter += 1
                    arpa_chr = k
            if counter == 1:
                arpa += arpa_chr + " "
            else:
                raise Exception("This IPA character either doesn't exist in the ARPABET or is not unique in it.")
        arpa = arpa.strip()
        return arpa

class Phon_Word(object):
    def __init__(self, spelling, sounds):
        self.spelling = spelling
        self.sounds = sounds

    def __str__(self):
        ipa_str = ''
        for s in self.sounds:
            ipa_str += str(s)
        return ipa_str

    def getVowels(self):
        vowels = []
        for s in self.sounds:
            if s.isVowel():
                vowels.append(s)
        return tuple(vowels)

    def getCons(self):
        cons = []
        for s in self.sounds:
            if not s.isVowel():
                cons.append(s)
        return tuple(cons)

    def getClusters(self):
        clust_list = []
        current_cluster = []
        idx = 0
        current_isVow = self.sounds[idx].isVowel()
        previous_isVow = self.sounds[idx].isVowel()
        while (True):
            if (current_isVow == previous_isVow):
                current_cluster.append(self.sounds[idx])
                idx += 1
            else:
                clust_list.append(tuple(current_cluster))
                current_cluster = [self.sounds[idx]]
                idx += 1
            if (idx == len(self.sounds)):
                clust_list.append(tuple(current_cluster))
                break
            else:
                previous_isVow = current_isVow
                current_isVow = self.sounds[idx].isVowel()
        return tuple(clust_list)

class Lexicon(object):
    def __init__(self):
        file_name = 'corrected_CMU.xml'  # name of data file
        full_path = os.path.abspath(os.path.join("data", file_name))  # get full path of data file todo: learn exactly what this does
        dom = ElementTree.parse(full_path)  # parse the XML data
        entries = dom.findall('entry')  # extract all the data entries
        phonetic_words = {}
        self.converter = ARPAtoIPA()
        self.inventory = Inventory()
        for e in entries:
            arpa_list = e.find('corrected_only').text.split()
            sound_list = []
            pol = 0
            for s in arpa_list:
                if ('ER' in s):
                    pol = 1
            if (pol == 1):
                continue
            for c in arpa_list:
                ipa_c = self.converter.getIPA(c)
                if (self.converter.arpa_to_ipa[self.converter.getARPASansStress(c)][0] == 'diph'):
                    new_sound1 = self.inventory.getSound(ipa_c[0])
                    new_sound2 = self.inventory.getSound(ipa_c[1])
                    sound_list.append(new_sound1)
                    sound_list.append(new_sound2)
                else:
                    new_sound = self.inventory.getSound(ipa_c)
                    sound_list.append(new_sound)
            sounds = tuple(sound_list)
            new_word = Phon_Word(e.find('word').text, sounds)
            phonetic_words[int(e.find('index').text)] = new_word
        self.p_words = phonetic_words

    def getWord(self, find_str):
        found_words = []
        for w in self.p_words.values():
            if w.spelling == find_str:
                found_words.append(w)
        return found_words

    def inWord(self, wd, snd):
        in_word = False
        sound = self.inventory.getSound(snd)
        for s in wd.sounds:
            if (sound == s):
                in_word = True
        return in_word

