from pathlib import Path

path = Path('gutenber.txt')
contents = path.read_text()

counted = contents.lower().count("the ")
print(counted)