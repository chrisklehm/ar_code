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
    euclid_dist = 0
    num_words = 1
    for word in lex.p_words.values():
        if len(word.sounds) > 1:
            num_words += 1
            euclid_dist += word.sounds[0].dist(word.sounds[-1])
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
    avg_euclidean_dist_between_first__and_last_letter = euclid_dist / num_words


    print('P(z|o) = ', prob_of_z_given_o)
    print('The average euclidean distance between the first and last sounds of words with at least two sounds long is',
          avg_euclidean_dist_between_first__and_last_letter)



main()