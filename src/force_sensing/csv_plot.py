#Role de ce fichier:
#Obtenir les donnees du port serie

import csv
from matplotlib import pyplot as plt

with open('force_data.csv','r') as csvfile_to_read:
    row_count = sum(1 for row in csvfile_to_read)
    print "Nombre de donnees a traiter:", row_count
csvfile_to_read.close()

x = []#range(row_count)
y = []

with open('force_data.csv','r') as csvfile_to_read:
    reader = csv.reader(csvfile_to_read,delimiter=',')
    print "Lecture des donnees..."
    for row in reader:
        x.append(row[0])
        y.append(row[1])
    print "...Donnees lues"
csvfile_to_read.close()

plt.xlabel('temps ecoule depuis 1er mesure (s)')
plt.ylabel("image de la force")
plt.plot(x,y)
plt.show()
