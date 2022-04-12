# 사용자로부터 나이를 입력받아 20살 이상이면 "Adult" 10살 이상 20살 미만 "Youth"
# 10살 미만이면 "Kid"를 출력하는 프로그램 작성

age = int(input("나이를 입력하시오 : "))

if age>=20:
    print("Adult")
elif 10<=age<20:
    print("Youth")
else:
    print("Kid")
