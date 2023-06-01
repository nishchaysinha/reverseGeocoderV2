import csv

def read(filename):
    data = []
    with open(filename, mode='r') as file:
        csvreader = csv.reader(file)
        for lines in csvreader:
            data.append(lines)
    return data