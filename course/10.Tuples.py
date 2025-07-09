#====Tuple====
#===creating empty list===
a=tuple()
print(a)  #()

implicit_tuple=1,"raji",5.1
print(implicit_tuple)  #(1, 'raji', 5.1)

#without giving paranthesis also we can create tuple
b=5,"ram",6.1
print(b)   #(5, 'ram', 6.1)

#===Accessing Elements===
#=Indexing=
a=(1,"vijji",3.2,5+7j,[1,2,3,4,5])
print(a[2])   #3.2
print(a[-4])  #vijji

#=slicing=
print(a[2:5])    #(3.2, (5+7j), [1, 2, 3, 4, 5])
print(a[:4])  #(1, 'vijji', 3.2, (5+7j))
print(a[::4]) #(1, [1, 2, 3, 4, 5])


#===operations on Tuple===
#=Concatenation(+)=
a=(1,2,3,4)
r=("i","love","Roastalmond","chocolate")
print(a+r)   #(1, 2, 3, 4, 'i', 'love', 'Roastalmond', 'chocolate')

#=repetition(*)=
print(r*2)   #('i', 'love', 'Roastalmond', 'chocolate', 'i', 'love', 'Roastalmond', 'chocolate')
print(a*0)   #()

#=Membership Testing==
print(1 in a)    #True
print("raji" in r) #False

#=tuple Unpacking=
raji,loves,paris,Switzerland=a  #even they are strings we cant give them in quotes
print(raji)  #1
print(paris) #3

#=====Tuple Methods====
x=("my","father","is","my","world")
print(len(x))   #5
print(len(x[1:4])) #3
print(x.index("is"))  #2
print(max(x))  #world
print(min(x))  #father

r=(1,2,4,5,6,7,8,9)
print(sum(r))  #42
print(sum(r[2:6]))  #22

y=[1,5,6,7,89,15]
print(y)  #[1, 5, 6, 7, 89, 15]
print(tuple(y))  #(1, 5, 6, 7, 89, 15)


#====Immutability&Tuple Behaviour====
'''we cant change the tuple but inside tuple when we have list or dict we can change it'''
#list
a=(1,2,3,"raji","ram",[5,"araku","bali",4.5])
print(a)
a[5].append("switzerland")  #=with the help of indexing we can append 
print(a)  #(1, 2, 3, 'raji', 'ram', [5, 'araku', 'bali', 4.5, 'switzerland'])


#dictionary
b=(1,5,15,"ice cream",{"name":"reddy","marital":"married"})
b[4].setdefault("age","20")
print(b)   #(1, 5, 15, 'ice cream', {'name': 'reddy', 'marital': 'married', 'age': '20'})




