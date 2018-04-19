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

def fp2x7(y):
    D1, D2, D3, D4, C1, C2, C3, C4, Q1, Q2, Q3, Q4, A = y

    # Rate constants  ###################################
    k1 = 0.3    # [1/s]
    k2 = 70000  # [1/(M*s)]
    k3 = 5.4    # [1/s]
    k4 = 100000  # [1/(M*s)]
    k5 = 1.58   # [1/s]
    k6 = 7000   # [1/(M*s)]

    L1 = 0.0001 # [1/s]
    L2 = 0.004  # [1/s]
    L3 = 0.5    # [1/s]

    h1 = 0.001  # [1/s]
    h2 = 0.01   # [1/s]
    H2b = 0.5   # [1/s]
    H3b = 0     # [1/s]

    # ODEs #####################################################
    dD1dt = k1*D2 - (3*k2*A + h1)*D1
    dD2dt = 3*k2*A*D1 + 2*k3*D3 + h2*C2 - (k1 + 2*k4*A + H3b)*D2
    dD3dt = 2*k4*A*D2 + 3*k5*D4 + H2b*Q1 - (2*k3 + k6*A)*D3
    dD4dt = k6*A*D3 + h2*Q2 - 3*k5*D4

    dC1dt = h1*D1 + k1*C2 + L1*C4 - 3*k2*A*C1
    dC2dt = H3b*D2 + 3*k2*A*C1 + 2*k3*Q1 - (k1 + 2*k4*A + h2)*C2
    dC3dt = 3*k2*A*C4 + 2*k1*Q4 - (k1 + 2*k2*A)*C3
    dC4dt = k1*C3 - (L1 + 3*k2*A)*C4

    dQ1dt = 2*k4*A*C2 + 3*k5*Q2 - (2*k3 + k6*A + H2b)*Q1
    dQ2dt = k6*A*Q1 + L2*Q3 - (3*k5 + L3 + h2)*Q2
    dQ3dt = k2*A*Q4 + L3*Q2 - (3*k1 + L2)*Q3
    dQ4dt = 2*k2*A*C3 + 3*k1*Q3 - (2*k1 + k2*A)*Q4

    dydt = [dD1dt, dD2dt, dD3dt, dD4dt, dC1dt, dC2dt, dC3dt, dC4dt, dQ1dt, dQ2dt, dQ3dt, dQ4dt]

    return dydt

def fJp2x7(y,rho):
    Q1, Q2, Q3, Q4 = y

    ## Electrochemistry properties for the estimation of inward current transient
    g12 = 1.5e-8    # [S]
    g34 = 4.5e-8    # [S]
    V = -0.06     # [V] -> the holding potential (used in NCX calculation as well)
    E12 = 0       # [V]
    E34 = 0       # [V]
    CaA = 0.1  # fraction of current contributed by Calcium transport

    ## Current generated from the P2X7 gating
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
    expF = rho          # Scale factor for over-expression of P2X4 on HEK293

    ## Influx via P2X4 Channels
    ### Conversion from the dimesion of HEK to the dimension of Microglia
    J = -(I/VcytMiG)*(AMiG/AHEK)/(2*F)*expF # [mol/(L*s) = M/s]

    return J
