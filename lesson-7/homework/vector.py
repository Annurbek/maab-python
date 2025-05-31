#vector 
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
    
    def __mul__(self,other):
        new_components=0
        if len(self.components)!=len(other.components):
            return "Unmatching number of components"
        for i in range(len(self.components)):
            new_components=new_components+((self.components[i]*other.components[i]))
        return new_components

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
# v5 = 3 * v1
# print(v5)   i did not undurstand how to do it , please teach me        
print(v1.magnitude())  
v_unit = v1.normalize()
print(v_unit)      