import random


password = "abc123"

while True:
    user_pass = input("Enter your password: ")
    if password == user_pass:
        print("you are in")
        break
    else:
        print("Worng password!")


sakhty = input("Bazi Ason(a) Bashe ya shakht(s)?")

if sakhty == 'a':
    tekrar = 10
else:
    tekrar = 5

adad_tasadofi = random.randint(1, 100)

for i in range(tekrar):
    user_input = int(input("Enter number: "))
    if user_input > adad_tasadofi:
        print("adad shoma bozorgtar bood!")
    elif user_input < adad_tasadofi:
        print("adad shoma kochaktar bood!")
    else:
        print("shoma bazi ro bordid!")
        break
    
print("payan bazi")