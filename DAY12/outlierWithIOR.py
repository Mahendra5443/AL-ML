import numpy as np
x = np.array([10,20,30,40,50,60,70,80,90,100,1000])
Q1 = np.percentile(x,25)
Q2 = np.percentile(x,50)
Q3 = np.percentile(x,75)
IQR = Q3 -Q1
#Q1
print(Q1)
#median
print(Q2)
#IQR
print(IQR)
#lower IQR bound
lower =(Q1-1.5*IQR)
print(lower)
#upper IQR bound
upper= (Q3+1.5*IQR)
print(upper)
#outlier 
print(x[~((x>lower)&(x<upper))])