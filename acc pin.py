class Account:

    def __init__(self, o, p):
        self.o = o
        self.__p = p

    def show_pin_status(self):
        print("Account Owner:", self.o)
        print("PIN is safely stored inside the class.")

    def set_pin(self, np):
        if len(np) == 4 and np.isdigit():
            self.__p = np
            print("PIN updated successfully.")
        else:
            print("Invalid PIN. PIN must be exactly 4 digits.")

    def check_pin(self, ep):
        if ep == self.__p:
            print("Access granted.")
        else:
            print("Access denied.")

    def __str__(self):
        return "Account holder: " + self.o


a = Account("Riya", "1234")

print(a)

a.show_pin_status()

a.__p = "9999"
print("Tried changing PIN directly from outside.")

a.check_pin("9999")
a.check_pin("1234")

a.set_pin("9999")

a.check_pin("9999")