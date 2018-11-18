import datetime

now = datetime.datetime.today()

print(now)
print(now.day)
print(now.weekday()) #są liczone od 0

x = datetime.datetime.strptime("2018-11-18", "%Y-%m-%d") #<-- bada jak jest zapisane?
print(x)

my_birthday = x = datetime.datetime(1982, 7, 17)
print(my_birthday.weekday())

print(now>my_birthday)

for i in range(20):
    print(now + datetime.timedelta(weeks=i))

delta = now - my_birthday
print(delta.days)