from random import randint

# 1~100 사이의 숫자가 랜덤으로 정답 숫자로 저장되요.
answer = randint(1, 100)

# input()으로 숫자를 입력 받아 변수 submit에 저장해 보세요.
submit = input()

# if-elif-else문으로 Up-Down Game을 구현해 보세요.

if(answer > int(submit)):
    print("정답보다 큰 수를 입력했어요.")
elif(answer == submit):
    print("정답이에요!")
else:
    print("정답보다 작은 수를 입력했어요.")