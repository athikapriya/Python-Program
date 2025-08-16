# stack is a data structures
# stack works as Last in First out (LIFO)

books = []

books.append("C")
books.append("C++")
books.append("Python")

print(books)

books.pop()
print(f"Now the top book is ", books[-1] )

books.pop()
books.pop()
print(books)

if not books:
    print("No books left")