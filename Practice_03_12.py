x, y = map(int, input("점의 좌표 x, y를 입력하시오 : ").split())
if(( (x*x) + (y*y) ) ** 0.5 <= 5):
    print("원 안에 있음")
else:
    print("원 밖에 있음")
