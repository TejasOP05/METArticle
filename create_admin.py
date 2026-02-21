#!/usr/bin/env python3
"""
Script to create the initial Admin (Super User) for JHCPP
Usage: python create_admin.py <username> <email> <password>
"""

from app import app, db
from models import User
import sys

def create_admin(username, email, password):
    with app.app_context():
        # Check if user already exists
        existing_user = User.query.filter((User.username == username) | (User.email == email)).first()
        if existing_user:
            print(f"Error: A user with that username or email already exists (Role: {existing_user.role}).")
            return False
        
        # Create new admin
        admin = User(
            username=username,
            email=email,
            role='admin',
            first_name="System",
            last_name="Administrator"
        )
        admin.set_password(password)
        
        db.session.add(admin)
        db.session.commit()
        
        print(f"\n[SUCCESS] Super User created!")
        print(f"  Username: {username}")
        print(f"  Email:    {email}")
        print(f"  Role:     admin")
        print("\nYou can now log in at http://localhost:5000/login")
        return True

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python create_admin.py <username> <email> <password>")
        print("\nExample: python create_admin.py admin jhcpp-admin@metarticles.edu secret123")
        sys.exit(1)
    
    username = sys.argv[1]
    email = sys.argv[2]
    password = sys.argv[3]
    create_admin(username, email, password)
