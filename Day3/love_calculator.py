print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
a=name1+name2
b=a.lower()
b1=b.count("t")
b2=b.count("r")
b3=b.count("u")
b4=b.count("e")
b_add=b1+b2+b3+b4

b6=b.count("l")
b7=b.count("o")
b8=b.count("v")
b9=b.count("e")
b_add_1=b6+b7+b8+b9

c=str(b_add)+str(b_add_1)
if int(c)<10 or int(c)>90:
    print(f"Your score is {c}, you go together like coke and mentos.")
elif(40<int(c)<50):
    print(f"Your score is {c}, you are alright together.")
else:
    print(f"Your score is {c}.")

