import random
import copy
import sys

from Group import Group


def setseatcount(gr: Group):
    try:
        gr.cols_count()
        gr.rows_count()
    except ValueError:
        print("유효 하지 않는 입력입니다.")
        sys.exit()

def supermark(superlist : list)-> list:

    for i in range(len(superlist[0])):
        superlist[0][i] = superlist[0][i] + "-지정"
    return superlist

def superpeople(superlist : list, gr: Group)-> list:
    reply = input("선택권 있나요 (있는 경우 ""네 입력"") ")
    if reply.replace(" ","") == "네":
        try:
            count = int(input("몇자리 까지 선택 하겠습니까? (숫자로 입력)"))
        except ValueError:
            print("숫자 이외의 입력입니다. 좌석 선택 함수를 종료합니다.")
            return superlist
        if count > gr.totalSeat:
            print("현재 좌석보다 많습니다. 좌석 선택 함수를 종료합니다.")
            return superlist
        for i in range(count):
            name = input(f"{i + 1}번째 사람의 이름은?")
            superList[0].append(name)
            try:
                if superlist[1]:
                    position = int(input(f"{name}의 자리는? 현재 사용중인 좌석. {superlist[1]} ex) 첫(01)번째 자리는 ""1""만 입력해 주세요. "))
                else:
                    position = int(input(f"{name}의 자리는? ex) 첫(01)번째 자리는 ""1""만 입력해 주세요. "))
                if position < 1 or position > gr.totalSeat:
                    print("전체 좌석중 해당 좌석이 없습니다. 좌석 선택 함수를 종료합니다.")
                    superlist.clear()
                    return superlist
                elif position in superlist[1]:
                    print("중복된 좌석입니다. 좌석 선택 함수를 종료합니다.")
                    superlist.clear()
                    return superlist

                superList[1].append(position)
            except ValueError:
                print("숫자 이외의 입력입니다. 좌석 선택 함수를 종료합니다.")
                superlist.clear()
                return superlist
        supermark(superlist)
        superList[1].sort()
    return superlist

def setname(namelist : list, superlist : list, gr: Group):

    issetname = input("이름을 작성하시겠습니까? (할 경우 ""네""를 입력해 주세요.")

    if issetname.replace(" ","") == "네":
        tmpname = input("이름을 띄어 쓰기로 구분하여 입력해 주세요.(마지막은 X) 다 적으셨다면 엔터를 눌러주세요.").split(" ")
        namelist.clear()
        namelist.extend(tmpname)

    print(len(namelist), len(superlist[1]), gr.totalSeat)
    if len(namelist) + len(superlist[1]) < gr.totalSeat:
        for i in range(gr.totalSeat - (len(nameList) + len(superList[0]))):
            nameList.append(f"EMPTY")

    if len(nameList) + len(superlist[1]) > gr.totalSeat:
        print("좌석 수 보다 인원 수 가 더 많습니다. 프로그램을 종료합니다.")
        sys.exit()

def duplicatename(duplist : list)-> list:

    for i in duplist:
        dupcount = 0
        dupversion = 1

        if duplist.count(i) > 1:
            for j, k in enumerate(duplist):
                if k == i and dupcount == 0:
                    dupcount += 1
                    continue
                elif k == i and dupcount != 0:
                    duplist[j] = duplist[j]+("-"+str(dupversion))
                    dupversion += 1

    return duplist

def makeseat(gr : Group, copynamelist : list, superlist : list)-> list:
    seatlist = []
    for i in range(gr.rows):
        seatlist.append({})
        for j in range(gr.cols):
            random.shuffle(copynamelist)
            if len(superlist[1]) >= 1 and (j+i*gr.cols+1) == superlist[1][0]:
                seatlist[i][j+i*gr.cols+1] = superlist[0].pop(0)
                superlist[1].pop(0)
            else:
                seatlist[i][j+i*gr.cols+1] = copynamelist.pop()
    return seatlist

def printseat(gr : Group, seatlist : list):
    for i in range(gr.rows):
        for j in range(gr.cols, 0, -1):  # (1,gr.cols+1)
            print(f"{i * gr.cols + j:02}번 {seatlist[i][j + i * gr.cols]:<3}\t", end="")
        print("\n")

if __name__ == '__main__':
    
    # 자리 수 관련 클래스 생성
    gr = Group()
    
    # 자리수 생성.
    # 세로 몇줄 가로 몇줄
    setseatcount(gr)


    superList = [[],[]]

    # 지정석 생성 여부 확인 및 생성
    superList = superpeople(superList,gr)
    # 지정석 이름중 같은 이름 중복 표시
    superList[0] = duplicatename(superList[0])

    # 학생 이름
    nameList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
    # 학생 이름 기존것 사용 여부 입력시 띄어쓰기로 구분
    setname(nameList,superList, gr)

    # 학생 이름중 중복 표시
    nameList = duplicatename(nameList)

    seatList = makeseat(gr, nameList, superList)

    printseat(gr, seatList)