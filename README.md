# Library Management System

A Library management system written in Python using OOP. 

This program will use "books.txt", by default, file that user will create as a database where  each  line  will  represent  a  single  book.  At each  line,  
* book title,  
* author, 
* first release year,
* number of pages,
* genre 
        
will be kept and separated with a comma.

## Features 

* List Books
    
    This method will list all the books in the file with book's name and author, respectively. 

    If there is no book in the library, it will print out "No books in the library." message.

* Add Book 

    This method will add a new book to the file by using user's inputs for title, author, publication year, number of pages, and genre.

* Remove Book 

    This method will delete the book with the given title from the file. 

    If there is no book in the library, it will print out "Library is empty." message. 

* Search Genre

    This method will list all the books in the file by genre. 

    If there is no book in the library, it will print out "Library is empty." message. 

    If there is no book in the library with that genre,it will print out "No books in the library with genre_name genre." message.


## Installation

1. Clone the repository:


```bash
git clone https://github.com/ironcopper/library_management_system.git
```

2. Navigate to the project directory:

```bash
cd library_management_system
```

3. Run the application:

```bash
python library_management_system.py
```

## Menu
```
*** MENU ***
1) List Books
2) Add Book
3) Remove Book
4) Search Genre
E) Exit
```



## License

[MIT](https://choosealicense.com/licenses/mit/)