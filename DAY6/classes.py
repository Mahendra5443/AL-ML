class student:
    __college = "ABC university"
    def __init__(self, name, age):
        print("constructor activated automatically")
        self.__name = name
        self.__age = age
    def show(self):
        print(f"printing student's name :{self.__name}\n printing student's age :{self.__age} \n printing student's college :{student.__college}")
    def setName(self, name):
        self.__name = name
    def setAge(self, age):
        self.__age = age
    def getName(self):
        return self.__name
    def getAge(self):
        return self.__age
s =student("mahendra", 23)
s.show()
# print(s.__age) name, age, collegename are private. so can't excess like this direactly from ouside the class
print(s.getName())
print(s.getAge())