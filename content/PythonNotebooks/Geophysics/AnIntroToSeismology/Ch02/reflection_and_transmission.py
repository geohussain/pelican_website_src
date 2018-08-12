"""
Code that illustrates how the harmonic wave solution is calculated
and plotted in terms of time and distance.
"""

import numpy as np
from matplotlib import pyplot as plt
import matplotlib
from mpl_toolkits.mplot3d import Axes3D

matplotlib.rcParams['mathtext.fontset'] = 'cm'

T0 = 0      # beginning time in s
TF = 4      # ending time in s
DT = 0.01    # time step

X0 = 0      # starting distance in m
XF = 4      # ending distance in m
DX = 0.01    # distance time step in m

OMEGA = np.pi       # angular frequency in s^(-1)
k = 2 * np.pi       # wavenumber in m^(-1)
A = 100             # amplitude of the harmonic function


T = np.arange(T0, TF+DT, DT)
X = np.arange(X0, XF+DX, DX)

TT, XX = np.meshgrid(T, X)

U = A * np.cos(OMEGA * TT - k * XX)

# plot the harmonic function
FIG = plt.figure(figsize=(8, 8), dpi=100, facecolor='w', edgecolor='k')
AX = plt.gca(projection=Axes3D.name)
AX.contour3D(TT, XX, U, 80)
AX.set_xlabel(r'time (s)', fontsize=18)
AX.set_ylabel(r'distance (m)', fontsize=18)
AX.set_zlabel(r'$u(x,t)$', fontsize=18)
AX.tick_params(labelsize=14)
AX.invert_xaxis()
plt.show()


# Additional insight comes by examining u(x,t) at a point in space x0.
UX0 = A * np.cos(OMEGA * T - k * X0)
FIG2 = plt.figure(figsize=(10, 6), dpi=100, facecolor='w', edgecolor='k')
plt.plot(T, UX0)
plt.xlabel(r'time (s)', fontsize=18)
plt.ylabel(r"$u(x_0, t)$", fontsize=18)
plt.tick_params(labelsize=18)
plt.show()

# Alternatively, we can examine u(x,t) at a fixed time, t0, and plot u(x,t0)
UT0 = A * np.cos(OMEGA * T0 - k * X)
FIG3 = plt.figure(figsize=(10, 6), dpi=100, facecolor='w', edgecolor='k')
plt.plot(X, UT0)
plt.xlabel(r'distance (s)', fontsize=18)
plt.ylabel(r"$u(x, t_0)$", fontsize=18)
plt.tick_params(labelsize=18)
plt.show()
