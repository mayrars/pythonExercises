import datetime

date = datetime.date(2025,1,23)
today = datetime.date.today()
time = datetime.time(12,30,45)
now = datetime.datetime.now()

now = now.strftime("%d/%m/%Y %H:%M:%S")

target_datetime = datetime.datetime(2030,1,2,12,30,1)
current_datetime = datetime.datetime.now()
print(date)
print(today)
print(time)
print(now)
