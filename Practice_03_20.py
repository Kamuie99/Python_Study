N = int(input("숫자를 입력하세요 : "))
for i in range(1, N+1):
    for j in range(N-i):
        print(' ', end="")
    for j in range(i):
        print('*', end="")
    print('')