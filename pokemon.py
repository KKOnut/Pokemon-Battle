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
        
    def attack(self, enemy):
        enemy.hp -= self.damage
        enemy.hp = max(enemy.hp, 0)

    def calculate_damage():
        pass


    def run(self, enemy):
        if self.hp > enemy.hp:
            return True
        
