import random
guess_number=random.randint(1,100)
print("1~100사이의 숫자를 입력하세요")
for i in range(5):
    num=int(input())
    if num > guess_number:
        print("그 이하")
    elif num < guess_number:
        print("그 이상")
    else :
        print("정답입니다.")
