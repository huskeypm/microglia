#!/bin/bash
#PBS -l nodes=1:ppn=64 
#PBS -q long    
#PBS -m abe

## For running dolfin jobs on holly 
### NOTE: Run 'module load FEniCS' interactively before
### using this with qsub.
export BASEDIR=$PBS_O_WORKDIR
export PROCS=64
export OMPI_MCA_orte_default_hostfile=$PBS_NODEFILE
export OMPI_MCA_orte_leave_session_attached=1
. /etc/profile.d/modules.sh

module load FEniCS.15
export LOC=$HOME/sources
export MYPATH=$LOC/mypython
export PYTHONPATH=$PYTHONPATH:$MYPATH/lib/python2.7/site-packages/


#cd /home/pmke226/sources/wholecell/



print "LEAVING!" 

