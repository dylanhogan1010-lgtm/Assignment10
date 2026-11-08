from database import DatabaseManager
from auth import AuthSystem
from game import Game

def main():
    db = DatabaseManager()
    auth = AuthSystem(db)
    
    user_data = auth.run()
    if user_data:
        game = Game(user_data, db)
        game.play()

if __name__ == "__main__":
    main()