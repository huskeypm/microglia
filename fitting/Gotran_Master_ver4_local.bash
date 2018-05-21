#!/bin/bash


############## Control Panel #####################

export ODEFILE=microgliav17.ode
export ODEFILEshort=microgliav18.ode
export ODEFILEfreq=microgliav18-freq.ode

ptxvalid=0  ### <---- 0 = OFF and 1 = ON
caivalid=0  ### 8 min ST validation (Hide data related)
no=0        ### No stimulation 

dura=0      ### Duration variation
freq=0      ### Frequency variation
rest=1      ### Resting variation 
sens1=0      ### Sensitivity Analysis
sens2=0

leng=0      ### Lengthy Stimulation
CaN=0       ### Special Edition for CaN Validation

#####################################
# P2X Validation ####################

if [ $ptxvalid -eq 1 ]
then
  echo "Validation of P2X is ON" # This code needs to be fixed ( millisecond time unit )
  python daisychain.py -dt 0.1 -jit -odeName p2x7_MG_fitted.ode -T 300 -iters 1 -var stim_amplitude 100 -name ./p2x7_fitted_100uMATP
  python daisychain.py -dt 0.1 -jit -odeName p2x7_MG_fitted.ode -T 300 -iters 1 -var stim_amplitude 320 -name ./p2x7_fitted_320uMATP
  python daisychain.py -dt 0.1 -jit -odeName p2x7_MG_fitted.ode -T 300 -iters 1 -var stim_amplitude 1000 -name ./p2x7_fitted_1000uMATP
  python daisychain.py -dt 0.1 -jit -odeName p2x4_MG_fitted.ode -T 450 -iters 1 -var stim_amplitude 100 -name ./p2x4_fitted_100uMATP
fi

if [ $no -eq 1 ]
then
  echo "No stimulation is ON"
  python daisychain.py -dt 1 -dSr 100 -jit -odeName $ODEFILEshort -T 300000 -iters 1 -var stim_period 2e3 -var size 1 -var stim_space 0 -var stim_amplitude 0 -name ./MG_0mMATP
fi

if [ $caivalid -eq 1 ]
then 
  echo "Validation of Cai is ON"

  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 2000000 -iters 1 -var stim_period 960e3 -var size 1 -var stim_space 0 -var pre_rest 100 -var stim_amplitude 1000 -name ./8min_MG_1mMATP 
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 2000000 -iters 1 -var stim_period 960e3 -var size 1 -var stim_space 0 -var pre_rest 100 -var stim_amplitude 100 -name ./8min_MG_0.1mMATP 
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 2000000 -iters 1 -var stim_period 960e3 -var size 1 -var stim_space 0 -var pre_rest 100 -var stim_amplitude 10 -name ./8min_MG_0.01mMATP 

fi

if [ $CaN -eq 1 ] 
then 
  echo "Validation of CaN is ON"

  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 500000 -iters 1 -var stim_period 2e3 -var size 1 -var stim_space 0 -var stim_amplitude 1000 -var pre_rest 100 -name ./1st1rsMGCaN_1mMATPnew
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 500000 -iters 1 -var stim_period 2e3 -var size 1 -var stim_space 200e3 -var stim_amplitude 1000 -var pre_rest 100 -name ./1st200rsMGCaN_1mMATPnew
  
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 500000 -iters 1 -var stim_period 2e3 -var size 1 -var stim_space 0 -var stim_amplitude 100 -var pre_rest 100 -name ./1st1rsMGCaN_0.1mMATPnew
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 500000 -iters 1 -var stim_period 2e3 -var size 1 -var stim_space 200e3 -var stim_amplitude 100 -var pre_rest 100 -name ./1st200rsMGCaN_0.1mMATPnew

  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 500000 -iters 1 -var stim_period 2e3 -var size 1 -var stim_space 0 -var stim_amplitude 10 -var pre_rest 100 -name ./1st1rsMGCaN_0.01mMATPnew
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 500000 -iters 1 -var stim_period 2e3 -var size 1 -var stim_space 200e3 -var stim_amplitude 10 -var pre_rest 100 -name ./1st200rsMGCaN_0.01mMATPnew


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

  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 2e3 -var size 1 -var stim_space 100e3 -var stim_amplitude 1000 -name ./1st100rsMG_1mMATPnew &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 10e3 -var size 1 -var stim_space 100e3 -var stim_amplitude 1000 -name ./20st120rsMG_1mMATPnew 
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 50e3 -var size 1 -var stim_space 100e3 -var stim_amplitude 1000 -name ./25st100rsMG_1mMATPnew &
  #python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 200e3 -var size 1 -var stim_space 0 -var stim_amplitude 1000 -name ./100st100rsMG_1mMATPnew 

  # Various duration with broad spacing at 0.1 mM ATP: 1,2,5, and 10 are only size working in this model due to periodic equation

  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 2e3 -var size 1 -var stim_space 100e3 -var stim_amplitude 100 -name ./1st100rsMG_0.1mMATPnew &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 10e3 -var size 1 -var stim_space 100e3 -var stim_amplitude 100 -name ./5st100rsMG_0.1mMATPnew 
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 50e3 -var size 1 -var stim_space 100e3 -var stim_amplitude 100 -name ./25st100rsMG_0.1mMATPnew &
  #python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 200e3 -var size 1 -var stim_space 0 -var stim_amplitude 100 -name ./100st100rsMG_0.1mMATPnew 

  # Various duration with broad spacing at 0.01 mM ATP: 1,2,5, and 10 are only size working in this model due to periodic equation

  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 2e3 -var size 1 -var stim_space 100e3 -var stim_amplitude 10 -name ./1st100rsMG_0.01mMATPnew &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 10e3 -var size 1 -var stim_space 100e3 -var stim_amplitude 10 -name ./5st100rsMG_0.01mMATPnew  
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 50e3 -var size 1 -var stim_space 100e3 -var stim_amplitude 10 -name ./25st100rsMG_0.01mMATPnew &
  #python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 200e3 -var size 1 -var stim_space 0 -var stim_amplitude 10 -name ./100st100rsMG_0.01mMATPnew 

  # Various duration with broad spacing at 0.001 mM ATP: 1,2,5, and 10 are only size working in this model due to periodic equation

  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 2e3 -var size 1 -var stim_space 100e3 -var stim_amplitude 1 -name ./1st100rsMG_0.001mMATPnew &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 10e3 -var size 1 -var stim_space 100e3 -var stim_amplitude 1 -name ./5st100rsMG_0.001mMATPnew  
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 50e3 -var size 1 -var stim_space 100e3 -var stim_amplitude 1 -name ./25st100rsMG_0.001mMATPnew &
  #python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 200e3 -var size 1 -var stim_space 0 -var stim_amplitude 1 -name ./100st100rsMG_0.001mMATPnew 

fi

if [ $freq -eq 1 ]
then
  echo "Frequency variation is ON" 

  # Various frequencies at 1 mM ATP

  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 2e3 -var size 1 -var stim_space 0 -var stim_amplitude 1000 -name ./1st1rsMG_1mMATPnew &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 10e3 -var size 1 -var stim_space 0 -var stim_amplitude 1000 -name ./5st5rsMG_1mMATPnew 
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 40e3 -var size 1 -var stim_space 0 -var stim_amplitude 1000 -name ./20st20rsMG_1mMATPnew &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 80e3 -var size 1 -var stim_space 0 -var stim_amplitude 1000 -name ./40st40rsMG_1mMATPnew
#  python daisychain.py -dt 1 -dSr 100 -jit -odeName $ODEFILEshort -T 6000 -iters 1 -var stim_period 80 -var size 1 -var stim_space 0 -var stim_amplitude 1000 -name ./40st40rsMG_1mMATPnew 
#  python daisychain.py -dt 1 -dSr 100 -jit -odeName $ODEFILEshort -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 0 -var stim_amplitude 1000 -name ./50st50rsMG_1mMATPnew 

  # Various frequencies at 0.1 mM ATP

  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 2e3 -var size 1 -var stim_space 0 -var stim_amplitude 100 -name ./1st1rsMG_0.1mMATPnew &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 10e3 -var size 1 -var stim_space 0 -var stim_amplitude 100 -name ./5st5rsMG_0.1mMATPnew 
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 40e3 -var size 1 -var stim_space 0 -var stim_amplitude 100 -name ./20st20rsMG_0.1mMATPnew &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 80e3 -var size 1 -var stim_space 0 -var stim_amplitude 100 -name ./40st40rsMG_0.1mMATPnew 
#  python daisychain.py -dt 1 -dSr 100 -jit -odeName $ODEFILEshort -T 6000 -iters 1 -var stim_period 80 -var size 1 -var stim_space 0 -var stim_amplitude 100 -name ./40st40rsMG_0.1mMATPnew
#  python daisychain.py -dt 1 -dSr 100 -jit -odeName $ODEFILEshort -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 0 -var stim_amplitude 100 -name ./50st50rsMG_0.1mMATPnew 

  # Various frequencies at 0.01 mM ATP

  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 2e3 -var size 1 -var stim_space 0 -var stim_amplitude 10 -name ./1st1rsMG_0.01mMATPnew &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 10e3 -var size 1 -var stim_space 0 -var stim_amplitude 10 -name ./5st5rsMG_0.01mMATPnew 
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 40e3 -var size 1 -var stim_space 0 -var stim_amplitude 10 -name ./20st20rsMG_0.01mMATPnew &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 80e3 -var size 1 -var stim_space 0 -var stim_amplitude 10 -name ./40st40rsMG_0.01mMATPnew
#  python daisychain.py -dt 1 -dSr 100 -jit -odeName $ODEFILEshort -T 6000 -iters 1 -var stim_period 80 -var size 1 -var stim_space 0 -var stim_amplitude 10 -name ./40st40rsMG_0.01mMATPnew 
#  python daisychain.py -dt 1 -dSr 100 -jit -odeName $ODEFILEshort -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 0 -var stim_amplitude 10 -name ./50st50rsMG_0.01mMATPnew 

  # Various frequencies at 0.001 mM ATP

  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 2e3 -var size 1 -var stim_space 0 -var stim_amplitude 1 -name ./1st1rsMG_0.001mMATPnew &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 10e3 -var size 1 -var stim_space 0 -var stim_amplitude 1 -name ./5st5rsMG_0.001mMATPnew  
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 40e3 -var size 1 -var stim_space 0 -var stim_amplitude 1 -name ./20st20rsMG_0.001mMATPnew &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_period 80e3 -var size 1 -var stim_space 0 -var stim_amplitude 1 -name ./40st40rsMG_0.001mMATPnew 
#  python daisychain.py -dt 1 -dSr 100 -jit -odeName $ODEFILEshort -T 6000 -iters 1 -var stim_period 80 -var size 1 -var stim_space 0 -var stim_amplitude 1 -name ./40st40rsMG_0.001mMATPnew 
#  python daisychain.py -dt 1 -dSr 100 -jit -odeName $ODEFILEshort -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 0 -var stim_amplitude 1 -name ./50st50rsMG_0.001mMATPnew 

fi 

if [ $rest -eq 1 ]
then 
  echo "Resting variation is ON"

  # Various resting time at 1 mM ATP: 100, 200, 300

  python daisychain.py -dt 0.1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var stim_period 40e3 -var stim_space 80e3 -var stim_amplitude 1000 -name ./20st80rsMG_1mMATPnew 
  python daisychain.py -dt 0.1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var stim_period 40e3 -var stim_space 120e3 -var stim_amplitude 1000 -name ./20st120rsMG_1mMATPnew 
  python daisychain.py -dt 0.1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var stim_period 40e3 -var stim_space 160e3 -var stim_amplitude 1000 -name ./20st160rsMG_1mMATPnew 
#  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEfreq -T 3700000 -iters 1 -var stim_period 2e3 -var n_freq 4 -var stim_freq 1 -var stim_amplitude 1000 -name ./1st9rsMG_1mMATPnew 

  # Various resting time at 1 mM ATP: 100, 200, 300

  python daisychain.py -dt 0.1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var stim_period 40e3 -var stim_space 80e3 -var stim_amplitude 100 -name ./20st80rsMG_0.1mMATPnew  
  python daisychain.py -dt 0.1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var stim_period 40e3 -var stim_space 120e3 -var stim_amplitude 100 -name ./20st120rsMG_0.1mMATPnew 
  python daisychain.py -dt 0.1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var stim_period 40e3 -var stim_space 160e3 -var stim_amplitude 100 -name ./20st160rsMG_0.1mMATPnew 
#  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEfreq -T 3700000 -iters 1 -var stim_period 2e3 -var n_freq 4 -var stim_freq 1 -var stim_amplitude 100 -name ./1st9rsMG_0.1mMATPnew

  # Various resting time at 1 mM ATP: 100, 200, 300

  python daisychain.py -dt 0.1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var stim_period 40e3 -var stim_space 80e3 -var stim_amplitude 10 -name ./20st80rsMG_0.01mMATPnew 
  python daisychain.py -dt 0.1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var stim_period 40e3 -var stim_space 120e3 -var stim_amplitude 10 -name ./20st120rsMG_0.01mMATPnew 
  python daisychain.py -dt 0.1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var stim_period 40e3 -var stim_space 160e3 -var stim_amplitude 10 -name ./20st160rsMG_0.01mMATPnew 
#  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEfreq -T 3700000 -iters 1 -var stim_period 2e3 -var n_freq 4 -var stim_freq 1 -var stim_amplitude 10 -name ./1st9rsMG_0.01mMATPnew 

  # Various resting time at 1 mM ATP: 100, 200, 300

  python daisychain.py -dt 0.1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var stim_period 40e3 -var stim_space 80e3 -var stim_amplitude 1 -name ./20st80rsMG_0.001mMATPnew 
  python daisychain.py -dt 0.1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var stim_period 40e3 -var stim_space 120e3 -var stim_amplitude 1 -name ./20st120rsMG_0.001mMATPnew 
  python daisychain.py -dt 0.1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var stim_period 40e3 -var stim_space 160e3 -var stim_amplitude 1 -name ./20st160rsMG_0.001mMATPnew 
#  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEfreq -T 3700000 -iters 1 -var stim_period 2e3 -var n_freq 4 -var stim_freq 1 -var stim_amplitude 1 -name ./1st9rsMG_0.001mMATPnew

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

    for SA in SAca SAnfat SApp38 SAptxs SAptxf SAcm SAnfatpc SAserca SAnancx #SAcn
      do

        for  (( i=0; i<=19; i++))
          do

          python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_amplitude $ATP -var stim_period 10e3 -var $SA ${array[$i]} -var stim_space 0 -name ./SA-$SA-${array[$i]}-$ATP

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

          python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3700000 -iters 1 -var stim_amplitude $ATP -var stim_period 10e3 -var $SA ${array[$i]} -var stim_space 0 -name ./SA-$SA-${array[$i]}-$ATP

          done

      done

    done

fi


### LENGTHY Stimulation ###

if [ $leng -eq 1 ]
then 
  echo "Lengthy Stimulation is ON" 

  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 120000 -iters 1 -var stim_pulse 0 -var stim_amplitude 1000 -var stim_space 0 -name ./1min_MG_1mMATP &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 300000 -iters 1 -var stim_pulse 0 -var stim_amplitude 1000 -var stim_space 0 -name ./5min_MG_1mMATP 
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 600000 -iters 1 -var stim_pulse 0 -var stim_amplitude 1000 -var stim_space 0 -name ./10min_MG_1mMATP &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 900000 -iters 1 -var stim_pulse 0 -var stim_amplitude 1000 -var stim_space 0 -name ./15min_MG_1mMATP 
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 1800000 -iters 1 -var stim_pulse 0 -var stim_amplitude 1000 -var stim_space 0 -name ./30min_MG_1mMATP &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var stim_pulse 0 -var stim_amplitude 1000 -var stim_space 0 -name ./60min_MG_1mMATP

  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 120000 -iters 1 -var stim_pulse 0 -var  stim_amplitude 3000 -var stim_space 0 -name ./1min_MG_3mMATP &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 300000 -iters 1 -var stim_pulse 0 -var stim_amplitude 3000 -var stim_space 0 -name ./5min_MG_3mMATP 
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 600000 -iters 1 -var stim_pulse 0 -var stim_amplitude 3000 -var stim_space 0 -name ./10min_MG_3mMATP &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 900000 -iters 1 -var stim_pulse 0 -var stim_amplitude 3000 -var stim_space 0 -name ./15min_MG_3mMATP 
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 1800000 -iters 1 -var stim_pulse 0 -var stim_amplitude 3000 -var stim_space 0 -name ./30min_MG_3mMATP &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var stim_pulse 0 -var stim_amplitude 3000 -var stim_space 0 -name ./60min_MG_3mMATP 

  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 900000 -iters 1 -var stim_pulse 0 -var stim_amplitude 0 -var stim_space 0 -name ./15min_MG_0mMATP &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 900000 -iters 1 -var stim_pulse 0 -var stim_amplitude 100 -var stim_space 0 -name ./15min_MG_01mMATP 
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 900000 -iters 1 -var stim_pulse 0 -var stim_amplitude 500 -var stim_space 0 -name ./15min_MG_05mMATP &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 900000 -iters 1 -var stim_pulse 0 -var stim_amplitude 5000 -var stim_space 0 -name ./15min_MG_5mMATP

  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 10800000 -iters 1 -var stim_pulse 0 -var stim_amplitude 10 -var stim_space 0 -name ./180min_MG_001mMATP &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 10800000 -iters 1 -var stim_pulse 0 -var stim_amplitude 100 -var stim_space 0 -name ./180min_MG_01mMATP
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 10800000 -iters 1 -var stim_pulse 0 -var stim_amplitude 1000 -var stim_space 0 -name ./180min_MG_1mMATP &

  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 7200000 -iters 1 -var stim_pulse 0 -var stim_amplitude 3000 -var stim_space 0 -name ./120min_MG_3mMATP
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 10800000 -iters 1 -var stim_pulse 0 -var stim_amplitude 3000 -var stim_space 0 -name ./180min_MG_3mMATP &

  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var stim_pulse 0 -var stim_amplitude 10 -var stim_space 0 -name ./60min_MG_001mMATP
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var stim_pulse 0 -var stim_amplitude 100 -var stim_space 0 -name ./60min_MG_01mMATP &

  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 10800000 -iters 1 -var stim_pulse 0 -var stim_amplitude 200 -var stim_space 0 -name ./180min_MG_02mMATP
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var stim_pulse 0 -var stim_amplitude 200 -var stim_space 0 -name ./60min_MG_02mMATP &

  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 3600000 -iters 1 -var stim_pulse 0 -var stim_amplitude 50 -var stim_space 0 -name ./60min_MG_005mMATP
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 120000 -iters 1 -var stim_pulse 0 -var stim_amplitude 50 -var stim_space 0 -name ./1min_MG_005mMATP &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 1800000 -iters 1 -var stim_pulse 0 -var stim_amplitude 50 -var stim_space 0 -name ./30min_MG_005mMATP
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 300000 -iters 1 -var stim_pulse 0 -var stim_amplitude 50 -var stim_space 0 -name ./5min_MG_005mMATP &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 600000 -iters 1 -var stim_pulse 0 -var stim_amplitude 50 -var stim_space 0 -name ./10min_MG_005mMATP
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 600000 -iters 1 -var stim_pulse 0 -var stim_amplitude 10 -var stim_space 0 -name ./10min_MG_001mMATP &
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 600000 -iters 1 -var stim_pulse 0 -var stim_amplitude 100 -var stim_space 0 -name ./10min_MG_01mMATP
  python daisychain.py -dt 1 -dSr 1000 -jit -odeName $ODEFILEshort -T 900000 -iters 1 -var stim_pulse 0 -var stim_amplitude 50 -var stim_space 0 -name ./15min_MG_005mMATP 


fi


echo "Calculation is done"



