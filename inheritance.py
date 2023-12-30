class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
    def get_price(self):
        return self.price

class Magazine:
    def __init__(self, title, author, pages, price, period):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.period = period
    def get_price(self):
        return self.price
class Newspaper:
    def __init__(self, title, publisher, price, period):
        self.title = title
        self.publisher = publisher
        self.price = price
        self.period = period
    def get_price(self):
        return self.price
B1 = Book("Book 1", "Author 1", 100, 50)
M1 = Magazine("Magazine 1", "Author 1", 200, 150, 2022)
N1 = Newspaper("Newzpaper 1", "Media Prints", 200, 2020)
print(B1.get_price())
print(M1.get_price())
print(N1.get_price())