
class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.user_balance = 0

    def make_deposit(self,amount):
        self.user_balance += amount

    def make_withdrawal(self,amount):
        self.user_balance -= amount
    
    def display_user_balance(self):
        print(f"User: {self.name} ----- Balance: {self.user_balance}")

    def transfer_money(self,other_user,amount):
        self.user_balance -= amount 
        other_user.user_balance += amount 
        self.display_user_balance()
        other_user.display_user_balance()


maria = User("Maria Mateo", "mariam2@gmail.com")
eva = User("Eva Mateo", "evam7@gmail.com")
diego = User("Diego Mateo", "diegom16@gmail.com")

maria.make_deposit(100)
maria.make_deposit(20)
maria.make_deposit(20)
maria.make_withdrawal(20)
maria.display_user_balance()


eva.make_deposit(100)
eva.make_deposit(50)
eva.make_withdrawal(10)
eva.make_withdrawal(50)
eva.display_user_balance()

diego.make_deposit(300)
diego.make_withdrawal(50)
diego.make_withdrawal(50)
diego.make_withdrawal(50)
diego.display_user_balance()

diego.transfer_money(eva,100)