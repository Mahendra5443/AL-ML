try:
    age = int(input("enter your age "))
    if(age<0):
        raise ValueError("age value can't be negative")
    elif(age>=18):
        print("you are eligible for voting")
    else:
        print("you are not eligible for voting")
except ValueError:
    print(f"error in age{ValueError}")
finally:
    print("program completed")