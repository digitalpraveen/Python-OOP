from abc import abstractmethod, ABCMeta
import xml.etree.ElementTree as ET

tree = ET.parse('creditCard.xml')
root = tree.getroot()


class CreditCard:

    @abstractmethod
    def creditPoints(self):
        pass


class Visa(CreditCard):
    def creditPoints(self):
        for child in root:
             child.tag,child.attribute



class Master(CreditCard):
    def creditPoints(self):


# fill your code
class Platinum(CreditCard):
    def creditPoints(self):


# fill your code

class Titanium(CreditCard):
    def creditPoints(self):


# fill your code


# Main
print("HDFC Credit Cards:")
print("1.Visa\n2.Master\n3.Platinum\n4.Titanium")
ch = input("Enter your card choice:")
if ch==1:
    s=Visa()
elif ch==2:
    s=Master()
elif ch==3:
    s=Platinum()
elif ch==4:
    s=Titanium()
else:
    print("Wrong Choice")

