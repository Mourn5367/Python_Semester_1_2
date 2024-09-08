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
        print("☆★ 선택지 안에서 고르시오 ☆★")
        return False
    if answer == Select_Question.ADDMONEY:
        return VM_State.INPUTMONEY
    elif answer == Select_Question.REORDER:
        return VM_State.SELECTMENU
    elif answer == Select_Question.ESCAPE:
        return  VM_State.STOP
    else:
        # 금액, 주문, 종료 이외의 값을 넣었을 경우의 예외 처리
        print("☆★ 숫자를 입력해 주세요. ☆★ ")
        return False
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

    VM_Question = Question()
    # Ques = ["1. 추가 금액 넣기", "2. 메뉴 다시 고르기", "3. 그만 두기"]
    # QuesDict = self.CreateDict()  # { 1 : "추가 금액 넣기"...
    # QuesNoneNumDict = self.CreateNoneNumDict()  # ["추가금액넣기"...
    VM_Wallet = 0
    curState = VM_State.PRINTMENU
    isAgain = False
    selectMenuPrice = 0
    selectMenu = ""
    VM_Basket = []
    print(f"구동 시작")
    while True:

        if curState == VM_State.PRINTMENU:
            print("==판매 목록==")
            print(", ".join(f"{menu}: {VM_Menu.ori[menu]}" for menu in VM_Menu.ori ))
            curState = VM_State.INPUTMONEY
            continue

        if curState == VM_State.INPUTMONEY:
            if isAgain:
                try:
                    inputMoney = int(input("☆★ 0 이상의 자연수만 입력해 주세요. ☆★"))
                    if inputMoney <= 0:
                        print("☆★ 0원 이하는 투입이 불가능 합니다.☆★")
                        continue
                    VM_Wallet += inputMoney
                except ValueError:
                    continue

                isAgain = True
                curState = VM_State.SELECTMENU
                continue

            try:
                inputMoney = int(input("금액을 투입해 주세요. "))
                if inputMoney <= 0:
                    isAgain = True
                    continue
                VM_Wallet += inputMoney
            except ValueError:
                isAgain = True
                continue
            isAgain = False
            curState = VM_State.SELECTMENU

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

        if curState == VM_State.CALCULATE:
            if isAgain or VM_Wallet - selectMenuPrice < 0:
                if VM_Wallet - selectMenuPrice < 0:
                    print("잔액이 부족합니다.")
                elif isAgain:
                    print("메뉴를 다시 고르거나 금액을 투입해 주세요")
                try:
                    answer = (input(", ".join(f"{item}"for item in VM_Question.list)))
                    answer = int(answer)
                except ValueError:
                    try:
                        answer = VM_Question.quesReversDict[answer.replace(" ","")]
                    except KeyError:
                        print("☆★ 정확히 입력해 주세요☆★")
                        isAgain = True
                        continue

                if convertAnswer(answer) == False:
                    isAgain = True
                    continue
                else:
                    curState = convertAnswer(answer)
                    isAgain = False
                    continue
            VM_Wallet -= selectMenuPrice
            try:
                VM_Basket.append(VM_Menu.name[int(selectMenu)])
            except ValueError:
                selectMenu = selectMenu.replace(" ", "")
                VM_Basket.append(VM_Menu.noneNumDict[selectMenu])
            curState = VM_State.RESULT

        if curState == VM_State.RESULT:
            if not isAgain:
                print("==구입한 목록==")
                print(", ".join(VM_Basket))
            try:
                print(f"현재 잔액: {VM_Wallet}")
                answer = int(input(", ".join(f"{item}"for item in VM_Question.list)))
            except ValueError:
                print("☆★ 정확히 입력해 주세요☆★")
                isAgain = True
                continue
            if convertAnswer(answer):
                curState = convertAnswer(answer)

        if curState == VM_State.STOP:
            if not VM_Basket:
                print("오늘 구입하신 물품은 없습니다.")
                print(f"투입 했던 금액 {VM_Wallet}원 돌려드리겠습니다.")
            else:
                print("==오늘 구입한 목록==")
                print(", ".join(VM_Basket))
                print(f"거스름돈은 {VM_Wallet}원입니다.")
            break



print("감사합니다.")




