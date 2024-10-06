# 2024_10_06_파이썬_기초_실습_과제
# 한국폴리텍대학_서울정수캠퍼스_인공지능소프트웨어과
# 2401110252_박지수
# 자리 추첨기 만들기

import random
import sys
from time import sleep

from Group import Group

def longnamecut(namelist: list)->list:
    for i, name in enumerate(namelist):
        if len(name) > 5:
            namelist[i] = name[:5]
    return namelist


# 좌석 수 설정
def setseatcount(gr: Group):
    try:
        gr.cols_count()
        gr.rows_count()
    except ValueError:
        print("유효 하지 않는 입력입니다.")
        sys.exit()
# 지정 좌석 표시
def supermark(superlist : list)-> list:
    # 리스트 길이만큼 반복해서 이름 부분에 문자열 추가로 붙이기.
    for i in range(len(superlist[0])):
        superlist[0][i] = superlist[0][i] + "-지"
    return superlist

# 지정 좌석 여부 확인 후 이름과 자리 위치 정하기
def superpeople(superlist : list, gr: Group)-> list:
    reply = input("선택권 있나요 (있는 경우 ""네 입력"") ")
    if reply.replace(" ","") == "네":
        try:
            count = int(input("몇자리 까지 선택 하겠습니까? (숫자로 입력)"))
            if count <= 0:
                print("1보다 작은 수를 입력하여 좌석 선택 함수를 종료합니다.")
                return superlist
        except ValueError:
            print("숫자 이외의 입력입니다. 좌석 선택 함수를 종료합니다.")
            return superlist
        if count > gr.totalSeat:
            print("현재 좌석보다 많습니다. 좌석 선택 함수를 종료합니다.")
            return superlist
        # 선택권이 있을 경우 선택권 갯수만큼 반복
        for i in range(count):
            name = input(f"{i + 1}번째 사람의 이름은?")
            # 0번째는 이름 1번째는 자리 위치
            superlist[0].append(name)
            try:
                # 처음 추가 했을 때와 아닐 때 질문이 조금 달라짐.
                if superlist[1]:
                    position = int(input(f"{name}의 자리는?(끝 자리는 {gr.totalSeat}입니다.) 현재 사용중인 좌석. "
                                         f"{superlist[1]} ex) 첫(01)번째 자리는 ""1""만 입력해 주세요. "))
                else:
                    position = int(input(f"{name}의 자리는?(끝 자리는 {gr.totalSeat}입니다.) "
                                         f"ex) 첫(01)번째 자리는 ""1""만 입력해 주세요. "))
                #선택한 자리가 0 같이 없는 숫자이거나 전체 좌석 자리수 보다 클 때.
                if position < 1 or position > gr.totalSeat:
                    print("전체 좌석중 해당 좌석이 없습니다. 좌석 선택 함수를 종료합니다.")
                    # 리스트에 넣어둔게 있으니 함수 도중 종료시 비움.
                    superlist.clear()
                    return superlist
                elif position in superlist[1]:
                    print("중복된 좌석입니다. 좌석 선택 함수를 종료합니다.")
                    superlist.clear()
                    return superlist
                # 정상적인 경우 자리도 리스트 첫번째에 추가
                superlist[1].append(position)
            except (ValueError):
                print("숫자 이외의 입력입니다. 좌석 선택 함수를 종료합니다.")
                superlist.clear()
                return superlist
        # 이름 뒤에 "이름-지정" 이렇게 표시
        supermark(superlist)
    return superlist

# 지정석 외 이름 정하기.
def setname(namelist : list, superlist : list, gr: Group):

    issetname = input("이름을 작성하시겠습니까? (할 경우 ""네""를 입력해 주세요.)")

    if issetname.replace(" ","") == "네":
        tmpname = input("이름을 띄어 쓰기로 구분하여 입력해 주세요.(마지막은 X) 다 적으셨다면 엔터를 눌러주세요.").split(" ")
        # 기존거 없애고 입력한것 추가하기.
        namelist.clear()
        namelist.extend(tmpname)
    else:
        print("기존 이름으로 진행합니다.")
    
    # 기입한 이름 또는 기존 코드의 이름수 + 지정석 인원 < 전체 좌석수인 경우
    # 빈자리라고 표시하기 위해서 이름 리스트에 추가
    if len(namelist) + len(superlist[0]) < gr.totalSeat:
        # 빈 인원수 만큼 추가
        for i in range(gr.totalSeat - (len(nameList) + len(superList[0]))):
            nameList.append(f"EMPTY")
        
    # 자리가 부족 할 경우
    if len(nameList) + len(superlist[0]) > gr.totalSeat:
        print("좌석 수 보다 인원 수 가 더 많습니다. 프로그램을 종료합니다.")
        sys.exit()

# 중복 이름 표시하기
def duplicatename(duplist : list)-> list:

    for i in duplist:
        # 중복 횟수
        dupcount = 0
        
        if duplist.count(i) > 1:
            # 인덱스와 값을 받음.
            for j, k in enumerate(duplist):
                # 중복된 값이 지금 k값이랑 같고 첫번째인 경우와 아닌 경우
                if k == i and dupcount == 0:
                    dupcount += 1
                    continue
                elif k == i and dupcount != 0:
                    # 첫번째가 아닌 경우에는 해당 인덱스의 값을 수정
                    duplist[j] = duplist[j]+("-"+str(dupcount))
                    dupcount += 1
    return duplist

# superlist를 dict 형태로 변경
def listtodict(superlist: list)-> dict:
    # 임시 dict
    tmpdict = {}
    # 키와 값을 딕셔너리 형태로 변경
    for i in range(len(superlist[0])):
        tmpdict[superlist[1][i]] = superlist[0][i]
    return tmpdict

# 기존 이름리스트와 지정석 이름 딕셔너리 두개를 합쳐서 좌석 리스트를 만듦.
def makeseat(gr : Group, namelist : list, superlist : dict)-> list:
    seatlist = []
    # 키 값을 리스트로 만듦.
    superlistkey = list(superlist.keys())
    for i in range(gr.rows):
        seatlist.append({})
        for j in range(gr.cols):
            # 무작위로 뽑기위해 random 모듈을 가져와서 리스트 셔플
            random.shuffle(namelist)
            # 지정석 키 값에 좌석 번호가 있음. 지금 추첨하는 자리 값이 지정석인지 확인
            if (j+i*gr.cols+1) in superlistkey:
                seatlist[i][j+i*gr.cols+1] = superlist[j+i*gr.cols+1]
            else:
                seatlist[i][j+i*gr.cols+1] = namelist.pop()
    return seatlist

# 지정석과 무작위 자리를 합친 리스트를 가져와서 출력하기
def printseat(gr : Group, seatlist : list):
    
    for i in range(gr.rows):
        # 왼쪽부터 1번인 경우  (1,gr.cols+1) 오른쪽이 1번인 경우 (gr.cols, 0, -1)
        for j in range(gr.cols, 0, -1):  # (1,gr.cols+1)
            # :02 이건 한자리 숫자일 경우 01로 표시
            # <3,ljust() 이건 정렬 방향과 전체 길이를 몇으로 조정할 것인지
            # end="" 자리 하나만 출력하고 줄 바꾸지 않을려고
            # print(f"{i * gr.cols + j:02}번 {seatlist[i][j + i * gr.cols]:<11}", end="\t")
            # sleep(0.2)
        # # 밑의 경우는 좌석 밑에 이름 나오게 출력 하는 경우
            print(f"{i * gr.cols + j:02}번".ljust(9), end="\t")
        print("")
        for k in range(gr.cols, 0, -1):
            print(f"{seatlist[i][k + i * gr.cols]}".ljust(8),end="\t")
            sleep(0.2)
        print("\n")

if __name__ == '__main__':
    print()
    # 자리 수 관련 클래스 생성
    gr = Group()
    
    # 자리수 생성.
    # 세로 몇줄 가로 몇줄
    setseatcount(gr)
    superList = [[],[]]
    # 지정석 생성 여부 확인 및 생성
    superList = superpeople(superList,gr)
    # 지정석 이름중 같은 이름 중복 표시
    if len(superList) > 1:
        superList[0] = duplicatename(superList[0])
    else:
        superList = [[],[]]
    # 학생 이름
    nameList = ["AA","BB","CC","DD","EE","FF","GG","HH","II","JJ","KK","LL","MM","NN","OO","PP","QQ","RR","SS","TT","UU","VV","WW","XX","YY","ZZ","AA","BB"]
    # 학생 이름 기존것 사용 여부 입력시 띄어쓰기로 구분
    setname(nameList,superList, gr)
    longnamecut(nameList)
    # 학생 이름중 중복 표시
    nameList = duplicatename(nameList)

    #리스트에서 딕셔너리로 변환
    superList = listtodict(superList)
    # seatList에 학생들 자리 생성
    seatList = makeseat(gr, nameList, superList)

    # 자리 출력하기
    printseat(gr, seatList)