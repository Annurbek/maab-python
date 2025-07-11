#vector 
import math

class Vector:
    def __init__(self, *args):
        self.components = tuple(args)

    def __str__(self):
        return f"Vector{self.components}"

    def __add__(self, other):
        if not isinstance(other, Vector) or len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))

    def __sub__(self, other):
        if not isinstance(other, Vector) or len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))

    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                raise ValueError("Vectors must have the same dimensions")
            return sum(a * b for a, b in zip(self.components, other.components))
        elif isinstance(other, (int, float)):
            return Vector(*(a * other for a in self.components))
        else:
            return NotImplemented

    def __rmul__(self, other):
        return self.__mul__(other)

    def __truediv__(self, scalar):
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        return Vector(*(a / scalar for a in self.components))

    def magnitude(self):
        return math.sqrt(sum(a ** 2 for a in self.components))

    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize zero vector")
        return Vector(*(round(a / mag, 3) for a in self.components))

# Example usage:
v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)
print(v1)
v3 = v1 + v2
print(v3)
v4 = v2 - v1
print(v4)
dot_product = v1 * v2
print(dot_product)
v5 = 3 * v1
print(v5)
print(v1.magnitude())
v_unit = v1.normalize()
print(v_unit)