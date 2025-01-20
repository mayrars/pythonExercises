import json
employee = {
    "name": "John Doe",
    "age": 30,
    "salary": 5000,
    "job" : "Software Engineer"
}
file_path = "output.json"
try:
    with open(file_path, "w") as file:
        json.dump(employee, file)
        print(f"Data written to '{file_path}'")
except FileExistsError:
    print(f"File '{file_path}' already exists")
