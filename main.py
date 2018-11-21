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




    print('P(z|o) = ', prob_of_z_given_o)
    print('The average euclidean distance between the first and last sounds of words with at least two sounds long is',
          avg_euclidean_dist_between_first__and_last_letter)



main()