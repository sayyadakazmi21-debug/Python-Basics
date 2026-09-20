class FamilyMember:
    def __init__(self,eyecolour,height):
        self.eyecolour=eyecolour
        self.height=height

    def __show_traits(self):
        print("eyecolour",self.eyecolour)
        print("height",self.height)


class kid(FamilyMember):

    def __init_(self,name,age,eyecolour,height):
        self.name=name
        self.age=age
        super().show_traits()

    def show_traits(self):
        print("name",self.name)
        print("age",self.age)
        super().show_traits


    def fav_hobby(self,hobby):
        print(self.name,"loves",hobby)



child=kid("siyu",16,"brown",164)

child.show_traits()
child.fav_hobby("painting")


print("is kid a subclass of FamilyMember?",issubclass(kid,FamilyMember))





