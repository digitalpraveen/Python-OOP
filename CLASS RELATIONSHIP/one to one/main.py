from idcard import Idcard
from Student import Student

idcard=Idcard(123,False)
stud=Student("praveen",idcard)

stud.idcard=idcard

print(stud)


