from datetime import date
class User:
    def __init__(self, first_name, last_name, dob, age, contact_no, user_name, password, email, street, city, state,
                 country, pincode):
        self.__first_name = first_name
        self.__last_name = last_name
        self.__dob = dob
        self.__age = age
        self.__contact_no = contact_no
        self.__user_name = user_name
        self.__password = password
        self.__email = email
        self.__street = street
        self.__city = city
        self.__state = state
        self.__country = country
        self.__pincode = pincode

    def display(i):
        print("First Name :", i.__first_name)
        print("Last Name :", i.__last_name)
        print("DOB :"+date.strftime(i.__dob,'%d-%m-%Y'))
        print("Age :", i.__age)
        print("Contact number :", i.__contact_no)
        print("User Name :", i.__user_name)
        print("Email :", i.__email)
        print("Street :", i.__street)
        print("City :", i.__city)
        print("State :", i.__state)
        print("Country :", i.__country)
        print("Postal Code :", i.__pincode)



