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

### SERCA Modeling
# Ca Influx via SERCA to ER lumen
def fJsercaER(y):
    Cai, CaER, T = y
    # SERCA pump calculation taken from Shannon-Bers model ###############################
    ## Constants
    Cai2 = Cai*10**6
    CaER2 = CaER*10**3
    Q10ERCa = 2.6
    QERCa = Q10ERCa**((T-310)/10)
    VmaxSERCA = 5.3114e-3 # [M/s] taken from script but their literature reported differently: This may need to be adjusted
    Kmf = 0.246         # [uM]
    Kmr = 1.7           # [mM]
    H = 1.787
    rV = 0.035/0.4        # Volume ratio of ER to Cytosol

    ## Transport via SERCA Pump from Cytosol to ER lumen
    top = ((Cai2/Kmf)**H)-((CaER2/Kmr)**H)
    bottom = 1+((Cai2/Kmf)**H)+((CaER2/Kmr)**H)
    JERtoCyt = QERCa*VmaxSERCA*top/bottom
    JCyttoER = JERtoCyt*rV
    #print(top, bottom, Cai2, CaER2)
    Jserca = [JERtoCyt, JCyttoER]

    return Jserca
