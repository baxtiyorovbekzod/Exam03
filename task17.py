import json

class User:
    def __init__(self, username, email, is_active):
        self.username = username
        self.email = email
        self.is_active = is_active

    def save(self):
     
        try:
            with open("data.json", "r") as f:
                users = json.load(f)
        except :
            print("chota bir nima nito")
            
            users = []

        
        users.append({
            "username": self.username,
            "email": self.email,
            "is_active": self.is_active
        })

       
        with open("data.json", "w") as f:
            json.dump(users, f, indent=4)

       
        with open("data.json", "r") as f:
            data = json.load(f)
            print(data)

    def deactivate(self):
    
        with open("data.json", "r") as f:
            users = json.load(f)

     
        for user in users:
            if user["email"] == self.email:
                user["is_active"] = False
                self.is_active = False

      
        with open("data.json", "w") as f:
            json.dump(users, f, indent=4)



user1 = User("Bekzod", "bek@gmail.com", True)
user2 = User("Azizbek", "aziz@gmail.com", False)
user3 = User("Muhammad Ali" , "ali@gmail.com", True)

user1.save()
user2.save()
user3.save()

user1.deactivate()