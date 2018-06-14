"""
For processing ODE outputs in support of Satin/Despa collaborations 
"""

from matplotlib.ticker import ScalarFormatter
import math
import cPickle as pickle
import matplotlib.pylab as plt
import numpy as np
#import analyzeODE as ao 
#import downSamplePickles as dsp
import json

class empty:pass
mM_to_uM = 1e3
ms_to_s = 1e-3


import re
def readPickle(name = "PCa0.75kss0.25.pkl",verbose=True,readSubset=None,readConcat=False):          

  if readConcat:
    print name 
    name = re.sub(r'\d+\.p', 'cat.p', name)  # pickle 
    print "Reading concatenated file %s instead" % name

  if verbose: 
    print "Reading " + name  
  pkl_file = open(name, 'rb')
  data1 = pickle.load(pkl_file)  
  pkl_file.close()

  if readSubset!=None:
    print "HARDCODED TO Cai, Ca_jct, Ca_SR for now"
    subsets = ["Cai","Ca_jct1","Ca_SR"]
    nTs = np.shape( data1["t"] )[0]
    ar = np.zeros([nTs, len(subsets)]) 
    si = data1["s"]
    s_idx = data1["s_idx"]
    for i,subset in enumerate(subsets):
      idx = s_idx.index(subset)
      ar[:,i] =  si[:, idx ] 
    # overwrite 
    data1["s"] = ar                  
    data1["s_idx"] = subsets             
  

  return data1  
# subset: None - load all attributes
#         [state1,state2, ...] 
def LoadPickles(caseDict,noOverwrite=False,
                verbose=True,readSubset=None,readConcat=False):
  for key,case in caseDict.iteritems():
    if verbose:
      print "# ", key
      print "Loading"  , case.name

    if hasattr(case,'data') and noOverwrite==True:
      print "Skipping read, since already populated"
    else: 
      case.data = readPickle(case.name,verbose=verbose,readSubset=readSubset, 
                             readConcat=readConcat) 

# loads data stored in ode object
# returns a single array with quantity of interest (valsIdx) 
# which is the time series of the idxName 
def GetData(data,idxName):
    #print "getting data" 
    datac = empty()
    datac.t = data['t'] * ms_to_s   # can't guarantee units are in [ms]
    #datac.s = data['s'] / mM_to_uM  # ??? not all states are in uM....
    datac.s_idx = data['s_idx']
    #datac.j = data['j']
    datac.j_idx = data['j_idx']

    if idxName in datac.j_idx:
      datac.v = data['j']   
      datac.v_idx = datac.j_idx
    # states 
    elif idxName in datac.s_idx:
      datac.v = data['s'] 
      datac.v_idx = datac.s_idx
    else:
      print idxName, " not found"
      datac.v =None

    idx = datac.v_idx.index(idxName)
    datac.valsIdx = datac.v[:,idx] 

    return datac

### taken from fitter.py/analyzeODE.py, used to process data made to put into panda format at the end.
# Most of the original implementation has been scrapped
def ProcessDataArray(dataSub,mode,timeRange=[0,1e3],key=None):

      # PRINT NO, NEED TO PASS IN TIME TOO 
      timeSeries = dataSub.t
      idxMin = (np.abs(timeSeries-timeRange[0])).argmin()  # looks for entry closest to timeRange[i]
      idxMax = (np.abs(timeSeries-timeRange[1])).argmin()
      valueTimeSeries = dataSub.valsIdx[idxMin:idxMax]
      print "obj.timeRange[0]: ", timeRange[0]
      print "valueTimeSeries: ", valueTimeSeries
   
      tRange = timeSeries[idxMin:idxMax] - timeSeries[idxMin]
      waveMax = np.argmax(valueTimeSeries)
      tRangeSub = tRange[waveMax:]
      caiSub = valueTimeSeries[waveMax:]
      if 1: # key=="Cai": # for debug
        tag = 12
        np.savetxt("test%d"%tag,valueTimeSeries)
      #print "dataSub.valsIdx: ", dataSub.valsIdx 
      if mode == "max":
          result = np.max(valueTimeSeries)
      elif mode == "min":
          result = np.min(valueTimeSeries)
      elif mode == "mean":
          result = np.mean(valueTimeSeries)
      elif mode == "amp":
          result = (np.max(valueTimeSeries) - np.min(valueTimeSeries))
      elif mode == "ptxsth":
 	  tpx = np.array([0,0,7.328244275,25.64885496,32.97709924,53.58778626,79.23664122,94.80916031,107.1755725,118.6259542,120.9160305,122.2900763])*10**-3
          Ipx = np.array([0,-0.0505952381,-0.06845238095,-0.08035714286,-0.09523809524,-0.2083333333,-0.5863095238,-0.8392857143,-0.8988095238,-0.9077380952,0.03273809524,0.002976190476])
          modeldata = [timeSeries, valueTimeSeries]
          litdata = [tpx, Ipx]
          result = fp.test(litdata,modeldata)*100
      else:
          raise RuntimeError("%s is not yet implemented"%output.mode)

      return result
