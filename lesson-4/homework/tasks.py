#python homework
#1-problem
list1 = set(1,1,2)
list2 = set(2, 3, 4)
list10=set()
for i,j in zip(list1,list2):
    if i not in list2:
        list10.add(i)
    if j not in list1:
        list10.add(j)
print(list10)
#2-problem
n=int(input("enter number: "))
for i in range(1,n):
     print(i**2)
#3-problem
txt=input("enter text: ")
i=3
oo=[]
uu=["a","u","e","i","o"]
while i<len(txt)-1:
    if txt[i-1] not in uu:
        if txt[i-1] not in oo:
            txt=txt[:i]+"_"+txt[i:]
            oo.append(txt[i-1])
            i+=4
        else:
            i+=1
    else:
        i+=1
print(txt)
#4-problem
import random
def randomgame():
    b=0
    rn = random.randint(1, 100)
    for i in range(10):
        n=int(input("guess the number 1 to 100: "))
        if n==rn:
            print("you win")
            b+=1
            break
        elif n<rn:
            print("Too low!")
        else:
            print("Too high")
    if b==0:
        print("you lose")
    o=input("do you want to play again: ")
    oo=['Y', 'YES', 'y', 'yes', 'ok']
    if o in oo:
            randomgame()
randomgame()

#5-problem
parol=input("enter password: ")
if len(parol)<8:
    print("password is too short!")
b=0
for i in parol:
    if i.isupper():
        b+=1
        break
if b==0:
     print("Password must contain an uppercase letter.")
if b>0 and len(parol)>=8:
    print("Password is strong")
#6-problem
primenumbers=[]
for i in range(2,100):
    if i==2:
        primenumbers.append(i)
    else:
        t=1
        for j in primenumbers:
            if i%j==0:
              t-=1
        if t==1:
            primenumbers.append(i)
print(primenumbers)
#bonus task
import random 
com=0
user=0
while (com<5 and user<5):
    l=["rock","paper","scissors"]
    t=random.choice(l)
    r=input("enter rock or paper or scissors: ")
    if t=="rock" and r=="paper":
        user+=1 
        print("plus 1 for user")
    if r=="rock" and t=="paper":
        com+=1 
        print("plus 1 for com")
    if t=="scissors" and r=="paper":
        com+=1 
        print("plus 1 for com")
    if r=="scissors" and t=="paper":
        user+=1 
        print("plus 1 for user")
    if t=="scissors" and r=="rock":
        user+=1 
        print("plus 1 for user")
    if r=="scissors" and t=="rock":
        com+=1 
        print("plus 1 for com")
    if t=="rock" and r=="rock":
          print("same")
    if t=="paper" and r=="paper":
        print("same")
    if t=="scissors" and r=="scissors":
        print("same")
if com==5:
    print("computer won!")
else:
    print("you won!")
