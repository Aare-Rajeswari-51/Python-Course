Python 3.13.5 (tags/v3.13.5:6cb20a2, Jun 11 2025, 16:15:46) [MSC v.1943 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.


s={1,2.3,"raji"}    #set
s
{1, 'raji', 2.3}


>>> d={1:raji,2:'ram',3:2.5}    #dict(explanation given below why the error came)
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    d={1:raji,2:'ram',3:2.5}
NameError: name 'raji' is not defined
>>> d={2:10,3:'15'}
>>> d
{2: 10, 3: '15'}


>>> s={2,3,4,5,1,,99,8}
SyntaxError: invalid syntax

>>> s={2,3,9,8,7,6,5}  #here in "set" we are given descending order but "it automatically  prints  in ascending order".
>>> s
{2, 3, 5, 6, 7, 8, 9}


>>> l=[9,8,7,76,4,3,2] #here in "list" we are given in descending order it gives the same output so "it doesn't need an order".  
>>> l
[9, 8, 7, 76, 4, 3, 2]


>>> i1=[1,2,3,4,4,4,5] #here also we have given same nums multiple times but it gives the same in output so "repetition also allowed in list"
>>> i1
[1, 2, 3, 4, 4, 4, 5]


>>> t=(1,2,3,4,5,67,7,7,7,8)#similarly in "tuple-repetition allowed&doesnt need any order".
>>> t
(1, 2, 3, 4, 5, 67, 7, 7, 7, 8)


>>> #List=it can be duplicate;collection of elements;can add,remove,del....;(Mutable-can change)==[ ]
>>> 
>>> 
>>> #tuple=it can be duplicate;collection of elements,cant change,...(immutable-cant change)==( )
>>> 
>>> 
>>> #dictionary= keys-unique;valus-can be duplicate..=={ }
>>> 
>>> 
>>> #set=during output they are becoming ordered even after giving unordered during program;;has to be unique{ }
>>> 
>>> 
>>> s={1,1,1,2,8,6,4,3,9} #here we have given repetition but it prints output in ascending order with unique nums(ignoring repetitive nums)
>>> s
{1, 2, 3, 4, 6, 8, 9}
>>> 
>>> 
>>> '''dictionary= if u want to give string  in 'value' u have to declare it before,
 if u wont declare it then it will show error as above'''


'''list,tuple=it willl show the output what u exactly written  input whatever u give like duplicates,unordered etc...,,
but in set it will give automatically arrange in ascending order plus remove duplicates in ouput'''
>>> 
>>> 
>>> 
>>> 
>>> 
