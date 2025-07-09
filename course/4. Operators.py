'''1.Arithmetic
     operators'''
a=10
b=3
print("Add(+):",a+b)   #Add(+): 13
print("sub(-):",a-b)   #sub(-): 7
print("multiply(*):",a*b)    #multiply(*): 30
print("div(/):",a/b)         #div(/): 3.3333333333333335==(quotient)
#floordivision(gives onlyy integral part,removes decimal)
print("floordiv(//):",a//b)     #floordiv(//): 3
print("Modulus(%):",a%b)        #Modulus(%): 1==(reminder)
#exponential(power)
print("expo(**):",a**b)     #expo(**): 1000




'''2.Comparison
       Operators'''
#Equal to(==)
a=5
b=15
print(a==b)  #False


#Not equal to(!=)
print(a!=b)   #True

#greater than(>)
print(a>b)  #False

#Less than(<)
print(a<b)   #True

#Greater than or equal to(>=)
print(a>=b)  #False

#Less than or equal to(<=)
print(a<=b)  #True



'''3.Assignment Operators
        (whenever we ar dealing with same variable
        and we have to modify it then we can use this operators)'''

'''Variable=Variable(Operator)value
   e=e+1
   Var(operator)=Value
   e+=1'''

a=10
print("Assign:",a)  #Assign: 10
a+=20
print("Add&Assign(+=):",a)  #Add&Assign(+=): 30
a-=5
print("Sub&Assign(-=):",a)  #Sub&Assign(-=): 25
a*=6
print("Multiply&Assign:",a)  #Multiply&Assign: 150
a**=3
print("Exponentiate&Assign:",a) #Exponentiate&Assign: 3375000
a/=5
print("Divide&Assign:",a)      #Divide&Assign: 675000.0
a//=2
print("Floor Division&Assign:",a) #Floor Division&Assign: 337500.0
a%=5
print("Modulus&Division:",a)   #Modulus&Division: 0.0



'''4.Logical Operators
            (when we have multiple conditions thn we will use
             and=when both conditions true-TRUE
             or=any one condition is true-TRUE
             not=when ntg is true-TRUE)
==Not==
Not True=False
Not false=True'''


a=10
b=5
print("AND:",a%5==0 and b%5==0) #AND: True==(T and T--T)
print("AND:",a%2==0 and b%6==0) #AND: False==(T and F--F)
print("OR:",a%3==0 or b%5==0)   #OR: True==(F or T--T)
print("OR:",a%1==0 or b%1==0)   #OR: True==(T or T--T)
print("OR:",a%3==0 or b%3==0)   #OR:False==(F or F--F)
print("NOT:",not a%5==0)   #NOT: False==(not T--F)
print("NOT:",not a%3==0)   #NOT: True==(not F--T)


''' 5.Membership Operators
    to check whether the specific element present in sequence or not
        in,not in'''


names=['Raji','Navi','Faheem','Ram','vijji']
print("in operator:",'Faheem' in names)         #in operator: True
print(" not in operator:",'Raji' not in names)  # not in operator: False


'''6.Identity Operators'''

a=[1,2,3,4,5]
b=[1,2,3,4,5]
print("a is b:",a is b)  #a is b: False  '''here even it is the same value they are stored in diff locations thats why it give false'''
print("id(a)",id(a))     #id(a) 1702630191104
print("id(b):",id(b))    #id(b): 1702629763904
c=b
print("b is c:",b is c)  #is c: True   '''here c is assigned to b so that same location it is gng to store thats why it gives true'''
print("id(c):",id(c))    #id(c): 1702629763904
print("b is not c:",b is not c) #b is not c: False


'''7.Bitwise Operators
1-000
2-010
3-011
4-100
5-101
6-110
7-111---
    And(&)--returns 1 if both are ,otherwise 0
    or(|)--returns 1 if any one is , otherwise 0
    Xor(^)--returns 1if both ar diff,if they are same returns 0
    Not(~)==  if a is given, then -(a+1)
    left shift(<<)--shifts specific no.of times to left
    Right shift(>>)--shifts specific no.of times to left'''
a=6
b=7
print("a and(&) b :",a&b)  #a and(&) b : 6
print("a or(|) b :",a|b)   #a or(|) b : 7
print("a xor(^) b:",a^b)   #a xor(^) b: 1
print(" not(~) a:",~a)     #not(~) a: -7
print("a Left shift(<<)3",a<<3)  #a Left shift(<<)3 48
print("b Right shift(>>)3",a>>3) #b Right shift(>>)3 0











             





















