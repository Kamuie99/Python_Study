win = [2, 3, 9]
number = list(map(int, input("세 복권 번호를 입력하시오 : ").split()))

print(set(win) & set(number))
if set(win) & set(number) == win:
    print("상금 1억 원")
elif set(win) & set(number) == {2, 3} or set(win) & set(number) == {3, 9} or set(win) & set(number) == {2, 9}:
    print("상금 1천만 원")
elif set(win) & set(number) == {2} or set(win) & set(number) == {3} or set(win) & set(number) == {9}:
    print("상금 1만 원")
else:
    print("다음 기회에...")
