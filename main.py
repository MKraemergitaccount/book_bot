from book_bot import book_bot

bb = book_bot()
bb.read_book(1)
bb.count_words()
bb.count_letters()
bb.which_chars_in_book()
bb.count_characters()

print(f' There are {bb.Get_amount_letters()} in the book.')
for letter, amount in bb.Get_amount_per_chars().items():
    print(f'The {letter} character was found {amount} times.')



