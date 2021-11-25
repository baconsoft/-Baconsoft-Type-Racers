import random
print("A [baconsoft] Production")
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
print("____________________")
print(rol)
if rol == 4:
    print("Your Car Broke And Wont be able to be used the next turn")
# Player 2 Rolls
print (ptwo + s + r + i)
sd = input("Are You Ready? ")
list1 = [1, 2, 3, 4, 5, 6]
prol = (random.choice(list1))
print("____________________")
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
print("____________________")
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
print("____________________")
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
print("____________________")
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
print("____________________")
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
print("____________________")
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
print("____________________")
print(prole)
if prole == 4:
    print("Your Car Broke And Wont be able to be used the next turn")

# Turn 5
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
    print("____________________")
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
    print("____________________")
    print(prolr)
    if prolr == 4:
        print("Your Car Broke And Wont be able to be used the next turn")
# Final Round 1 score
fioro = rol + rolq + rolw + role + rolr
pfioro = prol + prolq + prolw + prole + prolr
# Round 1 RESET
rol and rolq and rolw and role and rolr and prol and prolq and prolw and prole and prolr == 0
    # Turn 6 (1) (ROUND 2 STARTS)
# Player 1 Rolls
print("ROUND 2!")
print("Turn 1!")
print (pone + s + r + i)
sd = input("Are You Ready? ")
list1 = [1, 2, 3, 4, 5, 6]
rol = (random.choice(list1))
print("____________________")
print(rol)
if rol == 4:
    print("Your Car Broke And Wont be able to be used the next turn")
# Player 2 Rolls
print (ptwo + s + r + i)
sd = input("Are You Ready? ")
list1 = [1, 2, 3, 4, 5, 6]
prol = (random.choice(list1))
print("____________________")
print(prol)
if prol == 4:
    print("Your Car Broke And Wont be able to be used the next turn")

# Turn 7
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
print("____________________")
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
print("____________________")
print(prolq)
if prolq == 4:
    print("Your Car Broke And Wont be able to be used the next turn")

# Turn 8
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
print("____________________")
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
print("___________________")
print(prolw)    
if prolw == 4:
    print("Your Car Broke And Wont be able to be used the next turn")

# Turn 9
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
print("____________________")
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
print("____________________")
print(prole)
if prole == 4:
    print("Your Car Broke And Wont be able to be used the next turn")

# Turn 10
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
    print("____________________")
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
    print("____________________")
    print(prolr)
    if prolr == 4:
        print("Your Car Broke And Wont be able to be used the next turn")

# Final Round 2 score
fiort = rol + rolq + rolw + role + rolr
pfiort = prol + prolq + prolw + prole + prolr
# Round 3 RESET
rol and rolq and rolw and role and rolr and prol and prolq and prolw and prole and prolr == 0
# Turn 1
# START OF ROUND 4
# Player 1 Rolls
print("Turn 1!")
print (pone + s + r + i)
sd = input("Are You Ready? ")
list1 = [1, 2, 3, 4, 5, 6]
rol = (random.choice(list1))
print("____________________")
print(rol)
if rol == 4:
    print("Your Car Broke And Wont be able to be used the next turn")
# Player 2 Rolls
print (ptwo + s + r + i)
sd = input("Are You Ready? ")
list1 = [1, 2, 3, 4, 5, 6]
prol = (random.choice(list1))
print("____________________")
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
print("____________________")
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
print("____________________")
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
print("____________________")
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
print("____________________")
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
print("____________________")
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
print("____________________")
print(prole)
if prole == 4:
    print("Your Car Broke And Wont be able to be used the next turn")

# Turn 5
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
    print("____________________")
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
    print("____________________")
    print(prolr)
    if prolr == 4:
        print("Your Car Broke And Wont be able to be used the next turn")
# Final Round 4 score
fiorf = rol + rolq + rolw + role + rolr
pfiorf = prol + prolq + prolw + prole + prolr
# Round 4 RESET
rol and rolq and rolw and role and rolr and prol and prolq and prolw and prole and prolr == 0
    
    # Turn 7 (1) (ROUND 5 STARTS)
# Player 1 Rolls
print("ROUND 2!")
print("Turn 1!")
print (pone + s + r + i)
sd = input("Are You Ready? ")
list1 = [1, 2, 3, 4, 5, 6]
rol = (random.choice(list1))
print("____________________")
print(rol)
if rol == 4:
    print("Your Car Broke And Wont be able to be used the next turn")
# Player 2 Rolls
print (ptwo + s + r + i)
sd = input("Are You Ready? ")
list1 = [1, 2, 3, 4, 5, 6]
prol = (random.choice(list1))
print("____________________")
print(prol)
if prol == 4:
    print("Your Car Broke And Wont be able to be used the next turn")

# Turn 7
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
print("____________________")
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
print("____________________")
print(prolq)
if prolq == 4:
    print("Your Car Broke And Wont be able to be used the next turn")

# Turn 8
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
print("____________________")
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
print("___________________")
print(prolw)    
if prolw == 4:
    print("Your Car Broke And Wont be able to be used the next turn")

# Turn 9
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
print("____________________")
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
print("____________________")
print(prole)
if prole == 4:
    print("Your Car Broke And Wont be able to be used the next turn")

# Turn 10
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
    print("____________________")
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
    print("____________________")
    print(prolr)
    if prolr == 4:
        print("Your Car Broke And Wont be able to be used the next turn")

# Final Round 5 score
fiorff = rol + rolq + rolw + role + rolr
pfiorff = prol + prolq + prolw + prole + prolr
# Round 5 RESET
rol and rolq and rolw and role and rolr and prol and prolq and prolw and prole and prolr == 0

# Turn FINAL_CHECK
# Validation Checker
if fioro + fiort + fiorf + fiorff > 80 and pfioro + pfiort + pfiorf + pfiorff > 80:
    print("It's a tie! Both players reached [20]")
if fioro + fiort + fiorf + fiorff > 80:
    print(pone + "Wins!")
elif pfioro + pfiort + pfiorf + pfiorff > 80:
    print(ptwo + "Wins!")
else:
    print("It's A Tie!, none of you reached 20")
quit
