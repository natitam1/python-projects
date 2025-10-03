from pathlib import Path
import json

def get_stored_user(path):
    """Get stored user info if available."""
    if path.exists():
        try:
            contents = path.read_text()
            return json.loads(contents)
        except json.JSONDecodeError:
            return None
    return None

def get_new_user(path):
    """Prompt for new user info and store it."""
    name = input("What is your name? ").strip()
    age = input("How old are you? ").strip()
    favorite_color = input("What is your favorite color? ").strip()

    user_info = {
        "name": name,
        "age": age,
        "favorite_color": favorite_color
    }

    path.write_text(json.dumps(user_info))
    return user_info

def greet_user():
    """Greet the user with stored info or prompt for new details if not same user."""
    path = Path("user_info.json")
    user_info = get_stored_user(path)

    if user_info:
        print(f"Stored user: {user_info['name']}")
        confirm = input(f"Are you {user_info['name']}? (y/n): ").strip().lower()
        if confirm == 'y':
            print(f"Welcome back, {user_info['name']}!")
            print(f"We remember you're {user_info['age']} years old and love {user_info['favorite_color']}.")
        else:
            user_info = get_new_user(path)
            print(f"Thanks, {user_info['name']}! We'll remember you're {user_info['age']} and love {user_info['favorite_color']}.")
    else:
        user_info = get_new_user(path)
        print(f"Thanks, {user_info['name']}! We'll remember you're {user_info['age']} and love {user_info['favorite_color']}.")

greet_user()
