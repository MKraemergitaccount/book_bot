

class book_bot:

    _books = {
        1 : "./books/frankenstein.txt",
    }

    def __init__(self):
        self.book = None
        self.words = None
        self.letters = []
        self.amount_words = 0
        self.amount_letters = 0
        self.amount_per_chars_set = {}


    # Give the index of a book, receive its words in strings
    def read_book(self, book_number):
        with open(self._books[book_number]) as book:
            book_contents = book.read()
            self.words = book_contents.split()


    # counts the amount of words in the book.
    def count_words(self):
        for word in self.words:
            self.amount_words+=1


    # counts the amount of chars in the book.
    # sperates letters from words
    def count_letters(self):
        for word in self.words:
            for letter in word:
                self.letters.append(letter)
                self.amount_letters+=1


    # creates dict with all chars in book
    def which_chars_in_book(self):
        for word in self.words:
            for char in word:
                if char.isalpha():
                    self.amount_per_chars_set[char.lower()] = 0


    # counts the amount of each indiviual char and updates amount_per_chars.
    def count_characters(self):
        for key ,value in self.amount_per_chars_set.items():
            for letter in self.letters:
                if key==letter:
                    self.amount_per_chars_set[key]+=1
    

    def Get_words(self):
        return self.words


    def Get_amount_words(self):
        return self.amount_words


    def Get_amount_letters(self):
        return self.amount_letters

    
    def Get_amount_per_chars(self):
        return self.amount_per_chars_set
