from search import search_pokemon
from random import randint

def data_verification(options): #Data verification
    while True:
        try:
            action = int(input("Option: "))
            if action not in options:
                raise ValueError
            return action

        except ValueError:
            print("Invalid option\n")

pokemon_num = randint(1, 152)
secret_pokemon_data = search_pokemon(pokemon_num)

print(secret_pokemon_data["name"])
print(secret_pokemon_data["type 1"])
print(secret_pokemon_data["type 2"])
print(secret_pokemon_data["bst"])
print(f"{secret_pokemon_data["height"]} m")
print(f"{secret_pokemon_data["weight"]} Kg")