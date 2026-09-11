books = ["matilda", "harry potter", "wonder", "the jungle book", "charlie"]
copy_counts = [4, 0, 6, 3, 2]

library = {book: count for book, count in zip(books, copy_counts)}

print("Full Library:", library)

available = [book for book in books if library[book] > 0]

print("Available Books:", available)

chosen_book = input("Which book do you want to borrow? ").lower()

if chosen_book not in library or library[chosen_book] == 0:
    print(chosen_book, "is not available!")
    exit()

late_fees = [5, 8, 4, 6, 7]

extra_fee = int(input("Enter extra fee: "))

updated_fees = list(map(lambda fee: fee + extra_fee, late_fees))

print("Updated Fees:", updated_fees)

book_index = books.index(chosen_book)
chosen_fee = updated_fees[book_index]

print("Late fee for", chosen_book, ":", chosen_fee)

library[chosen_book] = library[chosen_book] - 1

print(chosen_book, "borrowed!")
print("Remaining copies:", library[chosen_book])

print()
print("===== LIBRARY SUMMARY =====")
print("Book:", chosen_book)
print("Late Fee:", chosen_fee)
print("Library Stock:", library)
print("===========================")