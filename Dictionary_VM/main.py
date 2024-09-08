# // 2024_09_02_파이썬_기초_실습_과제
# // 한국폴리텍대학_서울정수캠퍼스_인공지능소프트웨어과
# // 2401110252_박지수
# // 딕셔너리를 사용한 자동판매기 제작

from enum import Enum
from Menu import Menu
from Question import Question

# 자판기의 작동 상태를 나타내는 Enum 클래스
class VM_State(Enum):
    STOP = 0
    PRINTMENU = 1
    INPUTMONEY = 2
    SELECTMENU = 3
    CALCULATE = 4
    RESULT = 5

# 부족한 금액을 넣거나 추가 주문, 구입 종류를 할때 매핑하는 Enum 클래스
class Select_Question(Enum):
    ADDMONEY = 1
    REORDER = 2
    ESCAPE = 3

# 파이썬은 Enum의 숫자와 정수형의 숫자와 달라서 Question 클래스를 통해
# 답을 받았을때 VM_State 상태로 옮기기 위한 전환 함수.
def convertAnswer(answer):
    # 사용자의 답을 받았을때 무엇인지 확인
    try:
        answer = Select_Question(answer)
    # 타입이 안맞는 값이 들어올때의 예외처리 EX) String
    except ValueError:
        print("☆★ 선택지 안에서 고르시오. ☆★")
        return False
    if answer == Select_Question.ADDMONEY:
        return VM_State.INPUTMONEY
    elif answer == Select_Question.REORDER:
        return VM_State.SELECTMENU
    elif answer == Select_Question.ESCAPE:
        return  VM_State.STOP
    else:
        # 금액, 주문, 종료 이외의 값을 넣었을 경우의 예외 처리
        print("☆★ 숫자를 입력해 주세요. ☆★")
        return False

# 숫자와 글자 두개 다 입력받기위한 처리과정
def menu_processing(selectMenu):
    try:
        selectMenu = int(selectMenu)
        if isinstance(selectMenu, int):
            return VM_Menu.num[selectMenu]
    except ValueError:
        return VM_Menu.str[selectMenu]

if __name__ == '__main__':
    VM_Menu = Menu()
    # ori = {"1. 사이다": 1000, "2. 콜라": 1500, "3. 쿠키": 2000, "4. 레몬에이드": 2500}
    # str = self.createStringDict()  # {"사이다 : 1000...
    # num = self.createNumberDict()  # {"1: 1000...
    # name = self.extractMenu()  # { "","사이다"...
    # noneNumDict = self.CreateNoneNumDict()  # {"사이다" : "사이다"

    VM_Question = Question()
    # list = ["1. 추가 금액 넣기", "2. 메뉴 다시 고르기", "3. 그만 두기"]
    # quesDict = self.CreateDict()  # { 1 : "추가 금액 넣기"...
    # quesNoneNumDict = self.CreateNoneNumDict()  # ["추가금액넣기"...
    # quesReversDict = self.CreateReversDict()  # ["추가금액넣기" : 1...
    VM_Wallet = 0
    curState = VM_State.PRINTMENU
    isAgain = False
    selectMenuPrice = 0
    selectMenu = ""
    VM_Basket = []
    print(f"구동 시작")
    while True:

        # 판매목록 출력과 금액 투입으로 넘어감.
        if curState == VM_State.PRINTMENU:
            print("==판매 목록==")
            print(", ".join(f"{menu}: {VM_Menu.ori[menu]}" for menu in VM_Menu.ori ))
            curState = VM_State.INPUTMONEY
            continue

        # 금액을 투입하는 단계, 투입시 메뉴 선택으로 넘어감.
        # isAgain 변수를 통해 재입력시 경고문 출력.
        if curState == VM_State.INPUTMONEY:
            if isAgain:
                try:
                    inputMoney = int(input("☆★ 0 이상의 자연수만 입력해 주세요. 취소는 0입니다.☆★"))
                    if inputMoney < 0:
                        print("☆★ 0원 이하는 투입이 불가능 합니다. ☆★")
                        continue
                    elif inputMoney == 0:
                        curState = VM_State.RESULT
                        isAgain = False
                        continue
                    VM_Wallet += inputMoney
                except ValueError:
                    continue

                isAgain = True
                curState = VM_State.SELECTMENU
                continue

            try:
                inputMoney = int(input("금액을 투입해 주세요. "))
                if inputMoney < 0:
                    print("☆★ 0원 이하는 투입이 불가능 합니다. ☆★")
                    isAgain = True
                    continue
                elif inputMoney == 0:
                    curState = VM_State.RESULT
                    continue
                VM_Wallet += inputMoney
            except ValueError:
                isAgain = True
                continue

            isAgain = False
            curState = VM_State.SELECTMENU

        # 현재 금액 및 메뉴 출력
        # 한글 또는 숫자 입력시 계산 단계로 넘어감.
        if curState == VM_State.SELECTMENU:
            print(f"현재 금액: {VM_Wallet}원")
            print(", ".join(f"{menu}: {VM_Menu.ori[menu]}" for menu in VM_Menu.ori))
            try:
                selectMenu = input("원하시는 메뉴를 입력해주세요. ").replace(" ", "")
                selectMenuPrice = menu_processing(selectMenu)
            except KeyError:
                print("☆★ 숫자 또는 메뉴명을 입력해 주세요. ☆★")
                isAgain = True
                continue
            isAgain = False
            curState = VM_State.CALCULATE

        # 메뉴를 잘 선택하였다면 계산 단계로 넘어오게 됨 정상적으로 계산 완료했을시 결과 단계로 넘어감.
        # 투입한 금액과 선택한 메뉴 계산과 금액이 적어 실패 했을 때 다른 솔루션을 제공함.
        # 이때의 답 또한 한글로 입력 가능.
        if curState == VM_State.CALCULATE:
            if isAgain or VM_Wallet - selectMenuPrice < 0:
                if VM_Wallet - selectMenuPrice < 0:

                    #숫자로 받을 경우 "1" 이렇게 입력 받기 때문에 처리.
                    try:
                        print(f"{VM_Menu.name[int(selectMenu)]}을(를) 사기에는 잔액이 부족합니다.")
                    #글자로 받을 경우 그대로 나오기 때문에(SELECTMENU 상태에서 replace 처리한 상태) 그대로 출력
                    except ValueError:
                        print(f"{selectMenu}을(를) 사기에는 잔액이 부족합니다.")
                elif isAgain:
                    print("메뉴를 다시 고르거나 금액을 투입해 주세요")

                # 보유 금액 부족시 해결 방안 출력.
                try:
                    answer = (input(", ".join(f"{item}"for item in VM_Question.list)))
                    answer = int(answer)
                except ValueError:
                    try:
                        answer = VM_Question.quesReversDict[answer.replace(" ","")]
                    except KeyError:
                        print("☆★ 정확히 입력해 주세요☆★")
                        selectMenuPrice = 0
                        isAgain = True
                        continue
                
                # 해결방안에 대해 잘못된 값 입력시 다시 해당 단계 반복
                if convertAnswer(answer) == False:
                    isAgain = True
                    selectMenuPrice = 0
                    continue
                # 정확히 입력 하였다면 그 단계로 점프
                else:
                    curState = convertAnswer(answer)
                    isAgain = False
                    continue
            # 메뉴값과 투입한 금액이 더 많거나 같을시 금액 차감.
            # 그 외 다른 단계로 넘어가거나 잘못 입력시 해당 단계 반복 및 점프.
            VM_Wallet -= selectMenuPrice

            # 한글, 숫자 둘 다 입력받기 위한 전환 과정.
            try:
                VM_Basket.append(VM_Menu.name[int(selectMenu)])
            except ValueError:
                selectMenu = selectMenu.replace(" ", "")
                VM_Basket.append(VM_Menu.noneNumDict[selectMenu])
            curState = VM_State.RESULT

        # 계산까지 다 마쳤다면 구입한 목록들 출력, 추가 구매 유무 확인.
        if curState == VM_State.RESULT:
            if not isAgain:
                if VM_Basket:
                    print("==구입한 목록==")
                    print(", ".join(VM_Basket))
            try:
                print(f"현재 잔액: {VM_Wallet}")
                answer = (input(", ".join(f"{item}" for item in VM_Question.list)))
                answer = int(answer)
            except ValueError:
                try:
                    answer = VM_Question.quesReversDict[answer.replace(" ","")]
                except KeyError:
                    print("☆★ 정확히 입력해 주세요. ☆★")
                    isAgain = True
                    continue
            if convertAnswer(answer):
                curState = convertAnswer(answer)
                isAgain = False

        if curState == VM_State.STOP:
            if not VM_Basket:
                print("오늘 구입하신 물품은 없습니다.")
                print(f"투입 했던 금액 {VM_Wallet}원 돌려드리겠습니다.")
            else:
                print("==오늘 구입한 목록==")
                print(", ".join(VM_Basket))
                print(f"거스름돈은 {VM_Wallet}원입니다.")
            # 반복문 탈출
            break
    print("이용해 주셔서 감사합니다.")





