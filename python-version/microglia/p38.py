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

def fpp38(y):
    pp38, p38, Cai = y
    kb = 1/540 # 1 count/molecule per 540 seconds (9 mins) degradation
    kf = 1/(480*1e-6) # 1 count/molecule per 480 seconds (8 mins) -> due to Ca molecule/(sec-M)
    dpp38dt = -kb*pp38 + kf*p38*Cai
    dp38dt = kb*pp38 - kf*p38*Cai

    dydt = [dpp38dt, dp38dt]

    return dydt
