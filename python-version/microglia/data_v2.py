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

def data0():
    Cai = []
    CaM = []
    CaF = []
    CaS = []
    CaER = []
    p4D1 = []
    p4D2 = []
    p4D3 = []
    p4D4 = []
    p4D4 = []
    p4C1 = []
    p4C2 = []
    p4C3 = []
    p4C4 = []
    p4Q1 = []
    p4Q2 = []
    p4Q3 = []
    p4Q4 = []
    p4N = []
    p7D1 = []
    p7D2 = []
    p7D3 = []
    p7D4 = []
    p7D4 = []
    p7C1 = []
    p7C2 = []
    p7C3 = []
    p7C4 = []
    p7Q1 = []
    p7Q2 = []
    p7Q3 = []
    p7Q4 = []
    NFATpc = []
    NFATpn = []
    NFATNc = []
    NFATNn = []
    DNA = []
    DNA_TNF = []
    mRNA = []
    TNFa = []
    TNFa_leak = []
    TNFa_release = []
    TNFa_release_total = []
    time = []

    y0 = [Cai, CaM, CaF, CaS, CaER,
          p4D1, p4D2, p4D3, p4D4,
          p4C1, p4C2, p4C3, p4C4,
          p4Q1, p4Q2, p4Q3, p4Q4, p4N,
          p7D1, p7D2, p7D3, p7D4,
          p7C1, p7C2, p7C3, p7C4,
          p7Q1, p7Q2, p7Q3, p7Q4,
          NFATpc, NFATpn, NFATNc, NFATNn,
          DNA, DNA_TNF, mRNA, TNFa, TNFa_leak, TNFa_release, TNFa_release_total, time]

    return y0


def data(y0,y,t):
    Cai, CaM, CaF, CaS, CaER, p4D1, p4D2, p4D3, p4D4, p4C1, p4C2, p4C3, p4C4, p4Q1, p4Q2, p4Q3, p4Q4, p4N, p7D1, p7D2, p7D3, p7D4, p7C1, p7C2, p7C3, p7C4, p7Q1, p7Q2, p7Q3, p7Q4, NFATpc, NFATpn, NFATNc, NFATNn, DNA, DNA_TNF, mRNA, TNFa, TNFa_leak, TNFa_release, TNFa_release_total, time = y0

    Cai = np.append(Cai,y[:,0])                   # [M]
    CaM = np.append(CaM,y[:,1])                   # [M]
    CaF = np.append(CaF,y[:,2])                   # [M]
    CaS = np.append(CaS,y[:,3])                   # [M]
    CaER = np.append(CaER,y[:,4])                 # [M]
    p4D1 = np.append(p4D1,y[:,5])
    p4D2 = np.append(p4D2,y[:,6])
    p4D3 = np.append(p4D3,y[:,7])
    p4D4 = np.append(p4D4,y[:,8])
    p4C1 = np.append(p4C1,y[:,9])
    p4C2 = np.append(p4C2,y[:,10])
    p4C3 = np.append(p4C3,y[:,11])
    p4C4 = np.append(p4C4,y[:,12])
    p4Q1 = np.append(p4Q1,y[:,13])
    p4Q2 = np.append(p4Q2,y[:,14])
    p4Q3 = np.append(p4Q3,y[:,15])
    p4Q4 = np.append(p4Q4,y[:,16])
    p4N = np.append(p4N,y[:,17])
    p7D1 = np.append(p7D1,y[:,18])
    p7D2 = np.append(p7D2,y[:,19])
    p7D3 = np.append(p7D3,y[:,20])
    p7D4 = np.append(p7D4,y[:,21])
    p7C1 = np.append(p7C1,y[:,22])
    p7C2 = np.append(p7C2,y[:,23])
    p7C3 = np.append(p7C3,y[:,24])
    p7C4 = np.append(p7C4,y[:,25])
    p7Q1 = np.append(p7Q1,y[:,26])
    p7Q2 = np.append(p7Q2,y[:,27])
    p7Q3 = np.append(p7Q3,y[:,28])
    p7Q4 = np.append(p7Q4,y[:,29])
    NFATpc = np.append(NFATpc,y[:,30])             # [nM]
    NFATpn = np.append(NFATpn,y[:,31])             # [nM]
    NFATNc = np.append(NFATNc,y[:,32])             # [nM]
    NFATNn = np.append(NFATNn,y[:,33])             # [nM]
    DNA = np.append(DNA,y[:,34])                   # [molecule]
    DNA_TNF = np.append(DNA_TNF,y[:,35])             # [molecule]
    mRNA = np.append(mRNA,y[:,36])                   # [molecule]
    TNFa = np.append(TNFa,y[:,37])                 # [molecule]
    TNFa_leak = np.append(TNFa_leak,y[:,38])
    TNFa_release = np.append(TNFa_release,y[:,39]) # [molecule]
    TNFa_release_total = np.append(TNFa_release_total,y[:,40])
    time = np.append(time,t)                       # [second]

    y1 = [Cai, CaM, CaF, CaS, CaER,
          p4D1, p4D2, p4D3, p4D4,
          p4C1, p4C2, p4C3, p4C4,
          p4Q1, p4Q2, p4Q3, p4Q4, p4N,
          p7D1, p7D2, p7D3, p7D4,
          p7C1, p7C2, p7C3, p7C4,
          p7Q1, p7Q2, p7Q3, p7Q4,
          NFATpc, NFATpn, NFATNc, NFATNn,
          DNA, DNA_TNF, mRNA, TNFa, TNFa_leak, TNFa_release, TNFa_release_total, time]

    return y1
