import matplotlib.pyplot as plt
import numpy as np
import math
import csv
import sys

filename = sys.argv[1]

with open(filename, 'r') as csv_tq:
    tq = csv.reader(csv_tq)
    avg_list = list()
    samp_std_list = list()
    cores_list = list()
    
    last_cores_seen = 0
    for row in tq:
        if row[0] == "":
            timings = row[1:]
        else:
            if last_cores_seen != float(row[0]):
                tmp_list = row[1:]
                if tmp_list[-1] == '':
                    del tmp_list[-1]
                avg_list.append(map(float, tmp_list))
                cores_list.append(float(row[0]))
                last_cores_seen = float(row[0])
            else:
                tmp_list = row[1:]
                if tmp_list[-1] == '':
                    del tmp_list[-1]
                samp_std_list.append(map(float, tmp_list))

print timings
print avg_list, samp_std_list


fig = plt.figure()
ax = fig.add_subplot(111)
x_value = [i for i in range(len(timings))]
major_ticks = np.arange(0, 4, 1)
ax.set_xticks(major_ticks)
ax.set_xticklabels(timings)
ax.set_xlim(-0.2,3.2)

ax.set_xlabel('Duration (s)')
ax.set_ylabel('Tq (s)')
ax.set_title('Tq by Cores and Duration: ' + filename.split('.')[0])
ax.grid(True)

for i in range(len(avg_list)):
    x_value_adjusted = x_value
    if (len(x_value) - len(avg_list[i])) == 1:
        del x_value_adjusted[-1]
    ax.errorbar(x_value_adjusted, avg_list[i], yerr=samp_std_list[i], label="Cores = " + str(int(cores_list[i])))

ax.legend(loc='upper left')
plt.show()
