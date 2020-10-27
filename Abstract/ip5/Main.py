from abc import ABCMeta, abstractmethod
import sys


class AbstractList:

    @abstractmethod
    def add(self, data):
        pass


    @abstractmethod
    def display(self):
        pass

class Node:
    def __init__(self, data, nn=None):
        self.data=data
        self.nn=nn


class LinkedList(AbstractList):
    def __init__(self, head=None):
        self.head=head


    def add(self, item):
        pass




    def display(self):
        pass
class ArrayList(AbstractList):
    def __init__(self):
        self.arrlist=[]

    def add(self,item):
        self.item = item
        self.arrlist.append(self.item)
        for i in self.arrlist:
            print(i)


    def display(self):
        if self.item in self.arrlist:
            print(self.item)


# Main
print("Select List Type")
print("1. Linked List")
print("2. Array List")
ch =int(input(""))
if ch==1:

    for i in range(0,50):
        print("1.Add 2.Display 3.Exit")
        n = int(input(""))
        if n == 1:
            pass



        elif n == 1:
            pass

        else:
            break
elif ch==2:
    for i in range(0,50):
        print("1.Add 2.Display 3.Exit")
        n = int(input(""))
        if n == 1:
            item=input("Enter value to Insert")
            array = ArrayList()
            array.add(item)

        elif n == 2:
            array = ArrayList()
            array.display()

        else:
            break
else:
    print("Invalid choice")



