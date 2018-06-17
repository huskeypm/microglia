#!/bin/bash

#export LOC=/home/bch265/sources
#export MYPATH=$LOC/mypython
#export PYTHONPATH=$PYTHONPATH:/home/bch265/.local/lib/python2.7/site-packages/

#python2.7 -c "import instant"
#python2.7 -c "import modelparameters"
#python2.7 -c "import gotran"

cd /home/bch265/microglia/microglia/fitting


############## Control Panel #####################

export ODEFILEshort=microgliav54_lumped.ode
export ODEFILEfitted=microgliav20-fitted.ode

ptxvalidfitted=0
ptxvalid=1  ### <---- 0 = OFF and 1 = ON

caivalidfitted=0 ### 8 min ST validation (Hide data related)
caivalid=0
caitested=1

no=0        ### No stimulation

dura=0      ### Duration variation
freq=0      ### Frequency variation
sens1=0      ### Sensitivity Analysis
sens2=0
sens3=0

leng=0      ### Lengthy Stimulation
CaN=0      ### Special Edition for CaN Validation

#####################################
# for the periodicity control
# check the google spreadsheet
# https://docs.google.com/spreadsheets/d/1UpXEe90q5Tlcu7qWv07B5SrVTGP-gYaGT6FGdsQigr8/edit?usp=sharing
# test with pulse control tester
# microglia/gotran/Pulse-control-tester.ipynb in Bitbucket
# P2X Validation ####################

## Test Zone
#python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 10800000 -iters 1 -var pulse_switch 0 -var stim_amplitude 3000 -name ~/Data_storage/180min_MG_3mMATP_test
###

if [ $ptxvalidfitted -eq 1 ]
then
  echo "Validation of P2X-fitted is ON" # This code needs to be fixed ( millisecond time unit )
  python2.7 daisychain.py -dt 0.1 -dSr 1000 -jit -odeName $ODEFILEfitted -T 500e3 -iters 1 -var V_ptxf -0.06 -var stim_amplitude 100 -var stim_period 300e3 -var stim_gap1 250e3 -var stim_gap2 250e3 -var stim_low 1e3 -var stim_high 50e3 -name ~/Data_storage/p2x4_MacKay50st_100uMATP_new
  python2.7 daisychain.py -dt 0.1 -dSr 1000 -jit -odeName $ODEFILEfitted -T 500e3 -iters 1 -var V_ptxf -0.06 -var stim_amplitude 100 -var stim_period 300e3 -var stim_gap1 270e3 -var stim_gap2 270e3 -var stim_low 1e3 -var stim_high 30e3 -name ~/Data_storage/p2x4_Toulme30st_100uMATP_new
fi

if [ $ptxvalid -eq 1 ]
then
  echo "Validation of P2X is ON" # This code needs to be fixed ( millisecond time unit )
  python2.7 daisychain.py -dt 0.1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200e3 -iters 1 -var V_ptxs -0.04 -var stim_amplitude 100 -var stim_period 60e3 -var stim_gap1 50e3 -var stim_gap2 50e3 -var stim_low 1e3 -var stim_high 10e3 -name ~/Data_storage/p2x7_Duan15st_100uMATP_lumped &
  python2.7 daisychain.py -dt 0.1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200e3 -iters 1 -var V_ptxs -0.04 -var stim_amplitude 320 -var stim_period 60e3 -var stim_gap1 50e3 -var stim_gap2 50e3 -var stim_low 1e3 -var stim_high 10e3 -name ~/Data_storage/p2x7_Duan15st_320uMATP_lumped &
  python2.7 daisychain.py -dt 0.1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200e3 -iters 1 -var V_ptxs -0.04 -var stim_amplitude 1000 -var stim_period 60e3 -var stim_gap1 50e3 -var stim_gap2 50e3 -var stim_low 1e3 -var stim_high 10e3 -name ~/Data_storage/p2x7_Duan15st_1000uMATP_lumped &
  python2.7 daisychain.py -dt 0.1 -dSr 1000 -jit -odeName $ODEFILEshort -T 500e3 -iters 1 -var V_ptxf -0.06 -var stim_amplitude 10 -var stim_period 300e3 -var stim_gap1 270e3 -var stim_gap2 270e3 -var stim_low 1e3 -var stim_high 30e3 -name ~/Data_storage/p2x4_Toulme30st_10uMATP_total_lumped &
  python2.7 daisychain.py -dt 0.1 -dSr 1000 -jit -odeName $ODEFILEshort -T 500e3 -iters 1 -var V_ptxf -0.06 -var stim_amplitude 100 -var stim_period 300e3 -var stim_gap1 270e3 -var stim_gap2 270e3 -var stim_low 1e3 -var stim_high 30e3 -name ~/Data_storage/p2x4_Toulme30st_100uMATP_total_lumped &
  python2.7 daisychain.py -dt 0.1 -dSr 1000 -jit -odeName $ODEFILEshort -T 500e3 -iters 1 -var V_ptxf -0.06 -var stim_amplitude 1000 -var stim_period 300e3 -var stim_gap1 270e3 -var stim_gap2 270e3 -var stim_low 1e3 -var stim_high 30e3 -name ~/Data_storage/p2x4_Toulme30st_1000uMATP_total_lumped 
# Lit Data
# Toulme P2X4 MG ATP st 30s 100 uM
#time = np.array([0,0.2040816327,1.734693878,4.693877551,8.571428571,13.7755102,24.08163265,34.69387755]) # in second
#current = np.array([0,-366.8965517,-270.3448276,-171.0344828,-107.5862069,-57.93103448,-22.06896552,2.75862069]) # in pA

fi

if [ $no -eq 1 ]
then
  echo "No stimulation is ON"
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var pulse_switch 0 -var stim_amplitude 0 -name ~/Data_storage/MG_0mMATP
fi

if [ $caivalidfitted -eq 1 ]
then
  echo "Validation of Cai is ON"
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEfitted -T 2000000 -iters 1 -var stim_period 800e3 -var stim_gap1 400e3 -var stim_gap2 750e3 -var stim_low 1e3 -var stim_high 400e3 -var stim_amplitude 1000 -name ~/Data_storage/8min_MG_1mMATP_fitted
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEfitted -T 2000000 -iters 1 -var stim_period 800e3 -var stim_gap1 400e3 -var stim_gap2 750e3 -var stim_low 1e3 -var stim_high 400e3 -var stim_amplitude 100 -name ~/Data_storage/8min_MG_0.1mMATP_fitted
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEfitted -T 2000000 -iters 1 -var stim_period 800e3 -var stim_gap1 400e3 -var stim_gap2 750e3 -var stim_low 1e3 -var stim_high 400e3 -var stim_amplitude 10 -name ~/Data_storage/8min_MG_0.01mMATP_fitted
fi

if [ $caivalid -eq 1 ]
then
  echo "Validation of Cai is ON"
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 2000000 -iters 1 -var stim_period 800e3 -var stim_gap1 400e3 -var stim_gap2 750e3 -var stim_low 1e3 -var stim_high 400e3 -var stim_amplitude 1000 -name ~/Data_storage/8min_MG_1mMATP &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 2000000 -iters 1 -var stim_period 800e3 -var stim_gap1 400e3 -var stim_gap2 750e3 -var stim_low 1e3 -var stim_high 400e3 -var stim_amplitude 100 -name ~/Data_storage/8min_MG_0.1mMATP &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 2000000 -iters 1 -var stim_period 800e3 -var stim_gap1 400e3 -var stim_gap2 750e3 -var stim_low 1e3 -var stim_high 400e3 -var stim_amplitude 10 -name ~/Data_storage/8min_MG_0.01mMATP &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 2000000 -iters 1 -var stim_period 800e3 -var stim_gap1 400e3 -var stim_gap2 750e3 -var stim_low 1e3 -var stim_high 400e3 -var stim_amplitude 0 -name ~/Data_storage/8min_MG_0mMATP
fi

if [ $caitested -eq 1 ]
then
  echo "Validation of Cai is ON"
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 2000000 -iters 1 -var stim_period 800e3 -var stim_gap1 400e3 -var stim_gap2 750e3 -var stim_low 1e3 -var stim_high 400e3 -var stim_amplitude 1000 -name ~/Data_storage/8min_MG_1mMATPlumped &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 2000000 -iters 1 -var stim_period 800e3 -var stim_gap1 400e3 -var stim_gap2 750e3 -var stim_low 1e3 -var stim_high 400e3 -var stim_amplitude 100 -name ~/Data_storage/8min_MG_0.1mMATPlumped &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 2000000 -iters 1 -var stim_period 800e3 -var stim_gap1 400e3 -var stim_gap2 750e3 -var stim_low 1e3 -var stim_high 400e3 -var stim_amplitude 10 -name ~/Data_storage/8min_MG_0.01mMATPlumped &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 2000000 -iters 1 -var stim_period 800e3 -var stim_gap1 400e3 -var stim_gap2 750e3 -var stim_low 1e3 -var stim_high 400e3 -var stim_amplitude 0 -name ~/Data_storage/8min_MG_0mMATPlumped
fi


if [ $CaN -eq 1 ]
then
  echo "Validation of CaN is ON"

  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 500000 -iters 1 -var stim_period 2e3 -var stim_gap1 1e3 -var stim_gap2 1e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 1000 -name ~/Data_storage/1st1rsMGCaN_1mMATPnew
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 500000 -iters 1 -var stim_period 201e3 -var stim_gap1 200e3 -var stim_gap2 200e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 1000 -name ~/Data_storage/1st200rsMGCaN_1mMATPnew

fi
#####################################

#####################################

# Make sure your pre_rest is less than 500; otherwise, the calculation may crash.
# -var pre_rest 100
# Various duration with broad spacing at 1 mM ATP: 1,2,5, and 10 are only size working in this model due to periodic equation

if [ $dura -eq 1 ]
then
 echo "Duration variation is ON"

  # Various duration with broad spacing at 1 mM ATP: 1,2,5, and 10 are only size working in this model due to periodic equation

  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 19e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 1000 -name ~/Data_storage/1st19rsMG_1mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 15e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 5e3 -var stim_amplitude 1000 -name ~/Data_storage/5st15rsMG_1mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 10e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 10e3 -var stim_amplitude 1000 -name ~/Data_storage/10st10rsMG_1mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 5e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 15e3 -var stim_amplitude 1000 -name ~/Data_storage/15st5rsMG_1mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 1e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 19e3 -var stim_amplitude 1000 -name ~/Data_storage/19st1rsMG_1mMATPnew


  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 19e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 100 -name ~/Data_storage/1st19rsMG_0.1mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 15e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 5e3 -var stim_amplitude 100 -name ~/Data_storage/5st15rsMG_0.1mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 10e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 10e3 -var stim_amplitude 100 -name ~/Data_storage/10st10rsMG_0.1mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 5e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 15e3 -var stim_amplitude 100 -name ~/Data_storage/15st5rsMG_0.1mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 1e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 19e3 -var stim_amplitude 100 -name ~/Data_storage/19st1rsMG_0.1mMATPnew


  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 19e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 10 -name ~/Data_storage/1st19rsMG_0.01mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 15e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 5e3 -var stim_amplitude 10 -name ~/Data_storage/5st15rsMG_0.01mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 10e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 10e3 -var stim_amplitude 10 -name ~/Data_storage/10st10rsMG_0.01mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 5e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 15e3 -var stim_amplitude 10 -name ~/Data_storage/15st5rsMG_0.01mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 1e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 19e3 -var stim_amplitude 10 -name ~/Data_storage/19st1rsMG_0.01mMATPnew


  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 19e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 1 -name ~/Data_storage/1st19rsMG_0.001mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 15e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 5e3 -var stim_amplitude 1 -name ~/Data_storage/5st15rsMG_0.001mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 10e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 10e3 -var stim_amplitude 1 -name ~/Data_storage/10st10rsMG_0.001mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 5e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 15e3 -var stim_amplitude 1 -name ~/Data_storage/15st5rsMG_0.001mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 1e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 19e3 -var stim_amplitude 1 -name ~/Data_storage/19st1rsMG_0.001mMATPnew

#  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var pulse_switch 0 -var stim_amplitude 0 -name ~/Data_storage/180min_MG_0mMATP

fi

if [ $freq -eq 1 ]
then
  echo "Frequency variation is ON"
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 2e3 -var stim_gap1 1e3 -var stim_gap2 1e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 1000 -name ~/Data_storage/1st1rsMG_1mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 5e3 -var stim_gap1 4e3 -var stim_gap2 4e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 1000 -name ~/Data_storage/1st4rsMG_1mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 10e3 -var stim_gap1 9e3 -var stim_gap2 9e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 1000 -name ~/Data_storage/1st9rsMG_1mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 19e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 1000 -name ~/Data_storage/1st19rsMG_1mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 30e3 -var stim_gap1 29e3 -var stim_gap2 29e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 1000 -name ~/Data_storage/1st29rsMG_1mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 50e3 -var stim_gap1 49e3 -var stim_gap2 49e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 1000 -name ~/Data_storage/1st49rsMG_1mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 60e3 -var stim_gap1 59e3 -var stim_gap2 59e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 1000 -name ~/Data_storage/1st59rsMG_1mMATPnew

  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 2e3 -var stim_gap1 1e3 -var stim_gap2 1e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 100 -name ~/Data_storage/1st1rsMG_0.1mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 5e3 -var stim_gap1 4e3 -var stim_gap2 4e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 100 -name ~/Data_storage/1st4rsMG_0.1mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 10e3 -var stim_gap1 9e3 -var stim_gap2 9e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 100 -name ~/Data_storage/1st9rsMG_0.1mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 19e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 100 -name ~/Data_storage/1st19rsMG_0.1mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 30e3 -var stim_gap1 29e3 -var stim_gap2 29e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 100 -name ~/Data_storage/1st29rsMG_0.1mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 50e3 -var stim_gap1 49e3 -var stim_gap2 49e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 100 -name ~/Data_storage/1st49rsMG_0.1mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 60e3 -var stim_gap1 59e3 -var stim_gap2 59e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 100 -name ~/Data_storage/1st59rsMG_0.1mMATPnew

  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 2e3 -var stim_gap1 1e3 -var stim_gap2 1e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 10 -name ~/Data_storage/1st1rsMG_0.01mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 5e3 -var stim_gap1 4e3 -var stim_gap2 4e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 10 -name ~/Data_storage/1st4rsMG_0.01mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 10e3 -var stim_gap1 9e3 -var stim_gap2 9e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 10 -name ~/Data_storage/1st9rsMG_0.01mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 19e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 10 -name ~/Data_storage/1st19rsMG_0.01mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 30e3 -var stim_gap1 29e3 -var stim_gap2 29e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 10 -name ~/Data_storage/1st29rsMG_0.01mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 50e3 -var stim_gap1 49e3 -var stim_gap2 49e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 10 -name ~/Data_storage/1st49rsMG_0.01mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 60e3 -var stim_gap1 59e3 -var stim_gap2 59e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 10 -name ~/Data_storage/1st59rsMG_0.01mMATPnew

  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 2e3 -var stim_gap1 1e3 -var stim_gap2 1e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 1 -name ~/Data_storage/1st1rsMG_0.001mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 5e3 -var stim_gap1 4e3 -var stim_gap2 4e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 1 -name ~/Data_storage/1st4rsMG_0.001mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 10e3 -var stim_gap1 9e3 -var stim_gap2 9e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 1 -name ~/Data_storage/1st9rsMG_0.001mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 20e3 -var stim_gap1 19e3 -var stim_gap2 19e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 1 -name ~/Data_storage/1st19rsMG_0.001mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 30e3 -var stim_gap1 29e3 -var stim_gap2 29e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 1 -name ~/Data_storage/1st29rsMG_0.001mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 50e3 -var stim_gap1 49e3 -var stim_gap2 49e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 1 -name ~/Data_storage/1st49rsMG_0.001mMATPnew &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_period 60e3 -var stim_gap1 59e3 -var stim_gap2 59e3 -var stim_low 1e3 -var stim_high 2e3 -var stim_amplitude 1 -name ~/Data_storage/1st59rsMG_0.001mMATPnew

fi

if [ $rest -eq 1 ]
then
  echo "Resting variation is ON"


fi

### SENSITIVITY ANALYSIS ###
if [ $sens1 -eq 1 ]
then
array[0]=".01"
array[1]=".1"
array[2]=".2"
array[3]=".3"
array[4]=".4"
array[5]=".5"
array[6]=".6"
array[7]=".7"
array[8]=".8"
array[9]=".9"
array[10]=1
array[11]=2
array[12]=3
array[13]=4
array[14]=5
array[15]=6
array[16]=7
array[17]=8
array[18]=9
array[19]=10

  for ATP in 1000 100
    do

    for SA in SAca SAnfat SAptxs SAptxf SAcm SAnancx #SAcn
      do

        for  (( i=0; i<=19; i++))
          do

          python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_amplitude $ATP -var $SA ${array[$i]} -var stim_period 2e3 -var stim_gap1 1e3 -var stim_gap2 1e3 -var stim_low 1e3 -var stim_high 2e3 -name ~/Data_storage/SA-$SA-${array[$i]}-$ATP

          done

      done

    done

fi

if [ $sens2 -eq 1 ]
then
array[0]=".001" #".01"
array[1]=".01" #".1"
array[2]=".03" #".2"
array[3]=".06" #".3"
array[4]=".09" #".4"
array[5]=".1" #".5"
array[6]=".3" #".6"
array[7]=".6" #".7"
array[8]=".9" #".8"
array[9]=1 #".9"
array[10]="1.3" #1
array[11]="1.6" #2
array[12]="1.9" #3
array[13]="2.2" #4
array[14]="2.5" #5
array[15]="2.9" #6
array[16]="3.2" #7
array[17]="4.5" #8
array[18]=5 #9
array[19]=10

  for ATP in 1000 100
    do

    for SA in SAcn
      do

        for  (( i=0; i<=19; i++))
          do

          python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_amplitude $ATP -var $SA ${array[$i]} -var stim_period 2e3 -var stim_gap1 1e3 -var stim_gap2 1e3 -var stim_low 1e3 -var stim_high 2e3 -name ~/Data_storage/SA-$SA-${array[$i]}-$ATP

          done

      done

    done

fi

### SENSITIVITY ANALYSIS ###
if [ $sens3 -eq 1 ]
then
array[0]=".01"
array[1]=".1"
array[2]=".2"
array[3]=".3"
array[4]=".4"
array[5]=".5"
array[6]=".6"
array[7]=".7"
array[8]=".8"
array[9]=".9"
array[10]=1
array[11]=2
array[12]=3
array[13]=4
array[14]=5
array[15]=6
array[16]=7
array[17]=8
array[18]=9
array[19]=10

  for ATP in 1000 100
    do

    for SA in SApp38
      do

        for  (( i=0; i<=19; i++))
          do

          python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 200000 -iters 1 -var stim_amplitude $ATP -var $SA ${array[$i]} -var stim_period 2e3 -var stim_gap1 1e3 -var stim_gap2 1e3 -var stim_low 1e3 -var stim_high 2e3 -name ~/Data_storage/SA-$SA-${array[$i]}-$ATP

          done

      done

    done

fi


### LENGTHY Stimulation ###

if [ $leng -eq 1 ]
then
  echo "Lengthy Stimulation is ON"

  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 120000 -iters 1 -var pulse_switch 0 -var stim_amplitude 1000 -name ~/Data_storage/1min_MG_1mMATP
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 300000 -iters 1 -var pulse_switch 0 -var stim_amplitude 1000 -name ~/Data_storage/5min_MG_1mMATP &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 600000 -iters 1 -var pulse_switch 0 -var stim_amplitude 1000 -name ~/Data_storage/10min_MG_1mMATP
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 900000 -iters 1 -var pulse_switch 0 -var stim_amplitude 1000 -name ~/Data_storage/15min_MG_1mMATP &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 1800000 -iters 1 -var pulse_switch 0 -var stim_amplitude 1000 -name ~/Data_storage/30min_MG_1mMATP
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var pulse_switch 0 -var stim_amplitude 1000 -name ~/Data_storage/60min_MG_1mMATP &

  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 120000 -iters 1 -var pulse_switch 0 -var  stim_amplitude 3000 -name ~/Data_storage/1min_MG_3mMATP
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 300000 -iters 1 -var pulse_switch 0 -var stim_amplitude 3000 -name ~/Data_storage/5min_MG_3mMATP &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 600000 -iters 1 -var pulse_switch 0 -var stim_amplitude 3000 -name ~/Data_storage/10min_MG_3mMATP
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 900000 -iters 1 -var pulse_switch 0 -var stim_amplitude 3000 -name ~/Data_storage/15min_MG_3mMATP &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 1800000 -iters 1 -var pulse_switch 0 -var stim_amplitude 3000 -name ~/Data_storage/30min_MG_3mMATP
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var pulse_switch 0 -var stim_amplitude 3000 -name ~/Data_storage/60min_MG_3mMATP &

  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 900000 -iters 1 -var pulse_switch 0 -var stim_amplitude 0 -name ~/Data_storage/15min_MG_0mMATP
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 900000 -iters 1 -var pulse_switch 0 -var stim_amplitude 100 -name ~/Data_storage/15min_MG_01mMATP &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 900000 -iters 1 -var pulse_switch 0 -var stim_amplitude 500 -name ~/Data_storage/15min_MG_05mMATP
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 900000 -iters 1 -var pulse_switch 0 -var stim_amplitude 5000 -name ~/Data_storage/15min_MG_5mMATP &

  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 10800000 -iters 1 -var pulse_switch 0 -var stim_amplitude 10 -name ~/Data_storage/180min_MG_001mMATP
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 10800000 -iters 1 -var pulse_switch 0 -var stim_amplitude 100 -name ~/Data_storage/180min_MG_01mMATP &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 10800000 -iters 1 -var pulse_switch 0 -var stim_amplitude 1000 -name ~/Data_storage/180min_MG_1mMATP

  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 7200000 -iters 1 -var pulse_switch 0 -var stim_amplitude 3000 -name ~/Data_storage/120min_MG_3mMATP &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 10800000 -iters 1 -var pulse_switch 0 -var stim_amplitude 3000 -name ~/Data_storage/180min_MG_3mMATP

  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var pulse_switch 0 -var stim_amplitude 10 -name ~/Data_storage/60min_MG_001mMATP &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var pulse_switch 0 -var stim_amplitude 100 -name ~/Data_storage/60min_MG_01mMATP

  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 10800000 -iters 1 -var pulse_switch 0 -var stim_amplitude 200 -name ~/Data_storage/180min_MG_02mMATP &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var pulse_switch 0 -var stim_amplitude 200 -name ~/Data_storage/60min_MG_02mMATP

  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var pulse_switch 0 -var stim_amplitude 50 -name ~/Data_storage/60min_MG_005mMATP &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 120000 -iters 1 -var pulse_switch 0 -var stim_amplitude 50 -name ~/Data_storage/1min_MG_005mMATP
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 1800000 -iters 1 -var pulse_switch 0 -var stim_amplitude 50 -name ~/Data_storage/30min_MG_005mMATP &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 300000 -iters 1 -var pulse_switch 0 -var stim_amplitude 50 -name ~/Data_storage/5min_MG_005mMATP
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 600000 -iters 1 -var pulse_switch 0 -var stim_amplitude 50 -name ~/Data_storage/10min_MG_005mMATP &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 600000 -iters 1 -var pulse_switch 0 -var stim_amplitude 10 -name ~/Data_storage/10min_MG_001mMATP
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 600000 -iters 1 -var pulse_switch 0 -var stim_amplitude 100 -name ~/Data_storage/10min_MG_01mMATP &
  python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 900000 -iters 1 -var pulse_switch 0 -var stim_amplitude 50 -name ~/Data_storage/15min_MG_005mMATP


fi


echo "Calculation is done"
