#task-5
n=int(input("enter one number: "))
def is_prime(n):
    h=0
    if n==2:
       print(True)
    elif n>2:
        for i in range(2, n):
          if (n % i) == 0:
             print(False)
             h=1
             break
        if h==0:
             print(True)
    else:
         print(False)  

is_prime(n)
  