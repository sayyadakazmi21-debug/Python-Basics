class Vehicle:
    def __init__(self, b, s):
        self.b = b
        self.s = s

    def show_details(self):
        print("Brand:", self.b)
        print("Max Speed:", self.s, "km/h")


class Car(Vehicle):
    def __init__(self, m, se, b, s):
        self.m = m
        self.se = se
        super().__init__(b, s)

    def show_details(self):
        print("Model:", self.m)
        print("Seats:", self.se)
        super().show_details()

    def fuel_type(self, f):
        print(self.m, "uses", f)


c = Car("City Rider", 5, "Honda", 180)

c.show_details()
c.fuel_type("petrol")

print("Is Car a subclass of Vehicle?", issubclass(Car, Vehicle))