def generates():
    for i in range(1,11):
        yield i # it returns each value and continue code

def listmaker():
    list =[]
    for i in range(1,11):
        list.append(i);
    return list # return can return a single value

print(listmaker())
print(list(generates())) 

# or we can use iterator on it also
gen = generates()

for i in generates():
    print(next(gen))