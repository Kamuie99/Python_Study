x, y = map(float, input("점의 좌표 x, y를 입력하시오: ").split()) # x좌표값, y좌표값 저장

if (x>0 and y>0):
    print("1사분면에 있음")
elif (x<0 and y>0):
    print("2사분면에 있음")
elif (x<0 and y<0):
    print("3사분면에 있음")
elif (x>0 and y<0):
    print("4사분면에 있음")
else:
    print("어느 분면에도 있지 않음")

