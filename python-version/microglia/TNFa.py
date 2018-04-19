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
    NFATNn, Cai, DNA, DNA_TNF, mRNA, TNFa, TNFa_leak, TNFa_release, TNFa_release_total = y

    ## Constant ####
    ### DNA transcription/translation
    ktranscription = 0.0083   # [1/s]: k for transcription of mRNA from DNA per molecule -> 20 sec per molecule
    ktranslation = 0.83       # [1/s]: k for translation of TNFa from mRNA per molecule
    kdegTNF = 0.0415          # [1/s]: the rate of degradation of TNFa per molecule
    kdegRNA = 0.0623          # [1/s]: the rate of degradation of mRNA per molecule
    kgeneexpf = 0.0083        # [1/(molecule-s)]: Gene expression
    kgeneexpr = 0.0415        # [1/s]:

    ### Hill equation related constants for activation of DNA dynamics/TNFa release
    kmaxexo = 5             # [1/s]: R max of exocytosis of TNFa 150 15 15 10 1
    kmaxleak = 2.5              # [1/s]: constant leaks of TNFa 5 5 5 2.5 2.5
    nCaleak = 1.8
    nNFAT1 = 100                # Hill coefficient of NFAT related to transcription activation
    nNFAT2 = 1500                # Hill coefficient of NFAT related to TNFa exocytosis

    IC50Caleak = 0.1         # [M]: TNFa leaks related 4e-7 4e-7 1e-7 1e-7 1e-7
    IC50NFAT1 = 1.07         # [nM] Transcription related
    IC50NFAT2 = 1.0985           # [nM] TNFa exocytosis related 10 0.1 0.5 0.5 0.15 0.105

    ## Dimensions of Microglia
    rMiG = 2.6e-6                           # radius of microglia cell body in [meter]
    AMiG = 4*3.141592654*(rMiG)**2          # surface area of microglia in [sq. meter]
    VMiG = 1000*(4/3)*3.141592654*(rMiG)**3 # volume of microglia in [L]
    VNuMiG = VMiG*0.40                      # [L] The volume of cytoplasm in microglia -> This fraction was estimated from the figure (Liaury).
    Avo = 6.022e23                          # molecules per mole

    #if NFATNn >= 0.105:
    ## Converstion
    Rtranscript = ktranscription/(1+(IC50NFAT1/(NFATNn))**nNFAT1)*DNA
    Rtranslate = ktranslation*mRNA
    RdegTNF = kdegTNF*TNFa
    RdegRNA = kdegRNA*mRNA
    Rgeneexp = kgeneexpf*DNA*TNFa - kgeneexpr*DNA_TNF
    Rexo = (kmaxexo/(1+(IC50NFAT2/(NFATNn))**nNFAT2))*TNFa + (kmaxleak/(1+(IC50Caleak/(Cai*10**6))**nCaleak))*TNFa

    dDNAdt = -Rgeneexp
    dRNAdt = Rtranscript - RdegRNA
    dDNATNFdt = Rgeneexp
    dTNFadt = Rtranslate - RdegTNF - Rgeneexp - Rexo
    dTNFa_leakdt = (kmaxleak/(1+(IC50Caleak/(Cai*10**6))**nCaleak))*TNFa
    dTNFa_releasedt= (kmaxexo/(1+(IC50NFAT2/NFATNn)**nNFAT2))*TNFa
    dTNFa_release_totaldt = dTNFa_leakdt + dTNFa_releasedt

    dydt = [dDNAdt, dDNATNFdt, dRNAdt, dTNFadt, dTNFa_leakdt, dTNFa_releasedt, dTNFa_release_totaldt]

    return dydt
