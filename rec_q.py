i=0
def num():
    global i
    if i<=10:
        i+=1
        print(i)
        num()
num()
