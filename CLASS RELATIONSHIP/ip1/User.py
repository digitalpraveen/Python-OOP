class User:
    def __init__(self, name, age, gender):
        self.name=name
        self.age=age
        self.gender=gender

    # Fill your code here

    def __str__(self):
        return "Name:"+self.name+"\n"+"Age:"+self.age+"\n""Gender:"+self.gender