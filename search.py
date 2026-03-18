import requests

def create_data(search_type, search): #Sends data to the functions that called it
    url_search = f"https://pokeapi.co/api/v2/{search_type}/{search}" #Link PokeAPI
    requested = requests.get(url_search)
    if requested.status_code == 404:
        print(f"Error: '{search}' not found\n") #Finish if nothing was found
        return "error"
    if search == "":
        print("Empty answer\n")
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

def pokedex_entry_hint(pokemon_num):
    def en_entry():
        while True:
            for entry in data_species["flavor_text_entries"]:
                if entry["language"]["name"] == "en":
                    return entry["flavor_text"]
       
    data_species = create_data("pokemon-species", pokemon_num)
    pokedex_entry_raw = en_entry().replace("\n\n", "\n").replace(data_species["name"].capitalize(), "___")
    pokedex_entry_fixed = pokedex_entry_raw.replace(data_species["name"], "___").replace("\n", " ")
    pokedex_entry_fixed = pokedex_entry_fixed.replace(data_species["name"].upper(), "___").replace("\f", " ")
    print(pokedex_entry_fixed)

def pokemon_picker():
    from random import randint, choice
    pokemon_numbers = {
        1: [1, 151],
        2: [152, 251],
        3: [252, 386],
        4: [387, 493],
        5: [494, 649],
        6: [650, 721],
        7: [722, 809],
        8: [810, 905],
        9: [906, 1025]
    }
    
    options = list(range(1, 10))
    while True:
        try:
            generation_choice = input("Which generations: ")
            gens = [int(item) for item in generation_choice.split(",")]
            for gen in gens:
                if gen not in options:
                    raise ValueError
            break
        except ValueError:
            print("Invalid answer\n")

    gen = choice(gens)
    pokemon_number = randint(pokemon_numbers[gen][0], pokemon_numbers[gen][1])
    return pokemon_number