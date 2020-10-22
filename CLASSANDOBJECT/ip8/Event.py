from datetime import datetime
class Event:

    def __init__(self,name,date):
        self.__name=name
        self.__date=date

    def checkDate(self):
        result=(self.__date).month
        if (result%2==0):
            print("You are offered with the Birthday Bash on"+datetime.strftime(self.__date,"%b")+str((self.__date).day)+"of this year")
        else:
            print("You are not offered with the Birthday Bash ")

