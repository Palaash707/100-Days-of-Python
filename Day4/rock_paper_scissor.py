import random as r

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""
scissor = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
paper = """
        ______
    ---'    ___)______
            __________)
            ____________)
            ___________)
    ---._____________)
    """
image = [rock, scissor, paper]
print("Press 0 for Rock, 1 for Scissor, 2 for Paper")

a = int(input("Enter your choice: "))
print("You chose:")
print(image[a], "\n")

c = r.randint(0, 2)
print("Computer chose:")
print(image[c])

if a == c:
    print("DRAW")
elif (a == 0 and c == 1) or (a == 1 and c == 2) or (a == 2 and c == 0):
    print("YOU WIN")
else:
    print("YOU LOSE")
