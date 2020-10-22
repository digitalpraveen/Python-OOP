class User:
    def __init__(self, name, mob, un, pwd):
        self.name = name
        self.mob = mob
        self.un = un
        self.pwd = pwd


    def __str__(self):
          return "user detais as entered\n" + "name:"+self.name+"\n"+"mobile number:"+str(self.mob)+"\n"+"user name:"+str(self.un)+"\n"+"password:"+str(self.pwd)

