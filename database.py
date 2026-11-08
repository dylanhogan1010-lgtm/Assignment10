from tinydb import TinyDB, Query
import os

class DatabaseManager:
    def __init__(self, db_path="game_save.json"):
        self.db = TinyDB(db_path)
        self.users_table = self.db.table("users")
        self.user_query = Query()

    def register_user(self, username, password_hash):
        if self.users_table.contains(self.user_query.username == username):
            return False
        
        default_data = {
            "username": username,
            "password": password_hash,
            "level": 1,
            "xp": 0,
            "hp": 100,
            "max_hp": 100,
            "gold": 50,
            "inventory": ["Health Potion", "Wooden Sword"],
            "skills": ["Basic Attack", "Fireball"],
            "current_map": "Town",
            "position": [1, 1],
            "quests": {
                "main_quest": 1,
                "side_quest_1": False,
                "side_quest_2": False
            }
        }
        self.users_table.insert(default_data)
        return True

    def authenticate_user(self, username, password_hash):
        user = self.users_table.get((self.user_query.username == username) & (self.user_query.password == password_hash))
        return user

    def save_game(self, username, player_data):
        self.users_table.update(player_data, self.user_query.username == username)

    def load_game(self, username):
        return self.users_table.get(self.user_query.username == username)