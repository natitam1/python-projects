from pathlib import Path
import json

def know_favorite(path):
    """This will retrieve the stored favorite number"""
    if path.exists():
        contents = path.read_text()
        number = json.loads(contents)
        return number
    else:
        return None

def store_favorite(path):
    """Prompts the users to enter their favorite number and store it"""
    number = input("What is your favorite number? ")
    contents = json.dumps(number)
    path.write_text(contents)
    return number

def favorite_number():
    """Checks weather to store or retrieve the number."""
    path = Path('favorite_number.json')
    number = know_favorite(path)
    
    if number:
        print(f"I know your favorite number! It's {number}")
    else:
        number = store_favorite(path)
        print(f"We'll remember your number {number} for every!")

favorite_number()