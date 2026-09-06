tup = (2,3,1,4)
print(tup.count(2)) # count presence
print(tup.index(2)) # return first index, if not present the gives error
print(tup[-1]) # print last index
t1 = tup[1:3:2] # slice
for x in t1:
    print(x)

# Q how to slice tuple 

# any(true, false, false) ans true
# all(true, true, false) ans false
#sum(1,2,3,4,5,6) # add all elements
#min(1,2,3,4,56,8) # return min elements from it
#max(1,2,3,4,56,8) # return max elements from it
print(sorted(tup))
print(min(tup))
print(max(tup))
a,b,c,d = tup # a= 1, b= 2, c= 3, d = 4
t2 = tup*2 # repeat tup 2 times