class parent:
    def __init__(self,father_name, mother_name):
        self.father_name =father_name
        self.mother_name =mother_name
    def getMotherName(self):
        return self.mother_name
    def getFatherName(self):
        return self.father_name
    
class child1(parent):
    def __init__(self,name, father_name, mother_name):
        super().__init__(father_name, mother_name)
        self.name = name
        self.father_name = father_name
        self.mother_name = mother_name

ch1 = child1("ram","dashrath","kekayi")
print(ch1.getMotherName())
print(ch1.getFatherName())