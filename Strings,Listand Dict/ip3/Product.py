class Product:
    def __init__(self, name, brand, ptype, pcat, pcatsec, pcatarea, color, mat, dim, prate, city):
        self.__name = name
        self.__brand = brand
        self.__ptype = ptype
        self.__pcat = pcat
        self.__pcatsec = pcatsec
        self.__pcatarea = pcatarea
        self.__color = color
        self.__mat = mat
        self.__dim = dim
        self.__rate = prate
        self.__city = city

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def set_brand(self, brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

    def set_product_type(self, product_type):
        self.__ptype = product_type

    def get_product_type(self):
        return self.__ptype

    def set_category(self, cat):
        self.__pcat = cat

    def get_category(self):
        return self.__pcat

    def set_color(self, color):
        self.__color = color

    def get_color(self):
        return self.__color

    def set_material(self, material):
        self.__mat = material

    def get_material(self):
        return self.__mat

    def set_catalog_service_sector(self, catalog_service_sector):
        self.__pcatsec = catalog_service_sector

    def get_catalog_service_sector(self):
        return self.__pcatsec

    def set_catalog_service_area(self, catalog_service_area):
        self.__pcatarea = catalog_service_area

    def get_catalog_service_area(self):
        return self.__pcatarea

    def set_dimension(self, dim):
        self.__dim = dim

    def get_dimension(self):
        return self.__dim

    def set_rate(self, rate):
        self.__rate = rate

    def get_rate(self):
        return self.__rate

    def set_city(self, city):
        self.__city = city

    def get_city(self):
        return self.__city

    def search(self, id, dic):

    # fill your code here

    def update(self, id, city, dic):

    # fill your code here

    def delete(self, id, dic):

    # fill your code here

    def display(self, dic):
# fill your code here
