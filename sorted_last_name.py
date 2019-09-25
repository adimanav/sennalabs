import csv

class SortedLastName:
    dictionary = dict()

    def __init__(self, filename):
        with open(filename, 'rt') as f:
            data = csv.reader(f)
            for row in data:
                if (row[0] != "FirstName" and row[1] != "LastName"):
                    self.dictionary[row[1]] = row[0].strip() + " " + row[1].strip()
            
    def output(self):
        keys = []
        
        for key in self.dictionary:
            keys.append(key)

        keys.sort()

        result = []
        for key in keys:
            result.insert(len(result), self.dictionary[key])
        return result

if __name__ == '__main__':
    sln = SortedLastName("names.csv")
    result = sln.output()
    print(result)