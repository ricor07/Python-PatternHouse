n = int(input("Enter the number of rows: "))
spaces = 1
counter = n + 4
for i in range(1, n + 1):
    b = i
    for k in range(0, spaces):
        print(" ", end=" ")
    for j in range(0, counter):
        print("*", end=" ")
    counter = counter - 2
    spaces = spaces + 1
    print()
