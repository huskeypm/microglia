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

duration=240
iters=2
finalstep=2
sigma="0.001"

array[0]=".008"
array[1]="0.33"
array[2]="0.16"
array[3]=".55"
array[4]=".0002"
array[5]=".025"
array[6]="3.41"
array[7]=".00035"
array[8]=".029"
array[9]="0"
array[10]=3891
array[11]=5214
array[12]=233


for (( i=1; i<=$finalstep; i++))
  do
    j=0
    for name in k1_ptxs k3_ptxs k5_ptxs L1_ptxs L2_ptxs L3_ptxs H1_ptxs H2_ptxs H3_ptxs H4_ptxs k2_ptxs k4_ptxs k6_ptxs
      do
        python fittingAlgorithm.py -odeModel p2x7_MG.ode -myVariedParam $name -variedParamTruthVal ${array[$j]} -jobDuration $duration -fileName This_Is_A_Test.png -numRandomDraws 10 -numIters $iters -sigmaScaleRate $sigma -outputParamName I_ptxs -outputParamSearcher I_ptxs -outputParamMethod ptxso -outputParamTruthVal 0 >& log.ptxs1

        GUESS="$(bc <<< scale=6 ;grep bestVarDict log.ptxs1 | tail -1 | awk '{print $3}' | grep -Eo '[0-9\.]+')"
        echo "result of $name: $GUESS from trial number $i"
        echo "previous ${array[$j]} and current $GUESS "

        array[$j]=$GUESS
        j=$(($j+1))

      done
  done

k=0
for name in k1_ptxs k3_ptxs k5_ptxs L1_ptxs L2_ptxs L3_ptxs H1_ptxs H2_ptxs H3_ptxs H4_ptxs k2_ptxs k4_ptxs k6_ptxs
	  do
	    echo "new rate constant for $name is ${array[$k]}" >> ptxs1.results
    k=$(($k+1))
  done

echo "$(grep jobFitnesses log.ptxs1 | tail -1)" >> ptxs1.results
