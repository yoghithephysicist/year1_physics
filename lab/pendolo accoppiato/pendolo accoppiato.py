import numpy as np
import pandas as pd
import scipy.stats as stats
import matplotlib.pyplot as plt

# Lenghts
# Distance between arms 34 cm +/- 0.1 cm
# Arm lenght 54.2 cm +/- 0.1 cm
# Oscillation starting point parallel to ground 5cm (mode normals)
# Oscillation starting point parallel to ground 10cm (battimenti)
# 6.55 cm +/ 0.05 cm

peso_tot_1 = 470 # grams
sigma_1 = 5 # grams

peso_tot_2 = 465 # grams
sigma_2 = 5 # grams

def moment_inerzia(L, f):  # velocita tangenziale (L) e frequenza (f)
    return (L / (2 * numpy.pi * f ))

def pulsazione_angolare(m, g, l, I):  # massa, accel grav, lunghezza braccio, momento di inerzia
    return numpy.sqrt((m * g * l) / (I))

mis_pend_disac_a = []
mis_pend_disac_b = []
array_buff = []
with open("C:/Users/Marco/Desktop/pendolo-accopiato-contro-fase.txt", "r") as file:
    for line in file:
        if "#" not in line:
            array_buff.append(float(line.split("\t")[0]))
            array_buff.append(float(line.split("\t")[1]))
            mis_pend_disac_a.append(array_buff)
            array_buff = []
            array_buff.append(float(line.split("\t")[2]))
            array_buff.append(float(line.split("\t")[3]))
            mis_pend_disac_b.append(array_buff)
            array_buff = []

print(mis_pend_disac_a)
#print(mis_pend_disac_b)

mis_pend_disac_a_time = []
for time in mis_pend_disac_a:
    mis_pend_disac_a_time.append(time[0])
mis_pend_disac_a_mov = []
for mov in mis_pend_disac_a:
    mis_pend_disac_a_mov.append(mov[1])

mis_pend_disac_b_time = []
for time in mis_pend_disac_b:
    mis_pend_disac_b_time.append(time[0])
mis_pend_disac_b_mov = []
for mov in mis_pend_disac_b:
    mis_pend_disac_b_mov.append(mov[1])

xdata = np.asarray(mis_pend_disac_a_time)
ydata = np.asarray(mis_pend_disac_a_mov)
plt.plot(xdata, ydata, '-o')
xdata2 = np.asarray(mis_pend_disac_b_time)
ydata2 = np.asarray(mis_pend_disac_b_mov)
plt.plot(xdata2, ydata2, '-o')
plt.show()

#input()
