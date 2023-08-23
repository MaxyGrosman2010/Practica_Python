### First Class ###

#Dates
from datetime import datetime, time, date, timedelta

now = datetime.now()

print(f"{now.day}/{now.month}/{now.year}")
print(f"{now.hour}:{now.minute}:{now.second}")

timestamp = now.timestamp()#For api or management from machine to machine
print(timestamp)
year_2023 = datetime(2023, 1, 1)
print(year_2023)

current_time = time(18,21)

print(f"{current_time.hour}:{current_time.minute}:{current_time.second}")

current_date = date(2023,8,23)

print(f"{current_date.day}/{current_date.month}/{current_date.year}")

diff = year_2023 - now
print(diff)
diff = year_2023.date() - current_date
print(diff)
# diff = year_2023.time() - current_time Not possible
#Timedelta to stablish a period of time
time_delta_first = timedelta(200, 100, 100, weeks= 10)
time_delta_second = timedelta(200, 100, 100, weeks= 13)
print(time_delta_second - time_delta_first)
print(time_delta_second + time_delta_first)