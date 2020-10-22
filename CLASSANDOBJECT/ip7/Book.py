class Stall:
    def __init__(self,name,detail):
        self.name=name
        self.detail=detail

    def __str__(self):
        return "Initializing and printing using default Constructor and Str method\n"+"Details of the stall category:\n"+"Book Name : "+self.name+"\n"+"Detail : "+self.detail

    def get_detail(self):
        return self.detail

    def set_detail(self,a):
        self.detail=a

    def display(self):
        print("main")
        print("1.Use Construtor to initialize\n")
        print("2.Use setters and getters\n")
        print("Enter your choice\n")
