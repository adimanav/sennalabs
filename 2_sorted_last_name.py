import csv
from collections import defaultdict

class SortedLastName:
    dictionary = dict()

    def __init__(self, filename):
        with open(filename, 'rt') as f:
            data = csv.reader(f)
            for row in data:
                self.dictionary[row[1]] = row[0] + row[1]
            
    def output(self):
        keys = []
        
        for key in self.dictionary:
            keys.append(key)

        keys.sort()

        for key in keys:
            print(self.dictionary[key])

sln = SortedLastName("names.csv")
sln.output()