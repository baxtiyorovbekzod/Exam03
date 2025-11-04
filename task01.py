name=input("Ism:")
age=input("Yosh:")
with open("data.txt", "a") as f:
    f.write((f"{name} - {age} yosh"))