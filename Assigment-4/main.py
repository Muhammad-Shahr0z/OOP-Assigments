# 4. Class Variables and Class Methods
# Assignment:
# Create a class Bank with a class variable bank_name. Add a class method change_bank_name(cls, name) that allows changing the bank name. Show that it affects all instances.


class Bank:
    # Class variable to store the bank name
    bank_name = "Meezan Bank PVT LTE"

    @classmethod
    def change_bank_name(cls, name):
        """
        Class method to change the bank name for all instances.
        """
        cls.bank_name = name
        print(f"Bank Name Changed Successfully To {cls.bank_name}")


# Creating instances of the Bank class
client1 = Bank()
client2 = Bank()

# Changing the bank name using class method from client1
client1.change_bank_name("Bank Al Habib LTE")

# Changing the bank name again using class method from client1
client1.change_bank_name("Bank Alpha")

# Verifying the change in client2 as well, as the change affects all instances
print(f"Client2's Bank Name: {client2.bank_name}")
