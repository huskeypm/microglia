# Function for integreating ODE and displaying results
import scipy.integrate
from scipy.integrate import odeint
import numpy as np
import matplotlib.pylab as plt
import math
from math import exp
from scipy.interpolate import spline


# Importing the microglia related packages
import data_v5 as dt      # Data sorting code
import TNFa as ta      # TNFa release code
import NFAT as nt      # NFAT cycle code
import MSMp2x4v2 as p4   # Markov State Model for P2X4 channel
import MSMp2x7v2 as p7   # Markov State Model for P2X7 channel
import SBbuffers as bf # Buffers (Fura-2, Calmodulin, and Calsequestrin) code
import SERCAER as er   # SERCA Pump code
import NCX as nx       # Na/Ca exchanger code
import extraextrusion as ee

import numpy.random as npr
# normal random distribution
from numpy.random import normal as nprn
# uniform random distribution
from numpy.random import uniform as npru

def ft(y,t,p4A,p7A,rhop2x4,rhop2x7):
    # Assigning the variables from the initial input y(array)
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
    TNFa, TNFa_leak, TNFa_release, TNFa_release_total, maxflux] = y

    # Basic Condition & Constant
    T = 310 # [K] Temp

    # P2X4 Markov State
    ip2x4 = np.array([p4D1, p4D2, p4D3, p4D4, p4C1, p4C2, p4C3, p4C4, p4Q1, p4Q2, p4Q3, p4Q4, p4N, p4A])
    [dp4D1dt, dp4D2dt, dp4D3dt, dp4D4dt,
     dp4C1dt, dp4C2dt, dp4C3dt, dp4C4dt,
     dp4Q1dt, dp4Q2dt, dp4Q3dt, dp4Q4dt, dp4Ndt] = p4.fp2x4(ip2x4)

    # P2X7 Markov state
    ip2x7 = np.array([p7D1, p7D2, p7D3, p7D4, p7C1, p7C2, p7C3, p7C4, p7Q1, p7Q2, p7Q3, p7Q4, p7A])
    [dp7D1dt, dp7D2dt, dp7D3dt, dp7D4dt,
     dp7C1dt, dp7C2dt, dp7C3dt, dp7C4dt,
     dp7Q1dt, dp7Q2dt, dp7Q3dt, dp7Q4dt] = p7.fp2x7(ip2x7)

    # Ca influx via P2X4
    iJp2x4 = np.array([p4Q1, p4Q2, p4Q3, p4Q4])
    Jp2x4 = p4.fJp2x4(iJp2x4,rhop2x4)

    # Ca influx via P2X7
    iJp2x7 = np.array([p7Q1, p7Q2, p7Q3, p7Q4])
    Jp2x7 = p7.fJp2x7(iJp2x7,rhop2x7)

    # SERCA Term
    iJsercaER = np.array([Cai, CaER, T])
    JERtoCyt, JCyttoER = er.fJsercaER(iJsercaER)

    # Buffer Term
    ibuff = np.array([Cai, CaF, CaER, CaS, Ca2CaM, Ca4CaM, Ca4CN, CaMCN])
    dCa2CaMdt, dCa4CaMdt, dCa4CNdt, dCaMCNdt, dCaFdt, dCaSdt = bf.fbuff(ibuff)

    # NCX Term
    iJNCX = np.array([Cai,T])
    JNCX = nx.fNCX(iJNCX)

    # NFAT Cycle
    iNFAT = np.array([Cai, CaMCN, NFATpc, NFATpn, NFATNc, NFATNn])
    dNFATpcdt, dNFATpndt, dNFATNcdt, dNFATNndt = nt.fNFAT(iNFAT)

    # TNFa release
    iTNFa = np.array([NFATNn, Cai, DNA, DNA_TNF, mRNA, TNFa, TNFa_leak, TNFa_release, TNFa_release_total])
    dDNAdt, dDNATNFdt, dRNAdt, dTNFadt, dTNFa_leakdt, dTNFa_releasedt, dTNFa_release_totaldt = ta.fTNFa(iTNFa)

    maxflux = Jp2x4+Jp2x7

    print

    # Calcium concentration in cytosol and ER
    ##################################################################
    dCaidt = - dCa2CaMdt - dCa4CaMdt - dCa4CNdt - dCaFdt - JCyttoER + Jp2x4 + Jp2x7 + JNCX
    dCaERdt = JERtoCyt - dCaSdt
    #####################################################################################################

    dydt = [dCaidt,  dCaFdt, dCaSdt, dCaERdt,
            dCa2CaMdt, dCa4CaMdt, dCa4CNdt, dCaMCNdt,
            dp4D1dt, dp4D2dt, dp4D3dt, dp4D4dt,
            dp4C1dt, dp4C2dt, dp4C3dt, dp4C4dt,
            dp4Q1dt, dp4Q2dt, dp4Q3dt, dp4Q4dt, dp4Ndt,
            dp7D1dt, dp7D2dt, dp7D3dt, dp7D4dt,
            dp7C1dt, dp7C2dt, dp7C3dt, dp7C4dt,
            dp7Q1dt, dp7Q2dt, dp7Q3dt, dp7Q4dt,
            dNFATpcdt, dNFATpndt, dNFATNcdt, dNFATNndt,
            dDNAdt, dDNATNFdt, dRNAdt, dTNFadt, dTNFa_leakdt, dTNFa_releasedt, dTNFa_release_totaldt, maxflux]

    return dydt

def total(st,Du,step,interval,ATP,rhop2x4,rhop2x7):
    # st : ATP stimulation time in second
    # Du : Total running time in second
    # step : step size in linspace
    # interval : time between stimulation
    # ATP = [ATP] in uM
    # rho goes from 0 to 1

    d0 = dt.data0()

    iters = np.arange(Du)

    for i in iters:

        ti = i*interval          # 0, 30, 60, 90 ....
        tf = (i+1)*interval-st   # 28, 58, 88, 118 ....

        trs = scipy.linspace(ti,tf,(interval*step))  # time without ATP stimulation
        tst = scipy.linspace(tf,(tf+st),(st*step))  # time with ATP stimulation

        if i == 0 : # Very first step of calculation
            p4A = 0   # Turn off the ATP concentration for P2X4
            p7A = 0   # Turn off the ATP concentration for P2X7
            Cai0 = 3.5538633608641e-08    # [M]
            CaF0 = 4.70406410592e-06     # [M]
            CaS0 = 0.000438757171897     # [M]
            CaER0 = 0.000245592183505    # [M]
            Ca2CaM0 = 0                  # [M]
            Ca4CaM0 = 0
            Ca4CN0 = 0
            CaMCN0 = 0
            NFATpc0 = 0.994682667758    # [nM]
            NFATpn0 = 0.0463772043925   # [nM]
            NFATNc0 = 0.000112322167638 # [nM]
            NFATNn0 = 0.0581439005689   # [nM]
            dst = d0
            y0 = np.array([Cai0, CaF0, CaS0, CaER0,
                           Ca2CaM0, Ca4CaM0, Ca4CN0, CaMCN0,
                           0, 0, 0, 0,
                           1, 0, 0, 0,
                           0, 0, 0, 0, 0,
                           0, 0, 0, 0,
                           1, 0, 0, 0,
                           0, 0, 0, 0,
                           NFATpc0, NFATpn0, NFATNc0, NFATNn0,
                           50,0,0,100,0,0,0,0]) # Very first step
        else :
            y0 = np.array([Cai[-1], CaF[-1], CaS[-1], CaER[-1],
                           Ca2CaM[-1], Ca4CaM[-1], Ca4CN[-1], CaMCN[-1],
                           p4D1[-1], p4D2[-1], p4D3[-1], p4D4[-1],
                           p4C1[-1], p4C2[-1], p4C3[-1], p4C4[-1],
                           p4Q1[-1], p4Q2[-1], p4Q3[-1], p4Q4[-1], p4N[-1],
                           p7D1[-1], p7D2[-1], p7D3[-1], p7D4[-1],
                           p7C1[-1], p7C2[-1], p7C3[-1], p7C4[-1],
                           p7Q1[-1], p7Q2[-1], p7Q3[-1], p7Q4[-1],
                           NFATpc[-1], NFATpn[-1], NFATNc[-1], NFATNn[-1],
                           DNA[-1],DNA_TNF[-1],mRNA[-1],TNFa[-1],TNFa_leak[-1],TNFa_release[-1],TNFa_release_total[-1],0])

        # Solving for the resting state
        p4A = 0 # Turn off the ATP concentration for P2X4
        p7A = 0 # Turn off the ATP concentration for P2X7
        yrs = scipy.integrate.odeint(ft,y0,trs,args=(p4A,p7A,rhop2x4,rhop2x7,),mxstep=5000000)
        # Storing the data from the resting state calculation
        drs = dt.data(dst,yrs,trs)
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
        TNFa, TNFa_leak, TNFa_release, TNFa_release_total, maxflux, time] = drs

        del y0
        del p4A
        del p7A
        del yrs
        del trs

        # Solving for the stimulated state
        p4A = ATP*10**-6    # ATP uM ATP stimulation
        if ATP < 1: # Basal condition
            p7A = ATP*10**-6
        else:
            p7A = 4.11863563*math.exp(ATP*0.00479906)*10**-6
        y0 = np.array([Cai[-1], CaF[-1], CaS[-1], CaER[-1],
                       Ca2CaM[-1], Ca4CaM[-1], Ca4CN[-1], CaMCN[-1],
                       p4D1[-1], p4D2[-1], p4D3[-1], p4D4[-1],
                       p4C1[-1], p4C2[-1], p4C3[-1], p4C4[-1],
                       p4Q1[-1], p4Q2[-1], p4Q3[-1], p4Q4[-1], p4N[-1],
                       p7D1[-1], p7D2[-1], p7D3[-1], p7D4[-1],
                       p7C1[-1], p7C2[-1], p7C3[-1], p7C4[-1],
                       p7Q1[-1], p7Q2[-1], p7Q3[-1], p7Q4[-1],
                       NFATpc[-1], NFATpn[-1], NFATNc[-1], NFATNn[-1],
                       DNA[-1],DNA_TNF[-1],mRNA[-1],
                       TNFa[-1],0,0,0,0])
        yst = scipy.integrate.odeint(ft,y0,tst,args=(p4A,p7A,rhop2x4,rhop2x7,),mxstep=5000000)

        dst = dt.data(drs,yst,tst)
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
        TNFa, TNFa_leak, TNFa_release, TNFa_release_total, maxflux, time] = dst

        del yst
        del tst
        del ti
        del tf

    results = [Cai, CaF, CaS, CaER, # 5
               Ca2CaM, Ca4CaM, Ca4CN, CaMCN,
               p4D1, p4D2, p4D3, p4D4, # 9
               p4C1, p4C2, p4C3, p4C4, # 13
               p4Q1, p4Q2, p4Q3, p4Q4, p4N, # 15
               p7D1, p7D2, p7D3, p7D4, # 19
               p7C1, p7C2, p7C3, p7C4, # 23
               p7Q1, p7Q2, p7Q3, p7Q4, # 27
               NFATpc, NFATpn, NFATNc, NFATNn, # 31
               DNA, DNA_TNF, mRNA,
               TNFa, TNFa_leak, TNFa_release, TNFa_release_total, maxflux, time] # 39

    return results

def plots(results,width,height,xlimlow,xlimhigh):
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
    TNFa, TNFa_leak, TNFa_release, TNFa_release_total, time] = results

    conv_MtouM = 10**6
    Cai = Cai*conv_MtouM

    ##################################################
    plt.figure(figsize=(width,height))
    plt.subplot(1,3,1)
    plt.tick_params(labelsize=12)
    plt.plot(time,Cai,'r-',label="[Ca]i")
    plt.xlabel("time (s)",fontsize=12)
    plt.ylabel("conc. [uM]",fontsize=12)
    plt.legend(loc=0,fontsize=12)
    plt.xlim(xlimlow,xlimhigh)
    plt.ylim(0,0.30)
    plt.tight_layout()
    ##################################################
    #ax = plt.subplot(1,3,1)
    #ax2 = ax.twinx()
    #plt.tick_params(labelsize=12)
    #lns1 = ax.plot(time,Cai,'r-',label="[Ca]i")
    #lns2 = ax2.plot(time,NFATNn,'b-',label="[NFATNn]")

    #ax.set_xlabel("time (s)",fontsize=12)
    #ax.set_ylabel("conc. [uM]",fontsize=12)
    #ax2.set_ylabel("conc. [nM]",fontsize=12)

    #lns = lns1+lns2
    #labs = [l.get_label() for l in lns]
    #ax.legend(lns, labs, loc=0, fontsize=12)
    plt.xlim(xlimlow,xlimhigh)
    plt.tight_layout()
    ##################################################
    #plt.figure(figsize=(width,height))
    #plt.subplot(1,2,1)
    #plt.tick_params(labelsize=12)
    #plt.plot(time,NFATpc,'b-',label="[NFATpc]")
    #plt.plot(time,NFATpn,'k.-',label="[NFATpn]")
    #plt.plot(time,NFATNc,'g-',label="[NFATNc]")
    #plt.plot(time,NFATNn,'r.-',label="[NFATNn]")
    #plt.xlabel("time (s)",fontsize=12)
    #plt.ylabel("conc. [nM]",fontsize=12)
    #plt.legend(loc=0,fontsize=12)
    #plt.xlim(xlimlow,xlimhigh)
    #plt.tight_layout()
    ##################################################
    #plt.subplot(1,2,2)
    #plt.tick_params(labelsize=12)
    #plt.plot(time,TNFa,'k--',label="TNFa in nucleus")
    #plt.xlabel("time (s)",fontsize=12)
    #plt.ylabel("molecules",fontsize=12)
    #plt.legend(loc=0,fontsize=12)
    #plt.xlim(xlimlow,xlimhigh)
    #plt.ylim(14,18)
    #plt.tight_layout()
    ##################################################
    #plt.figure(figsize=(width,height))
    #ax = plt.subplot(1,2,1)
    #ax2 = ax.twinx()
    #plt.tick_params(labelsize=12)

    #lns1 = ax.plot(time,TNFa,'k--',label="TNFa in nucleus")
    #lns2 = ax2.plot(time,NFATNn,'r-',label="[NFATNn]")
    #lns = lns1 + lns2
    #labs = [l.get_label() for l in lns]
    #ax.legend(lns,labs,loc=0, fontsize=12)

    #ax.set_xlabel("time (s)",fontsize=12)
    #ax.set_ylabel("molecules",fontsize=12)
    #ax2.set_ylabel("conc. [nM]",fontsize=12)
    #ax.set_ylim(14,18)
    #plt.xlim(xlimlow,xlimhigh)
    #plt.tight_layout()
    ##################################################
    #plt.subplot(1,2,2)
    #plt.tick_params(labelsize=12)
    #plt.plot(time,DNA,label="DNA")
    #plt.plot(time,DNA_TNF,label="DNA-TNF complex")
    #plt.plot(time,mRNA,label="mRNA")
    #plt.plot(time,TNFa,label="TNFa in nucleus")
    #plt.plot(time,TNFa_release,label="exocytosolic TNFa")
    #plt.xlabel("time (s)",fontsize=12)
    #plt.ylabel("molecules",fontsize=12)
    #plt.xlim(xlimlow,xlimhigh)
    #plt.ylim(0,55)
    #plt.legend(loc=0,fontsize=12)
    #plt.tight_layout()
    ##################################################
    #plt.figure(figsize=(width,height))
    ax = plt.subplot(1,3,2)
    ax2 = ax.twinx()
    plt.tick_params(labelsize=12)
    lns1 = ax.plot(time,Cai,'r-',label="[Cai]")
    lns2 = ax2.plot(time,TNFa_release_total,'k-',label="Total TNFa released")
    lns3 = ax2.plot(time,TNFa_leak,'b--',label="TNFa leak by Ca")
    lns4 = ax2.plot(time,TNFa_release,'g--',label='TNFa released by NFAT')
    ax.set_xlabel("time (s)",fontsize=12)
    ax.set_ylabel("conc. [uM]",fontsize=12)
    ax2.set_ylabel("molecules",fontsize=12)
    lns = lns1 + lns2 + lns3 + lns4
    labs = [l.get_label() for l in lns]
    ax.legend(lns,labs,loc=0, fontsize=12)
    plt.xlim(xlimlow,xlimhigh)

    ax = plt.subplot(1,3,3)
    ax2 = ax.twinx()
    plt.tick_params(labelsize=12)
    lns1 = ax.plot(time,NFATNn,'r-',label="[NFATNn]")
    lns2 = ax2.plot(time,TNFa_release_total,'k-',label="Total TNFa released")
    lns3 = ax2.plot(time,TNFa_leak,'b--',label="TNFa leak by Ca")
    lns4 = ax2.plot(time,TNFa_release,'g--',label='TNFa released by NFAT')
    ax.set_xlabel("time (s)",fontsize=12)
    ax.set_ylabel("conc. [nM]",fontsize=12)
    ax2.set_ylabel("molecules",fontsize=12)
    lns = lns1 + lns2 + lns3 + lns4
    labs = [l.get_label() for l in lns]
    ax.legend(lns,labs,loc=0, fontsize=12)
    plt.xlim(xlimlow,xlimhigh)

    plt.tight_layout()

    return
