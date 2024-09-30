import random
import copy

if __name__ == '__main__':
    # seatList = []
    rows = int(3) # 가로 몇줄
    cols = int(10) # 세로 몇줄
    totalSeat = rows * cols # 총 자리 수
    # totalStudents = 28 # 총 학생 수
    # for i in range(rows):
    #     seatList.append([])
    #     for j in range(cols):
    #         seatList[i].append(j+1+i*10)
    # seatList = [[j+1+i*10 for j in range(cols)] for i in range(rows)]
    # print(seatList)

    superList = [[],[]]
    print(len(superList[0]))
    reply = input("선택권 있나요")
    if reply == "네":
        count = int(input("몇자리 까지?"))
        for i in range(count):
            name = str(input(f"{i+1}번째 사람의 이름은?"))
            superList[0].append(name)
            position = int(input(f"{name}의 자리는?"))
            superList[1].append(position)
        superList[1].sort()


    # nameList = input("이름을 입력하세요.(띄어 쓰기로 구분)").split(" ")
    nameList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"] # 학생 이름 적기
    if len(nameList) < totalSeat:
        for i in range(totalSeat - (len(nameList) + len(superList[0]))):
            nameList.append(f"EMPTY")
    copyNameList = copy.deepcopy(nameList)
    seatL = []

    for i in range(rows):
        seatL.append({})
        for j in range(cols):
            random.shuffle(copyNameList)
            if len(superList[1]) >= 1 and (j+i*10+1) == superList[1][0]:
                seatL[i][j+i*10+1] = superList[0].pop(0)
                superList[1].pop(0)
            else:
                seatL[i][j+i*10+1] = copyNameList.pop()
    # nameDict = {}
    # for i in range(1,totalSeat+1):
    #     nameDict[i] = nameList[i-1]
    # print(seatL)
    for i in range(rows):
        for j in range(cols,0,-1): # (1,cols+1)
            print(f"{i*10+j:02}번 {seatL[i][j+i*10]:<3}\t",end="")
        print("\n")
    # print(seatL[0])
    # print(seatL[1])
    # print(seatL[2])

