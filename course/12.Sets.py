#=====sets=====unordered,mutable ,unique elements
#creating empty
a=set()
print(a)  #set()
b={}
print(b) #{}

c={1,1,2,2,3,9,9,97,7,6,5,4,3,15}
print(c)  #{1, 2, 3, 4, 5, 6, 7, 97, 9, 15}

'''can add mutable data types but not immutable data types like list(),dict()
it will show error if u add'''
e={1,5.7,3+4j}

#===Set Operations=====
'''union(|),.union()=combining both sets
intersection(&)=common elements in both the sets
difference(-)=if a-b then it is going to del the "b" set elements in "a" set'''
a={1,2,3,4}
b={3,4,5,6,7}
print(a|b) #{1, 2, 3, 4, 5, 6, 7}
print(a&b) #{3, 4}
print(a-b) #{1, 2}
print(a.symmetric_difference(b)) #{1, 2, 5, 6, 7}

a={1,2,3,4,5,6}
b={2,3}
print(a.issubset(b))  #False  
print(a.issuperset(b)) #True 
print(a.isdisjoint(b)) #False


c={3,4,5,6,7,8,9}
d={1,2,3,15,11,17,18}
c.intersection_update(d)
print(c)  #{3}
c.difference_update(d)
print(c)  #set()
c.symmetric_difference_update(d)
print(c)  #{1, 2, 3, 11, 15, 17, 18}
print(len(a)) #6
print(max(a)) #6
print(min(a)) #1



