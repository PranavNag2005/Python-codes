class employee:
    def __init__(self,name,position):
        self.name=name
        self.position=position
        self.salary=0
    def set_salary(self,salary):
        if salary>0:
            self.salary=salary
            return "successfully assigned salary"
        else:
            print("Invalid salary!")
    def get_Salary(self):
        return self.salary
e=employee("pranav","Hr")
print(e.set_salary(1000))

print(e.get_Salary())