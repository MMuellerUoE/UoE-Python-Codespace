books = ["Calculus", "Linear Algebra", "Differential Equations",
         "Probability", "Coding", "Numerical Analysis"]

books_list_1 = [1,6,3]
for i in books_list_1:
    print(books[i-1])

books_2 = books[:]
books_2.append("Graphs and Networks")
books_2.insert(1,"Measure Theory")
print(books_2)

books_3 = books_2[:]
del books_3[5]
books_3.remove("Probability")
print(books_3)

books_3.sort()
print(books_3)

print(sorted(books_3,reverse=True))

print(len(books_3))

book_idx = range(1001,1001+len(books_2),1)
for i in range(len(books_2)):
    print(f"Book {book_idx[i]} available: {books_2[i]}")

books_long_titles = [book for book in books_2 if len(book) > 15]
print(books_long_titles)
print([min(book_idx),max(book_idx),sum(book_idx)])

print(books_2[:3])
print(books_2[-2:])

library_hours = ("9 AM", "5 PM")
print(f"The library is open from {library_hours[0]} to {library_hours[1]}.")
new_library_hours = ("10 AM", "6 PM")
print(f"The library is open from {new_library_hours[0]} to {new_library_hours[1]}.")
