class Move:
    def __init__(self,
                 name : str,
                 type : str,
                 value : int
                 ) -> None:
        self.name = name
        self.type = type
        self.value = value

#modified move
idle = Move(name="Idle", type="Normal", value= 0)

#ROWLET 
leafage = Move(name="Leafage", type="Grass", value=40)
peck = Move(name="Peck", type="Flying", value=35)
tackle = Move(name = "Tackle", type="Normal", value=40)
rowlet_moveset = [tackle, idle, leafage, peck]

#LITTEN
scratch = Move(name = "Tackle", type="Normal", value=40)
ember = Move(name="Ember", type="Fire", value=40)
lick = Move(name="Lick", type="Ghost", value=30)
litten_moveset = [scratch, idle, ember, lick]

#POPPLIO
pound = Move(name = "Pound", type="Normal", value=40)
water_gun = Move(name="Water Gun", type="Water", value=40)
disarming_voice = Move(name="Disarming Voice", type="Fairy", value=20)
popplio_moveset = [pound, idle, water_gun, disarming_voice]

pokemon_moveset = [litten_moveset, popplio_moveset, rowlet_moveset]