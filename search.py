from random import randint
import requests

def create_data(search_type, search): #Sends data to the functions that called it
    url_search = f"https://pokeapi.co/api/v2/{search_type}/{search}" #Link PokeAPI
    requested = requests.get(url_search)
    if requested.status_code == 404:
        print(f"Error: '{search}' not found") #Finish if nothing was found
        return "error"
    return requested.json()

#-------------------------------------------------------------
def data_verification(options): #Data verification
    while True:
        try:
            action = int(input("Option: "))
            if action not in options:
                raise ValueError
            return action

        except ValueError:
            print("Invalid option\n")

#-------------------------------------------------------------
secret_pokemon_num = randint(1, 152)

data = create_data("pokemon", secret_pokemon_num)
type1 = data["types"][0]["type"]["name"]
type2 = data["types"][-1]["type"]["name"]

if type1 == type2: #Mono-type
    type2 = "None"


secret_pokemon_data = {
    "name": data["name"].replace("-", " "),
    "type 1": type1,
    "type 2": type2,
    
    }

print(secret_pokemon_data["name"])
print(secret_pokemon_data["type 1"])
print(secret_pokemon_data["type 2"])