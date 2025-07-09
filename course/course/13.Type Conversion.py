#=====Type conversion======
a=10
print(str(a))  #10
print(float(a))#10.0
print(bool(a)) #True
print(complex(a)) #(10+0j)
'''we cant convert int into list,tuple,set,dict
-bcz they are collection of elements'''

b=12.1
print(str(b))  #12.1 
print(int(b))  #12
print(complex(b))#(12.1+0j)
print(bool(b)) #True
'''similarly we cant convert float into list,tuple,set,dict
-bcz they are collection of elements'''

c="raji"
print(list(c)) #['r', 'a', 'j', 'i']
print(tuple(c))#('r', 'a', 'j', 'i')
print(set(c))  #{'i', 'j', 'a', 'r'}
print(bool(c)) #True

r="10"
print(int(r))  #10--we can covert only nums into str cant convert alphabetics
'''we cant convert str into int,float,complex and dict'''

c=["a","b","c","d","e"]
print("".join(c))#abcde  "if we dont give quotes we cant convert list into str"
print(tuple(c))  #('a', 'b', 'c', 'd', 'e')
print(set(c))    #{'e', 'b', 'c', 'd', 'a'}
print(bool(c))   #True
'''we cant convert list into dict,int,float,complex,dict'''

c=("r","a","j","i","a","a","r","e")
print(" ".join(c))  #r a j i a a r e
print(list(c))  #['r', 'a', 'j', 'i', 'a', 'a', 'r', 'e']
print(set(c))  #{'j', 'r', 'e', 'a', 'i'}
print(bool(c)) #True
d=[("name","ram"),("relation","father"),("age","29")]  
print(dict(d))  #{'name': 'ram', 'relation': 'father', 'age': '29'}
'''we can convert tuple into dict by using tuples inside the list[()()], we cant convert tuple into int,float'''

f={"name":"faheem","relation":"bestie","ht":6.5}
print(list(f))  #['name', 'relation', 'ht']
print(tuple(f)) #('name', 'relation', 'ht')
print(set(f))   #{'relation', 'ht', 'name'}
print(str(f))   #{'name': 'faheem', 'relation': 'bestie', 'ht': 6.5}
print(bool(f))  #True









