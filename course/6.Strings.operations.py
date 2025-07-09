'''Strings'''
#String Operations
#sequence of characters enclosed in quotes(immutable)

'''1.operations'''
#==concatenation(+)==used for combining two strings
a="Raji"
print("Concatenation(+)1:",a+"Ram")  #Concatenation(+)1: RajiRam


x="lemon"
y="Rice"
print("Concatenation(+)2:",x+y)   #Concatenation(+)2: lemonRice



#==Repetition(*)== used for no.0f times repetition
a="Apple"
print("Repetition1(*):",a*15)  #Repetition1(*): AppleAppleAppleAppleAppleAppleAppleAppleAppleAppleAppleAppleAppleAppleApple

print("Repetition2(without using var):",'R'*10)  #Repetition2(without using var): RRRRRRRRRR

a="Raji "
print(a*8)  #Raji Raji Raji Raji Raji Raji Raji Raji (if we want space after every repetition then we have to give space in vaiable like above)



#==Indexing==we have to use square braces only ,if we use paranthesis it will give error
'''
-9 -8 -7 -6 -5 -4 -3 -2 -1 (negative indexing== "reverse")
R  A  J  E  S  W  A  R  I
0  1  2  3  4  5  6  7  8  (positive indexing)'''

a="Rajeswari"
print("positive indexing:",a[1])   #positive indexing: a
print("Negative indexing:",a[-5])  #Negative indexing: s



#==slicing== if we want specific part of a string then we use it
'''syntax==[start,stop+1,step]

#if we give neg slicing in ascending order[-15:-21]then it wont give anything
  so in neg slicing it hAS to be in descending order like[-21:-15]

  if we want to print in reverse order for specific seq in neg slicing then we have to give step value as -1


-22-21-20-19-18-17-16-15-14-13-12-11-10-9 -8 -7 -6 -5 -4 -3 -2 -1
M  U  D  A  M  S  H  A  I  K  H   A  B  D  U  L  F  A  H  E  E  M    
0  1  2  3  4  5  6  7  8  9  10  11 12 13 14 15 16 17 18 19 20 21
'''

a="Mudamshaikhabdulfaheem"
print(a[0:5])   #Mudam
print(a[16:22]) #faheem
print(a[1:22:2])#uasakadlaem==(if we want odd nums)
print(a[0:22:2])#Mdmhihbufhe==(if we want even nums)
print(a[:11])   #Mudamshaikh==(if we want from starting to 10th position)
print(a[5:])    #shaikhabdulfaheem==(if we want from 5th position to ending)
print(a[::-1])  #meehafludbahkiahsmaduM==(reversing a string)
print(a[-21:-11])  #udamshaikh==(if we want from 21th position to 10th position )
print(a[-21:-15])  #udamsh
print(a[-1:-21:-2])#mealdakasa==(negative slicing from 21th position[i.e starting position] to end with step 2[alt nums])
print(a[-1:-12:-1]) #meehafludba==(if we want to print in reverse order for specific seq in neg slicing then we have to give step value as -1)



#==membership==checking if a substring exists or not
a="Naveena"
print("a" in a) #True
print("raji" in a) #False
print("Nav" not in a) #False
















