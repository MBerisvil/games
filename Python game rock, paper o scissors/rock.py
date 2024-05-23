import random

randomm = random.randint(0, 3)
machine = ""
print("1. Rock")
print("2. Paper")
print("3. Scissors")
opcion = int(input("Choose your option: "))

if opcion == 1:
    user = "rock"
elif opcion == 2:
    user = "paper"
elif opcion == 3:
    user = "scissors"
print("You choises: ", user)

if randomm == 0:
    machine = "rock"
elif randomm == 1:
    machine = "paper"
elif randomm == 2:
    machine = "scissors"
print("Machine choises: ", machine)
print("... ")

if machine == "rock" and user == "paper":
    print("You win!, paper covers rock")
elif machine == "paper" and user == "scissors":
    print("You win!, scissors cuts paper")
elif machine == "scissors" and user == "rock":
    print("You win!, rock smashes scissors")
elif machine == "paper" and user == "rock":
    print("You lose!, paper covers rock")
elif machine == "scissors" and user == "paper":
    print("You lose!, scissors cuts paper")
elif machine == "rock" and user == "scissors":
    print("You lose!, rock smashes scissors")
elif machine == user:
    print("Tie")
else:
    print("Invalid option, please try again")