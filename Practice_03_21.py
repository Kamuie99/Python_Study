N = int(input("숫자를 입력하세요 : "))
P = 0

for i in range(2, N):
    if N % i ==0:
        P = 1

if P == 0:
    print("{0}는 소수입니다.".format(N))
else:
    print("{0}는 소수가 아닙니다.".format(N))