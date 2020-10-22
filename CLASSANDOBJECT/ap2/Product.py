class Product:
    def __init__(self,name,brand,product_type,color,material,dimension,rate):
        self.__name=name
        self.__brand=brand
        self.__product_type=product_type
        self.__color=color
        self.__material=material
        self.__dimension=dimension
        self.__rate=rate
    def getvalue(self):
        return(print("%-10s%-10s%-10s%-10s%-10s%-10s%-10s" % (self.__name,self.__brand,self.__product_type,self.__color,self.__material,self.__dimension,self.__rate)))
    def set_value(self):
        print("%-10s%-10s%-10s%-10s%-10s%-10s%-10s" % ("Name","Brand", "Type", "Color", "Material", "Dimensions", "Rate"))