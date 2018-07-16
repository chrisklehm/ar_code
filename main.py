import os
from xml.etree import ElementTree
import sounds

def soundSeq(sound_seq):
    sound_str = ''
    for s in sound_seq:
        sound_str += str(s)
    return sound_str

def main():


    lex = sounds.Lexicon()

    ways_to_say_this = lex.getWord('brandy')
    for w in ways_to_say_this:
        print(soundSeq(w.sounds))



main()