from Hall import Hall
import datetime
d1=input("Enter Start time \n")
d2=input("Enter the End time\n")
cost=int(input("Enter the cost per day\n"))
startdate=datetime.datetime.strptime(d1,'%b %d %Y').date()
enddate=datetime.datetime.strptime(d2, '%b %d %Y').date()
p=Hall(startdate,enddate,cost)
p.noDays()
p.cost(cost)