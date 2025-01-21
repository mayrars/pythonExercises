import json
file_path = "/home/mayra/Escritorio/output.json"
try:
    with open(file_path, "r") as file:
        content = json.load(file)
        print(content)
except FileNotFoundError:
    print("File not found")
except PermissionError:
    print("Permission denied")