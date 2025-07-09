#checking wheteher the user is valid or not(login credentials)==login page

data={
'raji@gmail.com':'raji@ram',
'faheem@gmail.com':'rafi@faheem',
'vijji@gmailcom':'vijji@raji'}
email,pwd=input("Enter the email,pwd: ").split()
if data.get(email)==pwd:   #data[email] alse we can use but some times we need to access them,thats why we use 'get'
    print("login successful")
else:
     print(" Invalid login")
'''
#Enter the email,pwd: raji@gmail.com 123
#Invalid login'''



#checking whether the item is present (or) not==restaurant(swiggy)
items=['chocolate','cake','icecream','dosa','idly']
stocks=[10,30,0,40,3]
data=input("Enter the item: ")
if data in items:
    ind=items.index(data)
    if stocks[ind]>=10:
        print("Item is available")
    elif stocks[ind]==0:
        print("stock is not available,please try another item..!")
    elif stocks[ind]<5:
        print("Hurry up..!, the stock is low")
else:
    print("Item is  not available")
    
'''
#Enter the item: coffe
#Item is  not available'''

#filtering the data in restaurant or cafe(swiggy)
items=['coffe','icecream','chocolate','dosa','idly','samosa']
distance=[25,10,7,15,39,18]
time=[20,30,19,40,25,9]
ratings=[4,3.8,4.3,3.9,4.1,2]
veg_status=['True','True','True','True','True','False',]
cost=[160,200,120,60,50,70]
data=input("Enter the item: ")
if data in items:
    ind=items.index(data)
    if distance[ind]<20 and time[ind]<30 and ratings[ind]>4 and veg_status[ind]==True and cost[ind]<190:
        print("distance,time,ratings,cost,veg_status applied")
    elif distance[ind]<20 and time[ind]<30 and ratings[ind]>4 and veg_status[ind]==True:
        print("distance,time,ratings,veg_status applied")
    elif distance[ind]<20 and time[ind]<30 and ratings[ind]>4 and cost[ind]<190:
        print("distance,time,ratings,cost applied")
    elif distance[ind]<20 and ratings[ind]>4:
        print("distance,ratings applied")
    elif distance[ind]<20 and cost[ind]<190:
        print("distance,cost applied")
    elif distance[ind]<20 and time[ind]<30:
        print("distance,time applied")
    elif time[ind]<30 and cost[ind]<190:
        print("time,cost applied")
    elif distance[ind]<20:
        print("distance applied")
    elif time[ind]<30:
        print("time applied")
    elif ratings[ind]>4:
        print("ratings applied")
else:
    print("item is not available")

'''
Enter the item: chocolate
distance,time,ratings,cost applied
'''

# Modify the Amazon stock example to check if the user has a discount coupon in addition to being a Prime member.
items=['trousers','baggy jeans','tops','kurtis','scarfs']
stocks=[20,10,15,5,0]
data=input("Enter the item: ").lower()
customer=input("Enter the name: ")
is_primary_customer=['raji','ram','hemanth']
coupon=input("Do u have a coupon code..!?: ").strip().upper()
valid_coupon=['NOTFEELINGWELL','MESSY','BEHAPppy']
if data in [item.lower() for item in items]:
    ind_data=[item.lower() for item in items].index(data)
    if stocks[ind_data]==0:
        print("amazon stock is not avaialable")
    elif stocks[ind_data]<=5:
        if customer in is_primary_customer:
            print("hurry up..!amazon stock is low")
        else:
            print("Stock is low, Try after sometime")
    elif  stocks[ind_data]>10:
         print("amazon stock is available..")
         if coupon.strip().upper() in [c.upper() for c in valid_coupon]:
             print("you get 10% discount on this product by using coupon code")
else:
    print("item is not available")
    
'''
Enter the item: kurtis
Enter the name: raji
Do u have a coupon code..!?: messy
hurry up..!amazon stock is low
you get 10% discount on this product by using coupon code
'''

#====leap year===
year=int(input("Enter the year: "))
if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("leap year")
else:
    print("Not a leap year=Century year")
'''
Enter the year: 2024
leap year'''

#===checking if the number is square of another===
num1=int(input("Enter the num1(small num): "))
num2=int(input("Enter the num2(big num): "))
if num1**2==num2:
  print(f"{num2} is the square of  {num1}")
else:
    print(f"{num2} is not the square of {num1}")

'''
Enter the num1(small num): 8
Enter the num2(big num): 64
64 is the square of  8'''

#======Another method=====:
import math
num=int(input("Enter the num: "))
sqrt_num=math.sqrt(num)
if sqrt_num==int(sqrt_num):
    print(f"{num} is the perfect square")
    print(f"it is the sqrt of {int(sqrt_num)}")
else:
    print(f"{num} is not a perfect square")

'''
Enter the num: 81
81 is the perfect square
it is the sqrt of 9'''


#===checking if a num is prime or not====
num=int(input("Enter the num: "))
if num>1:
    for i in range(2,num):
        if num%i==0:
            print(f"{num} is not a prime num")
            break
    else:
        print(f"{num} is a prime num")
else:
    print(f"{num} is not  a prime num")

'''
Enter the num: 11
11 is a prime num
'''

#===no need to check all n-1 if it find sqrt it stops the loops===
import math
num=int(input("Enter the num: "))
if num>1:
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            print(f"{num} is not a prime num")
            break
    else:
        print(f"{num} is a prime num")
else:
    print(f"{num} is not  a prime num")

'''
Enter the num: 17
17 is a prime num
'''

#checks if a triangle is perfect triangle===
a=float(input("Enter a: "))
b=float(input("Enter b: "))
c=float(input("Enter c: "))
if a+b>c and b+c>a and a+c>b:
    print("it is a valid triangle..")
elif a==b and b==c and c==a:
    print("it is equilateral triangle..")
else:
    print("it is a scalene triangle..")

'''
Enter a: 4
Enter b: 5
Enter c: 6
it is a valid triangle..
'''

#validate if a password length is strong
password=input("Enter the Password: ")
if len(password)<8:
    print("password tooo short,must contain atleast 8 characters.. ")
elif(re.search(r"[A-Z]",password) and re.search(r"[a-z]",password) and re.search(r"[0-9]".password) and re.search(r"[!@#$%^&*()_-=+<>?|]".password)):
    print("Strong Password")
else:
    print("weak password,must contain atleast one uppercase,lowercase,numerics and special characters")

'''
Enter the Password: raji@12
password tooo short,must contain atleast 8 characters.. 
'''


    



            




    
    
    
    
    
    
    

    
