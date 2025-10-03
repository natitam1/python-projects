from pathlib import Path

# Create a path object for the guest book file
path = Path("guest_book.txt")

# Start with an empty list to collect names
names = []

print("Enter 'q' to quit.")
while True:
    name = input("Please enter your name: ")
    if name.lower() == 'q':
        break
    print(f"Hello, {name.title()}! You've been added to the guest book.")
    names.append(name)

# Write all names to the file, one per line
with path.open(mode='w') as file:
    for name in names:
        file.write(f"{name}\n")

print("All names have been saved to guest_book.txt.")
