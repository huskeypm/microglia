# README #

Prelim data for microglia
- CaM is not behaving as a state for some reason 

### What is this repository for? ###

* Quick summary
* Version
* [Learn Markdown](https://bitbucket.org/tutorials/markdowndemo)

### How do I get set up? ###

* Summary of set up
* Configuration
* Dependencies
* Database configuration
* How to run tests

source configgotran.bash
gotranrun  simpleRyR.ode  --plot_y O --tstop=2000 --dt 1.

python /u1/pmke226/srcs//gotran/scripts//gotranrun test.ode  --plot_y logpATP --tstop=30 --dt 0.1

python /home/AD/bdst227/sources/gotran/scripts/gotranrun microglia.ode --plot_y logpATP --tstop=30000 --dt 0.1  # 30s

python /home/AD/bdst227/sources/gotran/scripts/gotranrun P2X4_test.ode --plot_y i_P2X --tstop=5000 --dt 0.1  # 5s

### tstop is in units of ms. 1000 ms = 1 s.

montage -label '(a)' Intracellular_logpATP_Test_Test2_Test3_plots.png -label '(b)' Intracellular_Ca_jct1_Test_Test2_Test3_plots.png -label '(c)' Intracellular_i_P2X_Test_Test2_Test3_plots.png -label '(d)' Intracellular_r_BDNF_Test_Test2_Test3_plots.png -pointsize 100 -tile 2x2 -geometry '+2+2+2+2>' merged_Test_logpATP_Ca_jct1_i_P2X_r_BDNF_Plots.png

python daisychain.py -dt 0.10 -jit -stim 1000 -T 10000 -iters 6 -fileOutputDirectory /home/AD/bdst227/ipython/ipython-notebooks/microglia/ranJobs/ -finalOutputDirectory /net/share/bdst227/microglia/microglia_Simulations_Data/ -downsampleRate 10 -odeName Starting_Point_2.ode -name /home/AD/bdst227/ipython/ipython-notebooks/microglia/ranJobs/test3_Starting_point_2 &

* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact
