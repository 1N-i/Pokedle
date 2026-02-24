from search import search_id_or_name, search_type, search_move, search_ability, random_page

while True:
    print("\nSelect: \n1- Search by name or ID \n2- Search by type \n3- Search move")
    print("4- Search hability \n5- See a random page \n6- Finish Program")
    options = [1, 2, 3, 4, 5, 6]

    try: #Data verification
        e = int(input("Action: "))
        if e not in options:
            raise ValueError

    except ValueError:
        print("Invalid action")
        continue

    if e == 1: #Search Pokémon by name or ID
        search1 = input("\nName or ID: ")
        search_id_or_name(search1)
        
    if e == 2: #Search type
        search2 = input("\nType: ")
        search_type(search2)
        
    if e == 3: #Search move
        search3 = input("\nMove: ")
        search_move(search3)

    if e == 4: #Search ability
        search4 = input("\nAbility name: ")
        search_ability(search4)

    if e == 5: #Random page
        random_page()
        
    if e == 6: #End Program
        print("Ending Program...")
        break