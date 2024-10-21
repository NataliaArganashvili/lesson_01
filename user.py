class User:
    def __init__(self, first_name, last_name):
        self.name = first_name
        self.surname = last_name

    def get_first_name(self):
        print(self.name)

    def get_last_name(self):
        print(self.surname)

    def get_user_info(self):
        print(f"Имя - {self.name}, фамилия - {self.surname}")
