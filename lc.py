import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import FormatStrFormatter
plt.rcParams.update({'font.size': 80})
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams['xtick.major.pad']='18'
plt.rcParams['ytick.major.pad']='18'
plt.rcParams["font.family"] = 'Times New Roman'


file = open("stha34_20210721_V_enslc_lco.dat", "r")
line = file.readline().split()
date = []
mag = []
magerr = []
while len(line)>1:
    date.append(float(line[0]))
    mag.append(float(line[1]))
    magerr.append(float(line[2]))
    line = file.readline().split()

file = open("stha34_20210722_zs_enslc_lco.dat", "r")
line = file.readline().split()
date1 = []
mag1 = []
magerr1 = []
while len(line)>1:
    date1.append(float(line[0]))
    mag1.append(float(line[1]))
    magerr1.append(float(line[2]))
    line = file.readline().split()

file = open("stha34_20210723_U_enslc_lco.dat", "r")
line = file.readline().split()
date2 = []
mag2 = []
magerr2 = []
while len(line)>1:
    date2.append(float(line[0]))
    mag2.append(float(line[1]))
    magerr2.append(float(line[2]))
    line = file.readline().split()

f, ax1 = plt.subplots(1,1,figsize=(40,20))

ax2 = ax1.twiny()
ax3 = ax1.twinx()
ax1.set_ylim(bottom=-4)
ax1.invert_yaxis()

P = 20.89
t0 = 2457681.9
t1 = date[0]
first_oc = (t1 - t0) / P
for i in range(7):
    ax1.axvline(t0+P*(np.int(first_oc)+i)-2457000, color='#696969', linewidth=5, ls='--')
ax1.errorbar(np.array(date2)-2457000, mag2-np.median(mag2)-2, magerr2, fmt='o', color='#012998', ms=24, label='U')
ax1.errorbar(np.array(date)-2457000, mag-np.median(mag)-1, magerr, fmt='o', color='#0247FE', ms=24, label='V')
ax1.errorbar(np.array(date1)-2457000, mag1-np.median(mag1), magerr1, fmt='o', color='#57beff', ms=24, label='Z')

ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

ax1.set_ylabel("Magnitude")
ax1.set_xlabel("BJD - 2457000")
for axis in [ 'bottom','left', 'top', 'right']:
    ax1.spines[axis].set_linewidth(2.5)
    ax1.tick_params(width=2.5, length=12)
ax1.minorticks_on()
ax1.tick_params(axis='both', which= 'minor', width= 2.5, length=5)

ax2.tick_params(axis='both', length=0)
ax3.tick_params(axis='both', length=0)
ax2.xaxis.set_ticklabels([])
ax3.yaxis.set_ticklabels([])

# ax3.set_xticks(np.linspace(ax1.get_xbound()[0], ax1.get_xbound()[1], 7))
# ax2.set_yticks(np.linspace(ax1.get_ybound()[0], ax1.get_ybound()[1], 6))
ax1.legend(fancybox=True, framealpha=1, shadow=True, loc=1, prop={'size': 60})
plt.savefig('periods.png', bbox_inches='tight')

#===========================================================================

f, ax1 = plt.subplots(1,1,figsize=(40,20))

ax2 = ax1.twiny()
ax3 = ax1.twinx()
ax1.set_ylim(bottom=-4)
ax1.invert_yaxis()

phase = (np.array(date) - t0) / P % 1
phase1 = (np.array(date1) - t0) / P % 1
phase2 = (np.array(date2) - t0) / P % 1
ax1.errorbar(phase2-1, mag2-np.median(mag2)-2, magerr2, fmt='o', color='#012998', ms=24)
ax1.errorbar(phase2, mag2-np.median(mag2)-2, magerr2, fmt='o', color='#012998', ms=24, label='U')
ax1.errorbar(phase2+1, mag2-np.median(mag2)-2, magerr2, fmt='o', color='#012998', ms=24)
ax1.errorbar(phase-1, mag-np.median(mag)-1, magerr, fmt='o', color='#0247FE', ms=24)
ax1.errorbar(phase, mag-np.median(mag)-1, magerr, fmt='o', color='#0247FE', ms=24, label='V')
ax1.errorbar(phase+1, mag-np.median(mag)-1, magerr, fmt='o', color='#0247FE', ms=24)
ax1.errorbar(phase1-1, mag1-np.median(mag1), magerr1, fmt='o', color='#57beff', ms=24)
ax1.errorbar(phase1, mag1-np.median(mag1), magerr1, fmt='o', color='#57beff', ms=24, label='Z')
ax1.errorbar(phase1+1, mag1-np.median(mag1), magerr1, fmt='o', color='#57beff', ms=24)
ax1.set_xlim(0,1.2)

ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

ax1.set_ylabel("Magnitude")
ax1.set_xlabel("Orbital Phase")
for axis in [ 'bottom','left', 'top', 'right']:
    ax1.spines[axis].set_linewidth(2.5)
    ax1.tick_params(width=2.5, length=12)
ax1.minorticks_on()
ax1.tick_params(axis='both', which= 'minor', width= 2.5, length=5)

ax2.tick_params(axis='both', length=0)
ax3.tick_params(axis='both', length=0)
ax2.xaxis.set_ticklabels([])
ax3.yaxis.set_ticklabels([])

# ax3.set_xticks(np.linspace(ax1.get_xbound()[0], ax1.get_xbound()[1], 7))
# ax2.set_yticks(np.linspace(ax1.get_ybound()[0], ax1.get_ybound()[1], 6))
ax1.legend(fancybox=True, framealpha=1, shadow=True, loc=1, prop={'size': 58})
plt.savefig('phasefold.png', bbox_inches='tight')
