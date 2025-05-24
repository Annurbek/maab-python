#task-3
n=int(input("enter a positive integer: "))
for i in range(1,n+1):
    if n%i==0:
        print(i, "is factor of ",n)