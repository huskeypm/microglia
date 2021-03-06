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

duration=250
iters=2
finalstep=5
sigma="0.0001"

array[0]=2198
array[1]=2155
array[2]=97
array[3]=".034"
array[4]=".453"
array[5]=".17"
array[6]=".491"
array[7]=".170"
array[8]=".051"
array[9]="2.437"
array[10]=".00081"
array[11]=".0294"
array[12]="0"

for (( i=1; i<=$finalstep; i++))
  do
    j=0
    for name in k2_ptxs k4_ptxs k6_ptxs k1_ptxs k3_ptxs k5_ptxs L1_ptxs L2_ptxs L3_ptxs H1_ptxs H2_ptxs H3_ptxs H4_ptxs
      do
        python fittingAlgorithm.py -odeModel p2x7_MG_test.ode -myVariedParam $name -variedParamTruthVal ${array[$j]} -jobDuration $duration -fileName This_Is_A_Test.png -numRandomDraws 10 -numIters $iters -sigmaScaleRate $sigma -outputParamName I_ptxs -outputParamSearcher I_ptxs -outputParamMethod ptxsth -outputParamTruthVal 0 >& log.ptxs1

        GUESS="$(bc <<< scale=6 ;grep bestVarDict log.ptxs1 | tail -1 | awk '{print $3}' | grep -Eo '[0-9\.]+')"
        echo "result of $name: $GUESS from trial number $i"
        echo "previous ${array[$j]} and current $GUESS "

        array[$j]=$GUESS
        j=$(($j+1))

      done
  done

k=0
for name in k2_ptxs k4_ptxs k6_ptxs k1_ptxs k3_ptxs k5_ptxs L1_ptxs L2_ptxs L3_ptxs H1_ptxs H2_ptxs H3_ptxs H4_ptxs
	  do
	    echo "new rate constant for $name is ${array[$k]}" >> ptxs1.results
    k=$(($k+1))
  done

echo "$(grep jobFitnesses log.ptxs1 | tail -1)" >> ptxs1.results
