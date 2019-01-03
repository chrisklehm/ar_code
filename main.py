import lexicon

def soundSeq(sound_seq):
    sound_str = ''
    for s in sound_seq:
        sound_str += str(s)
    return sound_str

def main():

    lex = lexicon.Lexicon()

    # find CVCVCV words
    cv_words = set()
    for w in lex.word_set:
        if len(w.sounds) < 4:       # make sure the word has at least 6 sounds
            pass
        elif w.isCVCVCV():          # find all the CVCVCV words
            cv_words.add(w)

    identC12 = set()
    identC23 = set()
    identC123 = set()
    identV12 = set()
    identV23 = set()
    identV123 = set()
    for w in cv_words:
        if w.sounds[0] == w.sounds[2]:      # check if the first two consonants are the same
            identC12.add(w)
            if (len(w.sounds) > 5):
                if w.sounds[2] == w.sounds[4]:  # check if the second two consonants are also the same
                    identC123.add(w)
        elif (len(w.sounds) > 5):
            if w.sounds[2] == w.sounds[4]:    # check if the second two consonants are the same
                identC23.add(w)
        if w.sounds[1] == w.sounds[3]:      # check if the first two vowels are the same
            identV12.add(w)
            if (len(w.sounds) > 5):
                if w.sounds[3] == w.sounds[5]:  # check if the second two vowels are also the same
                    identV123.add(w)
        elif (len(w.sounds) > 5):
            if w.sounds[3] == w.sounds[5]:    # check if the second two vowels are the same
                identV23.add(w)

    a = identC23 & identV23                 # resulting words with matching consonants and vowels
    b = identC23 - a                        # resulting words with matching consonants but not vowels
    c = identV23 - a                        # resulting words with matching vowels but not consonants
    q = (cv_words - identC23) - identV23    # resulting words that neither math consonants nor vowels
    print("total number of words: ", len(cv_words))
    print("resulting words with matching consonants and vowels: ",len(a))
    print("resulting words with matching consonants but not vowels: ", len(b))
    print("resulting words with matching vowels but not consonants: ", len(c))
    print("resulting words that neither math consonants nor vowels: ", len(q))
    #c = identC23 & identV23
    #d = identC23 - c

    #num_non_identC12 = len(cv_words) - len(identC12)






main()