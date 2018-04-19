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


### Shannon-Bers Buffer Modeling
# Ca buffers
def fbuff(y):
    Cai, CaF, CaER, CaS, Ca2CaM, Ca4CaM, Ca4CN, CaMCN = y
    # Constants for Buffers ############ [Soon To be Modified] ###########################
    BmFura = 0.025e-3 # [M] -> Shannon-Bers: Fluo-3 (Cytoplasm)
    BmCals = 0.14e-3  # [M] -> Shannon-Bers: Calsequestrin (ER)

    KonFura = 15e7    # [1/(M*s)] -> Chemical Calcium Indicators: Fura-2 (Cytoplasm)
    KonCals = 10e7    # [1/(M*s)] -> Shannon-Bers: Calsequestrin (ER)

    KoffFura = 23     # [1/s] -> Chemical Calcium Indicators: Fura-2 (Cytoplasm)
    KoffCals = 65000  # [1/s] -> Shannon-Bers: Calsequestrin (ER)
    rV = 0.035/0.4        # Volume ratio of ER to Cytosol

    # Constants for CaM-CN calculation: taken from the work of Bazzazi et al. by Rachel
    k20  =  10          # [s-1]
    k02 = 1e13          # [M-2*s-1]

    k42 = 500           # [s-1]
    k24 = 500*(1e13)    # [M-2*s-1]

    koffA = 1.0         # [s-1]
    konA = 1e10         # [M-1*s-1]

    konB = 2e12         # [M-2*s-1]
    koffB = 2*0.5       # [s-1]

    CNt = 2e-6          #[M]
    CaMt = 3e-6         #[M]

    CaM = CaMt - (Ca2CaM + Ca4CaM + CaMCN)
    Ca2CN = CNt - (Ca4CN + CaMCN)

    dCa2CaMdt = k02*CaM*(Cai**2) - k20*Ca2CaM + k42*Ca4CaM - k24*Ca2CaM*(Cai**2)
    dCa4CaMdt = k24*(Cai**2)*Ca2CaM - k42*Ca4CaM + koffA*CaMCN - konA*Ca4CaM*Ca4CN
    dCa4CNdt = konB*(Cai**2)*Ca2CN - koffB*Ca4CN + koffA*CaMCN - konA*Ca4CaM*Ca4CN
    dCaMCNdt = konA*Ca4CaM*Ca4CN - koffA*CaMCN

    dCaFdt = KonFura*Cai*(BmFura - CaF) - KoffFura*CaF
    dCaSdt = KonCals*CaER*(BmCals/rV - CaS) - KoffCals*CaS

    dydt = [dCa2CaMdt, dCa4CaMdt, dCa4CNdt, dCaMCNdt, dCaFdt, dCaSdt]

    return dydt
