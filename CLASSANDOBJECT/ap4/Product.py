class Product:
    def __init__(self , name , brand , product_type , product_category , catalog_service_sector , catalog_service_area , color , material , dimension , rate , city):
        self.__name=name
        self.__brand=brand
        self.__product_type=product_type
        self.__product_category=product_category
        self.__catalogue_service_sector=catalog_service_sector
        self.__catalogue_service_area=catalog_service_area
        self.__color=color
        self.__material=material
        self.__dim=dimension
        self.__rate=rate
        self.__city=city

    def __str__(self):
         return("%-15s%-15s%-15s%-15s%-15s%-15s%-15s%-15s%-15s%-15s%-15s"%(self.__name,self.__brand,self.__product_type,self.__product_category,self.__catalogue_service_sector,self.__catalogue_service_area,self.__color,self.__material,self.__dim,self.__rate,self.__city))