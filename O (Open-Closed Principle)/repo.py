from models import User

class UserRepository:
    def save_to_database(self, user: User):
        print(f"User {user.username} saved to database")
        