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

def fmax(y,init,final):
    dummy1 = y[init:final]
    dummy2 = max(dummy1)

    return dummy2

def frel(y):
    dummy1 = max(y)
    dummy2 = (y/dummy1)*100

    return dummy2
