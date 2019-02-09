class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("The email for {name} has been updated to {email}."
        .format(name=self.name, email=self.email))

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        values = self.books.values()
        sum = 0
        for value in values:
            sum += value
        return sum/len(values)

    def __repr__(self):
        return "User " + self.name + "email: "+ self.email +", books read: " + str(len(self.books))

    def __eq__(self, other):
        if self.name == other.name and self.email == other.email:
            return True
        else:
            return False


class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn_new):
        self.isbn = isbn_new
        print("The isbn for {book} has been updated to {isbn}"
        .format(book=self.title, isbn=self.isbn))

    def add_rating(self, rating):
        if 0 <= rating and rating >= 4:
            self.ratings.append(rating)
        else:
            print("Invalid Rating")

    def get_average_rating(self):
        sum = 0
        for rating in self.ratings:
            sum += rating
        return sum/len(self.ratings)

    def __eq__(self, other):
        if self.title == other.title and self.isbn == other.isbn:
            return True
        else:
            return False

    def __hash__(self):
        return hash((self.title, self.isbn))

    def __repr__(self):
        return self.title + " " + str(self.isbn)


class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        return  self.title + " by " + self.author


class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super() .__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        return self.title + ", a " + self.level + " manual on " + self.subject


class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        user = self.users.get(email)
        user.read_book(book, rating)
        if self.books.get(book) == None:
            self.books[book] = 1
        else:
            read = self.books.get(book)
            self.books[book] = read + 1

    def add_user(self, name, email, user_books=None):
        user = User(name, email)
        self.users[email] = user
        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in list(self.books):
            print(book)

    def print_users(self):
        for user in list(self.users.values()):
            print(user)

    def most_read_book(self):
        book_list = list(self.books)
        most_read = book_list[0]
        for book in book_list:
            if self.books[book] > self.books[most_read]:
                most_read = book
        return most_read

    def highest_rated_book(self):
        book_list = list(self.books)
        highest_rated = book_list[0]
        for book in book_list:
            if book.get_average_rating() > highest_rated.get_average_rating():
                highest_rated = book
        return highest_rated

    def most_positive_user(self):
        user_list = list(self.users.values())
        most_positive = user_list[0]
        for user in user_list:
            if user.get_average_rating() > most_positive.get_average_rating():
                most_positive = user
        return most_positive
