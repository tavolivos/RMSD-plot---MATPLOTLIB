import subprocess
import os
import matplotlib.pyplot as plt
import numpy


time_complex, rmsd_complex = numpy.loadtxt("rmsd_complex.xvg", unpack=True)
time_CA, rmsd_CA = numpy.loadtxt("rmsd_CA.xvg", unpack=True)
time_ligand, rmsd_ligand = numpy.loadtxt("rmsd_ligand.xvg", unpack=True)

fig = plt.figure(figsize=(4.1,2))
ax = fig.add_subplot(111)
fig.subplots_adjust(bottom=0.2)

#ax.fill_between(time, rmsd, color="white", linestyle="-", alpha=0.02)
ax.plot(time_complex, rmsd_complex, color="tomato", linestyle="-", linewidth=0.7)
ax.plot(time_CA, rmsd_CA, color="grey", linestyle="-", linewidth=0.7)
ax.plot(time_ligand, rmsd_ligand, color="royalblue", linestyle="-", linewidth=0.7)
ax.set_ylim(0)

ax.set_xlabel("Time (ns)")
ax.set_ylabel(r"RMSD (nm)")
ax.set_xlim(time_complex.min(), time_complex.max())

subprocess.call ('mkdir PLOTS', shell = True)

fig.savefig("PLOTS/rmsd.png", format='png', dpi=350, transparent=True)
fig.savefig("PLOTS/rmsd.svg", format='svg', dpi=350, transparent=True)
fig.savefig("PLOTS/rmsd.pdf", format='svg', dpi=350, transparent=True)
fig.savefig("PLOTS/rmsd.eps", format='eps', dpi=350, transparent=True)
fig.savefig("PLOTS/rmsd.tif", format='tif', dpi=350, transparent=True)
