import requests

def create_data(search_type, search): #Sends data to the functions that called it
    url_search = f"https://pokeapi.co/api/v2/{search_type}/{search}" #Link PokeAPI
    requested = requests.get(url_search)
    if requested.status_code == 404:
        print(f"Error: '{search}' not found") #Finish if nothing was found
        return "error"
    return requested.json()

def data_verification(options): #Data verification
    while True:
        try:
            action = int(input("Option: "))
            if action not in options:
                raise ValueError
            return action

        except ValueError:
            print("Invalid option\n")

def gen_traslate(generation): #Switch the letter by numbers and region names
    if generation == "generation-i":
        return "Kanto, generation 1"
    elif generation == "generation-ii":
        return "Johto, generation 2"
    elif generation == "generation-iii":
        return "Hoenn, generation 3"
    elif generation == "generation-iv":
        return "Sinnoh, generation 4"
    elif generation == "generation-v":
        return "Unova, generation 5"
    elif generation == "generation-vi":
        return "Kalos, generation 6"
    elif generation == "generation-vii":
        return "Alola, generation 7"
    elif generation == "generation-viii":
        return "Galar, generation 8"
    elif generation == "generation-ix":
        return "Paldea, generation 9"

def search_id_or_name(search): #Search Pokémon by name or ID
    if isinstance(search, str):
        search = search.lower()

    data_species = create_data("pokemon-species", search)
    if data_species == "error": #Finish if nothing was found
        return

    if len(data_species["varieties"]) != 1: #Show every alternate version of the Pokémon
        varieties = []
        for variety in data_species["varieties"]:
            varieties.append(variety["pokemon"]["name"])

        for i in range(len(varieties)):
            print(f"{i + 1}- {varieties[i].replace("-", " ")}")

        a = i + 1
        version = data_verification(range(1, a + 1))
    else:
        varieties = [search]
        version = 1

    data = create_data("pokemon", varieties[version - 1])
    name = data["name"].replace("-", " ")
    print(f"\nID: {data_species["id"]} \nPokémon: {name}") #ID and Name

    type1 = data["types"][0]["type"]["name"]
    type2 = data["types"][-1]["type"]["name"]

    if type1 == type2: #Mono-type
        print(f"Type: {type1}")
    else: #Dual-type
        print(f"Type: {type1}")
        print(f"Type: {type2}")

    if "-alola" in data["name"]: #Alola regional version
        print("First appearence in Alola, generation 7")
    elif "-galar" in data["name"]: #Galar regional version
        print("First appearence in Galar, generation 8")
    elif "-paldea" in data["name"]: #Paldea regional version
        print("First appearence in Paldea, generation 9")
    else:
        print(f"First appearence in {gen_traslate(data_species["generation"]["name"])}") #Region of origin

    while True: #Inside menu
        print("\nSelect:\n1- See moves\n2- See abilities\n3- See base stats\n4- See pokédex descriptions\n5- End search\n")
        action = data_verification([1, 2, 3, 4, 5])

        if action == 1: #Show moves
            print(f"\nMoves that {name} can learn:")
            for attack in data["moves"]:
                print(attack["move"]["name"].replace("-", " "))
            print(f"That's {len(data["moves"])} moves")

        if action == 2: #Show hability
            print(f"\nAbilities that {name} can have:")
            for ability in data["abilities"]:
                if ability["is_hidden"] == False:
                    print(ability["ability"]["name"].replace("-", " "))
                else: #Hidden ablities
                    print(f"\nHidden abilities: \n{ability["ability"]["name"].replace("-", " ")}")

        if action == 3: #Show bst (Base Stat Total)
            print(f"\nBase stats of {name}:")
            base_stat_total = []
            for stat in data["stats"]:
                print(f"{stat["stat"]["name"]}: {stat["base_stat"]}") #Each stats
                base_stat_total.append(stat["base_stat"])
            print(f"Base stat total: {sum(base_stat_total)}") #Total stats

        if action == 4: #Show pokedex descriptions
            all_entries = {}
            for description in data_species["flavor_text_entries"]:
                if description["language"]["name"] == "en": #Get the english entries
                    raw_entry = description["flavor_text"].replace("\n", " ")
                    clean_entry = raw_entry.lower().strip().replace(".", "")
                    game_version = description["version"]["name"]

                    if clean_entry not in all_entries: #Put only the unique entries
                        all_entries[clean_entry] = {
                            "text_to_show": raw_entry, 
                            "versions": []
                            }
                    all_entries[clean_entry]["versions"].append(game_version)
            for entry in all_entries: #Show the games and entry
                text = all_entries[entry]["text_to_show"]
                versions = ", ".join(all_entries[entry]["versions"])
                print(f"\n[{versions}]:")
                print(f"{text}")

        if action == 5: #End search
            print(f"\nEnding search on '{name}'")
            break

def search_type(search): #Search specific type
    if isinstance(search, str):
        search = search.lower()

    while True: #Inside menu
        data = create_data("type", search)
        if data == "error": #Finish if nothing was found
            return
        search = data["name"]
        
        print(f"\nSelect: \n1- See all {search} type pokémon \n2- See {search}:type pokémon")
        print(f"3- See {search} type moves \n4- See {search} type chart \n5- End search\n")
        action = data_verification([1, 2, 3, 4, 5])

        if action == 1: #See pokémon
            print(f"\n{search} type pokémon:")
            for pokemon in data["pokemon"]:
                print(pokemon["pokemon"]["name"].replace("-", " "))
            print(f"That's {len(data["pokemon"])} Pokémon")

        if action == 2: #Search with secondary type
            def pokemon_list():
                type_list = []
                for pokemon in data["pokemon"]:
                    type_list.append(pokemon["pokemon"]["name"])
                return type_list

            type1 = pokemon_list()

            search2 = input("\nSecond type: ")
            data = create_data("type", search2)
            if data == "error":
                search_type(search)
                return
            
            type2 = pokemon_list()

            print(f"{search}:{search2} pokémon:")
            total_pokemon = 0
            for a in type1:
                for b in type2:
                    if a == b:
                        print(b.replace("-", " "))
                        total_pokemon += 1
            print(f"That's {total_pokemon} Pokémon")
            
        if action == 3: #See moves
            for move in data["moves"]:
                print(move["name"])
            print(f"That's {len(data["moves"])} moves")

        if action == 4: #See type chart
            def chart(text):
                list = []
                for type in data["damage_relations"][text]:
                    list.append(type["name"])
                return list

            print(f"2x damage from-to:\n{chart("double_damage_from")} -> {search} -> {chart("double_damage_to")}\n")
            print(f"1/2x damage from-to:\n{chart("half_damage_from")} -> {search} -> {chart("half_damage_to")}\n")
            print(f"0x damage from-to:\n{chart("no_damage_from")} -> {search} -> {chart("no_damage_to")}")

        if action == 5: #End search
            print(f"Ending search on '{search}'")
            break

def search_move(search): #Search specific move
    if isinstance(search, str):
        search = search.lower().replace(" ", "-")

    data = create_data("move", search)
    if data == "error": #Finish if nothing was found
        return
    
    search = src_msg = data["name"].replace("-", " ")

    effect = "None"
    short_effect = "None"
    if data["effect_entries"] != []: #Recent generations were organized different
        effect = data["effect_entries"][0]["effect"].replace("\n\n", "\n").replace("  ", " ")
        short_effect = data["effect_entries"][0]["short_effect"].replace("\n\n", "\n").replace("  ", " ")

    elif data["flavor_text_entries"] != []: #Recent generations were organized different
        effect = data["flavor_text_entries"][0]["flavor_text"]

    print(f"\nMove: {src_msg}") #Move name
    print(f"Effect: \n{effect}") #Long description
    print(f"\nShort effect: \n{short_effect}") #Short description
    print(f"\nDamage class: {data["damage_class"]["name"]}")

    accuracy = data["accuracy"]
    if data["accuracy"] == None:
        accuracy = "-" #If it can't miss
    
    print(f"Power: {data["power"]}\nAccuracy: {accuracy}\nPP: {data['pp']}\nType: {data['type']['name']}\n") #Accuracy

    if data["priority"] != 0:
        print(f"Priority: {data["priority"]}") #Priority

    if data["stat_changes"]:
        change = data["stat_changes"][0]["change"]
        stat_name = data["stat_changes"][0]["stat"]["name"]
        print(f"Stat changes: {change} {stat_name}") #Change of stats
    
    print(f"Target: {data['target']['name'].replace("-", " ")}") #Target of the move

    while True: #Inside menu
        print(f"\nSelect: \n1- See pokémon that can learn {src_msg} \n2- End search")
        action = data_verification([1, 2])

        if action == 1: #Pokémon that can learn the move
            print(f"\nPokémon that learns {src_msg}:")
            for pokemon in data["learned_by_pokemon"]:
                print(pokemon["name"])
            print(f"That's {len(data["learned_by_pokemon"])} moves")

        if action == 2: #End search
            print(f"Ending search on '{src_msg}'")
            break

def search_ability(search): #Search ability
    if isinstance(search, str):
        search = search.lower().replace(" ", "-")

    data = create_data("ability", search)
    if data == "error": #Finish if nothing was found
        return
    
    src_msg = data["name"]
    print(f"\nAbility: {src_msg}")

    for ability in data["effect_entries"]:
        if ability["language"]["name"] == "en":
            print(f"Effect: \n{ability["effect"].replace("\n\n", " ")}".replace("  ", " "))
            print(f"\nShort version: \n{ability["short_effect"].replace("\n\n", " ").replace("  ", " ")}")

    while True:
        print("\nSelect: \n1- See Pokémon with this ability \n2- End search\n")
        action = data_verification([1, 2])

        if action == 1: #Pokémon with the ability
            print(f"\nPokémon with '{src_msg}' naturally:")
            ability_natural = 0
            for pokemon in data["pokemon"]:
                if pokemon["is_hidden"] == False:
                    print(f"{pokemon["pokemon"]["name"].replace("-", " ")}")
                    ability_natural += 1
            print(f"That's {ability_natural} Pokémon")
            print(f"\nPokémon with '{src_msg}' as a hidden ability:")

            hidden_ability = 0
            for pokemon in data["pokemon"]:
                if pokemon["is_hidden"] == True: #Hidden hability
                    print(f"{pokemon["pokemon"]["name"].replace("-", " ")}")
                    hidden_ability += 1
            print(f"That's {hidden_ability} Pokémon")

        if action == 2: #End search
            print(f"Ending search on '{src_msg}'")
            break

def random_page(): #Sends you to a random page
    from random import randint #The only one that uses random
    function = randint(1,5)

    if function == 1:
        search1 = randint(1,1025) #Limit avaiable for the link
        search_id_or_name(search1)

    elif function == 2:
        search2 = randint(1,19) #Limit avaiable for the link
        search_type(search2)

    elif function == 3:
        search3 = randint(1,919) #Limit avaiable for the link
        search_move(search3)

    elif function == 4:
        search4 = randint(1,307) #Limit avaiable for the link
        search_ability(search4)