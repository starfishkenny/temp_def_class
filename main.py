#main.py에서 calculation.py 정의한 함수 불러오기

import calculation as cal
a=3
b=4

def main():
    print('안녕하세요, main()입니다')
    print('a+b=', cal.plus(a,b))
    print('a-b=',cal.subtract(a,b))
    print('a*b=',cal.multiple(a,b))
if __name__ == '__main__':
    main()


# pandas -> pd 처럼
# 주피터 노트북 -> 1차적