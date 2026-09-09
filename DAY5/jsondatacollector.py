import json
def adddata():
    name = input("enter your name :")
    age = int(input("enter your age :"))
    data =[]
    try:
        with open ("DAY5/studentdata.txt","r") as file:
            data = json.load(file)
    except:
        print("no previous data found so creating a new one")
    data.append({"name":name,"age":age})
    with open("DAY5/studentdata.txt","w") as file:
        json.dump(data,file,indent=4)
    print(f"your {name} and {age} is saved in studentdata.txt file")

def display():
    with open ("DAY5/studentdata.txt","r") as file:
        print(json.load(file))

try:
    print("wanna add student data in studnetdata.txt file? y/n")
    ch=input()[0]
    if(ch.lower()=="y"):
        adddata()
    elif(ch.lower()=="n"):
        display()
    else:
        raise TypeError("typed another character")
except TypeError:
    print("typed other then y or n")