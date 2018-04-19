# Function for integreating ODE and displaying results
import scipy.integrate
from scipy.integrate import odeint
import numpy as np
import math
from math import exp
from scipy.interpolate import spline

# Importing the microglia related packages
import data as dt
import TNFa as Ta
import NFAT as Nt
import MSMp2x4 as p4
import SBbuffers as Bf

import numpy.random as npr
# normal random distribution
from numpy.random import normal as nprn
# uniform random distribution
from numpy.random import uniform as npru


def ft(y,t,A):
    # Assigning the variables from the initial input y(array)
    Cai, CaM, CaF, CaS, CaER, D1, D2, D3, D4, C1, C2, C3, C4, Q1, Q2, Q3, Q4, N, NFATpc, NFATpn, NFATNc, NFATNn, DNA, DNA_TNF, mRNA, TNFa, TNFa_release = y

    # Basic Condition & Constant
    T = 310 # [K] Temp

    # P2X4 Markov State
    ip2x4 = np.array([D1, D2, D3, D4, C1, C2, C3, C4, Q1, Q2, Q3, Q4, N, A])
    dD1dt, dD2dt, dD3dt, dD4dt, dC1dt, dC2dt, dC3dt, dC4dt, dQ1dt, dQ2dt, dQ3dt, dQ4dt, dNdt = fp2x4(ip2x4)

    # Ca influx via P2X4
    iJp2x4 = np.array([Q1, Q2, Q3, Q4])
    Jp2x4 = fJp2x4(iJp2x4)

    # SERCA Term
    iJsercaER = np.array([Cai, CaER, T])
    JERtoCyt, JCyttoER = fJsercaER(iJsercaER)

    # Buffer Term
    ibuff = np.array([Cai, CaM, CaF, CaER, CaS])
    dCaMdt, dCaFdt, dCaSdt = fbuff(ibuff)

    # NCX Term
    iJNCX = np.array([Cai,T])
    JNCX = fNCX(iJNCX)

    # NFAT Cycle
    iNFAT = np.array([Cai, CaM, NFATpc, NFATpn, NFATNc, NFATNn])
    dNFATpcdt, dNFATpndt, dNFATNcdt, dNFATNndt = fNFAT(iNFAT)

    # TNFa release
    iTNFa = np.array([NFATNn, Cai, DNA, DNA_TNF, mRNA, TNFa, TNFa_release])
    dDNAdt, dDNATNFdt, dRNAdt, dTNFadt, dTNFa_releasedt = fTNFa(iTNFa)

    # Calcium concentration in cytosol and ER
    ##################################################################
    dCaidt = - dCaMdt - dCaFdt - JCyttoER + Jp2x4 + JNCX
    dCaERdt = JERtoCyt - dCaSdt
    #####################################################################################################

    dydt = [dCaidt, dCaMdt, dCaFdt, dCaSdt, dCaERdt,
            dD1dt, dD2dt, dD3dt, dD4dt,
            dC1dt, dC2dt, dC3dt, dC4dt,
            dQ1dt, dQ2dt, dQ3dt, dQ4dt, dNdt,
            dNFATpcdt, dNFATpndt, dNFATNcdt, dNFATNndt,
            dDNAdt, dDNATNFdt, dRNAdt, dTNFadt, dTNFa_releasedt]

    return dydt
