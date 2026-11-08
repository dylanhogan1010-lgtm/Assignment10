from item import ITEMS_DATABASE

def run_shop(player):
    while True:
        print(f"\n\033[93m=== SHOP === (Your Gold: {player.gold} 🪙)\033[0m")
        items_list = list(ITEMS_DATABASE.keys())
        for idx, item_name in enumerate(items_list, 1):
            item = ITEMS_DATABASE[item_name]
            print(f"{idx}. {item.name} ({item.type}) - {item.value} Gold")
        print("0. Exit Shop")
        
        choice = input("Select item to buy (number): ").strip()
        if choice == '0':
            break
        
        try:
            c_idx = int(choice) - 1
            if 0 <= c_idx < len(items_list):
                item_name = items_list[c_idx]
                item = ITEMS_DATABASE[item_name]
                if player.gold >= item.value:
                    player.gold -= item.value
                    player.inventory.append(item.name)
                    print(f"\033[92mSuccessfully bought {item.name}!\033[0m")
                else:
                    print("\033[91mNot enough gold!\033[0m")
            else:
                print("\033[91mInvalid selection.\033[0m")
        except ValueError:
            print("\033[91mPlease enter a valid number.\033[0m")