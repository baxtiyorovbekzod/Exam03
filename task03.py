try:
    with open("data.txt", "r") as f:
        lines = len(f.readlines())
        print(f"data.txt faylida {lines} ta qator bor.") 
        
except:
    print("Fayl topilmadi!")


