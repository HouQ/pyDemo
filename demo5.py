class Employee:
    'all in all'
    empCount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
    def displayCount(self):
        print Employee.empCount
    def displayEmployee(self):
        print self.name,self.salary

emp1 = Employee('tom',1000)
emp2 = Employee('jack',2000)

emp1.displayEmployee()
emp2.displayEmployee()
print Employee.empCount
print Employee.__doc__
print Employee.__name__
print Employee.__bases__
print Employee.__dict__