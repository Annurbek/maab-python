universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]
student=[]
tuition=[]
def enrollment_stats(uni):
     for i in uni:
          student.append(i[1])
          tuition.append(i[2])
     return student,tuition
enrollment_stats(universities)
print("Total students: ", sum(student))
print("Total tuition: $ ",sum(tuition))
def mean(l):
    if l==student:
       print("Student mean: ",round(sum(l)/len(l),2) ) 
    else:
        print("Tuition mean: $ ",round(sum(l)/len(l),2)  ) 
def median(l):
    if l==student:
       print("Student median: ",sorted(l)[len(l)//2]) 
    else:
        print("Tuition median: $ ",sorted(l)[len(l)//2] ) 
mean(student)
median(student)
mean(tuition)
median(tuition)