import matplotlib.pyplot as plt
plt.rcParams.update({'font.size': 25})
import numpy as np
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
from matplotlib.ticker import FormatStrFormatter
plt.rcParams['xtick.major.pad']='18'
plt.rcParams['ytick.major.pad']='18'

file = open('stha34_20210721_V_enslc_lco.dat', 'r')
line = file.readline().split()
date = []
mag = []
magerr = []
while len(line)>1:
    date.append(float(line[0]))
    mag.append(float(line[1]))
    magerr.append(float(line[2]))
    line = file.readline().split()

def plot_lc():
    f, ax1 = plt.subplots(1,1,figsize=(10, 5))

    ax2 = ax1.twiny()
    ax3 = ax1.twinx()
    ax1.invert_yaxis()

    P = 20.89
    t0 = 2457681.9
    t1 = date[0]
    first_oc = (t1 - t0) / P
    for i in range(7):
        plt.axvline(t0+P*(np.int(first_oc)+i)-2457000, color='b')
    ax1.errorbar(np.array(date)-2457000, mag, magerr, fmt='o', color='k', ms=8)

    ax2.yaxis.set_ticklabels([])
    ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    ax2.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

    ax1.set_ylabel("V")
    ax1.set_xlabel("BJD - 2457000")
    for axis in [ 'bottom','left', 'top', 'right']:
        ax1.spines[axis].set_linewidth(1.5)
        ax1.tick_params(width=1.5, length=9)
    ax1.minorticks_on()
    ax1.tick_params(axis='both', which= 'minor', width= 1.5, length=3)
    ax2.xaxis.set_ticklabels([])
    ax3.yaxis.set_ticklabels([])
    ax3.minorticks_on()

    for axis in ['bottom', 'left', 'top', 'right']:
        ax2.spines[axis].set_linewidth(1.5)
        ax2.tick_params(width=1.5, length=9)
        ax3.tick_params(width=1.5, length=9)

    ax2.minorticks_on()
    ax2.xaxis.set_ticklabels([])

    ax2.tick_params(axis='both', which= 'minor', width= 1.5, length=3)
    ax3.tick_params(axis='both', which= 'minor', width= 1.5, length=3)

    ax2.xaxis.set_ticklabels([])
    ax3.set_xticks(np.linspace(ax1.get_xbound()[0], ax1.get_xbound()[1], 6))
    ax2.set_yticks(np.linspace(ax1.get_ybound()[0], ax1.get_ybound()[1], 6))
    plt.savefig('Vbandperiods')


def fold_lc():
    f, ax1 = plt.subplots(1,1,figsize=(10, 5))

    ax2 = ax1.twiny()
    ax3 = ax1.twinx()
    ax1.invert_yaxis()

    phase = (np.array(date) - t0) / P % 1
    ax1.errorbar(phase, mag, magerr, fmt='o', ms=8, color='k')
    ax1.errorbar(phase+1, mag, magerr, fmt='o', ms=8, color='k')
    ax1.set_xlim(0,1.2)

    ax2.yaxis.set_ticklabels([])
    ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    ax2.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

    ax1.set_ylabel("V")
    ax1.set_xlabel("Orbital Phase")
    for axis in [ 'bottom','left', 'top', 'right']:
        ax1.spines[axis].set_linewidth(1.5)
        ax1.tick_params(width=1.5, length=9)
    ax1.minorticks_on()
    ax1.tick_params(axis='both', which= 'minor', width= 1.5, length=3)
    ax2.xaxis.set_ticklabels([])
    ax3.yaxis.set_ticklabels([])
    ax3.minorticks_on()

    for axis in ['bottom', 'left', 'top', 'right']:
        ax2.spines[axis].set_linewidth(1.5)
        ax2.tick_params(width=1.5, length=9)
        ax3.tick_params(width=1.5, length=9)

    ax2.minorticks_on()
    ax2.xaxis.set_ticklabels([])

    ax2.tick_params(axis='both', which= 'minor', width= 1.5, length=3)
    ax3.tick_params(axis='both', which= 'minor', width= 1.5, length=3)

    ax2.xaxis.set_ticklabels([])
    ax3.set_xticks(np.linspace(ax1.get_xbound()[0], ax1.get_xbound()[1], 6))
    ax2.set_yticks(np.linspace(ax1.get_ybound()[0], ax1.get_ybound()[1], 6))
    plt.savefig('Vbandphasewrap')
