student = {
    "name" :"Mahendra Singh Sisodiya",
    "age" :21
}
def ageIncrement(*student):
    for a in student:
        a["age"] += 10
ageIncrement(student)
print(student["age"])