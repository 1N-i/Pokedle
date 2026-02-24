from search import search_pokemon
from random import randint

def game():
    pokemon_num = randint(1, 151)
    secret_pokemon_data = search_pokemon(pokemon_num)

    print(secret_pokemon_data["name"])

    def number_comparasion(guess_value, secret_value, unity):
        if guess_value == secret_value:
            print(f"{guess_value} {unity} -> ✓")
        elif guess_value < secret_value:
            print(f"{guess_value} {unity} -> ↑")
        elif guess_value > secret_value:
            print(f"{guess_value} {unity} -> ↓")

    while True:
        guess = input("\nGuess: ")
        guess_data = search_pokemon(guess)

        if guess_data["name"] == secret_pokemon_data["name"]: #Correct
            print(f"{guess_data["type 1"]} -> ✓")
            print(f"{guess_data["type 2"]} -> ✓")
            print(f"{guess_data["color"]} -> ✓")
            number_comparasion(guess_data["bst"], secret_pokemon_data["bst"], "bst") #Bst
            number_comparasion(guess_data["height"], secret_pokemon_data["height"], "m") #Height
            number_comparasion(guess_data["weight"], secret_pokemon_data["weight"], "Kg") #Weight
            number_comparasion(guess_data["generation"], secret_pokemon_data["generation"], "º generation") #Generation
            while True:
                try:
                    replay = input("Play again (Y/N)? ").lower()
                    if replay != "y" and replay != "n":
                        raise Exception

                    if replay == "y":
                        game()
                    elif replay == "n":
                        print("Thanks for playing!")
                    break #Break play again loop
                except Exception:
                    print()

            break #Break main game loop

        else: #Incorrect
            if guess_data["type 1"] == secret_pokemon_data["type 1"] or guess_data["type 1"] == secret_pokemon_data["type 2"]:
                print(f"{guess_data["type 1"]} -> ✓")
            else:
                print(f"{guess_data["type 1"]} -> X")

            if guess_data["type 2"] == secret_pokemon_data["type 1"] or guess_data["type 2"] == secret_pokemon_data["type 2"]:
                print(f"{guess_data["type 2"]} -> ✓")
            else:
                print(f"{guess_data["type 2"]} -> X")

            if guess_data["color"] == secret_pokemon_data["color"]:
                print(f"{guess_data["color"]} -> ✓")
            else:
                print(f"{guess_data["color"]} -> X")

            number_comparasion(guess_data["bst"], secret_pokemon_data["bst"], "bst") #Bst
            number_comparasion(guess_data["height"], secret_pokemon_data["height"], "m") #Height
            number_comparasion(guess_data["weight"], secret_pokemon_data["weight"], "Kg") #Weight
            number_comparasion(guess_data["generation"], secret_pokemon_data["generation"], "º generation") #Generation

game()