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
        if len(w.sounds) < 6:
            pass
        elif w.isCVCVCV():
            cv_words.add(w)

    



main()