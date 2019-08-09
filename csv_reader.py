import csv


def read(file):
    ret = []
    with open(file, 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            ret.append(row)
    csvFile.close()
    return ret
