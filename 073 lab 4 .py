class University:
    def __init__(self):
        self.age=0
        self.name=""
        self.marks=0
    def validate(self):
        if self.age>20 and self.marks in range(101):
            return True
        else :
            return False
    def check_qualification(self):
        if self.validate()==True:
            if self.marks>65 :
                return True
            else :
                return False
        else :
            return False
    def setter(self,name,age,marks):
        self.age=age
        self.name=name
        self.marks=marks
    def getter(self):
        print("Name is",self.name)
        print("Age is",self.age)
        print("Marks are",self.marks)
        print("Given information is valid:",self.check_qualification())
s1=University()
s1.setter("ra",24,50)
s1.getter()

s2=University()
s2.setter("ha",21,68)
s2.getter()
        
    
