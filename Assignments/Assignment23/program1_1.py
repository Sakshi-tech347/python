class BookStore:
    NoOfBook = 0

    def __init__(self ,A, B) :
        self.Name = A
        self.Author = B
        print("Object is created succefully ")
        BookStore.NoOfBook = BookStore.NoOfBook +1

    def Display(self):
        print("{self.A} By {self.B}  No of Books Are:",{BookStore.NoOfBook})

obj1 = BookStore("LSP","Robert Love")
obj1.Display()

obj2 = BookStore("c++","bjyarn strustrup")
obj2.Display()
