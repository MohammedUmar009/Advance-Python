file_path = r"C:\Users\mu261\OneDrive\Documents\python.txt.txt"

with open(file_path, "r", encoding="utf-8") as file:
    lines = file.readlines()

for number, line in enumerate(lines, start=1):
    print(f"{number}. {line.strip()}")