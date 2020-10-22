class Product:
    def __init__(self,name,brand,product_type,color,material,dimension,rate):
        self.name=name
        self.brand=brand
        self.product=product_type
        self.color=color
        self.material=material
        self.dimension=dimension
        self.rate=rate

    def display(self):
        print("%-10s%-10s%-10s%-10s%-10s%-10s%-10s" % (self.name,self.brand,self.product,self.color,self.material,self.dimension,self.rate))