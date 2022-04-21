from scipy.signal import lombscargle as lsp
from scipy.signal import spectral
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
plt.rcParams.update({'font.size': 40})
plt.rcParams["xtick.direction"] = "in"
plt.rcParams["ytick.direction"] = "in"
plt.rcParams['xtick.major.pad']='18'
plt.rcParams['ytick.major.pad']='18'
plt.rcParams["font.family"] = 'Times New Roman'


def p_gram(hjd,mag,f_min=None,f_max=None,oversample=100.0):
    '''
    A wrapper for the lomb-scargle periodogram implemented in scipy. It does
    all of the necessary normalization to make all the output power scalings
    appropriate.

    Parameters
    ----------
    hjd : array like
       Time of observations in days.
    mag : array like
       Value measured. Listed as magnitude but it could be anything.
    f_min : float, optional
       The low frequency end of search range in units of Hz (1/s). If left as
       None, the default, it will use one-over the half the length of the data
       set as the minimun frequency.
    f_max : float, optional
       The high frequency end of the search range in units of Hz (1/s). If left
       as None, the default, it will use one-over twice the minimum time
       difference between observations.
    oversample : float
       Rate at which to oversample the frequency space being searched.
       Default is 100. A higher value is fine but it will take longer to run.

    Returns
    -------
    pgm : array like
       Power associated with the frequencies searched.
    freqs : array like
       Frequencies searched over. f_min to f_max with a number of sampling
       points equal to the number of observations multiplied by the
       oversampling rate. The output frequency units are in 1/days

    Version History
    ---------------
    2016-12-05 - Start, tranfered over from p_lc
    '''

    t=np.array((hjd-np.min(hjd))*24.0*3600.0,dtype='float64')
    sort=np.argsort(t)
    t=t[sort]
    mag=np.array(mag[sort],dtype='float64')
    scaled_mag=(mag-np.mean(mag))/np.std(mag)
    if f_min == None:
        af_min=2.0*np.pi/(np.max(t)-np.min(t))/2.0
    else:
        af_min=2.0*np.pi*f_min
    if f_max == None:
        min_dt=np.min(np.abs(t-np.roll(t,1)))
        af_max=2.0*np.pi/(0.5*min_dt)
    else:
        af_max=2.0*np.pi*f_max
    afreqs=np.linspace(af_min,af_max,np.int(t.size*oversample))
    pgm=spectral.lombscargle(t,scaled_mag,afreqs)
    freqs=(afreqs/(2.0*np.pi))*3600.0*24.0

    return pgm, freqs

hjd1, mag1 = np.loadtxt('stha34_20210723_U_enslc_lco.dat', unpack=True, usecols=(0,1), dtype='f8,f8')
hjd2, mag2 = np.loadtxt('stha34_20210721_V_enslc_lco.dat', unpack=True, usecols=(0,1), dtype='f8,f8')
hjd3, mag3 = np.loadtxt('stha34_20210722_zs_enslc_lco.dat', unpack=True, usecols=(0,1), dtype='f8,f8')
pgm1, freqs1 = p_gram(hjd1, mag1, f_min=1/(30*24*3600), f_max=1/(2*24*3600), oversample=100.0)
pgm2, freqs2 = p_gram(hjd2, mag2, f_min=1/(30*24*3600), f_max=1/(2*24*3600), oversample=100.0)
pgm3, freqs3 = p_gram(hjd3, mag3, f_min=1/(30*24*3600), f_max=1/(2*24*3600), oversample=100.0)

f, ax1 = plt.subplots(1,1,figsize=(25,10))

P = 20.89
ax1.axvline(P, color='#696969', linewidth=2.5, ls='--')
ax1.plot((1/freqs1), pgm1, color='#012998', label='U', linewidth=2.5)
ax1.plot((1/freqs2), pgm2, color='#0247FE', label='V', linewidth=2.5)
ax1.plot((1/freqs3), pgm3, color='#57beff', label='Z', linewidth=2.5)

ax2 = ax1.twiny()
ax3 = ax1.twinx()
ax1.set_xlim([5,30])

ax1.yaxis.set_major_formatter(FormatStrFormatter('%.2f'))

ax1.set_ylabel("Power")
ax1.set_xlabel("Days")
for axis in [ 'bottom','left', 'top', 'right']:
    ax1.spines[axis].set_linewidth(2.5)
    ax1.tick_params(width=2.5, length=12)
ax1.minorticks_on()
ax1.tick_params(axis='both', which= 'minor', width= 2.5, length=5)

ax2.tick_params(axis='both', length=0)
ax3.tick_params(axis='both', length=0)
ax2.xaxis.set_ticklabels([])
ax3.yaxis.set_ticklabels([])


ax1.legend(fancybox=True, framealpha=1, shadow=True, loc=1)
plt.savefig('Periodogram.png', bbox_inches='tight')
