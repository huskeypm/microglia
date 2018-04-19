# Function for integreating ODE and displaying results
import scipy.integrate
from scipy.integrate import odeint
import numpy as np
import math
from math import exp
from scipy.interpolate import spline

import numpy.random as npr
# normal random distribution
from numpy.random import normal as nprn
# uniform random distribution
from numpy.random import uniform as npru

### Markov State Modeling based on rP2X4 in HEK293T
#1. Based on "Allosteric Regulation of the P2X4 Recepter Channel Pore Dilation" by Zemkova, Khadra, Rokic, Tvrdonova, Sherman, and Stojikovic.
#2. 13 states

# p2x4 ODE generator
def fp2x4(y):
    D1, D2, D3, D4, C1, C2, C3, C4, Q1, Q2, Q3, Q4, N, A = y

    # Constants for Markov State Model
    k = np.array([0.4, 600000, 0.5, 500000, 0.6, 400000]) # k1[1/s],k2[1/(M*s)],k3[1/s],k4[1/(M*s)],k5[1/s],k6[1/(M*s)]
    L = np.array([0.01, 0.04, 0.5])                       # L1[1/s], L2[1/s], L3[1/s]
    H = np.array([0.013, 0.35, 1.4, 0.001])               # H1[1/s], H2[1/s], H3[1/s], H4[1/s]

    al = 100 # unitless
    be = 1.4e-6 # [M]

    # IVM condition pre-set
    IVM = 0
    KIVM = IVM/(be + IVM)
    G = 1 + al*KIVM
    F = 1 - KIVM

    # 13 ODEs for Markov State Model ########################################################
    dD1dt = k[0]*D2 - (3*k[1]*A + H[0])*D1
    dD2dt = 3*k[1]*A*D1 + 2*k[2]*D3 + H[1]*C2 - (k[0] + 2*k[3]*A)*D2
    dD3dt = 2*k[3]*A*D2 + 3*k[4]*D4 + H[1]*Q1 - (2*k[2] + k[5]*A)*D3
    dD4dt = k[5]*A*D3 + H[1]*Q2 - (3*k[4] + H[2])*D4

    dC1dt = H[0]*D1 + k[0]*G*C2 + L[0]*C4 + H[3]*N - 3*k[1]*A*F*C1
    dC2dt = 3*k[1]*A*F*C1 + 2*k[2]*G*Q1 - (k[0]*G + 2*k[3]*A*F + H[1])*C2
    dC3dt = 3*k[1]*A*F*C4 + 2*k[0]*G*Q4 - (k[0]*G + 2*k[1]*A*F)*C3
    dC4dt = k[0]*G*C3 - (L[0] + 3*k[1]*A*F)*C4

    dQ1dt = 2*k[3]*A*F*C2 + 3*k[4]*G*Q2 - (2*k[2]*G + k[5]*A*F + H[1])*Q1
    dQ2dt = k[5]*A*F*Q1 + L[1]*Q3 - (3*k[4]*G + L[2]*(1-G) + H[1])*Q2
    dQ3dt = k[1]*A*F*Q4 + L[2]*(1-G)*Q2 - (3*k[0]*G + L[1])*Q3
    dQ4dt = 2*k[1]*A*F*C3 + 3*k[0]*G*Q3 - (2*k[0]*G + k[1]*A*F)*Q4

    dNdt = H[2]*D4 - H[3]*N
    #########################################################################################

    dydt = [dD1dt, dD2dt, dD3dt, dD4dt, dC1dt, dC2dt, dC3dt, dC4dt, dQ1dt, dQ2dt, dQ3dt, dQ4dt, dNdt]

    return dydt

### Conversion IP2X4 to JP2X4
# Ca Influx via p2x4 channel
def fJp2x4(y):
    Q1, Q2, Q3, Q4 = y

    ## Electrochemistry properties for the estimation of inward current transient
    g12 = 3e-8    # [S]
    g34 = 8e-8    # [S]
    V = -0.06     # [V] -> the holding potential (used in NCX calculation as well)
    E12 = 0       # [V]
    E34 = 0       # [V]
    CaA = 0.0824  # fraction of current contributed by Calcium transport

    ## Current generated from the P2X4 gating
    I = (g12*(Q1 + Q2)*(V - E12) + g34*(Q3 + Q4)*(V - E34))*CaA # in [A]

    ## Conversion from Current [A] to influx rate [M/s]
    ### Constants
    F = 96485.33289   # Faraday constant in [C/mol]
    ## Dimensions of HEK293 and Microglia
    rHEK = 6.5e-6 # radius of HEK293 cell body in [meter]
    rMiG = 2.6e-6 # radius of microglia cell body in [meter]
    AHEK = 4*3.141592654*(rHEK)**2 # surface area of HEK293 cell in [sq. meter]
    AMiG = 4*3.141592654*(rMiG)**2 # surface area of microglia in [sq. meter]
    VHEK = 1000*(4/3)*3.141592654*(rHEK)**3 # volume of HEK293 cell in [L]
    VMiG = 1000*(4/3)*3.141592654*(rMiG)**3 # volume of microglia in [L]
    VcytHEK = VHEK*0.65 # [L] The volume of cytoplasm in HEK293 cells -> This fraction was taken from Shannon-Bers paper
    VcytMiG = VMiG*0.40 # [L] The volume of cytoplasm in microglia -> This fraction was estimated from the figure (Liaury).
    VERMiG = VMiG*0.035 # [L] The volume of ER lumen in microglia -> This fraction was taken from Shannon-Bers paper
    expF = 0.1          # Scale factor for over-expression of P2X4 on HEK293

    ## Influx via P2X4 Channels
    ### Conversion from the dimesion of HEK to the dimension of Microglia
    J = -(I/VcytMiG)*(AMiG/AHEK)/(2*F)*expF # [mol/(L*s) = M/s]

    return J    
