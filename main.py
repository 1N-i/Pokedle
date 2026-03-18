from search import search_pokemon, pokemon_picker, pokedex_entry_hint

def game():
    guesses_before_hint = 3 #Number of guesses before the hint is unlocked
    hint_unlocked = False
    pokemon_num = pokemon_picker()
    secret_pokemon_data = search_pokemon(pokemon_num)
    print("\nPut '0' to give up.\nAfter 3 guesses you can write 'hint' to get\n")

    #print(secret_pokemon_data["name"]) #See the answer

    def text_comparasion(guess_text, secret_1, secret_2):
        if guess_text == secret_1 or guess_text == secret_2:
            print(f"{guess_text} -> ✓")
        else:
            print(f"{guess_text} -> X")

    def number_comparasion(guess_value, secret_value, unity):
        if guess_value == secret_value:
            print(f"{guess_value} {unity} -> ✓")
        elif guess_value < secret_value:
            print(f"{guess_value} {unity} -> ↑")
        elif guess_value > secret_value:
            print(f"{guess_value} {unity} -> ↓")

    while True:
        if guesses_before_hint > 0:
            print(f"{guesses_before_hint} guesses before unlocking the hint")
        elif guesses_before_hint <= 0 and hint_unlocked == False:
            print("Hint unlocked. \nWrite 'hint' to see the pokedex entry.")
        
        while True:
            try:
                guess = input("Guess: ").lower().strip()
                break
            except KeyboardInterrupt:
                print("\nInvalid value")

        if guess == "0":
            print(f"\nThe Pokémon was: {secret_pokemon_data["name"]}")
            print(f"{secret_pokemon_data["type 1"]}\n{secret_pokemon_data["type 2"]}\n{secret_pokemon_data["color"]}")
            print(f"{secret_pokemon_data["bst"]} bst\n{secret_pokemon_data["height"]} m")
            print(f"{secret_pokemon_data["weight"]} Kg\n{secret_pokemon_data["generation"]} º generation")
            break

        if guess == "hint" and guesses_before_hint <= 0:
            pokedex_entry_hint(pokemon_num)
            hint_unlocked = True
        else:
            guess_data = search_pokemon(guess)

        if guess_data and guess != "hint":
            if guess_data["name"] == secret_pokemon_data["name"]: #Correct
                text_comparasion(guess_data["type 1"], secret_pokemon_data["type 1"], secret_pokemon_data["type 2"]) #Type 1
                text_comparasion(guess_data["type 2"], secret_pokemon_data["type 1"], secret_pokemon_data["type 2"]) #Type 2
                text_comparasion(guess_data["color"], secret_pokemon_data["color"], secret_pokemon_data["color"]) #Color
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
                text_comparasion(guess_data["type 1"], secret_pokemon_data["type 1"], secret_pokemon_data["type 2"]) #Type 1
                text_comparasion(guess_data["type 2"], secret_pokemon_data["type 1"], secret_pokemon_data["type 2"]) #Type 2
                text_comparasion(guess_data["color"], secret_pokemon_data["color"], secret_pokemon_data["color"]) #Color
                number_comparasion(guess_data["bst"], secret_pokemon_data["bst"], "bst") #Bst
                number_comparasion(guess_data["height"], secret_pokemon_data["height"], "m") #Height
                number_comparasion(guess_data["weight"], secret_pokemon_data["weight"], "Kg") #Weight
                number_comparasion(guess_data["generation"], secret_pokemon_data["generation"], "º generation") #Generation
                guesses_before_hint -= 1
                print()

game()