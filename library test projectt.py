class book:
    def __init__(self,title,author):
        self.title=title
        self.authot=author
        self.is_borrowed=False


    def borrow(self):
        self.is_borrowed=True
        print(self.title," = borrowed")  


    def return_book(self):
        self.is_borrowed=False
        print(self.title," = returned")

book1=book("Harry potter","j.k rowling")
book2=book("the alchemist","authorxyz")
book3=book("silent patient","authonnn")

book1.borrow()
book2.borrow()
book3.borrow()

book1.return_book()
book2.return_book()
book3.return_book()
