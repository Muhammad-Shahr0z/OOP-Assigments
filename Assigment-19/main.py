# 19. callable() and __call__()
# Assignment:
# Create a class Multiplier with an __init__() to set a factor. Define a __call__() method that multiplies an input by the factor. Test it with callable() and by calling the object like a function.




class Multiplier:
    def __init__(self, factor):
        self.factor = factor  # store the factor

    def __call__(self, number):
        return number * self.factor  # when object is called like a function



d = Multiplier(5)
r= d(5)
print(r)

print(callable(d))