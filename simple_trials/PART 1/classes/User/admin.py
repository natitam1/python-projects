from users import User
class Privileges:
    def __init__(self, privileges):
        self.privileges = privileges
    def show_privileges(self):
        for privilege in self.privileges:
            print(privilege)

class Admin(User):
    def __init__(self, first_name, last_name, age, sex, email, city, login_attempts, privileges):
        super().__init__(first_name, last_name, age, sex, email, city, login_attempts)
        self.privileges = Privileges(privileges)

