import json

student = {
    "name": "Mahendra",
    "age": 21,
    "skills": ["Python", "React", "Node"]
}

with open(r"C:\Users\MY-PC\Desktop\test.txt","w") as file:
    json.dump(student,file, indent =4)

with open(r"C:\Users\MY-PC\Desktop\test.txt","r") as file:
    info = json.load(file)
    print(info["name"])
    print(info["age"])
    print(info["skills"])    
