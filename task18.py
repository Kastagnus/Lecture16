class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(2,4)
v2 = Vector(3, 5)
v3 = v1 + v2
print(v3)

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author


book1 = Book("The House of Mirth", "Edith Wharton")
book2 = Book("The House of Mirth", "Edith Wharton")
book3 = Book("Brave New World", "Aldous Huxley")
print(book1 == book2)
print(book1 == book3)