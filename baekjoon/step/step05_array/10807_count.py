"""총 N개의 정수가 주어졌을 때, 정수 v가 몇 개인지 구하는 프로그램을 작성하시오.

입력
첫째 줄에 정수의 개수 N(1 ≤ N ≤ 100)이 주어진다.
둘째 줄에는 정수가 공백으로 구분되어져있다. 셋째 줄에는 찾으려고 하는 정수 v가 주어진다.
입력으로 주어지는 정수와 v는 -100보다 크거나 같으며, 100보다 작거나 같다.

출력
첫째 줄에 입력으로 주어진 N개의 정수 중에 v가 몇 개인지 출력한다."""


import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
v = int(sys.stdin.readline())

print(arr.count(v))

"""
BOJ 10807 - 개수 세기

[문제 요약]
주어진 수열에서 특정 값 v가 몇 번 등장하는지 출력한다.

[핵심 개념]
- 1차원 배열(list)
- 순회(for)
- 조건문(if)
- 카운트 패턴

[접근]
리스트에 숫자들을 저장한 뒤,
하나씩 보면서 v와 같으면 카운트를 증가시킨다."""

# 핵심 패턴: for + if + counter

"""
혹은 
문자열을 받고 number 변수 리스트(인풋)
포문을 이용해 하나씩 살펴본다 -> 
n = int(input())                 # 숫자 개수 (지금은 그냥 읽기만)

numbers = input().split()        # 문자열 리스트로 받기
v = input()                      # 찾을 값도 문자열로 받기

count = 0
for x in numbers:
    if x == v:
        count += 1

print(count)
"""


