import csv

FileName = input("Name of the file: \t")
mat = []
f = open(FileName, "r")
reader = csv.reader(f)

i = 0
for row in reader:
    if i == 0:
        print(row)

    if i != 0:
        sp = (row[0].split("\t"))
        time = sp[1].split('.')
        mat.append([int(sp[0]), int(time[1])])
    i = 1

print(mat)
