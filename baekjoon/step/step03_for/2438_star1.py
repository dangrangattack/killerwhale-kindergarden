"""문제
첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제

입력
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.

출력
첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다."""

N = int(input())

# 점프투파이썬 예제 참고

for i in range(1, N + 1):
    for _ in range(i):
        print("*", end="")
    print()

"""while문 사용버전 

n = int(input())


i = 1                 # 줄 번호
while i <= n:
줄을 1번부터 n까지 찍겠다
    j = 1             # 별 개수
    while j <= i:
    별을 i개 찍겠다 
        print("*", end="")
        j += 1
        하나찍고 갯수증가 
    print()
    i += 1

    while j <= i:      # 조건: 몇 번 반복할지
    print("*")     # 행동: 별 하나 찍기
    j += 1         # 상태 변화: 횟수 증가


"""