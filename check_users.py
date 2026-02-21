from app import app, db
from models import User

with app.app_context():
    users = User.query.all()
    print("All users in DB:")
    for user in users:
        print(f"ID: {user.id}, Username: {user.username}, Email: {user.email}, Role: {user.role}")
