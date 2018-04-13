#!/bin/bash

#PBS -l nodes=1:ppn=8
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

duration=75
iters=2
finalstep=5
sigma="0.001"

array[0]=600000
array[1]=500000
array[2]=400000
array[3]=".4"
array[4]=".5"
array[5]=".6"
array[6]=".013"
array[7]=".35"
array[8]="1.4"
array[9]=".001"

for (( i=1; i<=$finalstep; i++))
  do
    j=0
    for name in k2_ptxf k4_ptxf k6_ptxf k1_ptxf k3_ptxf k5_ptxf H1_ptxf H2_ptxf H3_ptxf H4_ptxf
      do
        python fittingAlgorithm.py -odeModel p2x4_MG_test.ode -myVariedParam $name -variedParamTruthVal ${array[$j]} -jobDuration $duration -fileName This_Is_A_Test.png -numRandomDraws 10 -numIters $iters -sigmaScaleRate $sigma -outputParamName I_ptxf -outputParamSearcher I_ptxf -outputParamMethod pro -outputParamTruthVal 0 >& log.ptxf

        GUESS="$(bc <<< scale=6 ;grep bestVarDict log.ptxf | tail -1 | awk '{print $3}' | grep -Eo '[0-9\.]+')"
        echo "result of $name: $GUESS from trial number $i"
        echo "previous ${array[$j]} and current $GUESS "

        array[$j]=$GUESS
        j=$(($j+1))

      done
  done

k=0
for name in k2_ptxf k4_ptxf k6_ptxf k1_ptxf k3_ptxf k5_ptxf H1_ptxf H2_ptxf H3_ptxf H4_ptxf
	  do
	    echo "new rate constant for $name is ${array[$k]}" >> ptxf.results
    k=$(($k+1))
  done

echo "$(grep jobFitnesses log.ptxf | tail -1)" >> ptxf.results
