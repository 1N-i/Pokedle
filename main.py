from search import search_pokemon
from random import randint

def game():
    pokemon_num = randint(1, 151)
    secret_pokemon_data = search_pokemon(pokemon_num)

    print(secret_pokemon_data["name"])
    print(secret_pokemon_data["type 1"])
    print(secret_pokemon_data["type 2"])
    print(secret_pokemon_data["color"])
    print(secret_pokemon_data["bst"])
    print(f"{secret_pokemon_data["height"]} m")
    print(f"{secret_pokemon_data["weight"]} Kg")

    while True:
        guess = input("Guess: ")
        guess_data = search_pokemon(guess)

        if guess_data["name"] == secret_pokemon_data["name"]:
            print("You're correct!")
            while True:
                try:
                    i = input("Play again (Y/N)? ").lower()
                    if i != "y" and i != "n":
                        raise Exception

                    if i == "y":
                        game()
                    elif i == "n":
                        print("Thanks for playing")
                    break #Break play again loop
                except Exception:
                    print()

            break #Break main game loop
        else:
            print("n") #Make the comparator

game()