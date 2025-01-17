class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    
    def __str__(self):
        return f"'{self.title}' by {self.author}, {self.pages} pages"
    
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):
        return self.pages < other.pages
    
    def __gt__(self, other):
        return self.pages > other.pages

    def __add__(self, other):
        return self.pages + other.pages
    
    def __contains__(self, other):
        return other in self.title
    
    def __getitem__(self, key):
        if key=="title":
            return self.title
        elif key=="author":
            return self.author
        elif key=="pages":
            return self.pages
    
book1 = Book("Harry Potter", "J.K. Rowling", 500)
book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book3 = Book("To Kill a Mockingbird", "Harper Lee", 281)
book4 = Book("1984", "George Orwell", 328)

print(book3)
print(book1 == book2)
print(book2 < book3)
print(book1 > book4)
print(book1 + book2)
print("Harry" in book1)
print(book1["title"])