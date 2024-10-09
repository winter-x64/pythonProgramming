import datetime

date_today = datetime.date.today()
day_today = date_today.ctime()

print("The date today is ", date_today)
print("The date info. is ", day_today)

# you will get the current date and time in the format of "day, date month year time"
# Output
# The date today is  2024-10-09
# The date info. is  Wed Oct  9 00:00:00 2024
