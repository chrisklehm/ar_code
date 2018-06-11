import io, re


class ARPAtoIPA(object):
    def __init__(self):
        self.arpa_to_ipa = {}
        self.arpa_to_ipa[" "] = ['space', ' ']
        self.types = set(['vowel', 'cons', 'space'])
        with io.open('data/arpa_to_ipa.txt', 'r', encoding='utf8') as infile:
            for line in infile:
                line = line.strip()
                line_list = line.split()
                if line_list[0] not in self.types:
                    raise Exception('Character must be either "v" (vowel) or "c" (consonant)')
                else:
                    self.arpa_to_ipa[line_list[1]] = [line_list[0],line_list[2]]
        infile.close()

    def getIPA(self, arpa: str):
        arpa_sans_stress = re.sub('\d', '', arpa)
        arpa_list = arpa_sans_stress.split()
        ipa = ''
        for i in arpa_list:
            ipa += self.arpa_to_ipa[i][1]  + " "
        ipa = ipa.strip()
        return ipa

    def getARPA(self, ipa: str):
        arpa = ''
        ipa_list = ipa.split()
        for i in ipa_list:
            arpa_chr = ''
            counter = 0
            for k in self.arpa_to_ipa.keys():
                if self.arpa_to_ipa[k][1] == i:
                    counter += 1
                    arpa_chr = k
            if counter == 1:
                arpa += arpa_chr + " "
            else:
                raise Exception("This IPA character either doesn't exist in the ARPABET or is not unique in it.")
        arpa = arpa.strip()
        return arpa