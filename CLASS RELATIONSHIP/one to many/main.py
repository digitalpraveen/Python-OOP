from Library import Library
from Book import Book

lib=Library("dr apj")

'''
b1=Book("HP","JKR")
b2=Book("ABC","AUT1")
lib.book.append(b1)
lib.book.append(b2)
'''
n=int(input("enter the number of books"))
for i in range(n):
    print("enter book",i+1)
    name=input()
    author=input()
    b=Book(name,author)
    lib.book.append(b)


print(lib)
b=[]
b.append(Book("HP","JKR"))
b.append(Book("ABC","AUT1"))
b.append(Book("HP","Aut2"))

b1=Book("HP","aut4")
for i in b:
     if b1==i:
          print(i)

''''
print(b1.__eq__(b2))
print(b2.__eq__(b3))
print(b1==b2)
print(b1==b3)
'''''
