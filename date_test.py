from datetime import datetime
from datetime import date
from datetime import timedelta

today = date.today()
time_delta = timedelta(days=7)

print(today - time_delta)

bday = date(2023, 4, 12)
till_bday = bday - today

print(till_bday)
print('-----------------------------------------------')

# -----------------------------------------------


today_with_time = datetime.now()
print(today_with_time)
print(today_with_time.strftime('%a'))  # abbreviated weekday name
print(today_with_time.strftime('%A'))
print(today_with_time.strftime('%b'))
print(today_with_time.strftime('%B'))  # prints month name as string
print(today_with_time.strftime('%d'))  # prints day number as string
print(today_with_time.strftime('%W'))  # prints week number
print(today_with_time.strftime('%-m'))  # month as decimal number
print(today_with_time.strftime('%Y'))
print(today_with_time.strftime('%I'))  # Hour as 12-hour clock
print(today_with_time.strftime('%p'))  # AM or PM
print(today_with_time.strftime('%M'))  # minute as zero-padded decimal number
print(today_with_time.strftime('%S'))  # second as zero-padded decimal number
# day of the year as zero-padded decimal number
print(today_with_time.strftime('%j'))
print('-----------------------------------------------')
# -----------------------------------------------

str1 = '2022-10-12'
date1 = datetime.strptime(str1, "%Y-%m-%d")
print(date1)
print(date1.year)
print(date1.month)
print(date1.day)
