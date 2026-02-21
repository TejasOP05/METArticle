from app import app, db
from models import User
import sys

# Ensure stdout is utf-8
if sys.stdout.encoding != 'utf-8':
    import io
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with app.app_context():
    users = User.query.all()
    with open('users_debug.txt', 'w', encoding='utf-8') as f:
        f.write("All users in DB:\n")
        for user in users:
            f.write(f"ID: {user.id}, Username: {user.username}, Email: {user.email}, Role: {user.role}\n")
    print("Done writing to users_debug.txt")
