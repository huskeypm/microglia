#!/bin/bash

#PBS -l nodes=1:ppn=64
#PBS -q short
#PBS -m abe

## For running dolfin jobs on holly
### NOTE: Run 'module load FEniCS' interactively before
### using this with qsub.
export BASEDIR=$PBS_O_WORKDIR
export PROCS=8
export OMPI_MCA_orte_default_hostfile=$PBS_NODEFILE
export OMPI_MCA_orte_leave_session_attached=1
. /etc/profile.d/modules.sh

module load FEniCS.15
export LOC=/home/bch265/sources
export MYPATH=$LOC/mypython
export PYTHONPATH=$PYTHONPATH:$MYPATH/lib/python2.7/site-packages/
python -c "import instant"
python -c "import modelparameters"
python -c "import gotran"

cd /home/bch265/microglia/microglia/fitting


# Make sure your pre_rest is less than 500; otherwise, the calculation may crash.
# -var pre_rest 100 
# Various duration with broad spacing at 1 mM ATP: 1,2,5, and 10 are only size working in this model due to periodic equation

python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 900 -var stim_amplitude 1000 -name ./50st900rsMG_1mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 2 -var stim_space 900 -var stim_amplitude 1000  -name ./150st800rsMG_1mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 5 -var stim_space 900 -var stim_amplitude 1000  -name ./450st500rsMG_1mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 10 -var stim_space 900 -var stim_amplitude 1000  -name ./900st50rsMG_1mMATPnew

# Various duration with broad spacing at 0.1 mM ATP: 1,2,5, and 10 are only size working in this model due to periodic equation

python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 900 -var stim_amplitude 100 -name ./50st900rsMG_0.1mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 2 -var stim_space 900 -var stim_amplitude 100  -name ./150st800rsMG_0.1mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 5 -var stim_space 900 -var stim_amplitude 100  -name ./450st500rsMG_0.1mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 10 -var stim_space 900 -var stim_amplitude 100  -name ./900st50rsMG_0.1mMATPnew

# Various duration with broad spacing at 0.01 mM ATP: 1,2,5, and 10 are only size working in this model due to periodic equation

python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 900 -var stim_amplitude 10 -name ./50st900rsMG_0.01mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 2 -var stim_space 900 -var stim_amplitude 10  -name ./150st800rsMG_0.01mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 5 -var stim_space 900 -var stim_amplitude 10  -name ./450st500rsMG_0.01mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 10 -var stim_space 900 -var stim_amplitude 10  -name ./900st50rsMG_0.01mMATPnew

# Various duration with broad spacing at 0.001 mM ATP: 1,2,5, and 10 are only size working in this model due to periodic equation

python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 900 -var stim_amplitude 1 -name ./50st900rsMG_0.001mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 2 -var stim_space 900 -var stim_amplitude 1  -name ./150st800rsMG_0.001mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 5 -var stim_space 900 -var stim_amplitude 1  -name ./450st500rsMG_0.001mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 10 -var stim_space 900 -var stim_amplitude 1  -name ./900st50rsMG_0.001mMATPnew

# Various frequencies at 1 mM ATP

python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 20 -var size 1 -var stim_space 0 -var stim_amplitude 1000 -name ./10st10rsMG_1mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 40 -var size 1 -var stim_space 0 -var stim_amplitude 1000  -name ./20st20rsMG_1mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 80 -var size 1 -var stim_space 0 -var stim_amplitude 1000  -name ./40st40rsMG_1mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 0 -var stim_amplitude 1000  -name ./50st50rsMG_1mMATPnew

# Various frequencies at 0.1 mM ATP

python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 20 -var size 1 -var stim_space 0 -var stim_amplitude 100 -name ./10st10rsMG_0.1mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 40 -var size 1 -var stim_space 0 -var stim_amplitude 100  -name ./20st20rsMG_0.1mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 80 -var size 1 -var stim_space 0 -var stim_amplitude 100  -name ./40st40rsMG_0.1mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 0 -var stim_amplitude 100  -name ./50st50rsMG_0.1mMATPnew

# Various frequencies at 0.01 mM ATP

python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 20 -var size 1 -var stim_space 0 -var stim_amplitude 10 -name ./10st10rsMG_0.01mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 40 -var size 1 -var stim_space 0 -var stim_amplitude 10  -name ./20st20rsMG_0.01mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 80 -var size 1 -var stim_space 0 -var stim_amplitude 10  -name ./40st40rsMG_0.01mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 0 -var stim_amplitude 10  -name ./50st50rsMG_0.01mMATPnew


# Various frequencies at 0.001 mM ATP

python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 20 -var size 1 -var stim_space 0 -var stim_amplitude 1 -name ./10st10rsMG_0.001mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 40 -var size 1 -var stim_space 0 -var stim_amplitude 1  -name ./20st20rsMG_0.001mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 80 -var size 1 -var stim_space 0 -var stim_amplitude 1  -name ./40st40rsMG_0.001mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 0 -var stim_amplitude 1  -name ./50st50rsMG_0.001mMATPnew


# Various resting time at 1 mM ATP: 100, 200, 300

python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 100 -var stim_amplitude 1000 -name ./50st100rsMG_1mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 200 -var stim_amplitude 1000 -name ./50st200rsMG_1mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 300 -var stim_amplitude 1000 -name ./50st300rsMG_1mMATPnew


# Various resting time at 1 mM ATP: 100, 200, 300

python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 100 -var stim_amplitude 100 -name ./50st100rsMG_0.1mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 200 -var stim_amplitude 100 -name ./50st200rsMG_0.1mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 300 -var stim_amplitude 100 -name ./50st300rsMG_0.1mMATPnew


# Various resting time at 1 mM ATP: 100, 200, 300

python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 100 -var stim_amplitude 10 -name ./50st100rsMG_0.01mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 200 -var stim_amplitude 10 -name ./50st200rsMG_0.01mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 300 -var stim_amplitude 10 -name ./50st300rsMG_0.01mMATPnew


# Various resting time at 1 mM ATP: 100, 200, 300

python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 100 -var stim_amplitude 1 -name ./50st100rsMG_0.001mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 200 -var stim_amplitude 1 -name ./50st200rsMG_0.001mMATPnew
python daisychain.py -t 0.1 -jit -odeName microgliav10-freqcontrol.ode -T 6000 -iters 1 -var stim_period 100 -var size 1 -var stim_space 300 -var stim_amplitude 1 -name ./50st300rsMG_0.001mMATPnew





















