# 6. Constructors and Destructors
# Assignment:
# Create a class Logger that prints a message when an object is created (constructor) and another message when it is destroyed (destructor).



class Logger:
    def __init__(self):
        print("Logger Class Instance Created")  # Constructor message

    def __del__(self):
        print("Logger Class Instance Destroyed")  # Destructor message



L2 = Logger()
L3 = Logger()
L4 = Logger()
