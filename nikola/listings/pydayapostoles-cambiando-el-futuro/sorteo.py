import csv
import random

asistentes = []

with open('asistentes-pyday-apostoles.csv', 'r') as fh:
    for l in csv.reader(fh):
        asistentes.append(l[0:2])

print len(asistentes)

random.shuffle(asistentes)
print asistentes.pop()
print asistentes.pop()