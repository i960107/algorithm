'''myfile.txt 라는 이름의 파일을 읽어오기'''


def solution():
    f = open('myfile.txt', 'r')
    while True:
        line = f.readline()
        # EOF를 만날때까지
        if not line:
            break
        # 공백 포함한 str
        print(line)
        # 단어로 나눠서 list반환
        raw = line.split()
        print(raw)
    f.close()


def solution_with_as():
    '''with-as 구문을 사용하여 file read'''
    with open('myfile.txt') as file:
        for line in file.readlines():
            # strip() 앞뒤 whitespace제거
            # split() str -> list로 \t 기준으로 쪼개기. 언제 tab으로 인식되지? 네칸 띄우기로는 tab으로 인식 안되는데
            print(line.strip().split('\\t'))
    # file을 close하지 않아도 됨 - with-as블록이 종료되면 파일 자동으로 close
    # readlines가 EOF까지만 읽으므로, while문 안에서 EOF를 체크할 필요 없음.


solution()
solution_with_as()
