"""문제
두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.

입력
첫째 줄에 테스트 케이스의 개수 T가 주어진다.

각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)

출력
각 테스트 케이스마다 A+B를 출력한다."""

T = int(input())

#개수 T가 주어진 후 이를 반복
for _ in range(T):
    a, b = map(int, input().split())
    print(a+b)

#For 반복변수 in 반복범위
# for _ in range(T) : 아래 코드를 T번 시행해라
# a, b = map(int, input().split()) : 매반복시 입력처리 읽고 - 쪼개어 - 정수처리
# a+b : 출력하라