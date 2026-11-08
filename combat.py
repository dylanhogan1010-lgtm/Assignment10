import random
from skill import SKILL_REGISTRY

def run_combat(player, monster):
    print(f"\n\033[91m⚠️ A wild {monster.name} appears!\033[0m")
    
    while monster.hp > 0 and player.hp > 0:
        print(f"\n[Your HP: {player.hp}/{player.max_hp}] | [{monster.name} HP: {monster.hp}/{monster.max_hp}]")
        print("Choose Action:")
        print("1. Use Skill")
        print("2. Use Item (Potion)")
        print("3. Flee")
        
        choice = input("Action (1-3): ").strip()
        
        if choice == '1':
            print("Skills available:")
            for idx, s_name in enumerate(player.skills, 1):
                print(f"{idx}. {s_name}")
            s_choice = input("Select skill number: ").strip()
            try:
                s_idx = int(s_choice) - 1
                if 0 <= s_idx < len(player.skills):
                    s_name = player.skills[s_idx]
                    skill_obj = SKILL_REGISTRY[s_name]()
                    if s_name == "Heal":
                        skill_obj.use(player)
                    else:
                        skill_obj.use(player, monster)
                else:
                    print("\033[91mInvalid skill choice.\033[0m")
                    continue
            except ValueError:
                print("\033[91mInvalid input.\033[0m")
                continue
        elif choice == '2':
            if "Health Potion" in player.inventory:
                player.inventory.remove("Health Potion")
                player.hp = min(player.max_hp, player.hp + 50)
                print("\033[92mFlask consumed! Restored 50 HP.\033[0m")
            else:
                print("\033[91mNo Health Potions in inventory!\033[0m")
                continue
        elif choice == '3':
            print("You fled safely back to safety!")
            return False
        else:
            print("\033[91mInvalid choice.\033[0m")
            continue
            
        # Monster Counter-Attack
        if monster.hp > 0:
            monster.attack(player)
        else:
            print(f"\033[92m🎉 Victory! You defeated the {monster.name}!\033[0m")
            player.gain_xp(monster.xp_reward)
            player.gold += monster.gold_reward
            print(f"Loot collected: {monster.gold_reward} Gold 🪙")
            return True
            
        if player.hp <= 0:
            print("\033[91m💀 You have been defeated... Respawning with partial health.\033[0m")
            player.hp = int(player.max_hp / 2)
            return False