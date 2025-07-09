#===Creating Lists===
#using constructor
'''if we want to use constructor then we have to use
 it at the top of the program ,otherwise it will take it as function and
  rise an error like it is not callable'''
l=list()
print(l)   #[]  ==empty list

l1=[1,2,3,4,5,6]
print(l1)  #[1, 2, 3, 4, 5, 6]  ==with elements

#===Nested List===
a=[[1,2,3],["a","b","c"],[1.2,3.6,7.8]]
print(a)  #[[1, 2, 3], ['a', 'b', 'c'], [1.2, 3.6, 7.8]]


#====Accessing Elements using indexing&slicing====
#indexing
a=["a","raji","m","navi","ms","faheem"]   
print(a[3])   #navi
print(a[-4])  #m

#Slicing
print(a[2:4]) #['m', 'navi']
print(a[4:])  #['ms', 'faheem']  ==returns from 4th position to end of the list
print(a[-5::-1])  #['raji', 'a']  ==returns from -5th position to last position(neg indexing) in reverse order


#===Modifying list====
#=changing elements=
a=[10,20,30,40,50]
print(a)  #[10, 20, 30, 40, 50]
a[2]=15
print(a)  #[10, 20, 15, 40, 50]  ==at index 2 changing the num 30 to 15

#=Adding elements=
'''  .append()==appending at the end-can add only one element
     .insert(index,element)==inserting an element at particular index position
     .extend([]) #=can add more elements using extend but we have to use [],otherwise it will throws an error
'''
a=[1,2,3,4,5]
print(a)   #[1, 2, 3, 4, 5]  ==actual list
a.append(6)
print(a)   #[1, 2, 3, 4, 5, 6]  
a.insert(3,4.5)
print(a)   #[1, 2, 3, 4.5, 4, 5, 6]  
a.extend([7.5,"raji",[7,8,9],(1,2,3),{6,78,90},{"name":"ram","relation":"father"}])  
print(a)    #[1, 2, 3, 4.5, 4, 5, 6, 7.5, 'raji', [7, 8, 9], (1, 2, 3), {78, 90, 6}, {'name': 'ram', 'relation': 'father'}]


#=Removing elements=

'''   .remove()==removes particular element
      .pop(2)==removes element at 2nd index(at particular index)
      .pop()==removeslast element
      del a[1]==removes element at particular index(1 index)
'''
a=["I","want","to","visit","Araku","paris","maldives"]
print(a)  #['I', 'want', 'to', 'visit', 'Araku', 'paris', 'maldives'] ==actual list
a.remove("Araku")
print(a)  #['I', 'want', 'to', 'visit', 'paris', 'maldives']  
a.pop(3)
print(a) #['I', 'want', 'to', 'paris', 'maldives']
a.pop()
print(a)  #['I', 'want', 'to', 'paris']
del a[1]
print(a)   #['I', 'to', 'paris']

#====List methods====
'''
append(),extend(),insert(),remove(),pop(),clear(),index(),count(),sort(reverse=True),reverse(),copy()
.sort(reverse=True)=returns the reverse order of the list whatever they are
   .clear()==removes all the elements in list-returns empty list
   .index()=returns index position of which element we have given(we have to give element here to get index ,,we cant give index)
   .reverse()==returns reverse order of the string
   .copy()==it is used to copy the variaable(list) but cant change the real one(see below)'''

a=["reddy","hemanth","sudheer","suma","hemanth","manu","pandu","yashu"]
print(a)   #['reddy', 'hemanth', 'sudheer', 'suma', 'hemanth', 'manu', 'pandu', 'yashu']
a.sort(reverse=True)
print(a)   #['yashu', 'suma', 'sudheer', 'reddy', 'pandu', 'manu', 'hemanth', 'hemanth']
print(a.index("suma"))  #1
print(a.count("hemanth")) #2
print(a.count("h")) #0
a.reverse()
print(a) #['hemanth', 'hemanth', 'manu', 'pandu', 'reddy', 'sudheer', 'suma', 'yashu']

b=a.copy()
print(b)  #['hemanth', 'hemanth', 'manu', 'pandu', 'reddy', 'sudheer', 'suma', 'yashu']  ==copying 'a'
b.append("Aadi")
print(b)  #['hemanth', 'hemanth', 'manu', 'pandu', 'reddy', 'sudheer', 'suma', 'yashu', 'Aadi']
print(a)  #['hemanth', 'hemanth', 'manu', 'pandu', 'reddy', 'sudheer', 'suma', 'yashu']  ==it doesn't change even after b(duplicate one) changes(original list)
a.clear()
print(a)  #[]


a=["hemanth","ram","vijji","aadi","Aadi"]
a.sort(reverse=False) 
print(a)   #['Aadi', 'aadi', 'hemanth', 'ram', 'vijji']   ==it is used for ascending order


#====sorting&reversing lists====

a=["i","just","want","a","job"]
a.sort()
print(a)  #['a', 'i', 'job', 'just', 'want']

b=[98,9.4,1,5,8,5,3,345]
sorted(b)
print(b)  #[98, 9.4, 1, 5, 8, 5, 3, 345]



print(max(b))  #345
print(min(b))   #1


#==sum==
r=[5,6,2,9,15,11,56,37,82]
print(sum(r))  #223  ==returns whole list sum
print(sum(r[3:7]))  #91  ==when we want particular elements sum  then we use slicing
#==len==
print(len(r))  #9
print(any(r))  #True  ==atleast one element has to be TRUE
print(all(r))  #True  ==all elements should be TRUE

f=[0,1,2,3,4,5]
print(any(f))  #True
print(all(f))  #False  ==here '0' is there that's why it gives FALSE bcz in 'all'==all elements should be true
 















