# 7. Access Modifiers: Public, Private, and Protected
# Assignment:
# Create a class Employee with:

# a public variable name,

# a protected variable _salary, and

# a private variable __ssn.

# Try accessing all three variables from an object of the class and document what happens.


class Employee:
    def __init__(self):
        self.name = "Muhammad Shahroz"  # Public
        self._salary = 50000            # Protected
        self.__ssn = 78822              # Private


Obj = Employee()

# Public: Accessible
print(f"Public: {Obj.name}")

# Protected: Accessible (but not recommended)
print(f"Protected: {Obj._salary}")

# Private: Not accessible directly – this will raise an AttributeError
print({Obj.__ssn})  # ❌ Error: 'Employee' object has no attribute '__ssn'
