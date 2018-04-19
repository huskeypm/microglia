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

### NFAT Cycle by Coolings + TNFa release term
#### TNF-a Protein Synthesis (General Model)
#    1. DNA -> DNA + mRNA            		     k1  (transcription)
#    2. mRNA -> mRNA + TNFprotein       		 k2  (translation)
#    3. DNA + TNFprotein -> DNATNFComplex 	 k3f (binding)
#    4. DNATNFComplex -> DNA + TNFprotein 	 k3r (unbinding)
#    5. mRNA -> null                 		     k4  (degradation)
#    6. TNF -> null              	    	     k5  (degradation)
#    7. TNF release                          k6  (release of TNFa)

# NFAT Cycle
def fNFAT(y):
    Cai, CaMCN, NFATpc, NFATpn, NFATNc, NFATNn = y

    Cai = Cai*(1e9)         # in [nM]
    CaMCN = CaMCN*(1e9)     # in [nM]
    CNt = 2e3               # in [nM] Total number of calcineurin: this value is the same as used in buffer calculation

    #### NFAT Cycle Related Taken for Coolings ####
    kf1 = 7.69e-5    # [1/(nMs)] Adjusted from 7.69e-6 1/(nM-s)
    # This parameter was adjusted to fit the concentration of NFAT at the
    # steady state listed in Coolings paper, which is reported by Tomida et al.
    kr1 = 1.93e-2    # [1/s]
    kf2 = 1.44e-3    # [1/s]
    kf3 = 3.62e-4    # [1/s]
    kr3 = 4.71e-5    # [1/(nMs)]
    kf4 = 4.45e-4    # [1/s]
    KmN = 535        # [nM]
    n = 2.92
    Ccn = 1          # Volume ratio of Cytosol to Nucleus
    actN = CaMCN/CNt

    #### NFAT Cycle kinetics ####
    J1 = kf1*NFATpc*CaMCN - kr1*NFATNc*(1 - actN)
    J2 = NFATNc*kf2
    J3 = kf3*NFATNn*(1-actN) - kr3*NFATpn*CaMCN
    J4 = NFATpn*kf4

    #### NFAT : ODEs ####
    dNFATpcdt = J4/Ccn - J1
    dNFATNcdt = J1 - J2
    dNFATNndt = J2*Ccn - J3
    dNFATpndt = J3 - J4

    dydt = [dNFATpcdt, dNFATpndt, dNFATNcdt, dNFATNndt] # the outcome is in [nM/s]

    return dydt
