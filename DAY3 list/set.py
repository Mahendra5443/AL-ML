nums = [1,2,2,3,3,3,4]
s = set(nums)
s.add(5)
s1 = s.copy() # return a shallow copy of set
# s.remove(10) # it will give error as this number is not present
s.discard(10) # safely remove element from set
print(s.pop()) #remove first element inserted
print(s)
print(s.union(s1)) # add two set
print(s.intersection(s1)) # add element present in both set "&"
print(s.difference(s1)) # A-B set "-"
print(s.symmetric_difference(s1)) # in either A or B not A and B "^"
if 10 in s:
    print("yes 10 present")
else:
    print("no, 10 not present")