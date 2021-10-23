

# person1={'id':'s-001','name':'Nashid Pervez','email':'nashidpervez@gmail.com'}
# person2={'id':'s-002','name':'Afrin Sultana','email':'afrin@gmail.com'}
# person3={'id':'s-003','name':'Nawshin','email':'nawshin@gmail.com'}
# person4={'id':'s-004','name':'Shahin Rahim','email':'shahin@gmail.com'}
# person5={'id':'s-005','name':'Mahadi Hasan','email':'mahadi@gmail.com'}

persons=[
    {'id':'s-001','name':'Nashid Pervez','email':'nashidpervez@gmail.com'},
    {'id':'s-002','name':'Afrin Sultana','email':'afrin@gmail.com'},
    {'id':'s-003','name':'Nawshin','email':'nawshin@gmail.com'},
    {'id':'s-004','name':'Shahin Rahim','email':'shahin@gmail.com'},
    {'id':'s-005','name':'Mahadi Hasan','email':'mahadi@gmail.com'},
    {'id':'s-006','name':'Aziz Uddin','email':'aziz@gmail.com'},
    ]

# print('%10s %30s %20s' %('Id Number','Name','Email Address'))
print('%-10s %-30s %-20s' %('Id Number','Name','Email Address'))
print('='*80)


# persons=[person1,person2,person3,person4,person5]
for p in persons :
        print('%-10s %-30s %-20s'%(p['id'],p['name'],p['email']))
        print('-'*80)
       
        
      

# print('Id Number :  %s'%(person1['id']))
# print('Name :  %s'%(person1['name']))
# print('Email :  %s'%(person1['email']))
# print('='*50)
# print('Id Number :  %s'%(person2['id']))
# print('Name :  %s'%(person2['name']))
# print('Email :  %s'%(person2['email']))
# print('='*50)
# print('Id Number :  %s'%(person3['id']))
# print('Name :  %s'%(person3['name']))
# print('Email :  %s'%(person3['email']))
# print('='*50)
# print('Id Number :  %s'%(person3['id']))
# print('Name :  %s'%(person3['name']))
# print('Email :  %s'%(person3['email']))
# print('='*50)
# print('Id Number :  %s'%(person4['id']))
# print('Name :  %s'%(person4['name']))
# print('Email :  %s'%(person4['email']))




