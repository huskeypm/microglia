import matplotlib.pylab as plt
import analyzeGotran as aG

data1=aG.readPickle("test_cat.pickle") 

CaData1 = aG.GetData(data1,"Cai") 

plt.plot(CaData1.t*1000,CaData1.valsIdx) 
fileName = "test.png"
plt.gcf().savefig(fileName) 

print "Printed ", fileName

