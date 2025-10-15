import json

with open("users.json", "r") as file:
    users = json.load(file)

print(users)
