# for i in range(1, 8):
#     for j in range(7-i):
#         print(" ", end="")
#     for j in range(i*2-1):
#         print("*", end="")
#     print("")

x = int(input())

for i in range(1, x+1):
    for j in range(x-i):
        print(" ", end="")
    for j in range(i*2-1):
        print("*", end="")
    print("")

