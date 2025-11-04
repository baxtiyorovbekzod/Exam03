
class AgeError(Exception):
    pass


age = int(input("Yoshingizni kiriting: "))

try:
    if age < 0:
        raise AgeError("Yosh noto‘g‘ri!")
    else:
        print(f"Sizning yoshingiz: {age}")
except AgeError as e:
    print(e)