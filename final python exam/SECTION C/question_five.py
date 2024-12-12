# (i)
class Book:
     def __init__(self, title, author, pages):
          self.title = title
          self.author = author
          self.pages = pages

     def display_info(self):
       return f"Title: {self.title}, Author: {self.author}, pages: {self.pages}"

# an instance of the Book class
book = Book("Things Fall Apart","William Shakespear", 500)
print(book.display_info())


# (ii)

class EBook(Book):
        def __init__(self, title, author,pages,file_format):
          super().__init__(title, author, pages)
          self.file_format = file_format

def display_info(self):
               return f"Title: {self.title}, Author:{self.author}, pages:{self.pages}, format:{self.file_format}"
          
# additional attribute
class EBook:
    def __init__(self, title, author, format):
        self.title = title
        self.author = author
        self.format = format

    def display_info(self):
        return f"Title: {self.title}, Author: {self.author}, Format: {self.format}"

# (iii)
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def get_title_and_author(self):
            return f"Title : {self.title}, Author :{self.author}"
        
    Book = Book("Things Fall Apart","David Rubadiri")
    print(Book.get_title_and_author())
