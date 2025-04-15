class Book:
  def __init__(self,title,author):
    self.title=title
    self.author=author
  def read(self):
    print(f"The {self.title} is written by {self.author}.")
book1=Book("tintin","shakespear")
book.read()
