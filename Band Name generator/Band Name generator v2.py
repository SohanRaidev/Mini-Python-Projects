import random

adjectives = ["Electric", "Mystic", "Thunderous", "Silent", "Neon", "Wild", "Golden", "Funky", "Burning"]
nouns = ["Waves", "Shadows", "Revolution", "Echo", "Flames", "Sparks", "Riders", "Dreams", "Pirates"]


print("Welcome to Band Name Generator!")

city_name = input("Enter the name of your city: ").capitalize()
your_name = input("Enter your first name: ").capitalize()
fav_animal = input("Enter your favorite animal: ").capitalize()
fav_instrument = input("Enter a musical instrument you like: ").capitalize()

random_adjective = random.choice(adjectives)
random_noun = random.choice(nouns)

style = random.choice([
    f"The {random_adjective} {random_noun}",
    f"{random_adjective} {city_name}",
    f"{your_name} and the {fav_animal}s",
    f"{fav_instrument} {random_noun}",
    f"{city_name} {random_noun}",
    f"{your_name} & {random_adjective} {fav_instrument}s"
])

print("\nYour band name could be: " + style)
