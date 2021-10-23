'''
def functionName(Parameter):
    statement 1
    statement 2
    ...

'''
def display():
    persons=[
        {'id':'s-001','name':'Nashid Pervez','email':'nashidpervez@gmail.com'},
        {'id':'s-002','name':'Afrin Sultana','email':'afrin@gmail.com'},
        {'id':'s-003','name':'Nawshin','email':'nawshin@gmail.com'},
        {'id':'s-004','name':'Shahin Rahim','email':'shahin@gmail.com'},
        {'id':'s-005','name':'Mahadi Hasan','email':'mahadi@gmail.com'},
        {'id':'s-006','name':'Aziz Uddin','email':'aziz@gmail.com'},
        ]

print('%-10s %-30s %-20s' %('Id Number','Name','Email Address'))
print('='*80)

# for p in persons:
#     print('%-10s %-30s %-20s'%(p['id'],p['name'],p['email']))
#     print('-'*80)

#     # Calling function
display()
      





