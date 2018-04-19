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

# Na/Ca Exchanger
def fNCX(y):
    Cai, T = y
    R = 8.314 # [J/mol-k]

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

    # NCX parameters taken from Shannon-Bers model
    VmaxNCX = 9.0       # [A/F] modifeid from 9
    KmCai = 3.59e-6     # [M]
    KmCao = 1.3e-3      # [M]
    KmNai = 12.29e-3    # [M]
    KmNao = 87.5e-3     # [M]
    ksat = 0.27
    eta = 0.35
    KdAct = 0.256    # [uM]
    HNa = 3
    Q10NCX = 1.57    # modified from 1.57
    QNCX = Q10NCX**((T-310)/10)
    uniC = 1e-2         # [F/m**2] unit conductance
    Cm = uniC*AMiG      # [F] total conductance of microglia
    V = -0.06     # [V] -> the holding potential (used in NCX calculation as well)
    F = 96485.33289   # Faraday constant in [C/mol]

    ## Fixted substance concentrations
    Nae = 145e-3        # [M] Exocytosolic Na free concentration
    Nai = 8e-3         # [M] Cytosolic Na free concentration -> Neuroglia p.190 Fig 16.4 the range from 8-20 mM
    Cae = 2e-3          # [M] Exocytosolic Ca free concentration

    ## Lumped constants/terms
    Ka = 1/(1+(KdAct/(Cai*10**6)**3))
    Z = (V*F)/(R*T)      # [J/C*C/mol]/[J/(mol-K)*K]
    delta = (Nai**HNa)*Cae
    sigma = (Nae**HNa)*Cai

    top = Ka*QNCX*VmaxNCX*(exp(eta*Z)*delta - exp((eta-1)*Z)*sigma)
    bot = (KmCai*(Nae**HNa)*(1+(Nai/KmNai)**HNa) + (KmNao**HNa)*Cai*(1+(Cai/KmCai)) + KmCao*(Nai**HNa)
           + delta + sigma)*(1 + ksat*exp((eta-1))*Z)

    ## Current and influx via NCX
    INCX = top/bot            # [A/F]
    JNCX = (INCX*Cm)/(VMiG*F) # [M/s]

    return JNCX
