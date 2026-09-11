import numpy as np

def bestSizingMatrix(mtx):
    n= mtx.size
    bestRow =1
    for i in range(int(np.sqrt(n)),0,-1):
        if n%i==0:
            bestRow = i
            break
    bestCol = n//bestRow
    return mtx.reshape(bestRow,bestCol)
           
a = np.arange(1,13)
b = np.arange(2,50,7)
print("before")
print(a)
print()
print(b)
a =  bestSizingMatrix(a)
b =  bestSizingMatrix(b)
print("after")
print(a)
print()
print(b)
# issue: it doesn't work for prime no. as it's sqrt doesn't gets divisible with any number so raw conut wil remain 1

# NOW MULTIPLICATION TASK

print(a @ b) # it is a matrix multiplication we studies in 11-12 maths class
print(a*b) #happens only if dimension are same