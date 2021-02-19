class Book: 
    def __init__(self, title):
        self.title = title
    
    def __str__(self):
        return "Title: " + self.title

    def __repr__(self):
        return "Title: " + self.title

class BackPack:
    def __init__(self, books):
        #self.name = name
        self.books = books

    def __repr__(self):
        #return self.name
        return "Books: %s" % (self.books)

    def __str__(self):
        return "Books: %s" % (self.books)

    def __iter__(self):
        self.x = 0
        return self

    def __next__(self):
        if (self.x < len(self.books)):
            current_book = self.books[self.x]
            self.x = self.x+1
            return current_book
        else:
            raise StopIteration

b1 = Book("Harry Potter and the sorcerer's stone")
b2 = Book("Harry Potter and the chamber of secrets")
b3 = Book("Harrt Potter and the prisoner of azkaban")

books = [b1, b2, b3]

backpack = BackPack(books)

print(backpack)