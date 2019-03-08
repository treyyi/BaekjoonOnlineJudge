import datetime
w={0:"MON",1:"TUE",2:"WED",3:"THU",4:"FRI",5:"SAT",6:"SUN"}
m,d=map(int,input().split())
print(w.get(datetime.date(2007,m,d).weekday()))
