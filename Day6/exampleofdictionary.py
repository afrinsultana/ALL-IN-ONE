# example of dictionary
# ======================

students={1:'Ali',2:'Rahim',3:'Karim',4:'Tahmid',6:'habijabi'} # key Value
print(students)
print(students[4])
print(students[2])

employees=students.copy()
print(employees)
#
#  modify data using 'key'
employees.update({4:'Mahadi Hasan'})
print(employees)

employees.update({5:'Nasheed'})
print(employees)

# Delete Data using 'Del' Command

del employees[4]
print(employees)

print(dir(employees))
print('Display Items')
print('Employee Name %s'%(employees.items()))
print('Employee Name %s'%(list(employees.items())))

print('Display Only Keys')
for k in employees.keys():
    print(k)

print('Display Only Values')
for k in employees.values():
    print(k)

print('Key With Values')
for k in employees.keys():
    print(str(k)+'-'+str(employees[k]))

print('total Item '+str(len(employees)))

for k,v in employees.items():
    print(k,v)

for k,v in employees.items():
    print(f'id:{k}name:{v}')

print(employees.get(3))
employees[9]='Kormokar'
print(employees)

emp=list(employees.keys())
print(emp)

emp.sort()
print(emp)

if 5 in employees:
    print('Has Found')
else:
    print('Not Found')

x=1
while x <4:
    print(employees[x])
    x=x+1






