print("Enter the movie details")
n=int(input(""))
c=[]
print("Enter event details in CSV(Movie Name,Director,Actor Name)")
for i in range(n):
     x= input("").split(",")
     s =lambda x:("|".join(x))
     c.append(s(x))
for i in c:
     print(i)