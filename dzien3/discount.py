from datetime import date, datetime, timedelta
from time import strftime

today = date.today()
print(today)  # 2025-12-10
print(type(today))  # <class 'datetime.date'>

time = datetime.now()
print(time)  # 2025-12-10 14:40:05.327029
print(today.year)  # 2025
print(today.day)

formated_date = datetime.now().strftime("%d/%m/%Y")
print(formated_date)  # 10/12/2025

# H:M
formated_time = datetime.now().strftime("%H:%M")
print(formated_time)  # 14:45
print(datetime.now().max)  # 9999-12-31 23:59:59.999999
print(datetime.now().min)  # 0001-01-01 00:00:00

formated_time_12h = datetime.now().strftime("%I:%M %p")
print(formated_time_12h)  # 02:47 PM
print(formated_time_12h.removeprefix("0"))  # 2:48 PM

data_object = datetime.now().strptime("10/12/2025", "%d/%m/%Y")
print(data_object)  # 2025-12-10 00:00:00
print(type(data_object))  # <class 'datetime.datetime'>
