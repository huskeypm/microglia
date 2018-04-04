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

duration=120
iters=4
finalstep=10
sigma="0.001"

array[0]=70000
array[1]=100000
array[2]=7000
array[3]=".3"
array[4]="5.4"
array[5]="1.58"
array[6]=".0001"
array[7]=".004"
array[8]=".5"
array[9]=".001"
array[10]=".01"
array[11]=".5"
array[12]="0"

for (( i=1; i<=$finalstep; i++))
  do
    j=0
    for name in k2_ptxs k4_ptxs k6_ptxs k1_ptxs k3_ptxs k5_ptxs L1_ptxs L2_ptxs L3_ptxs H1_ptxs H2_ptxs H3_ptxs H4_ptxs
      do
        python fittingAlgorithm.py -odeModel p2x7_MG.ode -myVariedParam $name -variedParamTruthVal ${array[$j]} -jobDuration $duration -fileName This_Is_A_Test.png -numRandomDraws 10 -numIters $iters -sigmaScaleRate $sigma -outputParamName I_ptxs -outputParamSearcher I_ptxs -outputParamMethod prop2x7100 -outputParamTruthVal 0 >& log.txt

        GUESS="$(bc <<< scale=6 ;grep bestVarDict log.txt | tail -1 | awk '{print $3}' | grep -Eo '[0-9\.]+')"
        echo "result of $name: $GUESS from trial number $i"
        echo "previous ${array[$j]} and current $GUESS "

        array[$j]=$GUESS
        j=$(($j+1))

      done
  done

k=0
for name in k2_ptxs k4_ptxs k6_ptxs k1_ptxs k3_ptxs k5_ptxs L1_ptxs L2_ptxs L3_ptxs H1_ptxs H2_ptxs H3_ptxs H4_ptxs
	  do
	    echo "new rate constant for $name is ${array[$k]}" >> log.results
    k=$(($k+1))
  done

echo "$(grep jobFitnesses log.txt | tail -1)" >> log.results
