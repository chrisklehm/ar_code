import csv

def main():

  with open("corrected_CMU.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    counter = 0
    for line in csv_reader:
      if ('compound' in line['Excluded']):
        counter += 1
        #print(line['Word'])
    print(counter)

main()
