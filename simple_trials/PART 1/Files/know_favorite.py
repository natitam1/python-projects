from pathlib import Path
import json

def know_favorite():
    path = Path('favorite.json')
    contents = path.read_text()

    number = json.loads(contents)
    print(f"I know you favorite number! It's {number}")

know_favorite()