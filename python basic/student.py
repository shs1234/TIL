print("태어난 연도를 입력하세요 : ")
birth_year = int(input())
age2 = 2020-birth_year+1
if age2<=26 and age2>=20 :
    print("대학생")
elif age2<20 and age2>=17 :
    print("고등학생")
elif age2<17 and age2>=14 :
    print("중학생")
elif age2<14 and age2>=8 :
    print("초등학생")
else :
    print("학생이 아닙니다")
