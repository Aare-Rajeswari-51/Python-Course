#====Dictionary====
#creating empty dict
a=dict()
print(a)  #{}

r={"name":"raji","fav color":"white","age":20,"gen":"female"}
print(r.keys())   #dict_keys(['name', 'fav color', 'age', 'gen'])
print(r.values()) #dict_values(['raji', 'white', 20, 'female'])
print(r.items())  #dict_items([('name', 'raji'), ('fav color', 'white'), ('age', 20), ('gen', 'female')])

#===Accessing values====
print(r["fav color"])  #white
'''if we use r[key]==if the key is not there thn it will throws an error thats why we use .get()'''

#using get()
''' .get()==if in our program we dont want to rise an error if the search element is not there,
             then we can use get method
             
    if .get("age")==if age is there then it will give "age" - value
    if .get("age","age is not declared")==then also it will give "age"--value ignores the last msg
    
             if we give .get("mail")=if age is not there in dict the =n it just leaves doesnt rise an error
             .get("mail","mail is not declared")== if age is not there then it will give "mail is not declared"
             but it wont add it in dictionary jst give that msg
'''
print(r.get("age"))   #20
print(r.get("course","course is not declared")) #course is not declared 
print(r.get("batch","30")) #30

#====Adding&Updating items=====
a={"name":"ram","relation":"father","age":49,"occupation":"farmer"}
a["status"]="Married"
print(a)   #{'name': 'ram', 'relation': 'father', 'age': 49, 'occupation': 'farmer', 'status': 'Married'}

#====Removing items=====
#pop
print(a.pop("occupation"))  #farmer  ==we have to give 'key' not 'index'

#popitem()
print(a.popitem())  #('status', 'Married')  ==removes last item

#del
del a["name"]
print(a)   #{'relation': 'father', 'age': 49}

#clear()
a.clear()
print(a)  #{}


#====dict built-in functions====
#update
a={"fav color":"white","fav vehicle":"Thar","fav place":"paris"}
a.update({"fav choc":"Roastalmond","fav ice-cream":"Chocolate","fav international place":"paris"})
print(a)    #{'fav color': 'white', 'fav vehicle': 'Thar', 'fav place': 'paris', 'fav choc': 'Roastalmond', 'fav ice-cream': 'Chocolate', 'fav international place': 'paris'}

''' .update()== if we want to add 2 or more elements then we can use this 
'''

#set default
a.setdefault("fav person","nanna")
print(a)
#{'fav color': 'white', 'fav vehicle': 'Thar', 'fav place': 'paris', 'fav choc': 'Roastalmond', 'fav ice-cream': 'Chocolate', 'fav international place': 'paris', 'fav person': 'nanna'}
''' .setdefault()== it will check whether the "key" is present (or) not ,if it is there then it will give its value
                     otherwise it will add that into dict

    .get()--it wont add in the dict,just give value
    .setdefault()--it will add in the dict                     
'''
print(a.get("fav relation","brother&Sister")) #brother&Sister


a={"name":"vijji","relation":"mother","age":39,"gen":"female"}
print(len(a))  #4
print(max(a))  #relation
print(min(a))  #age
print(sorted(a)) #['age', 'gen', 'name', 'relation']


#=====Nested Dictionary=====
a={"a":1,"b":2,"c":3,"d":4}
print(a)   #{'a': 1, 'b': 2, 'c': 3, 'd': 4}

a["floats"]={"r":5.3,"s":6.2,"t":10.5,"u":11.8}
print(a)   #{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'floats': {'r': 5.3, 's': 6.2, 't': 10.5, 'u': 11.8}}











