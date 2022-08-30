n=int(input("enter a no::"))
r=n
a=1
c=0
while a<=n:
	if n%a==0:
			c=c+1
	a=a+1		
if c==2:
	print("this is praime num",r)
else:
	print("prime no: ",r)