from database import DatabaseManager
from player import Player
from map import MAPS
from npc import NPCS
from monster import spawn_monster
from combat import run_combat
from shop import run_shop
from quest import handle_quests

class Game:
    def __init__(self, user_data, db_manager: DatabaseManager):
        self.player = Player(user_data)
        self.db_manager = db_manager

    def play(self):
        # Story Intro
        print("\033[96m" + "="*60)
        print(" PROLOGUE: THE AWAKENING OF ELYRIA")
        print(" For centuries, the realm of Elyria lived in peace under the Crystal")
        print(" Scepter. Now, Malakor the Dragon Lord has plunged the lands into")
        print(" darkness. As an aspiring adventurer, your journey begins here...")
        print("="*60 + "\033[0m")
        
        while True:
            self.db_manager.save_game(self.player.username, self.player.to_dict())
            
            print(f"\n\033[94m=== LOCATION: {self.player.current_map} ===\033[0m")
            print("1. Explore / Move around map")
            print("2. Visit Shop")
            print("3. Check Quests & Journal")
            print("4. View Character Sheet")
            print("5. Talk to NPCs")
            print("6. Save & Exit Game")
            
            choice = input("\033[93mSelect option (1-6): \033[0m").strip()
            
            if choice == '1':
                current_map_obj = MAPS.get(self.player.current_map, MAPS["Town"])
                print("\nMap Grid (# = Wall, . = Path):")
                for row in current_map_obj.grid:
                    print(" ".join(row))
                
                action = input("Encounter check... Press Enter to search for monsters/events or type 'back' to menu: ").strip().lower()
                if action == 'back':
                    continue
                
                monster = spawn_monster(self.player.current_map)
                if monster:
                    won = run_combat(self.player, monster)
                    if monster.name == "Malakor the Dragon Lord" and won:
                        print("\n\033[92m🏆 CONGRATULATIONS! You defeated Malakor and saved Elyria! YOU WIN!\033[0m")
                        break
                else:
                    print("\033[92mThe area is peaceful. You find 5 Gold pieces on the ground!\033[0m")
                    self.player.gold += 5
            
            elif choice == '2':
                run_shop(self.player)
            elif choice == '3':
                handle_quests(self.player)
            elif choice == '4':
                self.player.view_progress()
            elif choice == '5':
                print("\nNPCs nearby:")
                for name, npc in NPCS.items():
                    print(f"- {name}: \"{npc.dialogue}\"")
            elif choice == '6':
                self.db_manager.save_game(self.player.username, self.player.to_dict())
                print("\033[92mGame successfully saved. Goodbye!\033[0m")
                break
            else:
                print("\033[91mInvalid input. Please choose between 1 and 6.\033[0m")