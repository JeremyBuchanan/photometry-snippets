import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
plt.rcParams.update({'font.size': 40})
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams['xtick.major.pad']='18'
plt.rcParams['ytick.major.pad']='18'
plt.rcParams["font.family"] = 'Times New Roman'

file1 = './stha34_20210723_U_enslc_lco.dat'
file2 = './stha34_20210721_V_enslc_lco.dat'
file3 = './stha34_20210722_zs_enslc_lco.dat'
days1, mags1 = np.loadtxt(file1, unpack=True, usecols=(0,1), dtype='f8,f8')
days2, mags2 = np.loadtxt(file2, unpack=True, usecols=(0,1), dtype='f8,f8')
days3, mags3 = np.loadtxt(file3, unpack=True, usecols=(0,1), dtype='f8,f8')
color1 = [[],[]]
color2 = [[],[]]
color3 = [[],[]]
threshold = 1/72
for i in range(len(days1)):
    dt1 = np.abs(days1[i] - days2)
    dt2 = np.abs(days1[i] - days3)
    match1 = (dt1 == np.min(dt1))
    match2 = (dt2 == np.min(dt2))
    dm1 = mags1[i] - mags2[match1]
    dm2 = mags1[i] - mags3[match2]
    if dt1[match1] < threshold:
        color1[0].append(dm1)
        color1[1].append(mags1[i])
    if dt2[match2] < threshold:
        color2[0].append(dm2)
        color2[1].append(mags1[i])
for i in range(len(days2)):
    dt3 = np.abs(days2[i] - days3)
    match3 = (dt3 == np.min(dt3))
    dm3 = mags2[i] - mags3[match3]
    if dt3[match3] < threshold:
        color3[0].append(dm3)
        color3[1].append(mags2[i])

f, ax1 = plt.subplots(1,1,figsize=(15,10))

ax1.arrow(-1.2, 3.25, 0.1375, 0.3875, width=0.01, color='tomato', length_includes_head=True, overhang=0.1, label='Reddening Vector')
ax1.scatter(color1[0], color1[1], color='#012998', label='U - V', s=120)
# ax1.scatter(color2[0], color2[1], color='#0247FE', label='U - Z', s=85)
# ax1.scatter(color3[0], color3[1], color='#57beff', label='V - Z', s=85)

ax2 = ax1.twiny()
ax3 = ax1.twinx()
ax1.invert_yaxis()

ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

ax1.set_ylabel("U Band")
ax1.set_xlabel("U - V")
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
# ax1.legend(fancybox=True, framealpha=1, shadow=True, loc=1)
plt.savefig('Colorplots.png', bbox_inches='tight')
