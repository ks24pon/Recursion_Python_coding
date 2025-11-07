class Person:
    def __init__(self, firstName, lastName):
        self.firstName = firstName
        self.lastName = lastName

    def getFullName(self):
        return self.firstName + " " + self.lastName
    
carly = Person("Carly", "Angelo")

print(carly)
print(carly.getFullName())