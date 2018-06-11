import os
from xml.etree import ElementTree
import arpa



def main():

    converter = arpa.ARPAtoIPA()

    file_name = 'corrected_CMU.xml'     # name of data file
    full_path = os.path.abspath(os.path.join("data", file_name))     # get full path of data file todo: learn exactly what this does
    dom = ElementTree.parse(full_path)      # parse the XML data
    entries = dom.findall('entry')      # extract all the data entries
    for e in entries:       # print every entry's word value
        print(converter.getIPA(e.find('corrected_only').text))

main()