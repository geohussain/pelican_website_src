"""
Code that illustrates how the harmonic wave solution is calculated
and plotted in terms of time and distance.
"""

import numpy as np
from matplotlib import pyplot as plt
import matplotlib

matplotlib.rcParams['mathtext.fontset'] = 'cm'
matplotlib.rcParams['font.family'] = 'Times New Roman'


# function [t,vtrace]=wave_solve_c(duration,dt,R,vp)
def wave_solve_c(_dur, _dt, _r, _vp, _f):
    '''
    Function that solves the homogeneous wave equation in time domain
    '''
    time = np.arange(0, _dur + _dt, _dt)
    # angular frequency of wave
    # omega = 2 * np.pi() * _f
    delay = _r / _vp + 1

    # definition of the ricker wavelet source
    ricker_wavelet = (2 * np.pi**2 * _f**2 * (time-delay)**2 - 1) * \
        np.exp(-np.pi**2 * _f**2 * (time-delay)**2)

    # definition of the ricker wavelet differentiation
    ricker_wavelet_diff = 2 * np.pi**2 * _f**2 * \
        np.exp(-np.pi**2 * _f**2 * (-time + delay)**2) * \
        (-time + delay) * (2 * np.pi**2 * delay**2 *
                           _f**2 - 4 * np.pi**2 * delay * _f**2 * time +
                           2 * np.pi**2 * _f**2 * time**2 - 3)

    # The ricker wavelet trace for displacement
    displacement_trace = ricker_wavelet / _r**2 + \
        ricker_wavelet_diff / (_r * _vp)

    return time, displacement_trace


# p-wave velocity in m/s
V_P = 2000.0
# s-wave velocity in m/s
V_S = 1000.0
# density in g/cc
RO0 = 2.0*1e3
# shear modulus
MU0 = RO0 * V_S**2
# bulk modulus
LAMBDA0 = RO0 * V_P**2 - 2 * MU0
# normalized amplitude
A_N = 4 * np.pi * (LAMBDA0 + 2 * MU0)

# Analytical Solution transformed from Time Domain
# Receiver locations
RI = np.arange(20, 2000 + 20, 20)
# time axis for traces
TIME_AXIS = np.arange(0, 10 + 0.01, 0.01)
# frequency used in Laplace-Fourier transform
FRE = 8
SIGMA = 1

# Create data in time domain
TRACES = np.empty((TIME_AXIS.shape[0], 0), float)
# Ricker source frequency
RICKER_SRC_FRE = 10
# time step for trace
TS = 0.01
# trace duration
DUR = 10
for _x in RI:
    TA, TRACE = wave_solve_c(DUR, TS, _x, V_P, RICKER_SRC_FRE)
    TRACE = TRACE / A_N
    TRACES = np.column_stack((TRACES, TRACE))

# trace located 20 m away from the source
plt.plot(TIME_AXIS, TRACES[:, 0])
plt.title(r"Time trace for receiver with offset = $" + str(RI[0]) + "m$")
plt.xlabel(r"Time (s)")
plt.ylabel(r"Amplitude")
plt.xlim([0, 3])
plt.grid()
plt.show()

# trace located 1000 m away from the source
plt.plot(TIME_AXIS, TRACES[:, 49])
plt.title(r"Time trace for receiver with offset = $" + str(RI[49]) + "m$")
plt.xlabel(r"Time (s)")
plt.ylabel(r"Amplitude")
plt.xlim([0, 3])
plt.grid()
plt.show()

# trace located 1000 m away from the source
plt.plot(TIME_AXIS, TRACES[:, 99])
plt.title(r"Time trace for receiver with offset = $" + str(RI[99]) + "m$")
plt.xlabel(r"Time (s)")
plt.ylabel(r"Amplitude")
plt.xlim([0, 3])
plt.grid()
plt.show()
