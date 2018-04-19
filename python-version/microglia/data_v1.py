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
    D1 = []
    D2 = []
    D3 = []
    D4 = []
    D4 = []
    C1 = []
    C2 = []
    C3 = []
    C4 = []
    Q1 = []
    Q2 = []
    Q3 = []
    Q4 = []
    N = []
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
          D1, D2, D3, D4,
          C1, C2, C3, C4,
          Q1, Q2, Q3, Q4, N,
          NFATpc, NFATpn, NFATNc, NFATNn,
          DNA, DNA_TNF, mRNA, TNFa, TNFa_leak, TNFa_release, TNFa_release_total, time]

    return y0


def data(y0,y,t):
    Cai, CaM, CaF, CaS, CaER, D1, D2, D3, D4, C1, C2, C3, C4, Q1, Q2, Q3, Q4, N, NFATpc, NFATpn, NFATNc, NFATNn, DNA, DNA_TNF, mRNA, TNFa, TNFa_leak, TNFa_release, TNFa_release_total, time = y0

    Cai = np.append(Cai,y[:,0])                   # [M]
    CaM = np.append(CaM,y[:,1])                   # [M]
    CaF = np.append(CaF,y[:,2])                   # [M]
    CaS = np.append(CaS,y[:,3])                   # [M]
    CaER = np.append(CaER,y[:,4])                 # [M]
    D1 = np.append(D1,y[:,5])
    D2 = np.append(D2,y[:,6])
    D3 = np.append(D3,y[:,7])
    D4 = np.append(D4,y[:,8])
    C1 = np.append(C1,y[:,9])
    C2 = np.append(C2,y[:,10])
    C3 = np.append(C3,y[:,11])
    C4 = np.append(C4,y[:,12])
    Q1 = np.append(Q1,y[:,13])
    Q2 = np.append(Q2,y[:,14])
    Q3 = np.append(Q3,y[:,15])
    Q4 = np.append(Q4,y[:,16])
    N = np.append(N,y[:,17])
    NFATpc = np.append(NFATpc,y[:,18])             # [nM]
    NFATpn = np.append(NFATpn,y[:,19])             # [nM]
    NFATNc = np.append(NFATNc,y[:,20])             # [nM]
    NFATNn = np.append(NFATNn,y[:,21])             # [nM]
    DNA = np.append(DNA,y[:,22])                   # [molecule]
    DNA_TNF = np.append(DNA_TNF,y[:,23])             # [molecule]
    mRNA = np.append(mRNA,y[:,24])                   # [molecule]
    TNFa = np.append(TNFa,y[:,25])                 # [molecule]
    TNFa_leak = np.append(TNFa_leak,y[:,26])
    TNFa_release = np.append(TNFa_release,y[:,27]) # [molecule]
    TNFa_release_total = np.append(TNFa_release_total,y[:,28])
    time = np.append(time,t)                       # [second]

    y1 = [Cai, CaM, CaF, CaS, CaER,
          D1, D2, D3, D4,
          C1, C2, C3, C4,
          Q1, Q2, Q3, Q4, N,
          NFATpc, NFATpn, NFATNc, NFATNn,
          DNA, DNA_TNF, mRNA, TNFa, TNFa_leak, TNFa_release, TNFa_release_total, time]

    return y1
