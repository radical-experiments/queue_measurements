import csv
import sys
from math import sqrt


filename_in = sys.argv[1]
filename_out = sys.argv[2]

str_split = filename_in.split('/')[-1].split('_')

cores = str_split[1].split('c')[0]
tx = str_split[2].split('m')[0]

tq = list()

fin = open(filename_in, 'rb')
for row in fin:
    tq.append(float(row.split()[-1]))
fin.close()

count = len(tq)
avg = sum(tq) / float(count)

f_square = lambda x : (x - avg)**2
samp_std = sqrt(sum(map(f_square, tq)) / float(len(tq) - 1))

fout = open(filename_out, 'a')
writer = csv.writer(fout)
writer.writerow([cores, tx, avg, samp_std, count])
fout.close()
