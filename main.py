from pokemon import Pokemon
from attack_moves import pokemon_moveset
import random
import os

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

#list_move_one[x].name
# x move selection; 0-3

print_selection()
val_select = input("Input : ")
first_player, second_player = select_pokemon(val_select)
list_move_one = first_player.moves
list_move_two = second_player.moves
print(f"Your opponent is {second_player.name}")
os.system("clear")

def ask_enter() -> None:
    input("Press Enter to continue!")
    os.system("clear")

turn = 0
print("Battle Start!")
print(f"{first_player.name:<8}VS{second_player.name:>8}")
ask_enter()

while first_player.health > 0:
    turn += 1
    print(f"""Turn - {turn}
{first_player.name:<8} - HP : {first_player.health}/{first_player.max_health}
{second_player.name:<8} - HP : {second_player.health}/{second_player.max_health}
Move :
    1. {list_move_one[0].name:<10}2. {list_move_one[1].name}
    3. {list_move_one[2].name:<10}4. {list_move_one[3].name}""")

    val_move_one = int(input("Input : "))
    first_val_atk = first_player.attack(second_player, list_move_one[val_move_one-1])
    print(f"{first_player.name} use {list_move_one[val_move_one-1].name}")

    val_move_two = random.randrange(1, 4)
    second_val_atk = second_player.attack(first_player, list_move_two[val_move_two])
    print(f"{second_player.name} use {list_move_two[val_move_two].name}")
    ask_enter()

    print(f"{first_player.name} deal {first_val_atk}")
    print(f"{second_player.name} deal {second_val_atk}")
    ask_enter()

    if second_player.health == 0:
        print("You win!")
        break
    elif first_player.health == 0:
        print("You lose!!! Loser loser!")
        break