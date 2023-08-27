row1 = ["0", "0", "0"]
row2 = ["0", "0", "0"]
row3 = ["0", "0", "0"]

map = [row1, row2, row3]

print(f"{row1}\n{row2}\n{row3}")

a = input("enter position: ")  # 13
ver = int(a[1]) - 1
hor = int(a[0]) - 1

map[hor][ver] = "1"
print(f"{row1}\n{row2}\n{row3}")
