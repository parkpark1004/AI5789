#7.25

print("사전 프로그램 시작... 종료는 q를 입력")

dictionary = {}

while True:
    command = input("$ ")

    if command == 'q':
        print("사전 프로그램을 종료합니다.")
        break

    if command.startswith('<'):
        text = command[1:].strip()
        if ':' in text:
            eng = text.split(':')[0].strip()
            kor = text.split(':')[1].strip()
            dictionary[eng] = kor
        else:
            print("입력오류가 발생했습니다.")

    elif command.startswith('>'):
        word = command[1:].strip()
        if word in dictionary:
            print(dictionary[word])
        else:
            print(word + "가 사전에 없습니다.")
    else:
        print("입력오류가 발생했습니다.")
