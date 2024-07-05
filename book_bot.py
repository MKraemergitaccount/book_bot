class book_bot:

    _books = {
        1 : "./books/frankenstein.txt",
    }

    def __init__(self):
        self.book = None
        self.words = None
        self.amount_letter = 0
        self.amount_per_chars = {}


    # Give the index of a book, receive its words in strings
    def read_book(self, book_number):
        with open(self._books[book_number]) as book:
            book_contents = book.read()
            self.words = book_contents.split()


    # counts the amount of letters in the book.
    def count_letters(self):
        for word in self.words:
            self.amount_letter+=1


    # creates dict with all chars in book
    def which_chars_in_book(self):
        for word in self.words:
            for char in word:
                self.amount_per_chars[char] = 0


    # counts the amount of each char and updates amount_per_chars.
    def count_characters(self):
        for key, value in self.amount_per_chars.items():

    def Get_words(self):
        return self.words


    def Get_amount_letters(self):
        return self.amount_letter


    def Get_amount_per_chars(self):
        return self.amount_per_chars
