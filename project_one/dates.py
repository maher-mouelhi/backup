import  datetime

now = datetime.datetime.now()

aniversary = datetime.datetime(2012,11,13,16,55)

import time
yesterday = datetime.datetime.fromtimestamp(time.time()- 3600*24)

print(now,aniversary,yesterday)

print(now.strftime("%A %d/%b/%Y %H:%M")) # formating date

datestring = "12/15/2013 15:30"
date_format = "%m/%d/%Y %H:%M"

mdate = datetime.datetime.strptime(datestring,date_format)
print(mdate)

next_week = now + datetime.timedelta(days=7) # it gives next week calculated

for i in range(15):
    #print((now+datetime.timedelta(days=i)).strftime("%a"))  # shows the days name short format
    #print((now + datetime.timedelta(days=i)))  # shows the dates
    print((now+datetime.timedelta(days=i)).strftime("%A"))  # shows the days name long format


import calendar

first_weekday,number_days = calendar.monthrange(2012,2)
print(first_weekday,number_days)

print(calendar.month(2012,2))