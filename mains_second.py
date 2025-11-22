from pokemon import Pokemon
from attack_moves import pokemon_moveset

#POKEMON SELECTION

def select_pokemon(val) -> None:
    if val == '1':
        print("You have selected Litten")
        first_player = lst_selection[0]
        second_player = lst_selection[2]
    elif val == '2':
        print("You have selected Popplio")
        first_player = lst_selection[1]
        second_player = lst_selection[0]
    elif val == '3':
        print("You have selected Rowlet")
        first_player = lst_selection[2]
        second_player = lst_selection[1]
    else:
        print("Error Value")
    return first_player, second_player

def print_selection() -> None:
    print("""-------------------------
WELCOME TO POKEMON BATTLE
-------------------------
Please select your Pokemon : 
    1. Litten (Fire)
    2. Popplio(Water)
    3. Rowlet (Grass)""")

lst_selection = [
Pokemon(name="Litten",
                 type="Fire",
                 damage=65,
                 health=45,
                 defense=40,
                 moves=pokemon_moveset[0]),

Pokemon(name="Popplio",
                 type="Water",
                 damage=54,
                 health=50,
                 defense=54,
                 moves=pokemon_moveset[1]),

Pokemon(name="Rowlet",
                 type="Grass",
                 damage=55,
                 health=68,
                 defense=55,
                 moves=pokemon_moveset[2])
]


#list_move_one[1].name
while True:
    print_selection()
    val_select = input("Input : ")
    first_player, second_player = select_pokemon(val_select)
    list_move_one = first_player.moves
    

    