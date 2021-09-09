# here is defined the dictionary inside List...
dict_phone = [
    {'number': 9879077786, 'name': 'ahmed'},
    {'number': 9879077723, 'name': 'hassan'},
    {'number': 9879077711, 'name': 'saleh'},
    {'number': 9879087744, 'name': 'mohammed'},
    {'number': 2222223333, 'name': 'nasr'},
    {'number': 9877117766, ' name': 'ammar'},
    {'number': 1111111111, 'name': 'hammed'}
]

#this is the function of Add new Contact
def add_new_cont(num,name):
    dict_phone.append({'number': num, 'name': name})
    pass

#this is the function of searching By Name
def Searching_name(nam):
    cc=next((item for item in dict_phone if item['name'] == nam),None)
    if cc==None:
        cc='Sorry!! This Name is not found...'

    return cc

#this is the function of searching By number
def Searching_num(num):
    if num.isdigit() and len(num) == 10:
        cc = next((item for item in dict_phone if item['number'] == int(num)), None)
        if cc == None:
            cc = 'Sorry!! This Number is not found...'
    else:
        print('Number is not valid')
        cc=None
    return cc



#Here To Ask User about his operation As List
i = int(input(
    'Hey there!! this is Telephone_Book.\nTo search about Name please enter the number: 1 \nTo search about Number please enter the number: 2 \nTo add a new Contact to Telephone_Book please enter the number: 3 \nTo exit press 0: '))
while i != 0:
    if i == 1:                                                                     #This choice to Search By name
        searche_name = input('please enter the Name that you want search:-\n')
        print(Searching_name(searche_name))                                        #This line to Call Function  Search name
    elif i == 2:                                                                   #This choice to Search By Number
        searche_num = input('please enter the number that you want search:-\n')
        print(Searching_num(searche_num))                                          #This line to Call Function  Search Number

    elif i == 3:                                                                   #This choice to Add new Concat
        num1 = input('please enter the number')
        nam1 = input('please enter the name')
        add_new_cont(num1, nam1)                                                   #This line to Call Function  Search Number
        print(dict_phone)

    else:
        print(" You must choose one of '1-2-3-4' ")
        break

    i = int(input(
         'Hey there!! this is Telephone_Book.\nTo search about Name please enter the number: 1 \nTo search about Number please enter the number: 2 \nTo add a new Contact to Telephone_Book please enter the number: 3 \nTo exit press 0: '))
