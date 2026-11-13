for i in range(2):
    for j in range(3):
        print("*", end="")
    print()

for i in range(1,5):
    for j in range(i):
        print("* ", end="")
    print()

for i in range(3):
    for j in range(3):
        print("A ", end="")
    print()

for i in range(1, 3):
    for j in range(1, 4):
        print(i, j)

for i in range (1, 4):
    for j in range(1, 4):
        print(i, "*", j, "=", i*j)


print(list(range(5, 0, -2)))