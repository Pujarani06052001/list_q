sale=int(input("enter a shal:"))
cost=int(input("enter a cost::"))
if sale==cost:
	print("no frofit and no loss")
elif sale >cost:
	print("profit",sale-cost)
else:
	print("loss",cost-sale)