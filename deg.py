class PlatformUser:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def login(self):
        print(f"{self.name} logged in.")
class Volunteer(PlatformUser):
    def __init__(self, name, email, skills):
        super().__init__(name, email) # Calls the parent constructor
        self.skills = skills # New attribute specific to volunteers
    def offer_help(self):
        print(f"{self.name} is offering help with: {', '.join(self.skills)}")
volunteer1 = Volunteer("Alice", "alice@example.com", ["AI", "Data Science", "Machine Learning"])
volunteer1.login() # Inherited method
volunteer1.offer_help() # Volunteer-specific method
