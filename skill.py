class Skill:
    def __init__(self, name, mana_cost, cooldown):
        self.name = name
        self.mana_cost = mana_cost
        self.cooldown = cooldown

    def use(self, caster, target):
        raise NotImplementedError("Subclasses must implement use()")

class Fireball(Skill):
    def __init__(self):
        super().__init__("Fireball", mana_cost=15, cooldown=2)

    def use(self, caster, target):
        damage = 25 + (caster.level * 3)
        target.hp -= damage
        print(f"\033[91m🔥 {caster.name} casts Fireball on {target.name} for {damage} damage!\033[0m")

class Heal(Skill):
    def __init__(self):
        super().__init__("Heal", mana_cost=20, cooldown=3)

    def use(self, caster, target=None):
        heal_amount = 30 + (caster.level * 5)
        caster.hp = min(caster.max_hp, caster.hp + heal_amount)
        print(f"\033[92m✨ {caster.name} casts Heal, restoring {heal_amount} HP!\033[0m")

class BasicAttack(Skill):
    def __init__(self):
        super().__init__("Basic Attack", mana_cost=0, cooldown=0)

    def use(self, caster, target):
        damage = 10 + caster.level * 2
        target.hp -= damage
        print(f"\033[94m⚔️ {caster.name} strikes {target.name} for {damage} physical damage!\033[0m")

SKILL_REGISTRY = {
    "Basic Attack": BasicAttack,
    "Fireball": Fireball,
    "Heal": Heal
}