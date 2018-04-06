 -l nodes=1:ppn=64
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

python daisychain.py -t 0.1 -jit -odeName microgliav4_noptx.ode -T 3600 -iters 1 -var MaxFlux 0.00186 -name ./noP2X_100 
python daisychain.py -t 0.1 -jit -odeName microgliav4_noptx.ode -T 3600 -iters 1 -var MaxFlux 0.00177 -name ./noP2X_95 
python daisychain.py -t 0.1 -jit -odeName microgliav4_noptx.ode -T 3600 -iters 1 -var MaxFlux 0.0013 -name ./noP2X_70 
python daisychain.py -t 0.1 -jit -odeName microgliav4_noptx.ode -T 3600 -iters 1 -var MaxFlux 0.0011 -name ./noP2X_60 
python daisychain.py -t 0.1 -jit -odeName microgliav4_noptx.ode -T 3600 -iters 1 -var MaxFlux 0.00093 -name ./noP2X_50
python daisychain.py -t 0.1 -jit -odeName microgliav4_noptx.ode -T 3600 -iters 1 -var MaxFlux 0.00074 -name ./noP2X_40
python daisychain.py -t 0.1 -jit -odeName microgliav4_noptx.ode -T 3600 -iters 1 -var MaxFlux 0.00056 -name ./noP2X_30
python daisychain.py -t 0.1 -jit -odeName microgliav4_noptx.ode -T 3600 -iters 1 -var MaxFlux 0.000093 -name ./noP2X_5
python daisychain.py -t 0.1 -jit -odeName microgliav4_noptx.ode -T 3600 -iters 1 -var MaxFlux 0.0 -name ./noP2X_0 

#mail -s "job is done" "bending456@gmail.com"
