#import datetime
from datetime import datetime, timedelta

a = datetime(2023, 6, 1)
b = datetime(2023, 6, 1, 9, 30, 15)
print(a) # 2023-06-01 00:00:00
print(b) # 2023-06-01 09:30:15

c = datetime.now()
print(c) 

f = datetime.strptime("23/06/2023 09:30", "%d/%m/%Y %H:%M")
print(f)

print(f.day)
print(f.month)
print(f.year)

#f.day = 29
print(f.date())
print(f.strftime("%d/%m/%Y %H:%M"))

t1 = timedelta(days=1, hours=10)
print(t1)

print(f + t1)

