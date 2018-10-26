#!/bin/bash

export LOC=/home/bch265/sources
export MYPATH=$LOC/mypython
export PYTHONPATH=$PYTHONPATH:/home/bch265/.local/lib/python2.7/site-packages/

python2.7 -c "import instant"
python2.7 -c "import modelparameters"
python2.7 -c "import gotran"

cd /home/bch265/microglia/microglia/fitting

python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName microgliav19-1.ode -T 3600000 -iters 1 -var stim_amplitude 10 -name ./test_10uMATP1st2rs
python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName microgliav19-1.ode -T 3600000 -iters 1 -var stim_amplitude 100 -name ./test_100uMATP1st2rs
python2.7 daisychain.py -dt 1 -dSr 1000 -jit -odeName microgliav19-1.ode -T 3600000 -iters 1 -var stim_amplitude 1000 -name ./test_1000uMATP1st2rs


