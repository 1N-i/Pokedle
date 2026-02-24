import requests

def create_data(search_type, search): #Sends data to the functions that called it
    url_search = f"https://pokeapi.co/api/v2/{search_type}/{search}" #Link PokeAPI
    requested = requests.get(url_search)
    if requested.status_code == 404:
        print(f"Error: '{search}' not found") #Finish if nothing was found
        return "error"
    return requested.json()

#-------------------------------------------------------------
def search_pokemon(pokemon_num):
    data = create_data("pokemon", pokemon_num)
    type1 = data["types"][0]["type"]["name"]
    type2 = data["types"][-1]["type"]["name"]

    if type1 == type2: #Mono-type
        type2 = "None"

    base_stat_total = []
    for stat in data["stats"]:
        base_stat_total.append(stat["base_stat"])

    pokemon_data = {
        "name": data["name"].replace("-", " "),
        "type 1": type1,
        "type 2": type2,
        "bst": sum(base_stat_total),
        "height": data["height"] / 10,
        "weight": data["weight"] / 10
        }
    return pokemon_data