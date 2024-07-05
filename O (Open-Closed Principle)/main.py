from models import User
from repo import UserRepository
from services import EmailService

class UserService:
    def __init__(self, user_repo, email_service):
        self.user_repo= user_repo
        self.email_service= email_service

    def register_user(self, username, email):
        user= User(username=username, email=email)
        self.user_repo.save_to_database(user)
        self.email_service.send_email(user, "Welcome to our service!")

def main():
    user_repo= UserRepository()
    email_service= EmailService()

    user_service= UserService(user_repo, email_service)
    
    user_service.register_user('simona_shrestha', 'simonashrestha@gmail.com')

print(main())
    

