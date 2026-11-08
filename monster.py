import random

class Monster:
    def __init__(self, name, hp, attack_power, xp_reward, gold_reward):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.attack_power = attack_power
        self.xp_reward = xp_reward
        self.gold_reward = gold_reward

    def attack(self, player):
        damage = random.randint(self.attack_power - 2, self.attack_power + 3)
        player.hp = max(0, player.hp - damage)
        print(f"\033[91m{self.name} attacks you for {damage} damage!\033[0m")

class Goblin(Monster):
    def __init__(self):
        super().__init__("Goblin", hp=40, attack_power=8, xp_reward=20, gold_reward=15)

class Skeleton(Monster):
    def __init__(self):
        super().__init__("Skeleton", hp=60, attack_power=12, xp_reward=35, gold_reward=25)

class Orc(Monster):
    def __init__(self):
        super().__init__("Orc", hp=90, attack_power=18, xp_reward=60, gold_reward=45)

class DarkMage(Monster):
    def __init__(self):
        super().__init__("Dark Mage", hp=75, attack_power=22, xp_reward=80, gold_reward=70)

class Boss(Monster):
    def __init__(self):
        super().__init__("Malakor the Dragon Lord", hp=250, attack_power=32, xp_reward=500, gold_reward=300)

def spawn_monster(map_name):
    if map_name == "Town":
        return None
    elif map_name == "Dark Forest":
        return random.choice([Goblin(), Skeleton()])
    elif map_name == "Dragon's Lair":
        return random.choice([Orc(), DarkMage()])
    elif map_name == "Boss Arena":
        return Boss()
    return None