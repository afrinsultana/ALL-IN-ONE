import datetime

datetime_obj=datetime.datetime.now()
print(datetime_obj)

datetime_obj=datetime.date.today()
print(datetime_obj)

from datetime import datetime,date

datetime_obj=datetime.now()
print(datetime_obj)

datetime_obj=date.today()
print(datetime_obj)

cdate=datetime.now()
print(cdate)

print(cdate.year)
print(cdate.month)
print(cdate.day)

print(cdate.hour)
print(cdate.minute)
print(cdate.second)
print(cdate.microsecond)
#  week day 
print(cdate.strftime('%a')) # week day short form
print(cdate.strftime('%A')) # week day Long format
print(cdate.strftime('%w')) # Number of Week
# Month Format
print(cdate.strftime('%b')) # Month Short format
print(cdate.strftime('%B')) # Month Long Format
print(cdate.strftime('%m')) # Month Number

# day
print(cdate.strftime('%d')) # Day Short format

# Year
print(cdate.strftime('%y')) # Year short Format- without century
print(cdate.strftime('%Y')) # Year  long Number
print('-'*50)
#time
print(cdate.strftime('%H')) # 
print(cdate.strftime('%I'))
print(cdate.strftime('%p'))
print(cdate.strftime('%M'))
print(cdate.strftime('%S'))
print(cdate.strftime('%f'))
print('-'*50)
# Custom Formatting
print(cdate.strftime('%d-%m-%y'))
print(cdate.strftime('%A,%m/%d/%y'))

print(cdate.strftime('%H:%M:%S'))
print(cdate.strftime('%I:%M:%S %p'))

