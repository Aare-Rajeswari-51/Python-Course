'''strings.methods'''
#1.==Case conversion methods==
a="I need sometime to set here"
print("converting all letters into Uppercases:",a.upper())
print("converting all letters into lowercases:",a.lower())
print("Capitalizing the first letter:",a.capitalize())
print("capitalizing the first letter of each word:",a.title())
print("swapping low->up,up->low:",a.swapcase())
b="ẞá"
c="û"
d="ámûñø"
e="ẞ"
print("converting special chars to lower1:",b.casefold())
print("converting special chars to lower2:",c.casefold())
print("converting special chars to lower3:",d.casefold())
print("converting special chars to lower4:",e.casefold())

#converting all letters into Uppercases: I NEED SOMETIME TO SET HERE
#converting all letters into lowercases: i need sometime to set here
#Capitalizing the first letter: I need sometime to set here
#capitalizing the first letter of each word: I Need Sometime To Set Here
#swapping low->up,up->low: i NEED SOMETIME TO SET HERE
#converting special chars to lower1: ssá
#converting special chars to lower2: û
#converting special chars to lower3: ámûñø
#converting special chars to lower4: ss


#2.==Alignment&Formatting methods==
'''center(width,fillchar)
ljust(width,fillchar)
rjust(width,fillchar)
zfill(width)
format()
format_map(mapping)'''
a="maddineni naveena"
print("centers the string within width:",a.center(40,"="))
print("left-aligns the string within width:",a.ljust(40,"*"))  #==we have to use single operator only if we use 2 0r 3 operators then it will shows an error
print("Right-aligns the string within width:",a.rjust(40,"#"))
print("fill the string with zeroes on the left:",'52'.zfill(6))
print("fill the string with zeroes on the left:",'raji'.zfill(8))
print("Format strings dynamically:",'Name:{}, Age:{}'.format("raji",20))
print("Formats using dictionary:",'{name} is {age}'.format_map({"name":'Navi', "age":21}))#== here we have to use{} otherwise it will shows error bcz dict={}


#centers the string within width: ===========maddineni naveena============
#left-aligns the string within width: maddineni naveena***********************
'''if i want every string ends with same like
   #for example:   Name   :
                   Age    :
                   Gender :    like this we want correct allignment then we can use this'''
#Right-aligns the string within width: #######################maddineni naveena
'''if i want every string ends with same like
   #for example:   '  Name:
                      Age:
                   'Gender:    like this we want correct allignment then we can use this'''

#fill the string with zeroes on the left: 000052
#fill the string with zeroes on the left: 0000raji
#Format strings dynamically: Name:raji, Age:20
#Formats using dictionary: Navi is 21

#3.==Search&Find methods==
'''
  "find"=for suppose if we have given a char i.e, not in str then we get "-1".
   index=for suppose if we have given a char i.e, not in str then we get "error". '''

a="Vijayalakshmi"
print("finding the index of first occurance:",a.find("a"))
print("finding the index of last occurance:",a.rfind("a"))  #if we dont give quotes then it will give 0 
print("finding the index of last occurance:",a.find("r"))
print("Index of first occurance:",a.index("i"))
print("Index of last occurance:",a.rindex("i"))
print("Counting how many times 'a'(sub)appears:",a.count("a"))


#finding the index of first occurance: 3
#finding the index of last occurance: 7
#finding the index of last occurance: -1
#Index of first occurance: 1
#Index of last occurance: 12
#Counting how many times 'a'(sub)appears: 3


b="sai pallavi is a dancer"
print("finding the index of multiple parameters:",b.find("sai"))
print("finding the index of multiple parameters:",b.find("pallavi"))
print("finding the index of multiple parameters:",b.find("dancer"))

#finding the index of multiple parameters: 0
#finding the index of multiple parameters: 4
#finding the index of multiple parameters: 17



#4.==String Testing Methods(Boolean Results)==
'''
isalpha()=it doesn,t take any parameters,if we give any parameters then it will throws an error
           if there is any space in ur string with all alphabetics then it will give false
           for ex:: "raji aaare".isalpha()==false
                      "rajiaare".isalpha()==True'''
a="Saipallavi"
print(a.startswith("S"))
print("starts with:",a.startswith("sai"))
print(a.endswith("a"))
print("checking if all characters are alphabets:",a.isalpha())   
print("checking if all characters are alphanumeric:",a.isalnum())
print("checking if all characters are lower:",a.islower())   
print("checking if all characters are upper:",a.isupper())
print(a.isspace())  #False
print("d a n c e".isspace()) #False 
print(" ".isspace())  #True
print(a.istitle())    #True
print("checking if a string is python identifier:",a.isidentifier())

#True
#False
#False
#checking if all characters are alphabets: True
#checking if all characters are alphanumeric: True
#checking if all characters are lower: False
#checking if all characters are upper: False
#False
#False
#True
#True
#checking if a string is python identifier: True

#5.==Replace&Modify methods==
'''
replace(old,new)
translate(table)
   #print("translate:",a.translate(str.maketrans("kedarnath","Bali")))==gives error bcz it should have equal length
   if we map sai->ram
   then  s--r
         a--a(no change)
         i--m   these way only they will replaced wherever 'i' there it replaced with 'm'..like this...

maketrans()'''

a="I want to visit kedarnath"
print("Replacing1:",a.replace('a','*'))
print("Replacing2:",a.replace("kedarnath","paris"))
print("translate1:",a.translate(str.maketrans("i","@")))
print("translate2:",a.translate(str.maketrans("want","hate")))
print(a.maketrans("a","#"))  #prints ascii value
print(a.maketrans("abc","#@^")) 

#checking if a string is python identifier: True
#Replacing1: I w*nt to visit ked*rn*th
#Replacing2: I want to visit paris
#translate1: I want to v@s@t kedarnath
#translate2: I hate eo visie kedartaeh
#{97: 35}
#{97: 35, 98: 64, 99: 94}


#6.==splitting&Joining methods==

a="Saipallavi is the heroine in Thandel movie"
print("spliiting with single letter from start:",a.split("a"))
print("spliiting with single letter in reverse:",a.rsplit("a"))
print("splitting with multi letters from start:",a.split("th"))
print("splitting with multi letters in reverse:",a.rsplit("th"))
print("spliiting lines:",a.splitlines("a"))


#spliiting with single letter from start: ['S', 'ip', 'll', 'vi is the heroine in Th', 'ndel movie']
#spliiting with single letter in reverse: ['S', 'ip', 'll', 'vi is the heroine in Th', 'ndel movie']
#splitting with multi letters from start: ['Saipallavi is ', 'e heroine in Thandel movie']
#splitting with multi letters in reverse: ['Saipallavi is ', 'e heroine in Thandel movie']
#spliiting lines: ['Saipallavi is the heroine in Thandel movie']


b="raji@ram@vijji@aare"
print(b.split("@"))   #['raji', 'ram', 'vijji', 'aare']
print(b.rsplit("i"))  #['raj', '@ram@v', 'jj', '@aare']

#splitlines
s=''' i am
    not
      interested'''
print("splitting the lines:",s.splitlines())   #splitting the lines: [' i am', '    not', '      interested']
print("joining the list:",' '.join(["raji","navi"]))  #joining the list: raji navi
print("joining the tuple:",' '.join(("hyd","is","not","good","enough")))  #joining the tuple: hyd is not good enough

#join(string)
a="I am not happy"
print('#'.join(a))  #==#I# #a#m# #n#o#t# #h#a#p#p#y
print(' this '.join(a))  #I this   this a this m this   this n this o this t this   this h this a this p this p this y
#==join==it is used to convert list,tuple into string
#list
c=["I","miss","my","dad"]  
print("@".join(c))  ##I@miss@my@dad
print(" ".join(c))  #I miss my dad
#tuple
d=("she","is","sick")
print("%".join(d))   #she%is%sick

#set
d={"she","is","sick"}
print("#".join(d))  #== is#she#sick==it is set thats why it always prints in a ASCII value based


#==partition==
a="I@miss@my@something"
print(a.partition("@"))  #('I', '@', 'miss@my@something')
print(a.rpartition("@")) #('I@miss@my', '@', 'something')


#7.===whitespace&Trimming===
#strip=it is used to remove white spaces on both left&right but not in the middle of the string
#lstrp=it is used to remove white spaces on both left but not in the middle of the string,,rstrip removes right side
a="      she is a good dancer      "
print(a.strip())  #she is a good dancer     
print(a.lstrip()) #she is a good dancer
print(a.rstrip()) #      she is a good dancer

#8.===Encoding&Decoding methods===
#encode=mostly used to convert dat into bytes format for storing purpose or if we want to pass inf through layers websites at that time we use this

a="Rajeswari"
print(a.encode())  #b'Rajeswari'
print(b'Rajeswari'.decode())  #Rajeswari

b="Hello नमते你好 café 🙂"
print(b.encode())  #b'Hello \xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xa4\xe0\xa5\x87\xe4\xbd\xa0\xe5\xa5\xbd caf\xc3\xa9 \xf0\x9f\x99\x82'
print(b'Hello \xe0\xa4\xa8\xe0\xa4\xae\xe0\xa4\xa4\xe0\xa5\x87\xe4\xbd\xa0\xe5\xa5\xbd caf\xc3\xa9 \xf0\x9f\x99\x82'

.decode())    #Hello नमते你好 café 🙂

















    










