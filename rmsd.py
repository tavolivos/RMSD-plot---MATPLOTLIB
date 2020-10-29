###################################
#  By: Gustavo E. Olivos-Ramirez  #
#      gustavo.olivos@upch.pe     #
#      Lima-Peru                  #
###################################

import subprocess
import os
import matplotlib.pyplot as plt
import numpy

font = {'family' : 'DejaVu Sans',
        'weight' : 'normal',
        'size'   : 16}
plt.rc('font', **font)

time_all, rmsd_all = numpy.loadtxt("rmsd.dat", unpack=True)
time_sbs, rmsd_sbs = numpy.loadtxt("rmsd2.dat", unpack=True)

fig = plt.figure(figsize=(8,4))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.2)

ax.plot(time_all, rmsd_all, color="tomato", linestyle="-", linewidth=0.7, label='Protein')
ax.plot(time_sbs, rmsd_sbs, color="grey", linestyle="-", linewidth=0.7, label='SBS')
ax.set_ylim(0)
ax.set_xlim(0,60000)

ax.set_xlabel("Time (ns)")
ax.set_ylabel("RMSD (Å)")
ax.legend()

labels = ['0', '100', '200', '300', '400', '500', '600']
ax.set_xticklabels(labels)

subprocess.call ('mkdir PLOTS', shell = True)

fig.savefig("PLOTS/rmsd.png", format='png', dpi=350, transparent=True)
fig.savefig("PLOTS/rmsd.svg", format='svg', dpi=350, transparent=True)
fig.savefig("PLOTS/rmsd.tif", format='tif', dpi=350, transparent=True)



