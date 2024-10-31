import random

print("Welcome to the Restaurant Random Selector!")

people_input = input("Enter the names of people separated by comma: ")
people = [name.strip() for name in people_input.split(",")]

print("\nList of People:")
for index, person in enumerate(people, start=1):
    print(f"{index}. {person}")

random_person = random.choice(people)

print(f"\nThe person to pay the bill is: {random_person}\n")
