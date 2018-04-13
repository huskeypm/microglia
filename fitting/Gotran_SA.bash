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

python daisychain.py -t 0.1 -jit -odeName microgliav4_noptx.ode -T 3600 -iters 1 -var CNt_NFAT 4e3 -name ./noP2X_CNt_4uM 
python daisychain.py -t 0.1 -jit -odeName microgliav4_noptx.ode -T 3600 -iters 1 -var CNt_NFAT 3e3 -name ./noP2X_CNt_3uM 
python daisychain.py -t 0.1 -jit -odeName microgliav4_noptx.ode -T 3600 -iters 1 -var CNt_NFAT 2.4e3 -name ./noP2X_CNt_2.4uM 
python daisychain.py -t 0.1 -jit -odeName microgliav4_noptx.ode -T 3600 -iters 1 -var CNt_NFAT 2.2e3 -name ./noP2X_CNt_2.2uM 
python daisychain.py -t 0.1 -jit -odeName microgliav4_noptx.ode -T 3600 -iters 1 -var CNt_NFAT 2e3 -name ./noP2X_CNt_2uM
python daisychain.py -t 0.1 -jit -odeName microgliav4_noptx.ode -T 3600 -iters 1 -var CNt_NFAT 1.8e3 -name ./noP2X_CNt_1.8uM
python daisychain.py -t 0.1 -jit -odeName microgliav4_noptx.ode -T 3600 -iters 1 -var CNt_NFAT 1.6e3 -name ./noP2X_CNt_1.6uM
python daisychain.py -t 0.1 -jit -odeName microgliav4_noptx.ode -T 3600 -iters 1 -var CNt_NFAT 1e3 -name ./noP2X_CNt_1uM
python daisychain.py -t 0.1 -jit -odeName microgliav4_noptx.ode -T 3600 -iters 1 -var CNt_NFAT 0e3 -name ./noP2X_CNt_0uM 

#mail -s "job is done" "bending456@gmail.com"
