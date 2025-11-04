name=input("Ism:")
age=input("Yosh:")
with open("data.txt", "a") as f:
    f.write(str(f"{name} - {age} yosh"))