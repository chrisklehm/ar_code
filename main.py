import lexicon

def soundSeq(sound_seq):
    sound_str = ''
    for s in sound_seq:
        sound_str += str(s)
    return sound_str

def main():

    lex = lexicon.Lexicon()
    for w in lex.word_set:
        if lex.inWord(w, "M"):
            print(w)





main()