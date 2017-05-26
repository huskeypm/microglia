Ccn = 50.0
#Kd1 = 1760
per_sec_to_per_ms =1 # Nevermind for now / 1e-3
K_dN = 1760.
k_f1 = 7.69e-6*per_sec_to_per_ms
k_r1 = 1.93e-2*per_sec_to_per_ms
k_f2 = 1.44e-3*per_sec_to_per_ms
k_f3 = 3.62e-4*per_sec_to_per_ms
k_r3 = 4.71e-5*per_sec_to_per_ms
k_f4 = 4.45e-4*per_sec_to_per_ms
K_mN = 535.
M = 6000.
n = 2.92
Ntot = 1000.
Ca = 100. # nM 
NFATp_c = 9.83e-1  # nM
NFATp_n = 2.76e-1
NFATN_c =1.70e-3
NFATN_n=5.09e-1

# J1 only
#k_f2=0; k_f3=0; k_r3=0; k_f4=0;

def ActN(Ca):
    act_N = np.power(Ca, n) / (np.power(Ca, n) + np.power(K_mN, n) * (1  + K_dN / M))
    return act_N

def Cooling(Ca,NFATp_c,NFATp_n,NFATN_c,NFATN_n):
    # fract activated N
    act_N = ActN(Ca)
    act_N = 1
    J1 = k_f1 * NFATp_c * Ntot * act_N - k_r1 * NFATN_c * (1 - act_N)
    J2 = k_f2 * NFATN_c
    J3 = k_f3 * NFATN_n * (1  - act_N) - k_r3 * NFATp_n * Ntot * act_N
    J4 = k_f4 * NFATp_n
    dNFATp_c_dt = J4 / Ccn - J1
    dNFATp_n_dt = J3 - J4
    dNFATN_c_dt = J1 - J2
    dNFATN_n_dt = J2 * Ccn - J3
    return dNFATp_c_dt,dNFATp_n_dt,dNFATN_c_dt,dNFATN_n_dt
#nuclearNFAT = NFATN_n + NFATp_n

