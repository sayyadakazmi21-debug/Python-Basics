class Pet:
    print("Hi, I am a pet profile class!")

p = Pet()

class PetProfile:
    category = "pet"

    def __init__(self, n, t, a, f):
        self.n = n
        self.t = t
        self.a = a
        self.f = f

p1 = PetProfile("Buddy", "Dog", 4, "Biscuits")
p2 = PetProfile("Milo", "Cat", 3, "Fish")

print("Buddy is a {}".format(p1.category))
print("Milo is also a {}".format(p2.category))

print("{} is a {} and is {} years old.".format(p1.n, p1.t, p1.a))
print("{} likes eating {}.".format(p1.n, p1.f))

print("{} is a {} and is {} years old.".format(p2.n, p2.t, p2.a))
print("{} likes eating {}.".format(p2.n, p2.f))