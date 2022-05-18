bill=float(input("Enter the bill amount: $"))
tip=int(input("Enter percentage of tip u would like to give 10,12 or 15? :"))
s=int(input("How many people to split the bill: "))
if tip==10:
    tot_bill=bill+(bill/10)
elif tip==12:
    tot_bill=bill+((bill*12)/100)
else:
    tot_bill=bill+((bill*15)/100)
a=round(tot_bill/s,2)

print("Each person should pay:$",a)