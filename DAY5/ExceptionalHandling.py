try:
    a = int(input("enter a number "))
    b = int(input("enter another number "))
    print(f"division of {a} and {b} is :{a/b}")
except ValueError:
    print("invalid number")
except ZeroDivisionError:
    print("error in dividing")
else: # runs only if no error occur
    a = int(input("enter a number "))
    b = int(input("enter another number "))
    print(f"division of {a} and {b} is :{a/b}")
finally: # always runs, either error occur or not
    a = int(input("enter a number "))
    b = int(input("enter another number "))
    print(f"division of {a} and {b} is :{a/b}")