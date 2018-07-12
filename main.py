import os
from xml.etree import ElementTree
import sounds



def main():

    inventory = sounds.Inventory()
    lex = sounds.Lexicon()

    ways_to_say_sharpshooter = lex.getTranscription('read')
    print('You can say "read" in the following ways:')
    for w in ways_to_say_sharpshooter:
        print(w.sounds)


main()