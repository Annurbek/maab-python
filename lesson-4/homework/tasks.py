#python homework
#1-problem
list1 = [1, 1, 2]
list2 = [2, 3, 4]

set1 = set(list1)
set2 = set(list2)

result = set1.symmetric_difference(set2)
print(result)
#2-problem
n=int(input("enter number: "))
for i in range(1,n):
     print(i**2)
#3-problem
txt = input("enter text: ")
result = ""
unli = {'a', 'e', 'i', 'o', 'u'}
count = 0

for i in range(len(txt)):
    result += txt[i]
    count += 1
    
    if i < len(txt) - 1 and count == 3:
        if txt[i] in unli or (i > 0 and result[-2] == '_'):
            count = 2
        else:
            result += '_'
            count = 0

print(result)
#4-problem
import random
while True: 
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
    if o not in oo:
            break

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
primenumbers = []
for i in range(2, 100):
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primenumbers.append(i)
print(primenumbers)
#bonus task
import random
choices = ["rock", "paper", "scissors"]
win_conditions = {
    ("rock", "scissors"): "user",
    ("paper", "rock"): "user",
    ("scissors", "paper"): "user"
}

com_score = 0
user_score = 0

while com_score < 5 and user_score < 5:
    com_choice = random.choice(choices)
    
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    while user_choice not in choices:
        print("Invalid choice! Please enter rock, paper, or scissors.")
        user_choice = input("Enter rock, paper, or scissors: ").lower()
        
    print(f"Computer chose: {com_choice}")
    
    if com_choice == user_choice:
        print("It's a tie!")

    elif (user_choice, com_choice) in win_conditions:
        user_score += 1
        print(f"Plus 1 for user! Score: User {user_score}, Computer {com_score}")

    else:
        com_score += 1
        print(f"Plus 1 for computer! Score: User {user_score}, Computer {com_score}")

if com_score == 5:
    print("Computer won!")
else:
    print("You won!")