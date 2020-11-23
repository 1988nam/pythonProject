# chapter 10-2
# 행맨 미니 게임 제작
# 프로그램 완성 및 최종 테스트

import time
import csv
import random
import winsound

name = input("What is your name ?")

print("Hi, " + name, "Time to play hangman")
print()

time.sleep(1)

print("Start loading")
print()
time.sleep(0.5)

# csv 단어 리스트
words = []

# 문제 csv 파일 로드
with open('./resource/word_list.csv', 'r') as f:
    reader = csv.reader(f)
    # 헤더 스킵
    next(reader)

    for c in reader:
        words.append(c)

# 리스트 섞기

random.shuffle(words)

q = random.choice(words)

# 정답 단어
word = q[0].strip()

# 추측 단어
guesses = ''

# 기회
turns = 10

# 핵심 while Loop
# 찬스 카운트가 남아 있을 경우

while turns > 0:
    # 실패 횟수(단어 매치 수)
    failed = 0

    # 정답 단어 반복
    for char in word:
        # 정답 단어 내 추측 문자가 포함되어 있는 경우
        if char in guesses:
            # 추측 단어 출력
            print(char, end=' ')
        else:
            # 틀린 경우
            print("_", end=' ')
            failed += 1
    # 단어 추측이 성공 한 경우
    if failed == 0:
        print()
        print()
        # 성공 사운드 입력
        winsound.PlaySound('./sound/good.wav', winsound.SND_FILENAME)
        print('Good')
        # while 구문 중단
        break
    print()

    # 추측 단어 문자 단위 입력
    print()
    print('Hint : {}'.format(q[1].strip()))
    guess = input("guess a character")

    guesses += guess

    # 정답 단어에 추측한 문자가 포함되어 있지 않으면
    if guess not in word:
        turns -= 1

        # 오류 메시지
        print("oops worng")
        # 남은 기회 출력
        print("you have", turns, "no more guesses!")


        if turns == 0:
            # 실패 사운드
            winsound.PlaySound('./sound/bad.wav', winsound.SND_FILENAME)
            # 실패 메시지
            # print("you failed")

