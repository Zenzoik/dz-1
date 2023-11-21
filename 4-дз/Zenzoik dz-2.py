import math

class Vector:
    def __init__(self, components):
        self.components = components
    def __str__(self):
        return '(' + ','.join(map(str, self.components)) + ')'
    def equals(self, second):
        return self.components == second.components
    def add(self, second):
        if len(self.components) != len(second.components):
            raise ValueError("Different lenght")
        result = [a + b for a, b in zip(self.components, second.components)]
        return Vector(result)

    def subtract(self, second):
        if len(self.components) != len(second.components):
            raise ValueError("Different lenght")
        result = [a - b for a, b in zip(self.components, second.components)]
        return Vector(result)

    def dot(self, second):
        if len(self.components) != len(second.components):
            raise ValueError("Different lenght")
        result = sum(a * b for a, b in zip(self.components, second.components))
        return result

    def norm(self):
        result = math.sqrt(sum(a ** 2 for a in self.components))
        return result