import hashlib
from database import DatabaseManager

class AuthSystem:
    def __init__(self, db_manager: DatabaseManager):
        self.db_manager = db_manager

    def _hash_password(self, password: str) -> str:
        return hashlib.sha256(password.encode()).hexdigest()

    def run(self):
        while True:
            print("\033[96m=== WELCOME TO THE REALM OF ELYRIA ===\033[0m")
            print("1. Login")
            print("2. Register")
            print("3. Exit")
            
            choice = input("\033[93mChoose an option (1-3): \033[0m").strip()
            
            if choice == "1":
                username = input("Username: ").strip()
                password = input("Password: ").strip()
                if not username or not password:
                    print("\033[91mError: Fields cannot be empty.\033[0m")
                    continue
                
                user = self.db_manager.authenticate_user(username, self._hash_password(password))
                if user:
                    print(f"\033[92mLogin successful! Welcome back, {username}.\033[0m")
                    return user
                else:
                    print("\033[91mInvalid username or password.\033[0m")
            
            elif choice == "2":
                username = input("Choose Username: ").strip()
                password = input("Choose Password: ").strip()
                if len(username) < 3 or len(password) < 4:
                    print("\033[91mError: Username must be >= 3 chars, password >= 4 chars.\033[0m")
                    continue
                
                success = self.db_manager.register_user(username, self._hash_password(password))
                if success:
                    print("\033[92mRegistration successful! You can now log in.\033[0m")
                else:
                    print("\033[91mUsername already exists.\033[0m")
            
            elif choice == "3":
                print("Goodbye!")
                exit(0)
            else:
                print("\033[91mInvalid choice. Please enter 1, 2, or 3.\033[0m")