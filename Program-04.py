#Wap in python if the given list elements repeated then print them twice otherwise print them only once.
L= [2,3,1,1,4,4,4,6,6,6,6,6,7,7,7,8]
L.sort()
len1 =len(L)
a=[]
for i in range(0,len1):
    if L.count(i)>1:
            a.append(i)
            a.append(i)
    elif L.count(i)==1:
        a.append(i)
    
print(a)                


