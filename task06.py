import json

name = input("Ism: ")
age = input("Yosh: ")

try:
    with open("data.json", "r") as f:
        users = json.load(f)
except:
    print("Fayl bo'sh")
    users = []


users.append({
    "name": name,
    "age": age
})


with open("data.json", "w") as f:
    json.dump(users, f, indent=4)

print("Foydalanuvchi JSON faylga qo‘shildi!")