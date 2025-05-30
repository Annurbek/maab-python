import math

class Vector:
    def __init__(self, *args):
        
        self.components = tuple(args)
    
    def __str__(self):
        
        return f"Vector{self.components}"
    
    def __add__(self, other):
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions")
        return Vector(*(a + b for a, b in zip(self.components, other.components)))
    
    def __sub__(self, other):
        
        if len(self.components) != len(other.components):
            raise ValueError("Vectors must have the same dimensions")
        return Vector(*(a - b for a, b in zip(self.components, other.components)))
    
    def __mul__(self, other):
        if isinstance(other, Vector):
            if len(self.components) != len(other.components):
                return "Unmatching number of components"
            result = 0
            for i in range(len(self.components)):
                result += self.components[i] * other.components[i]
            return result
        elif isinstance(other, (int, float)):
            return Vector([x * other for x in self.components])
        else:
            raise TypeError("Operand must be a Vector or a number")
    
    
    def truediv(self, scalar):
        
        if scalar == 0:
            raise ValueError("Cannot divide by zero")
        return Vector(*(a / scalar for a in self.components))
    
    def magnitude(self):
        
        return math.sqrt(sum(a**2 for a in self.components))
    
    def normalize(self):
        magnitude=self.magnitude()
        new_components=()
        for i in range(len(self.components)):
            new_components=new_components+(round(self.components[i]/magnitude,3),)
        return Vector(new_components)
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
print(v1.magnitude())  
v_unit = v1.normalize()
print(v_unit)
