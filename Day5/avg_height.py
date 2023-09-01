# sum = 0
# l = [10, 20, 30, 40]
# for x in l:
#     sum += x                        # sum=sum+x
# print(sum // len(l))
# print(sum(l))

"""
l=[]
x=int(input("enter length of the list: "))
for i in range(x):
    a=int(input("enter number: "))
    l.append(a)
"""
l = [10, 20, 50, 40]
# m = l[0]
# for i in range(1, len(l) - 1):
#     if m < l[i]:
#         m = l[i]
# print(m)

l.sort()
print(l[-1])


# RA2111003010319
import RPi.GPIO as GPIO
