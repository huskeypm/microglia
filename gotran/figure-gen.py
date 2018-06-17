# This is "Plot Generator" and python2 is required due to the pickle files wrtten in python2 by gotran
# Author: Ben Chun
# README #
# Path of directories used in this script is customized for the author.
## Make sure the path of analyzeGotran pacakge and the pickle files generated as the outcome of gotran calculation

# routlines for analyzing odes
import sys
import pickle as pk
import numpy as np
sys.path.append('/home/AD/bch265/Dropbox/Postdoctoral2017-/Modeling-Codes/repo/pkh-code/fitting')
import analyzeGotran as ao
import matplotlib.pylab as plt

## P2X4 validation ## P2X4 validation ## P2X4 validation ## P2X4 validation ## P2X4 validation ## P2X4 validation
## Calculation results of P2X4
data1a = ao.readPickle("/home/AD/bch265/Data_storage/p2x4_Toulme30st_10uMATP_total_new_cat.pickle")
data2a = ao.readPickle("/home/AD/bch265/Data_storage/p2x4_Toulme30st_100uMATP_total_new_cat.pickle")
data3a = ao.readPickle("/home/AD/bch265/Data_storage/p2x4_Toulme30st_1000uMATP_total_new_cat.pickle")

# Toulme P2X4 MG ATP st 30s 100 uM
t_toulme = np.array([0,0.2040816327,1.734693878,4.693877551,8.571428571,13.7755102,24.08163265,34.69387755]) # in second
I_toulme = np.array([0,-366.8965517,-270.3448276,-171.0344828,-107.5862069,-57.93103448,-22.06896552,2.75862069]) # in pA

stateLabel = "I_f" # <- I_f uses literature membrane rev. potential whereas I_ptxf is the current to calculate Ca influx
subData1a = ao.GetData(data1a,stateLabel)
subData2a = ao.GetData(data2a,stateLabel)
subData3a = ao.GetData(data3a,stateLabel)

I_scaled_toulme = I_toulme/30 # This is reported in their paper as the effect of P2X4-HA expressions on the microglia cell membrane

plt.figure(figsize=(7,7),dpi=100)
plt.tick_params(labelsize=12)
plt.plot(t_toulme+1.2,I_scaled_toulme,'b--x',linewidth=1,markersize=10,label="Toulme et al. - 100 uM ATP")
plt.plot(subData1a.t,subData1a.valsIdx*(1e9),'r-',linewidth=1,label="Model - 10 uM ATP",alpha=1)
plt.plot(subData2a.t,subData2a.valsIdx*(1e9),'m-',linewidth=1,label="Model - 100 uM ATP",alpha=1)
plt.plot(subData3a.t,subData3a.valsIdx*(1e9),'g-',linewidth=1,label="Model - 1.0 mM ATP",alpha=1)

plt.plot([1.5,30+1.5],[0.2,0.2],'k',lw=5,label="ATP - Toulme") # this generates bar that indicates ATP application
plt.xlabel("time (s)",fontsize=15)
plt.ylabel("Inward Current (pA)",fontsize=15)
plt.ylim(-13.5,1)
#plt.yticks(np.arange(-400/30, 1, 100/30))
plt.xlim(0,40)
plt.tight_layout()
plt.legend(loc=0,fontsize=12)

plt.savefig("p2x4valid.png")

## P2X4: probability density distribution of states
stateLabel = "D1_ptxf"
subData1a1 = ao.GetData(data1a,stateLabel)
stateLabel = "D2_ptxf"
subData1a2 = ao.GetData(data1a,stateLabel)
stateLabel = "D3_ptxf"
subData1a3 = ao.GetData(data1a,stateLabel)
stateLabel = "D4_ptxf"
subData1a4 = ao.GetData(data1a,stateLabel)
stateLabel = "C1_ptxf"
subData1a5 = ao.GetData(data1a,stateLabel)
stateLabel = "C2_ptxf"
subData1a6 = ao.GetData(data1a,stateLabel)
stateLabel = "Q1_ptxf"
subData1a7 = ao.GetData(data1a,stateLabel)
stateLabel = "Q2_ptxf"
subData1a8 = ao.GetData(data1a,stateLabel)
stateLabel = "N_ptxf"
subData1a9 = ao.GetData(data1a,stateLabel)

plt.figure(figsize=(7,7),dpi=100)
plt.tick_params(labelsize=12)
plt.plot(subData1a1.t,subData1a1.valsIdx,'r-',linewidth=1,label="D1",alpha=1)
plt.plot(subData1a2.t,subData1a2.valsIdx,'r--',linewidth=1,label="D2",alpha=1)
plt.plot(subData1a3.t,subData1a3.valsIdx,'b-',linewidth=1,label="D3",alpha=1)
plt.plot(subData1a4.t,subData1a4.valsIdx,'b--',linewidth=1,label="D4",alpha=1)
plt.plot(subData1a5.t,subData1a5.valsIdx,'k-',linewidth=1,label="C1",alpha=1)
plt.plot(subData1a6.t,subData1a6.valsIdx,'k--',linewidth=1,label="C2",alpha=1)
plt.plot(subData1a7.t,subData1a7.valsIdx,'g-',linewidth=1,label="Q1",alpha=1)
plt.plot(subData1a8.t,subData1a8.valsIdx,'g--',linewidth=1,label="Q2",alpha=1)
plt.plot(subData1a9.t,subData1a9.valsIdx,'m-',linewidth=1,label="N",alpha=1)
plt.plot([1.5,30+1.5],[1.05,1.05],'k',lw=5,label="ATP")
plt.xlabel("time (s)",fontsize=15)
plt.ylabel("Probability of states",fontsize=15)
#plt.yticks(np.arange(-400, 1, 100))
plt.xlim(0,50)
plt.ylim(-0.1,1.1)
plt.tight_layout()
plt.legend(loc=0,fontsize=12)

plt.savefig("p2x4valid_state_prob_dist.png")

## P2X7 Validation ## P2X7 Validation ## P2X7 Validation ## P2X7 Validation ## P2X7 Validation ## P2X7 Validation
data2a = ao.readPickle("/home/AD/bch265/Data_storage/p2x7_Duan15st_100uMATP_total_cat.pickle")
data3a = ao.readPickle("/home/AD/bch265/Data_storage/p2x7_Duan15st_320uMATP_total_cat.pickle")
data4a = ao.readPickle("/home/AD/bch265/Data_storage/p2x7_Duan15st_1000uMATP_total_cat.pickle")

# Duan2003 P2X7 in microglia at 0.1 mM
t1=np.array([0, 1.52866242, 3.312101911, 6.751592357, 10.44585987,11.71974522]) # in second
y1=np.array([0,0,-28.94736842,-6.578947368,-1.315789474,0]) # in pA

# Duan2003 P2X7 in microglia at 0.3 mM
t2=np.array([0,1.146496815,6.878980892,13.75796178]) # in second
y2=np.array([0,-40.78947368,-28.94736842,-7.894736842]) # in pA

# Duan2003 P2X7 in microglia at 1 mM
t3=np.array([0,1.146496815,3.184713376,12.3566879,14.26751592]) # in second
y3=np.array([0,-46.05263158,-55.26315789,-36.84210526,0]) # in pA

stateLabel2 = "I_s" # <- I_s uses literature membrane rev. potential whereas I_ptxs is the current to calculate Ca influx
subData1a = ao.GetData(data2a,stateLabel2)
subData2a = ao.GetData(data3a,stateLabel2)
subData3a = ao.GetData(data4a,stateLabel2)

plt.figure(figsize=(7,7),dpi=100)
plt.tick_params(labelsize=12)
plt.plot(subData1a.t,subData1a.valsIdx*(10**9),'b-',label="Model - 100 uM ATP")
plt.plot(subData2a.t,subData2a.valsIdx*(10**9),'r-',label="Model - 320 uM ATP")
plt.plot(subData3a.t,subData3a.valsIdx*(10**9),'g-',label="Model - 1.0 mM ATP")
plt.plot(t1+1.5,y1,'b--x',label="Duan et al. - 100 uM ATP")
plt.plot(t2+1.5,y2,'r--x',label="Duan et al. - 320 uM ATP")
plt.plot(t3+1.5,y3,'g--x',label="Duan et al. - 1.0 mM ATP")
plt.plot([1.5,10+1.5],[3,3],'black',lw=5,label="ATP")
plt.xlabel("time (s)",fontsize=15)
plt.ylabel("Inward Current (pA)",fontsize=15)
plt.ylim(-61,5)
plt.xlim(0,20)
plt.legend(loc=0,fontsize=12)
plt.tight_layout()

plt.savefig("p2x7valid.png")


## P2X7: probability density distribution of states
data1a = ao.readPickle("/home/AD/bch265/Data_storage/p2x7_Duan15st_1000uMATP_total_cat.pickle")
stateLabel = "D1_ptxf"
subData1a1 = ao.GetData(data1a,stateLabel)
stateLabel = "D2_ptxf"
subData1a2 = ao.GetData(data1a,stateLabel)
stateLabel = "D3_ptxf"
subData1a3 = ao.GetData(data1a,stateLabel)
stateLabel = "D4_ptxf"
subData1a4 = ao.GetData(data1a,stateLabel)
stateLabel = "C1_ptxf"
subData1a5 = ao.GetData(data1a,stateLabel)
stateLabel = "C2_ptxf"
subData1a6 = ao.GetData(data1a,stateLabel)
stateLabel = "Q1_ptxf"
subData1a7 = ao.GetData(data1a,stateLabel)
stateLabel = "Q2_ptxf"
subData1a8 = ao.GetData(data1a,stateLabel)
stateLabel = "N_ptxf"
subData1a9 = ao.GetData(data1a,stateLabel)

plt.figure(figsize=(7,7),dpi=100)
plt.tick_params(labelsize=12)
plt.plot(subData1a1.t,subData1a1.valsIdx,'r-',linewidth=1,label="D1",alpha=1)
plt.plot(subData1a2.t,subData1a2.valsIdx,'r--',linewidth=1,label="D2",alpha=1)
plt.plot(subData1a3.t,subData1a3.valsIdx,'b-',linewidth=1,label="D3",alpha=1)
plt.plot(subData1a4.t,subData1a4.valsIdx,'b--',linewidth=1,label="D4",alpha=1)
plt.plot(subData1a5.t,subData1a5.valsIdx,'k-',linewidth=1,label="C1",alpha=1)
plt.plot(subData1a6.t,subData1a6.valsIdx,'k--',linewidth=1,label="C2",alpha=1)
plt.plot(subData1a7.t,subData1a7.valsIdx,'g-',linewidth=1,label="Q1",alpha=1)
plt.plot(subData1a8.t,subData1a8.valsIdx,'g--',linewidth=1,label="Q2",alpha=1)
plt.plot([1.5,10+1.5],[1.05,1.05],'k',lw=5,label="ATP")
plt.xlabel("time (s)",fontsize=15)
plt.ylabel("Probability of states",fontsize=15)
#plt.yticks(np.arange(-400, 1, 100))
plt.xlim(0,20)
plt.ylim(-0.1,1.1)
plt.tight_layout()
plt.legend(loc=0,fontsize=12)

plt.savefig("p2x7valid_state_prob_dist.png")


# Ca Transients Validation against Hide et al. # Ca Transients Validation against Hide et al. # Ca Transients Validation against Hide et al.
data0 = ao.readPickle("/home/AD/bch265/Data_storage/8min_MG_1mMATPtest_cat.pickle")
data1 = ao.readPickle("/home/AD/bch265/Data_storage/8min_MG_0.1mMATPtest_cat.pickle")
data2 = ao.readPickle("/home/AD/bch265/Data_storage/8min_MG_0.01mMATPtest_cat.pickle")
data3 = ao.readPickle("/home/AD/bch265/Data_storage/8min_MG_0mMATPtest_cat.pickle")

stateLabel = "Cai"
subData0 = ao.GetData(data0,stateLabel)
subData1 = ao.GetData(data1,stateLabel)
subData2 = ao.GetData(data2,stateLabel)
subData3 = ao.GetData(data3,stateLabel)

stateLabel = "Catot"
subData0a = ao.GetData(data0,stateLabel)
subData1a = ao.GetData(data1,stateLabel)
subData2a = ao.GetData(data2,stateLabel)
subData3a = ao.GetData(data3,stateLabel)

# Experimental data from Hide et al.: Calcium change profile
ly1 = np.array([0,0,27.10982659,36.41618497,17.80346821,-1.61849711,-6.473988439]) # in nM at 10 uM ATP
ly2 = np.array([0,-0.4046242775,46.93641618,35.60693642,35.20231214,39.65317919,39.65317919,17.39884393,10.92485549,7.283236994,4.450867052,3.641618497]) # in nM at 100 uM ATP
ly3 = np.array([0,0,52.60115607,26.70520231,27.10982659,25.89595376,21.44508671,19.01734104,16.99421965,16.99421965,16.1849711]) # in nM at 1.0 mM ATP

lt1 = np.array([0,1.185185185,1.259259259,1.703703704,2.296296296,3.407407407,7.62962963]) # in mins
lt2 = np.array([0,1.185185185,1.333333333,1.481481481,1.555555556,1.851851852,2.148148148,3.555555556,4.148148148,4.962962963,6.222222222,7.481481481]) # in mins
lt3 = np.array([0,1.407407407,1.555555556,1.777777778,2.074074074,2.37037037,2.740740741,2.962962963,3.925925926,6.592592593,7.703703704]) # in mins


plt.figure(figsize=(7,7),dpi=100)
ax = plt.subplot(1,1,1)
ax2 = ax.twinx()
ax.tick_params(labelsize=12)
ax2.tick_params(labelsize=12)

lns1 = ax.plot((subData0.t)/60+0.9,(subData0.valsIdx-subData3.valsIdx)*1000,
               'g-',linewidth=1.5,label="Model - 1.0 mM [ATP]")
lns2 = ax.plot((subData1.t)/60+0.9,(subData1.valsIdx-subData3.valsIdx)*1000,
               'b-',linewidth=1.5,label="Model - 100 uM [ATP]")
lns3 = ax.plot((subData2.t)/60+0.9,(subData2.valsIdx-subData3.valsIdx)*1000,
               'r-',linewidth=1.5,label="Model - 10 uM [ATP]")

lns4 = ax.plot(lt3-0.5,ly3,'g--',alpha=0.8,label="Hide et al. - 1.0 mM [ATP]")
lns5 = ax.plot(lt2-0.3,ly2,'b--',alpha=0.8,label="Hide et al. - 100 uM [ATP]")
lns6 = ax.plot(lt1-0.3,ly1,'r--',alpha=0.8,label="Hide et al. - 10 uM [ATP]")

lns7 = ax.plot([1,7.5],[-8,-8],'k',label='ATP',linewidth=7)

lns8 = ax2.plot((subData0a.t)/60+0.9,(subData0a.valsIdx-subData3a.valsIdx)/1000,
                'g:',linewidth=1.5,label="Total - 1.0 mM [ATP]",alpha=1)
lns9 = ax2.plot((subData1a.t)/60+0.9,(subData1a.valsIdx-subData3a.valsIdx)/1000,
                'b:',linewidth=1.5,label="Total - 100 uM [ATP]",alpha=1)
lns0 = ax2.plot((subData2a.t)/60+0.9,(subData2a.valsIdx-subData3a.valsIdx)/1000,
                'r:',linewidth=1.5,label="Total - 10 uM [ATP]",alpha=1)


ax.set_xlabel("time (min)",fontsize=15)
ax.set_ylabel("d[Ca] (nM)",fontsize=15)
ax2.set_ylabel("d[Ca]tot (mM)",fontsize=15)
ax.set_xlim(0/60,500/60)
ax2.set_ylim(-10,60)
lns = lns1 + lns2 + lns3 + lns4 + lns5 + lns6 + lns8 + lns9 + lns0 + lns7
labs = [l.get_label() for l in lns]
ax.legend(lns,labs,loc=0,fontsize=12)
plt.tight_layout()

plt.savefig("CaSigHide400secStim.png")


## Corresponding current profiles
stateLabel = "I_ptxf"
subData4 = ao.GetData(data0,stateLabel)
subData5 = ao.GetData(data1,stateLabel)
subData6 = ao.GetData(data2,stateLabel)

stateLabel = "I_ptxs"
subData8 = ao.GetData(data0,stateLabel)
subData9 = ao.GetData(data1,stateLabel)
subData10 = ao.GetData(data2,stateLabel)

plt.figure(figsize=(7,7),dpi=100)

plt.tick_params(labelsize=12)
plt.plot((subData0.t)/60,(subData4.valsIdx)*1e9*0.08,'g-',linewidth=1.5,label="P2X4 - 1.0 mM [ATP]",alpha=0.5)
plt.plot((subData1.t)/60,(subData5.valsIdx)*1e9*0.08,'b-',linewidth=1.5,label="P2X4 - 100 uM [ATP]",alpha=0.5)
plt.plot((subData2.t)/60,(subData6.valsIdx)*1e9*0.08,'r-',linewidth=1.5,label="P2X4 - 10 uM [ATP]",alpha=0.5)
plt.plot((subData0.t)/60,(subData8.valsIdx)*1e9*0.1,'g--',linewidth=1.5,label="P2X7 - 1.0 mM [ATP]")
plt.plot((subData1.t)/60,(subData9.valsIdx)*1e9*0.1,'b--',linewidth=1.5,label="P2X7 - 100 uM [ATP]")
plt.plot((subData2.t)/60,(subData10.valsIdx)*1e9*0.1,'r--',linewidth=1.5,label="P2X7 - 10 uM [ATP]")
plt.plot([0.1,6.6],[0.25,0.25],'k',label='ATP',linewidth=7)
plt.xlabel("time (min)",fontsize=15)
plt.ylabel("Inward Currents (pA)",fontsize=15)
plt.xlim(-0.2,460/60)
plt.legend(loc=0,fontsize=12)

plt.tight_layout()
plt.savefig("CurrentsHide400secStim.png")

## Corresponding Ca Conc. Change via P2X Channels
stateLabel1 = "Captxs"
subData11 = ao.GetData(data0,stateLabel1)
subData12 = ao.GetData(data1,stateLabel1)
subData13 = ao.GetData(data2,stateLabel1)
subData14 = ao.GetData(data3,stateLabel1)

stateLabel2 = "Captxf"
subData21 = ao.GetData(data0,stateLabel2)
subData22 = ao.GetData(data1,stateLabel2)
subData23 = ao.GetData(data2,stateLabel2)
subData24 = ao.GetData(data3,stateLabel2)

min11 = min(subData14.valsIdx)
min12 = min(subData14.valsIdx)
min13 = min(subData14.valsIdx)

min21 = min(subData24.valsIdx)
min22 = min(subData24.valsIdx)
min23 = min(subData24.valsIdx)

plt.figure(figsize=(7,7),dpi=100)
plt.tick_params(labelsize=12)

plt.plot((subData11.t)/60,(subData11.valsIdx-min11)/1000,'g-',linewidth=1.5,label="P2X7 - 1.0 mM [ATP]")
plt.plot((subData12.t)/60,(subData12.valsIdx-min12)/1000,'b-',linewidth=1.5,label="P2X7 - 100 uM [ATP]")
plt.plot((subData13.t)/60,(subData13.valsIdx-min13)/1000,'r-',linewidth=1.5,label="P2X7 - 10 uM [ATP]")
plt.plot((subData21.t)/60,(subData21.valsIdx-min21)/1000,'g--',linewidth=1.5,label="P2X4 - 1.0 mM [ATP]")
plt.plot((subData22.t)/60,(subData22.valsIdx-min22)/1000,'b--',linewidth=1.5,label="P2X4 - 100 uM [ATP]")
plt.plot((subData23.t)/60,(subData23.valsIdx-min23)/1000,'r--',linewidth=1.5,label="P2X4 - 10 uM [ATP]")

plt.plot([0,400/60],[-2,-2],'k',label='ATP',linewidth=7)

plt.legend(loc=0,fontsize=12)

plt.xlim(0,400/60)
plt.ylim(-5,50)

plt.xlabel("time (min)",fontsize=15)
plt.ylabel("[Ca] via P2X (mM)",fontsize=15)
plt.tight_layout()
plt.savefig("CaInViaP2XHide400secStim.png")


plt.figure(figsize=(7,7),dpi=100)
plt.tick_params(labelsize=12)

plt.plot((subData11.t)/60,(subData11.valsIdx-min11+subData21.valsIdx-min21)/1000,'g-',linewidth=1.5,label="1.0 mM [ATP]")
plt.plot((subData12.t)/60,(subData12.valsIdx-min12+subData22.valsIdx-min22)/1000,'b-',linewidth=1.5,label="100 uM [ATP]")
plt.plot((subData13.t)/60,(subData13.valsIdx-min13+subData23.valsIdx-min23)/1000,'r-',linewidth=1.5,label="10 uM [ATP]")

plt.plot([0,400/60],[-2,-2],'k',label='ATP',linewidth=7)

plt.legend(loc=0,fontsize=12)

plt.xlim(0,400/60)
plt.ylim(-5,50)

plt.xlabel("time (min)",fontsize=15)
plt.ylabel("[Ca] via P2X (mM)",fontsize=15)
plt.tight_layout()
plt.savefig("CaInViaP2XtotalHide400secStim.png")

# NFAT & TNFa validation - no pulse-tile stimulation in this case
data1 = ao.readPickle("/home/AD/bch265/Data_storage/1min_MG_1mMATP_cat.pickle") #
data2 = ao.readPickle("/home/AD/bch265/Data_storage/15min_MG_1mMATP_cat.pickle") #
data3 = ao.readPickle("/home/AD/bch265/Data_storage/30min_MG_1mMATP_cat.pickle") #
data4 = ao.readPickle("/home/AD/bch265/Data_storage/60min_MG_1mMATP_cat.pickle") #

data5 = ao.readPickle("/home/AD/bch265/Data_storage/1min_MG_3mMATP_cat.pickle") #
data6 = ao.readPickle("/home/AD/bch265/Data_storage/15min_MG_3mMATP_cat.pickle") #
data7 = ao.readPickle("/home/AD/bch265/Data_storage/30min_MG_3mMATP_cat.pickle") #
data8 = ao.readPickle("/home/AD/bch265/Data_storage/60min_MG_3mMATP_cat.pickle") #

data9 = ao.readPickle("/home/AD/bch265/Data_storage/15min_MG_0mMATP_cat.pickle") #
data10 = ao.readPickle("/home/AD/bch265/Data_storage/15min_MG_01mMATP_cat.pickle") #
data11 = ao.readPickle("/home/AD/bch265/Data_storage/15min_MG_05mMATP_cat.pickle") #
data12 = ao.readPickle("/home/AD/bch265/Data_storage/15min_MG_5mMATP_cat.pickle") #

data13 = ao.readPickle("/home/AD/bch265/Data_storage/5min_MG_1mMATP_cat.pickle") #
data14 = ao.readPickle("/home/AD/bch265/Data_storage/10min_MG_1mMATP_cat.pickle") #

data15 = ao.readPickle("/home/AD/bch265/Data_storage/5min_MG_3mMATP_cat.pickle") #
data16 = ao.readPickle("/home/AD/bch265/Data_storage/10min_MG_3mMATP_cat.pickle") #

data17 = ao.readPickle("/home/AD/bch265/Data_storage/180min_MG_001mMATP_cat.pickle") #
data18 = ao.readPickle("/home/AD/bch265/Data_storage/180min_MG_01mMATP_cat.pickle") #
data19 = ao.readPickle("/home/AD/bch265/Data_storage/180min_MG_1mMATP_cat.pickle") #

data26 = ao.readPickle("/home/AD/bch265/Data_storage/180min_MG_02mMATP_cat.pickle")
data29 = ao.readPickle("/home/AD/bch265/Data_storage/120min_MG_3mMATP_cat.pickle")
data30 = ao.readPickle("/home/AD/bch265/Data_storage/180min_MG_3mMATP_cat.pickle")
data31 = ao.readPickle("/home/AD/bch265/Data_storage/15min_MG_0mMATP_cat.pickle")
data0 = ao.readPickle("/home/AD/bch265/Data_storage/15min_MG_0mMATP_cat.pickle")


# NFAT change with respect to time of exposure
stateLabel = "NFATNn"
subData0 = ao.GetData(data8,stateLabel)

stateLabel = "NFATNc"
subData1a = ao.GetData(data8,stateLabel)

NFAT0 = subData0.valsIdx[1] + subData1a.valsIdx[1]
NFAT1 = subData0.valsIdx[60] + subData1a.valsIdx[60]
NFAT2 = subData0.valsIdx[5*60] + subData1a.valsIdx[5*60]
NFAT3 = subData0.valsIdx[10*60] + subData1a.valsIdx[10*60]
NFAT4 = subData0.valsIdx[15*60] + subData1a.valsIdx[15*60]
NFAT5 = subData0.valsIdx[30*60] + subData1a.valsIdx[30*60]
NFAT6 = subData0.valsIdx[60*60] + subData1a.valsIdx[60*60]

NFAT = np.array([NFAT0,NFAT1,NFAT2,NFAT3,NFAT4,NFAT5,NFAT6])
maxN = max(NFAT)
NFATr = NFAT/maxN

dura = np.array([0,1,5,10,15,30,60]) # in min
## Ferrari et al.
LitNFATr = np.array([0,0.26,0.95,1,0.95]) # in fraction
Littime = np.array([0,1,15,30,60]) # in min

plt.figure(figsize=(7,7),dpi=100)
plt.tick_params(labelsize=12)
plt.plot(dura,NFATr,'b-s',label="Model at 3 mM [ATP]")
plt.plot(Littime,LitNFATr,'r--s',label="Ferrari et al., at 3 mM [ATP]")

plt.xlim(-2,62)
plt.ylim(-0.05,1.05)

plt.legend(loc=0,fontsize=12)
plt.xlabel("ATP exposure time (min)",fontsize=15)
plt.ylabel("Dephosphorylated NFAT conc. (fraction of max)",fontsize=15)
plt.tight_layout()
plt.savefig("NFATvalidFerraritime.png")


# NFAT change with resepct to concentration of ATP
stateLabel = "NFATNn"
subData1 = ao.GetData(data9,stateLabel)
subData2 = ao.GetData(data10,stateLabel)
subData3 = ao.GetData(data11,stateLabel)
subData4 = ao.GetData(data2,stateLabel)
subData5 = ao.GetData(data6,stateLabel)
subData6 = ao.GetData(data12,stateLabel)

stateLabel = "NFATNc"
subData1a = ao.GetData(data9,stateLabel)
subData2a = ao.GetData(data10,stateLabel)
subData3a = ao.GetData(data11,stateLabel)
subData4a = ao.GetData(data2,stateLabel)
subData5a = ao.GetData(data6,stateLabel)
subData6a = ao.GetData(data12,stateLabel)


start = 0
end = 2000

NFAT1 = subData1.valsIdx[-1] + subData1a.valsIdx[-1]
NFAT2 = subData2.valsIdx[-1] + subData2a.valsIdx[-1]
NFAT3 = subData3.valsIdx[-1] + subData3a.valsIdx[-1]
NFAT4 = subData4.valsIdx[-1] + subData4a.valsIdx[-1]
NFAT5 = subData5.valsIdx[-1] + subData5a.valsIdx[-1]
NFAT6 = subData6.valsIdx[-1] + subData6a.valsIdx[-1]

NFAT = np.array([NFAT1,NFAT2,NFAT3,NFAT4,NFAT5,NFAT6])
maxN = max(NFAT)
NFATr = NFAT/maxN

ATPmM = np.array([0,0.1,0.5,1,3,5])
LitNFATr = np.array([0,0.05,0.1,0.5,1,0.3])

plt.figure(figsize=(7,7),dpi=100)
plt.tick_params(labelsize=12)
plt.plot(ATPmM,NFATr,'b-s',label="Model for 15 min")
plt.plot(ATPmM,LitNFATr,'r--s',label="Ferrari et. al., for 15 min")

plt.xlim(-0.1,5.1)
plt.ylim(-0.05,1.05)

plt.legend(loc=0,fontsize=12)
plt.xlabel("ATP conc. (mM)",fontsize=15)
plt.ylabel("Dephosphorylated NFAT conc. (fraction of max)",fontsize=15)
plt.tight_layout()
plt.savefig("NFATvalidFerrariconc.png")

## TNF validation vs. ATP conc
stateLabel = "TNFa"
subData0 = ao.GetData(data31,stateLabel)
subData1 = ao.GetData(data17,stateLabel)
subData2 = ao.GetData(data18,stateLabel)
subData3 = ao.GetData(data19,stateLabel)
subData4 = ao.GetData(data26,stateLabel)

tnfa0 = subData0.valsIdx[600]
tnfa1 = max(subData1.valsIdx)
tnfa2 = max(subData2.valsIdx)
tnfa3 = max(subData4.valsIdx)
tnfa4 = max(subData3.valsIdx)

tnfa = np.array([tnfa0, tnfa1, tnfa2, tnfa3, tnfa4])
maxtnfa = max(tnfa)
tnfar = tnfa/maxtnfa

## Hide's data
ATP1 = np.array([0.01,0.1,0.2,1])
ATP2 = np.array([0,0.01,0.1,0.2,1])
Hide = np.array([0.04,0.26,0.35,1])

plt.figure(figsize=(7,7),dpi=100)
plt.tick_params(labelsize=12)
plt.plot(ATP2,tnfar,'b-s',label="Model - 3 hr")
plt.plot(ATP1,Hide,'r--s',label="Hide et al. - 3 hr")

plt.xlim(-0.1,1.1)
plt.ylim(-0.02,1.02)

plt.legend(loc=0,fontsize=12)
plt.xlabel("[ATP] (mM)",fontsize=15)
plt.ylabel("TNFa synthesized (fraction of max)",fontsize=15)
plt.tight_layout()
plt.savefig("TNFavsATPHide.png")


## TNFa vs. time -> Hide
stateLabel = "TNFa"
subData3 = ao.GetData(data30,stateLabel)

tnfa1 = subData3.valsIdx[3600]
tnfa2 = subData3.valsIdx[7200]
tnfa3 = subData3.valsIdx[10800]

tnfar = np.array([0,tnfa1/tnfa3, tnfa2/tnfa3, tnfa3/tnfa3])
hrs = np.array([0,1,2,3])
Hide = np.array([0,0.054,0.54,1])

plt.figure(figsize=(7,7),dpi=100)
plt.tick_params(labelsize=12)
plt.plot(hrs,tnfar,'b-s',label="Model - 3 mM ATP")
plt.plot(hrs,Hide,'r--s',label="Hide et al. - 3 mM ATP")

plt.xlim(-0.2,3.2)
plt.ylim(-0.05,1.25)

plt.legend(loc=0,fontsize=12)
plt.xlabel("time (hr)",fontsize=15)
plt.ylabel("TNFa synthesized (fraction of max)",fontsize=15)
plt.tight_layout()
plt.savefig("TNFavsExpoTimeHide.png")

# p-p38 validation -> Hide and Trang

data0 = ao.readPickle("/home/AD/bch265/Data_storage/15min_MG_0mMATP_cat.pickle")
data1 = ao.readPickle("/home/AD/bch265/Data_storage/1min_MG_005mMATP_cat.pickle")
data2 = ao.readPickle("/home/AD/bch265/Data_storage/5min_MG_005mMATP_cat.pickle")
data3 = ao.readPickle("/home/AD/bch265/Data_storage/15min_MG_005mMATP_cat.pickle")
data4 = ao.readPickle("/home/AD/bch265/Data_storage/30min_MG_005mMATP_cat.pickle")
data5 = ao.readPickle("/home/AD/bch265/Data_storage/60min_MG_005mMATP_cat.pickle")

data6 = ao.readPickle("/home/AD/bch265/Data_storage/10min_MG_1mMATP_cat.pickle")
data7 = ao.readPickle("/home/AD/bch265/Data_storage/5min_MG_1mMATP_cat.pickle")
data8 = ao.readPickle("/home/AD/bch265/Data_storage/1min_MG_1mMATP_cat.pickle")

data9 = ao.readPickle("/home/AD/bch265/Data_storage/10min_MG_001mMATP_cat.pickle")
data10 = ao.readPickle("/home/AD/bch265/Data_storage/10min_MG_01mMATP_cat.pickle")
data11= ao.readPickle("/home/AD/bch265/Data_storage/10min_MG_1mMATP_cat.pickle")


stateLabel = "pp38"
subData0 = ao.GetData(data0,stateLabel)
subData1 = ao.GetData(data1,stateLabel)
subData2 = ao.GetData(data2,stateLabel)
subData3 = ao.GetData(data3,stateLabel)
subData4 = ao.GetData(data4,stateLabel)
subData5 = ao.GetData(data5,stateLabel)
subData6 = ao.GetData(data6,stateLabel)
subData7 = ao.GetData(data7,stateLabel)
subData8 = ao.GetData(data8,stateLabel)

pp380 = max(subData0.valsIdx)
pp381 = max(subData1.valsIdx)
pp382 = max(subData2.valsIdx)
pp383 = max(subData3.valsIdx)
pp384 = max(subData4.valsIdx)
pp385 = max(subData5.valsIdx)

pp386 = max(subData6.valsIdx)
pp387 = max(subData7.valsIdx)
pp388 = max(subData8.valsIdx)

pp38 = np.array([pp380,pp381,pp382,pp383,pp384,pp385])
maxN = max(pp38)
pp38r = pp38/maxN

pp38hide = np.array([pp380,pp388,pp387,pp386])
maxN2 = max(pp38hide)
pp38r2 = pp38hide/maxN2
Expt = np.array([0,1,5,15,30,60])
Expt2 = np.array([0,1,5,10])
Litr2 = np.array([0.7,0.8,0.95,1])# Hide
Litr = np.array([0.94,1]) # Trang
Litt = np.array([5,60]) # Trang

plt.figure(figsize=(7,7),dpi=100)
plt.tick_params(labelsize=12)
#plt.plot(Expt,pp38r,'r-s',label="Model at 50 uM ATP")
#plt.plot([5,60],[0.94,1],'r--s',label="Trang et al., at 50 uM ATP")
#plt.plot(60,1,'r--o',label="Trang et al., at 50 uM ATP")
plt.plot(Expt2,pp38r2,'b-s',label="Model at 1 mM ATP")
plt.plot(Expt2,Litr2,'r--s',label="Hide et al., 1 mM ATP")
plt.legend(loc=0,fontsize=12)
plt.ylim(0.45,1.05)
plt.xlim(-1,11)
plt.tight_layout()
plt.xlabel("ATP exposure time (min)",fontsize=15)
plt.ylabel("Relative pp38 amount (Fraction of max)",fontsize=15)
plt.savefig("pp38validHidetime.png")

stateLabel = "pp38"
subData0 = ao.GetData(data0,stateLabel)
subData1 = ao.GetData(data1,stateLabel)
subData2 = ao.GetData(data2,stateLabel)
subData3 = ao.GetData(data3,stateLabel)
subData4 = ao.GetData(data4,stateLabel)
subData5 = ao.GetData(data5,stateLabel)
subData6 = ao.GetData(data6,stateLabel)
subData7 = ao.GetData(data7,stateLabel)
subData8 = ao.GetData(data8,stateLabel)

pp380 = max(subData0.valsIdx)
pp381 = max(subData1.valsIdx)
pp382 = max(subData2.valsIdx)
pp383 = max(subData3.valsIdx)
pp384 = max(subData4.valsIdx)
pp385 = max(subData5.valsIdx)

pp386 = max(subData6.valsIdx)
pp387 = max(subData7.valsIdx)
pp388 = max(subData8.valsIdx)

pp38 = np.array([pp380,pp381,pp382,pp383,pp384,pp385])
maxN = max(pp38)
pp38r = pp38/maxN

pp38hide = np.array([pp380,pp388,pp387,pp386])
maxN2 = max(pp38hide)
pp38r2 = pp38hide/maxN2
Expt = np.array([0,1,5,15,30,60])
Expt2 = np.array([0,1,5,10])
Litr2 = np.array([0.7,0.8,0.95,1])# Hide
Litr = np.array([0.94,1]) # Trang
Litt = np.array([5,60]) # Trang

plt.figure(figsize=(7,7),dpi=100)
plt.tick_params(labelsize=12)
plt.plot(Expt,pp38r,'b-s',label="Model at 50 uM ATP")
plt.plot([5,60],[0.94,1],'r--s',label="Trang et al., at 50 uM ATP")
#plt.plot(60,1,'r--o',label="Trang et al., at 50 uM ATP")
#plt.plot(Expt2,pp38r2,'b-s',label="Model at 1 mM ATP")
#plt.plot(Expt2,Litr2,'b--s',label="Hide et al., 1 mM ATP")
plt.legend(loc=0,fontsize=12)
plt.ylim(0.75,1.05)
plt.xlim(-2,62)
plt.tight_layout()
plt.xlabel("ATP exposure time (min)",fontsize=15)
plt.ylabel("Relative pp38 amount (Fraction of max)",fontsize=15)
plt.savefig("pp38vsEpT50uMATPTrang.png")
