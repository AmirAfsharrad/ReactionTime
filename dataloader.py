import csv
import numpy
from matplotlib import pyplot

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
        time = sp[1].split(':')
        mat.append([int(sp[0]), float(time[2]), int(sp[2])])
    i = 1

times_odd = []
times_norm = []
n_odd = []
n_norm = []
wrong_odd = 0
wrong_norm = 0

step = range(len(mat))
print(mat)

for j in range(len(mat)):
    if mat[j][0] == 0:
        times_norm.append(mat[j][1] * 1000)
        n_norm.append(step[j])
        wrong_norm = wrong_norm + mat[j][2]
    if mat[j][0] == 1:
        times_odd.append(mat[j][1] * 1000)
        n_odd.append(step[j])
        wrong_odd = wrong_odd + mat[j][2]

print("Wrong Response to Odd Stimuli : ", format(wrong_odd))
print("Wrong Response to Normal Stimuli :", format(wrong_norm))


bins = numpy.linspace(0, 500, 20)
pyplot.hist(times_odd, bins, alpha=0.5, label='Odd', density=1)
pyplot.hist(times_norm, bins, alpha=0.5, label='Normal', density=1)
pyplot.legend(loc='upper right')
pyplot.show()

pyplot.figure()
pyplot.plot(n_odd, times_odd)
pyplot.plot(n_norm, times_norm)
pyplot.show()

