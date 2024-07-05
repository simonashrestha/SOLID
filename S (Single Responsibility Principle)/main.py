from models import User 
from repo import UserRepository
from services import EmailService

def main():
    user= User(username='simona_shrestha', email='simonashrestha@gmail.com')
    print(f"Created {user}")

    user_repo =UserRepository()
    user_repo.save_to_database(user)

    email_service= EmailService()
    email_service.send_email(user, "Welcome to our service!")

print(main())

    