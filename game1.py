import time   #시간 모듈  불러오기
import random #랜덤함수 모듈 불러오기

mapping = {
    "가위": 1,
    "바위": 2,
    "보": 3,
    1: "가위",
    2: "바위",
    3: "보"
}


user_name = input("가위바위보의 왕의 자리를 노리는게 누구냐!: ")
print("\n")
time.sleep(1)
print(f"{user_name}.. 이라, 좋다. 게임을 시작하지. ")
print("\n")
time.sleep(1)


#hero 대답은 문자열, computer는 숫자. 결국 승패를 나누는건 숫자를 기반으로
#그럼 hero의 대답을 숫자로, computer의 선택을 문자로 보여주는 단계있어야함. mapping(찾아보기)

# 1 hero 에게 입력값 받기

print("룰은 알고있겠지? 가위, 바위, 보 중 하나를 선택하면 된다. ")
time.sleep(1)

hero =  input("선택을 입력해주세요:  ")
hero_num = mapping[hero]

# 2 computer 입력값 받기

computer_num = random.randrange(1,4)
computer = mapping[computer_num]


# 판정 결과 보여주기

print("\n")
print("가위.. 바위.. 보!")
print("\n")
time.sleep(1)
print("-" * 20)
print(f"히어로의 선택: {hero}")
print("-" * 20)
print("\n")
time.sleep(1)
print("빌런: 후훗 나의 선택은!...")
time.sleep(1)
print("\n")
time.sleep(1.5)
print("-" * 20)
print(f"빌런의 선택: {computer}")
print("-" * 20)
print("\n")


# 3 승패 판정하기

score = (hero_num, computer_num)

win = [(1,3),(2,1),(3,2)] #-2, 1 1
tie = [(1,1),(2,2),(3,3)]
lose = [(1,2),(2,3),(3,1)] #-1 -1 2

#-2,-1,1 딕셔너리 형 if 문 하나로 끝낼 수 있음 (key 호출 1회 - 답)

if score in win:
    print("승리!")
    time.sleep(1.5)
    print("\n")
    print("쳇- 강한놈이군")

elif score in tie:
    print("무승부!")
    time.sleep(1.5)
    print("\n")
    print("좀 놀줄아는 놈이구만! 허허")

elif score in lose:
    print("패배!")
    time.sleep(1.5)
    print("\n")
    print("우유나 더먹고와 애송이!")



#깃허브만듬 개꿀












