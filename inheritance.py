class Publication:
    def __init__(self, title, price):
        self.title = title
        self.price = price
    def get_price(self):
        return self.price
class Book(Publication):
    def __init__(self, title, author, pages, price):
        super().__init__(title, price)
        self.author = author
        self.pages = pages

class Magazine(Publication):
    def __init__(self, title, author, pages, price, period):
        super().__init__(title, price)
        self.author = author
        self.pages = pages
        self.period = period
class Newspaper(Publication):
    def __init__(self, title, publisher, price, period):
        super().__init__(title, price)
        self.publisher = publisher
        self.period = period

B1 = Book("Book 1", "Author 1", 100, 50)
M1 = Magazine("Magazine 1", "Author 1", 200, 150, 2022)
N1 = Newspaper("Newzpaper 1", "Media Prints", 200, 2020)
print(B1.get_price())
print(M1.get_price())
print(N1.get_price())