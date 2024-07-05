from models import User

class EmailService:
    def send_email(self, user:User, message: str):
        print (f"Sending email to {user.email}: {message}")