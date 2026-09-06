student = {
    "name" :"Mahendra Singh Sisodiya",
    "age" :21
}
student["class"] = 12
student["Age"] = 25
del student["Age"] # to delete "Age" give error if not present
student["Age"] = 25
student.pop("Age") # to delete "Age" give error if not present
if "Age" in student:
    student.pop("Age")
else:
    print("No Age present")
print(student)
print(student.keys()) # print all keys
print(student.values()) # print all values
print(student.get("Age","no Age present"))