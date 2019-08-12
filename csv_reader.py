import csv


def read(file, separator=','):
    ret = []
    with open(file, 'r', encoding="ISO_8859-1") as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            ret.append(row)
    csvFile.close()
    if not separator == ',':
        for line in range(len(ret)):
            ret[line] = ret[line][0].split(separator)
    return ret
