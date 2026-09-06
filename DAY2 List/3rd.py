numbers = [2,4,5,7,98,43,56,23,10]
count = 0
counteven = 0
for i in range(len(numbers)): # for x in numbers:
    if(numbers[i]>10): # print element greater then 10 in list
        count+=1
    if(numbers[i]%2 == 0): # print elements are even in list
        counteven+=1
print(f"total number of elements greater then 10 are :{count}")
print(f"total number of even elements are :{counteven}")