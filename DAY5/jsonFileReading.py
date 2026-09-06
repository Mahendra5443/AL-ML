import json
data = [
    {"name": "A", "marks": 85},
    {"name": "B", "marks": 62},
    {"name": "C", "marks": 91}
]
with open("student.json","w") as file:
    json.dump(data,file,indent=4, sort_keys=True)

with open("student.json","r") as file:
    info = json.load(file)
    print(sorted(info, key=lambda x: x["marks"], reverse=True))