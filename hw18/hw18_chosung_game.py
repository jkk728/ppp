import random

word={"ㄱㅌㄱ":"김태곤","ㅇㄱㄷ":"윤경담","ㅇㅅㅇ":"윤시원","ㅇㅈㅇ":"이준우","ㅅㅁㅌㅍ":"스마트팜","ㅈㅂㄷ":"전북대","ㅍㅇㅅ":"프원실"}

def chosung(game):

    answer = input(f"전북대 스마트팜학과와 관련된 단어 -> {game} <- 맞혀보세요: ")

    if answer == word[game]:
        print("정답입니다.")
    else:
        print("오답입니다.")
    return answer

def main():
    game = random.choice(list(word.keys()))
    answer = chosung(game)

if __name__=="__main__":
    main()

