import random
print("Welcome to type race")
pone = (input("Player 1,Your name is: "))
ptwo = (input("Player 2,Your name is: "))
r = ('Roll')
s = (" ")
i = " is"
# Turn 1
# Player 1 Rolls
print("Turn 1!")
print (pone + s + r + i)
sd = input("Are You Ready? ")
list1 = [1, 2, 3, 4, 5, 6]
rol = (random.choice(list1))
print(rol)
if rol == 4:
    print("Your Car Broke And Wont be able to be used the next turn")
# Player 2 Rolls
print (ptwo + s + r + i)
sd = input("Are You Ready? ")
list1 = [1, 2, 3, 4, 5, 6]
prol = (random.choice(list1))
print(prol)
if prol == 4:
    print("Your Car Broke And Wont be able to be used the next turn")

# Turn 2
# Player 1 Rolls
print("Turn 2!")
print (pone + s + r + i)
if rol != 4:
    sd = input("Are You Ready? ")
    list1 = [1, 2, 3, 4, 5, 6]
    rolq = (random.choice(list1))
else:
    rolq = 0
    print("Your Car Is Broken!")
print(rolq)
if rolq == 4:
    print("Your Car Broke And Wont be able to be used the next turn")
# Player 2 Rolls
print (ptwo + s + r + i)
if prol != 4:
    sd = input("Are You Ready? ")
    list1 = [1, 2, 3, 4, 5, 6]
    prolq = (random.choice(list1))
else:
    prolq = 0
    print("Your Car Is Broken!")
print(prolq)
if prolq == 4:
    print("Your Car Broke And Wont be able to be used the next turn")

# Turn 3
print("Turn 3!")
# Player 1 Rolls
print (pone + s + r + i)
if rolq != 4:
    sd = input("Are You Ready? ")
    list1 = [1, 2, 3, 4, 5, 6]
    rolw = (random.choice(list1))
else:
    rolw = 0
    print("Your Car Is Broken!")
print(rolw)
if rolw == 4:
    print("Your Car Broke And Wont be able to be used the next turn")
# Player 2 Rolls
print (ptwo + s + r + i)
if prolq != 4:
    sd = input("Are You Ready? ")
    list1 = [1, 2, 3, 4, 5, 6]
    prolw = (random.choice(list1))
else:
    prolw = 0
    print("Your Car Is Broken!")
print(prolw)
if prolw == 4:
    print("Your Car Broke And Wont be able to be used the next turn")

# Turn 4
# Player 1 Rolls
print("Turn 4!")
print (pone + s + r + i)
if rolw != 4:
    sd = input("Are You Ready? ")
    list1 = [1, 2, 3, 4, 5, 6]
    role = (random.choice(list1))
else:
    role = 0
    print("Your Car Is Broken!")
print(role)
if role == 4:
    print("Your Car Broke And Wont be able to be used the next turn")
# Player 2 Rolls
print (ptwo + s + r + i)
if prolw != 4:
    sd = input("Are You Ready? ")
    list1 = [1, 2, 3, 4, 5, 6]
    prole = (random.choice(list1))
else:
    prole = 0
    print("Your Car Is Broken!")
print(prole)
if prole == 4:
    print("Your Car Broke And Wont be able to be used the next turn")

# Turn 5

# Validation Checker
if rol + rolq + rolw + role > 20 and prol + prolq + prolw + prole > 20:
    print("It's a tie!")
if rol + rolq + rolw + role > 20:
    print(pone + "Wins!")
elif prol + prolq + prolw + prole > 20:
    print(ptwo + "Wins!")
else:
# Player One  Rolls
    print("Turn 5!")
    print (pone + s + r + i)
    if role != 4:
        sd = input("Are You Ready? ")
        list1 = [1, 2, 3, 4, 5, 6]
        rolr = (random.choice(list1))
    else:
        rolr = 0
        print("Your Car Is Broken!")
    print(rolr)
    if rolr == 4:
        print("Your Car Broke And Wont be able to be used the next turn")
    # Player 2 Rolls
    print (ptwo + s + r + i)
    if prole != 4:
        sd = input("Are You Ready? ")
        list1 = [1, 2, 3, 4, 5, 6]
        prolr = (random.choice(list1))
    else:
        prolr = 0
        print("Your Car Is Broken!")
    print(prolr)
    if prolr == 4:
        print("Your Car Broke And Wont be able to be used the next turn")

# Turn FINAL CHECK

# Validation Checker
if rol + rolq + rolw + role + rolr > 20 and prol + prolq + prolw + prole + prolr > 20:
    print("It's a tie!")
if rol + rolq + rolw + role + rolr > 20:
    print(pone + "Wins!")
elif prol + prolq + prolw + prole + prolr > 20:
    print(ptwo + "Wins!")
else:
    print("It's A Tie!")
quit