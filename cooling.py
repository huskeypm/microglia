import numpy as np

class Params():
  def __init__(self, NFAT=None, pkh=False):
    self.Ccn = 50.0 # ratio of cytosol to nucleus
    self.K_dN = 1760.  # CaM binding coeff. [nM]  
    self.k_f1 = 7.69e-6
    self.k_r1 = 1.93e-2
    self.k_f2 = 1.44e-3
    self.k_f3 = 3.62e-4
    self.k_r3 = 4.71e-5
    self.k_f4 = 4.45e-4
    self.K_mN = 535.
    self.M = 6000.
    self.n = 2.92
    self.Ntot = 1000.
    self.CaMin  = 100. # [fixed]  nM 
    self.Ca = 100. # [variable] nM 
    self.NFATp_c = 9.83e-1  # nM
    self.NFATp_n = 2.76e-1
    self.NFATN_c =1.70e-3
    self.NFATN_n=5.09e-1

    # for Ca stuff
    self.removalRate = 0  #72.* .972 # [nM/m]
    self.eta = 0.2
    self.rateLCC = 30.
    self.vRate = 2.0

    # for voltage 
    self.period = 20.  # [s] 
    self.decay = 10.
    self.pulseAmplitude = 70 # [mV] 


    self.NFAT = NFAT# Need to define when used  

    if pkh==True:
      self.k_f1 = 2.69e-6 
      self.k_r3 =1.71e-5
      self.decay = 20.


# J1 only
#k_f2=0; k_f3=0; k_r3=0; k_f4=0;
p= Params()

def ActN(Ca):
    act_N = np.power(Ca, p.n) / (np.power(Ca, p.n) + np.power(p.K_mN, p.n) * (1  + p.K_dN / p.M))
    return act_N

def CalcNtot(Ca):
    return ActN(Ca)*p.Ntot

def CoolingNFAT(Ca,NFATp_c,NFATp_n,NFATN_c,NFATN_n):
    #print p.Ccn
    # fract activated CaN
    act_N = ActN(Ca)
    #act_N = 1.       
    
    # Cytosolic
    J1 = p.k_f1 * NFATp_c * p.Ntot * act_N - p.k_r1 * NFATN_c * (1 - act_N)
    J2 = p.k_f2 * NFATN_c
    # Nuclear
    J3 = p.k_f3 * NFATN_n * (1  - act_N) - p.k_r3 * NFATp_n * p.Ntot * act_N
    J4 = p.k_f4 * NFATp_n
    dNFATp_c_dt = J4 / p.Ccn - J1
    dNFATp_n_dt = J3 - J4
    dNFATN_c_dt = J1 - J2
    dNFATN_n_dt = J2 * p.Ccn - J3
    return dNFATp_c_dt,dNFATp_n_dt,dNFATN_c_dt,dNFATN_n_dt
#nuclearNFAT = NFATN_n + NFATp_n
def PKHNFAT(Ca,NFATp_c,NFATp_n,NFATN_c,NFATN_n):   
    1

