#!/bin/bash

#SBATCH -N 2
#SBATCH -n 32
#SBATCH -p short
#SBATCH --mem=64G
#SBATCH -t 12:00:00

## For running dolfin jobs on holly
### NOTE: Run 'module load FEniCS' interactively before
### using this with qsub.
export BASEDIR=$PBS_O_WORKDIR
export PROCS=32
export OMPI_MCA_orte_default_hostfile=$PBS_NODEFILE
export OMPI_MCA_orte_leave_session_attached=1
. /etc/profile.d/modules.sh

module load singularity

singularity exec /share/apps/fenics/fenics-2017.2.img /home/bch265/microglia/microglia/fitting/Gotran_Master_ver6.bash

