import io

# sound object with id (ARPA string) and symbol (IPA string)
class Sound (object):
    def __init__(self, arpa, symbol, cons):
        self.arpa = arpa
        self.symbol = symbol
        self.cons = cons

    def __str__(self):
        return self.symbol

class Inventory (object):
    def __init__(self):
        self.sound_set = set()
        with io.open("data/arpa_to_ipa.txt", 'r', encoding='utf8') as sound_file:   # open text file containing the ARPA and IPA for each sound
            for sound in sound_file:
                sound = sound.strip()
                sound = sound.split()
                is_cons = True
                if sound[0] == "vowel":     # check whether the sound is a consonant
                    is_cons = False
                new_sound = Sound(sound[1], sound[2], is_cons)  # create new sound with arpa, ipa, and consonant values
                self.sound_set.add(new_sound)
        sound_file.close()

    def getSound(self, target):
        for s in self.sound_set:
            if s.arpa == target:
                return s
        return None
