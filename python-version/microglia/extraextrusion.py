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

#### TNF release function
#3. The release of TNF-alpha will be fully assumed based on general RNA transcription and translation.
#https://www.mathworks.com/help/simbio/gs/-model-a-gene-regulation-pathway.html?requestedDomain=true

def fextra(y,t):
    Cai, CaER, p4A, i, interval, st = y

    p4AuM= p4A*10**6

    # Arbitary Rate constants
    Dmax = 0.01 # [1/s]
    nleak = 2.5
    Kd = 50

    Katp = 0.01*st
    natp = 15

    if p4A > 0:
        tint = interval*(i+1)-t
        if tint <= 0.01:
            tint = 0.01

        newATP = p4AuM/(1+(Katp/tint)**natp)

        fER = 1/(1+(Kd/newATP)**nleak)

    elif p4A == 0:
        fER = 0

    dCaleakERdt = Dmax*(CaER-Cai) #*fER

    dydt = dCaleakERdt

    return dydt
