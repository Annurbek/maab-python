#homework 5
#1-problem
def convert_cel_to_far(F):
           C = (F - 32) * 5/9
           print(F,"degrees F =",round(C,2),"degrees C")
           
F=int(input("Enter a temperature in degrees F: "))
convert_cel_to_far(F)


def convert_cel_to_cel(C):
           F = C * 9/5 + 32
           print(C,"degrees C =",round(F,2),"degrees F")
           
C=int(input("Enter a temperature in degrees C: "))
convert_cel_to_cel(C)



       
