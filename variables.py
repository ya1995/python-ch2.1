# 변수 이름은 문자, 숫자, _로 구성해야한다.
import keyword

friend = 1
a = 10
my_name = '김영애'
_your_name = '둘리'
member1 = '도우너'

# 에러
# $friend = 2
# a!    언더바 빼고 특수문자 안됨
# 1abc = 10

# 에러 : 예약어는 사용할 수 없다
# def = 10

print(keyword.kwlist)

# 한글이름의 변수도 가능하다
가격1 = 2000
print(가격1 - 200)

