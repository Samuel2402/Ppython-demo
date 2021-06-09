class Books():
    class_ = "Books"
    def __init__(self, author, title, pages):
        self.author = author 
        self.title = title 
        self.pages = pages 

    def book_description(self):
        return (f'Book author is: {self.author}, Book Title is: {self.title}, Has: {self.pages} pages')

mybook = Books("Philip Pullman", "The Book of Dust", 550)

print(mybook.book_description())
