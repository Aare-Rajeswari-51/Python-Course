#====for loop====
'''for loop is used to iterate over items like lists, strings, or ranges.'''
#checking app usage workdone=1,notdone=0

work=[1,1,0,1,1,0,0,1]
current_streak=0
long_streak=0
for day in work:
    if day==1:
        current_streak+=1
        if current_streak>long_streak:
            long_streak=current_streak
    else:
        current_streak=0
print("longest_streak:",long_streak)

'''longest_streak: 2'''

#=====while loop====
'''while loop repeats a block of code as long as a condition is True.'''

#max attempts of password
crct_password="raji@ram"
attempts=0
max_attempts=3
while attempts < max_attempts:
    password=input("Enter the password:")
    if password == crct_password :
        print("password is correct")
        break
    else:
        attempts+=1
        print("Incorrect pin,try after some time..")
else:
    print("Account is locked,due to too many wrong attempts..!")
    
'''
Enter the password:raji
Incorrect pin,try after some time..
Enter the password:123
Incorrect pin,try after some time..
Enter the password:raji@ram
password is correct
'''


