#initiate the class
class Employee:
    # special method/magic method/dunder method - contructor
    def __init__(self):
        print(id(self))
        #print("Started executing attribute/data") 
        self.id = 123
        self.salary = 50000
        self.designation = "SDE"
        
    def travel(self):
        print(f"Traveling to Delhi")
        
# create an object of the class
Ram = Employee()
print(id(Ram))

shaktiman = Employee()
print(id(shaktiman))

#print(Ram.designation)
#Ram.travel("New York")
