#=====Input Format======
#str
name=input("Enter the name: ")
print(name)
'''Enter the name: vijayalakshmi
vijayalakshmi'''

#int
age=int(input("Enter the age: "))
print(age)
'''Enter the age: 39
39'''

#float
discount=float(input("Enter the discount:"))
print(discount)
'''Enter the discount:55.4
55.4'''

#list
names_list=input("Enter the names: ").split()
print(names_list)
'''Enter the names: raji ram vijji hemanth
['raji', 'ram', 'vijji', 'hemanth']'''

#list.int
list_int=list(map(int,input("Enter the numbers: ").split()))
print(list_int)
'''Enter the numbers: 1 2 3 4 5 6
[1, 2, 3, 4, 5, 6]'''

#list.float
list_float=list(map(float,input("Enter the numbers: ").split()))
print(list_float)
'''Enter the numbers: 565 2543616 193986
[565.0, 2543616.0, 193986.0]'''

#Tuple
names_tuple=tuple(input("Enter the names: ").split())
print(names_tuple)
'''Enter the names: 434 12764 2891798
('434', '12764', '2891798')'''

#tuple.float
tuple_float=tuple(map(float,input("Enter the numbers: ").split()))
print(tuple_float)
'''Enter the numbers: 322 5 87 90 34 
(322.0, 5.0, 87.0, 90.0, 34.0)'''

#tuple_int
tuple_int=tuple(map(int,input("Enter the numbers: ").split()))
print(tuple_int)
'''Enter the numbers: 1 57 35 79 13 15 18
(1, 57, 35, 79, 13, 15, 18)'''

#set
names_set=set(input("Enter the names: ").split())
print(names_set)
'''Enter the names: reddy suma sudheer raji manu pandu yashu
{'suma', 'sudheer', 'manu', 'yashu', 'reddy', 'raji', 'pandu'}'''

#set.int
set_int=set(map(int,input("Enter the numbers: ").split()))
print(set_int)
'''Enter the numbers: 56 38 1289 21 74 532
{38, 1289, 74, 532, 21, 56}'''

#set.float
set_float=set(map(float,input("Enter the numbers: ").split()))
print(set_float)
'''Enter the numbers: 7 89 54 32 69
{32.0, 69.0, 7.0, 54.0, 89.0}'''
s
#dict
dict_names=eval(input("Enter the data: "))
print(dict_names)
'''enter the data: {"names":"roastalmond","flavour":"chocolate","brand":"dairymilk"}
   {'names': 'roastalmond', 'flavour': 'chocolate', 'brand': 'dairymilk'}
'''

#multiple level with unpacking
username,mail,password=input("Enter the username,mail,password: ").split()
print("username: ",username)
print("mail: ",mail)
print("password: ",password)

'''Enter the username,mail,password: Rajeswari raji@gmail.com raji@123
Username: Rajeswari
mail: raji@gmail.com
password: raji@123'''

