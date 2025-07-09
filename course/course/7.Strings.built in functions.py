# String.Built-in Functions
'''==ord()==print("ASCII value of a(whole string):",ord(a))
    ==it wont gives whole string ascii value

    ==sorted()==
        it will give ascending order on the basis of ASCII value
        #for example if you give Rajeswari-then 'R' will the first one
        rajeswari-then 'a' will be the first one
          --bcz 'R' ascii value is less than 'a' ascii value'''

a="Rajeswari"
print("Length of the string:",len(a)) 
print("Minimum ascii value of the string:",min(a))
print("Maximum ascii value of the string:",max(a))
print("ASCII value of R:",ord("R"))  #cant take multiple parameters like "aje"
print("alphabet for ascii value(69):",chr(69))
print("Sorting the string(a):",sorted(a))

#Length of the string: 9
#Minimum ascii value of the string: R
#Maximum ascii value of the string: w
#ASCII value of R: 82
#alphabet for ascii value(65): E
#Sorting the string(a): ['R', 'a', 'a', 'e', 'i', 'j', 'r', 's', 'w']






