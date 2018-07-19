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

    num_words_containing_o = 0
    num_words_containing_z = 0
    num_words_containing_o_and_z = 0
    for word in lex.p_words.values():
        if lex.inWord(word,'z') and lex.inWord(word,'o'):
            num_words_containing_o += 1
            num_words_containing_z += 1
            num_words_containing_o_and_z += 1
        elif lex.inWord(word,'z'):
            num_words_containing_z += 1
        elif lex.inWord(word,'o'):
            num_words_containing_o += 1
        else:
            continue

    prob_of_z_given_o = num_words_containing_o_and_z / num_words_containing_o

    print('P(z|o) = ', prob_of_z_given_o)



main()