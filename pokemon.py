class Pokemon:
    def __init__(self,
                 name : str,
                 type : str,
                 damage : int,
                 health : int,
                 defense : int,
                 moves : list
                 ) -> None :
        self.name = name
        self.type = type
        self.damage = damage
        self.health = health
        self.max_health = health
        self.defense = defense
        self.moves = moves
        
    def attack(self, enemy, move):
        enemy.health -= round(move.value * 0.01 * self.damage)
        enemy.health = max(enemy.health, 0)

    def calculate_damage():
        pass


    def run(self, enemy):
        if self.hp > enemy.hp:
            return True
        
