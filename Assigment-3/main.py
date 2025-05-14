# 3. Public Variables and Methods
# Assignment:
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.


class Car:
    brand = "Toyota"  # public variable

    def start(self):
        print(f"Car Started")  # public method

# Object creation
Corolla = Car()

# Accessing public variable
print(Corolla.brand)

# Accessing public method
Corolla.start()


