name = str(input("Please enter your name: "))
up = 0
low = 0
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lower = "abcdefghijklmnopqrstuvwxyz"
for count in name:
    if count in upper:
        up+=1
    elif count in lower:
        low+=1
print("Lower case = "+ count)
print("Upper Case = "+ count)