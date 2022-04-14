print("맛나 식당에 오신 것을 환영합니다. 메뉴는 다음과 같습니다.")
print("1) 햄버거")
print("2) 치킨")
print("3) 피자")
N = int(input("1에서 3까지 메뉴를 선택하세요 : "))
while(True):
    if(1 > N or 3 < N):
        N = int(input("메뉴를 다시 입력하세요: "))
    else:
        break

if(N==1):
    print("햄버거를 선택하였습니다.")
elif(N==2):
    print("치킨을 선택하였습니다.")
elif(N==3):
    print("피자를 선택하였습니다.")
else:
    print("오류가 발생하였습니다.")
