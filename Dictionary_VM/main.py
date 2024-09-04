from enum import Enum

class VM_State(Enum):
    STOP = 0
    PRINTMENU = 1
    INPUTMONEY = 2
    SELECTMENU = 3
    CALCULATE = 4
    RESULT = 5
class Question(Enum):
    ADDMONEY = 1
    AGAINMENU = 2
    ESCAPE = 3
def VM_Question(answer):
    try:
        answer = Question(answer)
    except ValueError:
        print("잘못된 입력")
        return False
    if answer == Question.ADDMONEY:
        return VM_State.INPUTMONEY
    elif answer == Question.AGAINMENU:
        return VM_State.SELECTMENU
    elif answer == Question.ESCAPE:
        return  VM_State.STOP
    else:
        print("제대로 입력")
        return False
if __name__ == '__main__':
    #VM_Menu = {"1. 사이다" : 1000, "2. 콜라" : 1500, "3. 쿠키" : 2000 , "4. 레몬에이드" : 2500}
    VM_Menu = {"사이다": 1000, "콜라": 1500, "쿠키": 2000, "레몬에이드": 2500}
    VM_Wallet = 0

    curState = VM_State.PRINTMENU
    isAgain = False
    selectMenuPrice = 0
    selectMenu = ""
    addQuestion = 0
    VM_Basket = []
    while curState != 0:

        if curState == VM_State.PRINTMENU:
            print("ㅁㅁ판매 목록ㅁㅁ")
            print(", ".join(f"{menu}: {VM_Menu[menu]}" for menu in VM_Menu ))
            curState = VM_State.INPUTMONEY
            continue

        if curState == VM_State.INPUTMONEY:
            if isAgain:
                try:
                    inputMoney = int(input("정수의 숫자만 입력해 주세요"))
                    if inputMoney == 0:
                        print("0원은 투입이 불가능 합니다. ")
                        continue
                    VM_Wallet += inputMoney
                except ValueError:
                    isAgain = True
                    continue

                isAgain = False
            try:
                inputMoney = int(input("금액을 투입해 주세요. "))
                VM_Wallet += inputMoney
            except ValueError:
                print("정수의 숫자만 입력해 주세요. ")
                continue
            curState = VM_State.SELECTMENU

        if curState == VM_State.SELECTMENU:
            if not isAgain:
                print(f"현재 금액: {VM_Wallet}원")
            try:
                selectMenu = input("원하시는 메뉴를 입력해주세요. ")
                selectMenuPrice = VM_Menu[selectMenu]
            except KeyError:
                print("메뉴에 적힌것만 해줘.")
                isAgain = True
                continue
            isAgain = False
            curState = VM_State.CALCULATE

        if curState == VM_State.CALCULATE:
            if isAgain or VM_Wallet - selectMenuPrice < 0:
                print("잔액이 부족합니다. 메뉴를 다시 고르거나 금액을 투입해 주세요")
                try:
                    answer = int(input("1. 추가 금액 넣기 2. 메뉴 다시 고르기 3. 그만 두기"))
                except ValueError:
                    print("제대로 입력")
                    isAgain = True
                    continue
                if VM_Question(answer) == False:
                    isAgain = True
                    continue
                else:
                    curState = answer
                    continue
            VM_Wallet -= selectMenuPrice
            VM_Basket.append(selectMenu)
            curState = VM_State.RESULT

        if curState == VM_State.RESULT:
            if not isAgain:
                print("ㅁㅁ구입한 목록ㅁㅁ")
                print(", ".join(VM_Basket))
            try:
                print(f"현재 잔액: {VM_Wallet}")
                answer = int(input("1. 추가 금액 넣기 2. 메뉴 다시 고르기 3. 그만 두기"))
            except ValueError:
                print("제대로 입력")
                isAgain = True
                continue
            if not VM_Question(answer):
                isAgain = True
                continue
            else:
                curState = VM_Question(answer)
            isAgain = False

print("감사합니다.")




