#1.sum of nums from 1 to N using for loop
sum=0
for i in range(1,10):
    sum+=i
    i=i+1
    print(sum)
#2.odd nums from 1 to N using for loop
for i in range(1,10):
    if i%2!=0:
        print(i)

#3.Factorial of a number using for loop
fact=1
n=int(input("Enter the number: "))
for i in range(1,n+1):
    fact*=i
    n=n-1
print(f"Factorial of a number:{fact}")
'''
Enter the number: 16
Factorial of a number:20922789888000'''

#4.Multiplication table of N using for loop
num=int(input("Enter the num: "))
for i in range(1,11):
    mul=num*i
    print(f" {num}*{i}={mul}")

'''
Enter the num: 16
 16*1=16
 16*2=32
 16*3=48
 16*4=64
 16*5=80
 16*6=96
 16*7=112
 16*8=128
 16*9=144
 16*10=160'''

#5.prime num using for loop
N=int(input("Enter the N: "))
for i in range(1,N):
    if N>1:
        if N%i==0:
            print(f"{N} is not a prime num")
            break
        else:
            print(f"{N} is a prime num")
    else:
        print(f"{N} is not a prime num")

'''
Enter the N: 111
111 is not a prime num'''

#6.sum of digits of a num using while loop
sum=0
while(i<=10):
    sum+=i
    i+=1
print(f"sum of 1 to 10: {sum}")

'''
sum of 1 to 10: 55'''

#7.fibonacci series using for loop
n=int(input("Enter the num: "))
a=0
b=1
for i in range(n):
    print(a, end= ',')
    next_term=a+b
    a=b
    b=next_term
'''
Enter the num: 11
0,1,1,2,3,5,8,13,21,34,55,
'''

#8.palindrome using while loop
num=int(input("Enter num: "))
original=num
reverse=0
while num>0:
    digit=num%10  #to get the last digit
    reverse=reverse*10+digit  #to shift digits to the left in the reversed number
    num//=10  #to remove the last digit
if original==reverse:
    print(f"it is a palindrome")
else:
    print(f"it is not a palindrome")

'''
🔁 Iteration by Iteration:
Step	num	digit = num % 10	reverse = reverse * 10 + digit	Updated num (num // 10)
1	1234	4	                    0 * 10 + 4 = 4	           123
2	123	3	                    4 * 10 + 3 = 43	           12    
3	12	2	                    43 * 10 + 2 = 432	            1
4	1	1	                    432 * 10 + 1 = 4321	            0

➡️ Loop ends because num = 0

'''
#9.sum of prime numbers  upto n using for loop
import math
n=int(input("enter the num: "))
sum=0
for num in range(2,n+1):
    is_prime=True
    for i in range(2,int(math.sqrt(num))+1):
        if num%i==0:
            is_prime=False
            break
    if is_prime:
        sum+=num
print(f"sum of palindrome {n} is {sum}")


#10.product of digits of a number using while loop
product=1
i=1
while(i<=10):
    product*=i
    i+=1
print(f"product is:{product}")

'''product is:3628800
'''

#11.multiples of 5 upto N using for loop
num=int(input("Enter the num: "))
for i in range(1,n+1):
    if i%5==0:
        print(f"{i} is multiple of 5")
else:
    print(f"{i} is Not a multiple of 5")

'''
Enter the num: 11
5 is multiple of 5
10 is multiple of 5
11 is Not a multiple of 5
'''
#12.Right angle triangle using for loop
sides=[]
for i in range(3):
    side=float(input(f"Enter the side{i+1}:"))  #taking inputs
    sides.append(side)
sides.sort()
if round(sides[0]**2+sides[1]**2,5)==round(sides[2]**2,5):
    print("it is a right angled triangle.. ")
else:
    print("it is not  a right angled triangle.. ")

'''
Enter the side1:5
Enter the side2:4
Enter the side3:3
it is a right angled triangle.. 
'''

#13.Hallow Square pattern using for loop
n=int(input("Enter the size of a square: "))
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''
Enter the size of a square: 6
******
*    *
*    *
*    *
*    *
******   '''

#14. Hallow rectangle using for loop
row=int(input("Enter row of a rectangle: "))
coloumn=int(input("Enter coloumn of a rectangle: "))
for i in range(row):
    for j in range(coloumn):
        if i==0 or i==row-1 or j==0 or j==coloumn-1:
            print("*",end="")
        else:
            print(" ",end="")
    print()

'''
Enter row of a rectangle: 5
Enter coloumn of a rectangle: 9
*********
*       *
*       *
*       *
*********  '''

#15.Hallow triangle using for loop
n=int(input("Enter the size of a triangle: "))
for i in range(1,n+1):
    for j in range(1,n+1):
        if j==1 or j==i or i==n:
            print("*",end="")
        else:
            print(" ",end="")
    print()
'''
Enter the size of a triangle: 7
*      
**     
* *    
*  *   
*   *  
*    * 
*******  '''

#16.checking whether a num is perfect or not
#6=divisors:1+2+3
num=int(input("Enter the num: "))
sum=0
if num>0:
    for i in range(1,num):
        if num%i==0:
            sum+=i
            print(f"{i} is a divisor of {num}")
    if sum==num:
        print(f"{num} is a perfect number")
    else:
         print(f"{num} is not a perfect number")        
else:
    print(f"{num} is not a perfect number")

'''
Enter the num: 6
1 is a divisor of 6
2 is a divisor of 6
3 is a divisor of 6
6 is a perfect number'''

#17.LCM(Least Common Factor)of 2 nums using while loop
'''
factors of 4=4,8,12,16
6=6,12,18--
LCM(4,6)=12

lcm(a,b)=(a*b)//gcd(a,b)'''
a=int(input("Enter the num1: "))
b=int(input("Enter the num2: "))
if a>b:
    greater=a
else:
    greater=b
while True:
    if greater%a==0 and greater%b==0:
       lcm=greater
       break
    greater+=1
print(f"LCM of {a} and {b} is {lcm}")

'''
Enter the num1: 15
Enter the num2: 10
LCM of 15 and 10 is 30
'''
#another method
import math
a=int(input("Enter a:"))
b=int(input("Enter b:"))
lcm=(a*b)//math.gcd(a,b)
print(f"LCM of {a} and {b} is {lcm}")
'''
Enter a:4
Enter b:6
LCM of 4 and 6 is 12'''

#18.GCD(Greatest Common Divisior) using while loop
'''
GCD of 12 and 18 is 6, because:
Divisors of 12 → 1, 2, 3, 4, 6, 12
Divisors of 18 → 1, 2, 3, 6, 9, 18
Common divisors: 1, 2, 3, 6 → Highest is 6'''

a=int(input("Enter first num:"))
b=int(input("Enter second num:"))
while b!=0:
    a,b=b,a%b
print(f"GCD is {a} ")
'''
Enter first num:11
Enter second num:16
GCD is 1 
'''

#19.Armstrong number using for loop
#153=1**3+5**3+3**3
num=int(input("Enter the number: "))
original=num
count_num=count(num)
for i in num(1,count_num+1)
    if i**3



    
    
        


         
    

    
    

    

