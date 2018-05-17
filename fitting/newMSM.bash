#!/bin/bash
alias python="python2.7"

python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName microglia-newMSM.ode -T 2000e3 -iters 1 -var stim_period 800e3 -var stim_amplitude 10 -name ./10
python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName microglia-newMSM.ode -T 2000e3 -iters 1 -var stim_period 800e3 -var stim_amplitude 100 -name ./100
python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName microglia-newMSM.ode -T 2000e3 -iters 1 -var stim_period 800e3 -var stim_amplitude 1000 -name ./1000

python2.7 plotter.py

display test.png

#mail -s "job is done" "bending456@gmail.com"
