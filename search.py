import requests

def create_data(search_type, search): #Sends data to the functions that called it
    url_search = f"https://pokeapi.co/api/v2/{search_type}/{search}" #Link PokeAPI
    requested = requests.get(url_search)
    if requested.status_code == 404:
        print(f"Error: '{search}' not found") #Finish if nothing was found
        return "error"
    return requested.json()

def gen_traslate(generation): #Switch the letter by numbers and region names
    if generation == "generation-i":
        return "1"
    elif generation == "generation-ii":
        return "2"
    elif generation == "generation-iii":
        return "3"
    elif generation == "generation-iv":
        return "4"
    elif generation == "generation-v":
        return "5"
    elif generation == "generation-vi":
        return "6"
    elif generation == "generation-vii":
        return "7"
    elif generation == "generation-viii":
        return "8"
    elif generation == "generation-ix":
        return "9"

def search_pokemon(pokemon_num):
    data_species = create_data("pokemon-species", pokemon_num)
    if data_species == "error": #Finish if nothing was found
        return

    data = create_data("pokemon", pokemon_num)
    if data == "error": #Finish if nothing was found
        return
    
    type1 = data["types"][0]["type"]["name"]
    type2 = data["types"][-1]["type"]["name"]

    if type1 == type2: #If it's Mono-type
        type2 = "none"

    base_stat_total = []
    for stat in data["stats"]:
        base_stat_total.append(stat["base_stat"])

    generation = gen_traslate(data_species["generation"]["name"])

    pokemon_data = {
        "name": data["name"].replace("-", " "),
        "type 1": type1,
        "type 2": type2,
        "color": data_species["color"]["name"],
        "bst": sum(base_stat_total),
        "height": data["height"] / 10,
        "weight": data["weight"] / 10,
        "generation": generation
        }
    return pokemon_data