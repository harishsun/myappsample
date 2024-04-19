#For Loop

""" 

planet = "Earth"

for i in planet:
    print(i)


vaccines = ("Moderna", "Pfizer", "Sputlink", "Covaxin", "Astra z")

for vac in vaccines:
    print(f"{vac} provides immunization against Covid 19 Virus")

print("End of code")


vaccines = ["Moderna", "Pfizer", "Sputlink", "Covaxin", "Astra z"]

for vac in vaccines:
    print(f"{vac} provides immunization against Covid 19 Virus")

print("End of code")



x = 0
while x <= 10:
    print("Value of X is: ", x)
    x = x + 1



vaccines = ["Moderna", "Pfizer", "Sputlink", "Covaxin", "Astra z"]

for vac in vaccines:
    print("")
    print("I would like to take a shot of: ")
    for i in vac:
        print(i)

print("End of code")




import time
x = 2
while True:
    print("Value of X is: ", x)
    x*=2
    time.sleep(2)



# Break Statement
for i in "DevOps":
    print(i)
    if i == "O":
        print("Found my data.")
        break
print("Out of loop")


# Continue Statement
for i in "DevOps":
    if i == "O":
        print("Found my data.")
        continue
    print(f"The value of i is {i}")
print("Out of loop")


    """

# Random

import random
vaccines = ["Moderna", "Pfizer", "Sputlink", "Covaxin", "Astra z"]

random.shuffle(vaccines)

print(vaccines)

lucky = random.choice(vaccines)

print(f"The luckiest vaccine is {lucky}.")

for vac in vaccines:
    print(f"######### Testing the vaccines {vac} #############")
    if vac == lucky:
        print("*****************************************")
        print(f"{lucky} vaccine test is successfull")
        print("*****************************************")
        print()
        break
        


