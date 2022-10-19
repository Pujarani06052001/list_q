a=[1,2,2,2,2, 4,42,1,8.2,8]
i=0
l=[]
while i<len(a):
    if a[i] not in l:
        l.append(a[i])
    i+=1
print(l)