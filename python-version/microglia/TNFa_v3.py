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

def fTNFa(y):
    [NFATNn, Cai, pp38,
     DNA, DNA_TNF, mRNA, TNFa,
     TNFa_leak, TNFa_release, TNFa_release_total] = y

    ## Constant ####
    ### DNA transcription/translation
    ktrnscrpt = 1/3600   # [1/s]: k for transcription of mRNA from DNA per molecule
    ktrnsl = 100/3600       # [1/s]: k for translation of TNFa from mRNA per molecule
    kdegTNF = 50/3600          # [1/s]: the rate of degradation of TNFa per molecule
    kdegRNA = 0.5/3600          # [1/s]: the rate of degradation of mRNA per molecule
    kgeneexpf = 1/(3600*2.5)        # [1/(molecule-s)]: Gene expression
    kgeneexpr = 1/3600        # [1/s]:
    kfpp38 = 2/3600            # 1 count per 100 seconds

    ### Hill equation related constants for activation of DNA dynamics/TNFa release
    kmaxexo = 5/1800             # [1/(M-s)]: R max of exocytosis of TNFa 150 15 15 10 1
    #kmaxexo = 5             # [1/s]: R max of exocytosis of TNFa 150 15 15 10 1
    kmaxleak = 2.5              # [1/s]: constant leaks of TNFa 5 5 5 2.5 2.5
    nCaleak = 1.8
    nNFAT1 = 100                # Hill coefficient of NFAT related to transcription activation
    nNFAT2 = 1500                # Hill coefficient of NFAT related to TNFa exocytosis

    IC50Caleak = 0.1         # [M]: TNFa leaks related 4e-7 4e-7 1e-7 1e-7 1e-7
    IC50NFAT1 = 1.07         # [nM] Transcription related
    IC50NFAT2 = 1.0985           # [nM] TNFa exocytosis related 10 0.1 0.5 0.5 0.15 0.105

    #if NFATNn >= 0.105:
    ## Converstion
    Rtranscript = ktrnscrpt/(1+(IC50NFAT1/(NFATNn))**nNFAT1)*DNA
    Rtranslate = ktrnsl*mRNA
    RdegTNF = kdegTNF*TNFa
    RdegRNA = kdegRNA*mRNA
    Rgeneexp = kgeneexpf*DNA*TNFa - kgeneexpr*DNA_TNF
    Rpp38 = kfpp38*pp38
    Rexo = (kmaxexo/(1+(IC50Caleak/(Cai*10**6))**nCaleak))*TNFa*Cai*10**6
    #Rexo = (kmaxexo/(1+(IC50NFAT2/(NFATNn))**nNFAT2))*TNFa + (kmaxleak/(1+(IC50Caleak/(Cai*10**6))**nCaleak))*TNFa

    dDNAdt = -Rgeneexp
    dRNAdt = Rtranscript - RdegRNA
    dDNATNFdt = Rgeneexp
    dTNFadt = Rtranslate + Rpp38 - RdegTNF - Rgeneexp - Rexo
    dTNFa_leakdt = 0
    dTNFa_releasedt = 0
    #dTNFadt = Rtranslate - RdegTNF - Rgeneexp - Rexo
    #dTNFa_leakdt = (kmaxleak/(1+(IC50Caleak/(Cai*10**6))**nCaleak))*TNFa
    #dTNFa_releasedt= (kmaxexo/(1+(IC50NFAT2/NFATNn)**nNFAT2))*TNFa
    dTNFa_release_totaldt = Rexo

    dydt = [dDNAdt, dDNATNFdt, dRNAdt, dTNFadt, dTNFa_leakdt, dTNFa_releasedt, dTNFa_release_totaldt]

    return dydt
