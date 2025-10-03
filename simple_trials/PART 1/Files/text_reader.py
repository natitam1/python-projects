from pathlib import Path

def read_file(path: Path):
    """Try to open and read the file, or handle if it's missing."""
    try:
        contents = path.read_text()
        print(f"\nContents of {path.name}:\n{contents}")
    except FileNotFoundError:
        pass

# Define file paths using pathlib
cats_path = Path("cats.txt")
dogs_path = Path("dogs.txt")

# Loop through each file
for file_path in [cats_path, dogs_path]:
    read_file(file_path)
