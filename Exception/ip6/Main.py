import datetime
try:
    print("Enter the stage event start date and end date")
    start=datetime.datetime.strptime(input(""),'%d-%m-%Y %H:%M:%S')
    end=datetime.datetime.strptime(input(""),'%d-%m-%Y %H:%M:%S')
    print("Start date:%d-%m-%Y %H:%M:%S",datetime.(start))
    print("End date:%d-%m-%Y %H:%M:%S",datetime.datetime.strftime(end))


except:
    print("Input dates should be in the format 'dd-MM-yyyy HH:mm:ss'")
