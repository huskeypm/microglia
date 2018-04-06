Copied from Ben's (bens-code) repo

# To run basic test
source ../configgotran.bash 
python ../fitting/daisychain.py -odeName microgliav3.ode 

# To run case with a specific NFAT concentration and ATP concentration, saved to a named .pickle file 
python ../fitting/daisychain.py -odeName microgliav3.ode -t 0.1 -T 100 -iters 1 -jit -var CNt_NFAT 2e3 -var stim_amplitude 10 -name NFAT2e3_ATP10.pickle

# To reproduce Ca transients in microglia
python ../fittingdaisychain.py -t 0.1 -jit -odeName microgliav3.ode -T 10000 -iters 1 -outBase "test.pickle"

# To print latex 
python  /home/AD/pmke226/sources//gotran/scripts/gotran2latex microgliav2.ode 

# To run no p2x simulation
Please, check "fitting directory". Everything is automated. To analyze data, try to use daisy.ipynb file previously used by Ben