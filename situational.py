name = input("What is your name? ")
health = 100
location = "city"

health -=20
print(f" {name} You are {health} health points")

def show_status(name, health, location):
    print(f"{name} is in {location} and has {health} health points")

show_status(name, health, location)

choice =input("where do you want to go? home(h) or go to the park(p)? ")
if choice == 'h':
    print("stay at home and realax")
    health += 10
elif choice == 'p':
        print("You go to the park and play")
        health -= 10
else:
        print("You don't know where to go")

choice =input("you want to play slides? are you going to play (y) or (n)? ")
if choice == 'y':
    print("You chose to play slides")
    health -= 10

elif choice == 'n':
        print("okay just relax on the bench")
        health += 5

show_status(name, health, location)
