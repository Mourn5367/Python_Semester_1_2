
from HW_VM.Menu import Menu
from HW_VM.VendingMachine import VendingMachine

if __name__ == '__main__':
    # 메뉴 객체 생성
    menu = Menu()
    # 자판기 객체 생성
    VM =  VendingMachine()
    while True:
        # 사용자의 입력을 받아 어떤 음료를 고를것인지
        # 999를 입력하여 관리자모드로 들어갈 것인지
        # 종료 혹은 음료수 개수 +1 만큼 눌러 구입을 중단할 것인지
        userSelectBeverage = VM.SelectMenuOrEnterAdminMode(menu)
        if userSelectBeverage == "종료":
            VM.ReturnChangeMoney()
            break
        if userSelectBeverage:
            userSelectCount = VM.CountOrder(userSelectBeverage)

            if userSelectCount:
                
                VM.ShowOrderPrice(userSelectBeverage, userSelectCount)
                if VM.insertMoney >= userSelectCount * userSelectBeverage.GetPrice():
                    isCount = VM.CheckChoiceAndMoney(userSelectBeverage, userSelectCount)
                else:
                    if VM.UserInsertMoney():
                        isCount = VM.CheckChoiceAndMoney(userSelectBeverage, userSelectCount)
                    else:
                        continue

                if isCount:
                    isContinue = VM.CalculateOrder(userSelectBeverage,userSelectCount)

                    if isContinue:
                        continue
                    elif not isContinue:
                        VM.ReturnChangeMoney()
                        break

