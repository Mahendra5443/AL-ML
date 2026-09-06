number =[1,2,3,4,5,6,7,8,9,10]
number.sort(key= lambda x:x,reverse=True) # function, reverse
print(sorted(number,key = lambda x:x, reverse= True)) # list/tuple, function, reverse
print(number)