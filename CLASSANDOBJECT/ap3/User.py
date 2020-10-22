class User:
    def __init__(self,first_name,last_name,dob,age,contact,email,username,password,role,address):
        self.__firstname=first_name
        self.__lastname=last_name
        self.__dob=dob
        self.__age=age
        self.__contact=contact
        self.__email=email
        self.__username=username
        self.__password=password
        self.__role=role
        self.__address=address

    def __eq__(self, obj):
        # fill your code
        if self.__username == obj.__username and self.__email == obj.__email and self.__contact==obj.__contact:
              print("Both users are same")
        else:
            print("Both users are not same")

