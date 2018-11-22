import re, os, inventory
from xml.etree import ElementTree

class Phon_Word(object):
    def __init__(self, spelling, sounds):
        self.spelling = spelling
        self.sounds = sounds

    def __str__(self):
        new_str = ""
        for s in self.sounds:
            new_str += s.symbol
        return new_str

    def isCVCVCV (self):
        if not self.sounds[0].cons:     # make sure the first sound is a consonant
            return False
        if self.sounds[-1].cons:    # make sure the last sound isn't a consonant
            return False
        for i in range(1, len(self.sounds)):    # make sure the vowels and consonants alternate
            if self.sounds[i].cons == self.sounds[i-1].cons:
                return False
        return True


class Lexicon(object):
    def __init__(self):
        self.inv = inventory.Inventory()
        self.word_set = set()
        file_name = 'corrected_CMU.xml'  # name of data file
        full_path = os.path.abspath(os.path.join("data", file_name))  # get full path of data file
        dom = ElementTree.parse(full_path)  # parse the XML data
        entries = dom.findall('entry')  # extract all the data entries
        for e in entries:
            word = e.find('word').text
            arpa_list = e.find('corrected_only').text.split()   # get transcription of current word
            sound_list = []
            for a in arpa_list:
                arpa = re.sub('\d', '', a)  # remove numerals indicating stress
                new_sound = self.inv.getSound(arpa)
                sound_list.append(new_sound)
            new_word = Phon_Word(word, sound_list)
            self.word_set.add(new_word)

    def getWord(self, find_str):
        found_words = []
        for w in self.word_set:
            if w.spelling == find_str:
                found_words.append(w)
        return found_words

    def inWord(self, wd, snd):
        in_word = False
        sound = self.inv.getSound(snd)
        for s in wd.sounds:
            if (sound == s):
                in_word = True
        return in_word
