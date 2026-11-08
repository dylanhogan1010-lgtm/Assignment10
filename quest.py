def handle_quests(player):
    print("\n\033[96m=== QUEST JOURNAL ===\033[0m")
    mq_stage = player.quests["main_quest"]
    
    if mq_stage == 1:
        print("Main Quest: Speak with Elder Martin in Town and travel to the Dark Forest.")
        choice = input("Proceed to Dark Forest? (y/n): ").strip().lower()
        if choice == 'y':
            player.current_map = "Dark Forest"
            player.position = [1, 1]
            player.quests["main_quest"] = 2
            print("\033[92mYou travel deep into the Dark Forest! Main Quest updated.\033[0m")
    elif mq_stage == 2:
        print("Main Quest: Defeat monsters in the Dark Forest and reach Level 3.")
        if player.level >= 3:
            print("\033[92mYou feel strong enough to face the Final Boss! Portal opened to Boss Arena.\033[0m")
            player.current_map = "Boss Arena"
            player.quests["main_quest"] = 3
        else:
            print(f"Current Level: {player.level}/3. Keep training!")
    elif mq_stage == 3:
        print("Main Quest: Defeat Malakor the Dragon Lord in the Boss Arena to win the game!")
        
    # Side Quests
    print("\n--- Side Quests ---")
    sq1 = "Completed" if player.quests["side_quest_1"] else "Available: Clear 3 Forest beasts (Reward: 50 Gold & 40 XP)"
    print(f"1. Forest Extermination: {sq1}")
    
    if not player.quests["side_quest_1"]:
        c = input("Claim Side Quest 1 reward / complete? (y/n): ").strip().lower()
        if c == 'y':
            player.gold += 50
            player.gain_xp(40)
            player.quests["side_quest_1"] = True
            print("\033[92mSide Quest Completed! +50 Gold, +40 XP\033[0m")