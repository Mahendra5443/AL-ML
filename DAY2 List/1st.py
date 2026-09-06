numbers = [1,2,3,4,5]
numbers.append(6)  # add 6 in end
numbers.extend([7,8,9]) # add another list in end
numbers.insert(len(numbers),10) # insert at given index
if 11 in numbers: # safe way to check if a number is present in list or not
    numbers.remove(11) # remove first accarance of that number
numbers.count(10) # count occurance
numbers.index(5) # Find index of 5
num = numbers.copy() # shallow copy
numSlice = num[0:(int)(len(num)/2):2] # slice [from,end,step]
num.sort() # sort list
num.reverse() # reverse a list
print(f"minimum element in list is {min(num)} and maximum element in list is {max(num)}")# min and max
for i in range(len(numbers)): # loop #len() for length of list or use for x in numbers:
    print(numbers[i])