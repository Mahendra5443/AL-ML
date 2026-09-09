numbers = [10,20,30]
#1st way
for i in numbers:
    print(f"{i}")
#2nd way

i = iter(numbers)
print(next(i))
print(next(i))
print(next(i))

#3rd
i = iter(numbers)
for x in range(len(numbers)):
    print(next(i))