# 15. Method Resolution Order (MRO) and Diamond Inheritance
# Assignment:
# Create four classes:

# A with a method show(),

# B and C that inherit from A and override show(),

# D that inherits from both B and C.

# Create an object of D and call show() to observe MRO.



class A:
    def show(self):
        print("A class Method Called")

class B(A):
    def show(self):
        print("B class Method Called")

class C(A):
    def show(self):
        print("C class Method Called")

class D(B, C):
    pass
    # def show(self):
    #     print("D class Method Called")
      

# Create object
obj = D()
obj.show()  # Output will depend on MRO Class B Called
