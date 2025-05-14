# 5. Static Variables and Static Methods
# Assignment:
# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.xz


class MathUtils:
    
    @staticmethod
    def add(a,b):
        return a + b


Result = MathUtils.add(5 ,6)
print(f"Result : {Result}")

