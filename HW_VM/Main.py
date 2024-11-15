
from HW_VM.Menu import Menu
from HW_VM.VendingMachine import VendingMachine
from Beverage import Beverage

if __name__ == '__main__':
    menu = Menu()
    VM =  VendingMachine()
    while True:
        userSelectBeverage = VM.SelectMenuOrEnterAdminMode(menu)
        if userSelectBeverage == "종료":
            VM.ReturnChangeMoney()
            break
        if userSelectBeverage:
            userSelectCount = VM.CountOrder(userSelectBeverage)

            if userSelectCount:
                
                # 이거 돈 적게 넣으면 그거에 맞는 피드백 넣어야함
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

