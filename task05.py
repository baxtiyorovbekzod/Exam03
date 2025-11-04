import json

try:
    with open("data.json", "r") as f:
        users = json.load(f) 
except:
    print("Fayl topilmadi!")
else:
    for user in users:
        print(f"Name: {user['name']}, Age: {user['age']}")