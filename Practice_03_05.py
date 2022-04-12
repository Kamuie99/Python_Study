# 2개의 임의의 정수를 받아서 가장 작은수 부터 큰수까지 나열하는 프로그램 작성

a, b = map(int, input("두 정수를 입력하시오 : ").split())

if a >= b:
    print(a, b)
else:
    print(b, a)

