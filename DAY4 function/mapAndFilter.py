#map
# 
number = [1,2,3,4,5,6]
def squaring(x):
    return x*x;
print(list(map(squaring,number))) # or map(lambda x:x*x,number)
#print(list(map(lambda x:x%2==0,number)))
def clear(x):
    if x%2==0:
        return x;
# print(list(filter(clear,number)))
print(list(filter(lambda x:x/2,number)))