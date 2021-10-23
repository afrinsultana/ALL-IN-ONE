import calendar

yy=1999
mm=5
print(calendar.month(yy,mm))

print(calendar.calendar(1999))

if calendar.isleap(2000):
    print('The year is Leap Year')
else:
    print('The Year is not Leap Year')

c=calendar.TextCalendar(calendar.SUNDAY)
str=c.formatmonth(1999,5)
print(str)


hc=calendar.HTMLCalendar(calendar.SUNDAY)
str=hc.formatmonth(1999,5)
print(str)



