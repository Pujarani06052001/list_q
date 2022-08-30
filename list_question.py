

# ascending order

array=[23,10,30,50,5,1]
i=0
while i<len(array):
    j=0
    while j<len(array):
        if array[i]<array[j]:
            array[i],array[j]=array[j],array[i]
        j+=1
    i+=1
print(array)


# descending order

array=[23,10,30,50,5,1]
i=0
while i<len(array):
    j=0
    while j<len(array):
        if array[i]>array[j]:
            array[i],array[j]=array[j],array[i]
        j+=1
    i+=1
print(array)



# min number

a=[23,10,30,50,5,1]
i=0
min=a[i]
while i<len(a):
    if a[i]<min:
        min=a[i]
    i+=1
print(min)


# max number

a=[23,10,30,50,5,1]
i=0
max=0
while i<len(a):
    if a[i]>max:
        max=a[i]
    i+=1
print(max)