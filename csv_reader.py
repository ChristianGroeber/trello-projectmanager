import csv


def read():
    ret = []
    with open('file.csv', 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            ret.append(row)
    csvFile.close()
    return ret
