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
    CaF = []
    CaS = []
    CaER = []
    Ca2CaM = []
    Ca4CaM = []
    Ca4CN = []
    CaMCN = []
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

    y0 = [Cai, CaF, CaS, CaER,
          Ca2CaM, Ca4CaM, Ca4CN, CaMCN,
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
    [Cai, CaF, CaS, CaER,
    Ca2CaM, Ca4CaM, Ca4CN, CaMCN,
    p4D1, p4D2, p4D3, p4D4,
    p4C1, p4C2, p4C3, p4C4,
    p4Q1, p4Q2, p4Q3, p4Q4, p4N,
    p7D1, p7D2, p7D3, p7D4,
    p7C1, p7C2, p7C3, p7C4,
    p7Q1, p7Q2, p7Q3, p7Q4,
    NFATpc, NFATpn, NFATNc, NFATNn,
    DNA, DNA_TNF, mRNA,
    TNFa, TNFa_leak, TNFa_release, TNFa_release_total, time] = y0

    Cai = np.append(Cai,y[:,0])                   # [M]
    CaF = np.append(CaF,y[:,1])                   # [M]
    CaS = np.append(CaS,y[:,2])                   # [M]
    CaER = np.append(CaER,y[:,3])
    Ca2CaM = np.append(Ca2CaM,y[:,4])
    Ca4CaM = np.append(Ca4CaM,y[:,5])
    Ca4CN = np.append(Ca4CN,y[:,6])
    CaMCN = np.append(CaMCN,y[:,7])                 # [M]
    p4D1 = np.append(p4D1,y[:,8])
    p4D2 = np.append(p4D2,y[:,9])
    p4D3 = np.append(p4D3,y[:,10])
    p4D4 = np.append(p4D4,y[:,11])
    p4C1 = np.append(p4C1,y[:,12])
    p4C2 = np.append(p4C2,y[:,13])
    p4C3 = np.append(p4C3,y[:,14])
    p4C4 = np.append(p4C4,y[:,15])
    p4Q1 = np.append(p4Q1,y[:,16])
    p4Q2 = np.append(p4Q2,y[:,17])
    p4Q3 = np.append(p4Q3,y[:,18])
    p4Q4 = np.append(p4Q4,y[:,19])
    p4N = np.append(p4N,y[:,20])
    p7D1 = np.append(p7D1,y[:,21])
    p7D2 = np.append(p7D2,y[:,22])
    p7D3 = np.append(p7D3,y[:,23])
    p7D4 = np.append(p7D4,y[:,24])
    p7C1 = np.append(p7C1,y[:,25])
    p7C2 = np.append(p7C2,y[:,26])
    p7C3 = np.append(p7C3,y[:,27])
    p7C4 = np.append(p7C4,y[:,28])
    p7Q1 = np.append(p7Q1,y[:,29])
    p7Q2 = np.append(p7Q2,y[:,30])
    p7Q3 = np.append(p7Q3,y[:,31])
    p7Q4 = np.append(p7Q4,y[:,32])
    NFATpc = np.append(NFATpc,y[:,33])             # [nM]
    NFATpn = np.append(NFATpn,y[:,34])             # [nM]
    NFATNc = np.append(NFATNc,y[:,35])             # [nM]
    NFATNn = np.append(NFATNn,y[:,36])             # [nM]
    DNA = np.append(DNA,y[:,37])                   # [molecule]
    DNA_TNF = np.append(DNA_TNF,y[:,38])             # [molecule]
    mRNA = np.append(mRNA,y[:,39])                   # [molecule]
    TNFa = np.append(TNFa,y[:,40])                 # [molecule]
    TNFa_leak = np.append(TNFa_leak,y[:,41])
    TNFa_release = np.append(TNFa_release,y[:,42]) # [molecule]
    TNFa_release_total = np.append(TNFa_release_total,y[:,43])
    time = np.append(time,t)                       # [second]

    y1 = [Cai, CaF, CaS, CaER,
          Ca2CaM, Ca4CaM, Ca4CN, CaMCN,
          p4D1, p4D2, p4D3, p4D4,
          p4C1, p4C2, p4C3, p4C4,
          p4Q1, p4Q2, p4Q3, p4Q4, p4N,
          p7D1, p7D2, p7D3, p7D4,
          p7C1, p7C2, p7C3, p7C4,
          p7Q1, p7Q2, p7Q3, p7Q4,
          NFATpc, NFATpn, NFATNc, NFATNn,
          DNA, DNA_TNF, mRNA, TNFa, TNFa_leak, TNFa_release, TNFa_release_total, time]

    return y1
