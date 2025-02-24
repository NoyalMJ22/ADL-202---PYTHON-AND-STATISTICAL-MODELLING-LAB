import numpy as np

Populations=np.array([4779736,710231,6392017,2915918,37253956,5029196,3574097,897934])

mean=np.sum(Populations)/len(Populations)
median=np.median(Populations)
variance=np.sum((Populations -mean)**2/len(Populations)-1)

print("Mean:",mean)
print("Median :",median)
print("Variance:",variance)
