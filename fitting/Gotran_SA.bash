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

# This is the code for sensitivity analysis with pp38, CaM, CNt, P2X7, P2X4, and NFATpc. 
# Frequency is set to 100 sec per cycle (50 secs of stimulation and 50 secs of relaxation).
 # To adjust, add line 
 # -var stim_period 100 (for 100 per cycle: default)
# Pre_resting is set to 100 secs
 # To adjust, add line
 # -var pre_rest 100 (100 sec: default)
# ATP concentration is set to 1 mM (1000)
 # To adjust, add line
 # -var stim_amplitude 1000 (1 mM: default in the unit of uM)

for SA in SApp38 SAcn SAptxs SAptxf SAcm SAnfatpc
  do
    for num in "0.01" "0,1" "0.2" "0.3" "0.4" "0.5" "0.6" "0,7" "0.8" "0.9" "1" "2" "3" "4" "5" "6" "7" "8" "9" "10" 
      do 
      python daisychain.py -t 0.1 -jit -odeName microgliav10_freqcontrol.ode -T 3800 -iters 1 -var $SA $num -name ./SA.$SA.$num
      done
  done
 

#mail -s "job is done" "bending456@gmail.com"
