Created:  07-16-2018
This program is intended to take English phonetic lexicon data and look for generalizations. 

The DATA folder contains the following files:
  - arpa_to_ipa.txt
    This file contains three collumns: sound type, ARPA symbol, and IPA symbol. I created it from the ARPA wikipedia page.    
  - corrected_CMU.csv, corrected_CMU.xls, corrected_CMU_with_xml.csv, corrected_CMU.xml
    All the 'corrected_CMU' files are various versions of the corrected CMU transcription database. The application onl references the xml data.   
  - sounds_and_features.xml
    This file contains sounds with their corresponding feature values. The feature set was chosen because it came in a nifty table from my undergraduate phonology class. All feature values except 'symbol', which is the sound's IPA symbol as a string, are binary valued.
    
The sounds.py file contains the following classes:
  - Sound
    This class stores a dictionary of feature name/value pairs. The isVowel method returns a boolean for whether the sound is a vowel or not. The dist method returns the euclidean distance between two sounds 
  - Inventory
  - ARPAtoIPA
  - Phon_Word
  - Lexicon
