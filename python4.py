a=[2,4,7,5,9,8]
print(a)
for i in a:
 if(i%2==0):
   print(i*10)
 else:
    print(i+10)


#print palindromes
b=[12,45,66,777,89]
print(b)
for i in b:
   if(str(i)[::-1]==str(i)):
      print(i)
         
#print duplicates and uniques
l=[1,3,5,6,2,7,4,3,9,8,10]
print(l)
d=[]
u=[]
for i in l:
    if(l.count(i)==1):
       u.append(i)
    else:
      d.append(i)
print("duplicates:",end="")
print(sorted(set(d)))
print("uniques:",end="")
print(sorted(set(u)))
