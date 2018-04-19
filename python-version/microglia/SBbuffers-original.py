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
    Cai, CaM, CaF, CaER, CaS = y
    # Constants for Buffers ############ [Soon To be Modified] ###########################
    BmCalm = 0.024e-3 # [M] -> Shannon-Bers: Calmodulin (Cytoplasm)
    BmFura = 0.025e-3 # [M] -> Shannon-Bers: Fluo-3 (Cytoplasm)
    BmCals = 0.14e-3  # [M] -> Shannon-Bers: Calsequestrin (ER)

    KonCalm = 3.4e7   # [1/(M*s)] -> Shannon-Bers: Calmodulin (Cytoplasm)
    KonFura = 15e7    # [1/(M*s)] -> Chemical Calcium Indicators: Fura-2 (Cytoplasm)
    KonCals = 10e7    # [1/(M*s)] -> Shannon-Bers: Calsequestrin (ER)

    KoffCalm = 238    # [1/s] -> Shannon-Bers: Calmodulin (Cytoplasm)
    KoffFura = 23     # [1/s] -> Chemical Calcium Indicators: Fura-2 (Cytoplasm)
    KoffCals = 65000  # [1/s] -> Shannon-Bers: Calsequestrin (ER)
    rV = 0.035/0.4        # Volume ratio of ER to Cytosol

    dCaMdt = KonCalm*Cai*(BmCalm - CaM) - KoffCalm*CaM
    dCaFdt = KonFura*Cai*(BmFura - CaF) - KoffFura*CaF
    dCaSdt = KonCals*CaER*(BmCals/rV - CaS) - KoffCals*CaS

    dydt = [dCaMdt, dCaFdt, dCaSdt]

    return dydt
