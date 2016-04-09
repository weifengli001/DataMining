import csv


def csvToList(filepath):
    with open('./data/randomdata_x.csv', 'r') as f:
        reader = csv.reader(f)
        l = list(reader)
    return [float(x) for x in l[0]]

print(csvToList('./data/randomdata_x.csv'))

