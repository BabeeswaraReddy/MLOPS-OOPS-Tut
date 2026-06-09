#initiate the class
class Employee:
    # special method/magic method/dunder method - contructor
    def __init__(self):
         
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        
    def travel(self,destination):
        print(f"Traveling to {destination}")
        
# create an object of the class
Ram = Employee()

print(Ram.designation)
Ram.travel("New York")
