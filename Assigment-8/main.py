# 8. The super() Function
# Assignment:
# Create a class Person with a constructor that sets the name. Inherit a class Teacher from it, add a subject field, and use super() to call the base class constructor.


class Person:
    def __init__(self, name):
        self.name = name
        print(f"Teacher's name set to {self.name} from the parent class Person.")


class Teacher(Person):
    def __init__(self, subject, name):
        super().__init__(name)
        self.subject = subject
        print(f"Received name: {name} at the time of object creation. The subject has now been set to {subject} as {self.subject}.")


Teacher1 = Teacher("Math", "Muhammad Shahroz")
Teacher2 = Teacher("English", "Haroon Rashid")
Teacher3 = Teacher("Physics", "Tayyab")




