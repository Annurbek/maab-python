import math

class Vector:
    def __init__(self, *args):
        if len(args) == 1 and isinstance(args[0], (list, tuple)):
            self.components = tuple(args[0])
        else:
            self.components = tuple(args)
    
    def __str__(self):
        return f"Vector{self.components}"
    
    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for addition")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))
    
    def __sub__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions for subtraction")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions for dot product")
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*(x * other for x in self.components))
        else:
            raise TypeError("Operand must be a Vector or a number")

    def __rmul__(self, other):
        return self.__mul__(other)
    
    def __truediv__(self, scalar):
        if not isinstance(scalar, (int, float)):
            raise TypeError("Division is only supported by scalar values")
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        return Vector(*(x / scalar for x in self.components))
    
    def magnitude(self):
        return math.sqrt(sum(x * x for x in self.components))
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector")
        return Vector(*(round(x/mag, 3) for x in self.components))

if __name__ == "__main__":
    v1 = Vector(1, 2, 3)
    v2 = Vector(4, 5, 6)
    
    print(v1)
    v3 = v1 + v2
    print(v3)
    v4 = v2 - v1
    print(v4)
    dot_product = v1 * v2
    print(dot_product)  
    v5 = v1 * 3
    print(v5)
    v6 = 3 * v1
    print(v6)
    print(v1.magnitude())
    v_unit = v1.normalize()
    print(v_unit)
