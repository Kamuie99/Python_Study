N = int(input("1에서 9까지의 수를 입력하세요: "))

while(True):
    if(1 > N or 9 < N):
        N = int(input("1에서 9까지의 수를 다시 입력하세요: "))
    else:
        break

if(1 <= N <= 9):
    for i in range(1, 10, 1):
        print("{0} * {1} = {2}".format(N, i, N*i))
else:
    print("1에서 9까지의 수를 입력하세요: ")