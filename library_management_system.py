import sys

class Library:
    def __init__(self, file="books.txt"):   # constructer method to open the file
        self.file = file
        self.file = open(self.file, "a+")


    def __del__(self):                      # destructor method to close the file
        self.file.close()


    def list_books(self):
        self.file.seek(0)                       # Move the file pointer to the beginning
        books = self.file.read().splitlines()   # Read the contents of the file and add each line to a list

        if not books:                   
            print("No books in the library.")
        else:
            for book in books:
                book_name, author, year, page, genre = Library.split_str(book)
                print(f"Book: {book_name}, Author: {author}")
            print(f"Number of the books in the library: {len(books)}")


    def add_book(self):
        title = input("Title: ")
        author = input("Author: ")
        year = input("Publication year: ")
        page = input("Number of pages: ")
        genre = input("Genre: ")

        new_book = title + "," + author + "," + year + "," + page + "," + genre + "\n"
        
        self.file.write(new_book)           # Append a new book to the file
        print(f"New book \"{title.upper()}\" added to the library.")


    def remove_book(self):
        self.file.seek(0)
        books_list = self.file.readlines()

        if not books_list:                   
            print("Library is empty.")

        else:
            book_title  = input("Enter the book title to remove: ").rstrip()
                        
            for book in books_list:             # Find the index of the book to be deleted
                book_name, author, year, page, genre = Library.split_str(book)
                if book_name == book_title:
                    index = books_list.index(book)
                    books_list.pop(index)
 
            self.file.seek(0)
            self.file.truncate()  # Clear the contents of the file
            self.file.writelines(books_list)


    def search_genre(self):
        """
        This method will list all the books in the books.txt file by genre. 
        """
        self.file.seek(0)
        book_list = self.file.readlines()   
        genree = []                         # list of a specific genre's index numbers

        if not book_list:
            print("Library is empty.")

        else:
            genre_ = input("Enter the genre: ").rstrip()

            for book in book_list:             # Find the index of the book to be deleted
                book_name, author, year, page, genre = Library.split_str(book)
                genre = genre.replace("\n","")

                if genre == genre_:
                    genree.append(book_list.index(book))
                else:
                    pass
            
            if not genree:
                print(f"No books in the library with \"{genre_.upper()}\" genre.")

            else:
                print("Book,Author,Year,Page,Genre")

                for i in range(len(genree)):
                    print(book_list[genree[i]],end="")
                print(f"Number of the books in the library: {len(genree)}")


    @classmethod            # class method for splitting string
    def split_str(cls,line):
        return line.split(",")


    def menu(self):         # menu of the library
        print("*** MENU ***")
        print("1) List Books")
        print("2) Add Book")
        print("3) Remove Book")
        print("4) Search Genre")
        print("E) Exit")




def main():
    lib = Library()     # Create an object lib with Library class

    while True:
        lib.menu()      # call the menu

        choice = input("Action(1-2-3-4-E): ").strip()

        if choice == "1":
            lib.list_books()

        elif choice == "2":
            lib.add_book()

        elif choice == "3":
            lib.remove_book()

        elif choice == "4":
            lib.search_genre()

        elif choice == "E":
            sys.exit("Exiting...")

        else:
            print("Invalid choice.\nPlease enter 1, 2, 3, 4 or E.")


if __name__ == "__main__":
    main()
