
from HW_VM.Menu import Menu
from HW_VM.VendingMachine import VendingMachine

if __name__ == '__main__':
    menu = Menu()
    VM =  VendingMachine()
    #menu.setBeverage()\
    while True:
       # ㅁㄴㅇ= VM.SelectMenuOrEnterAdminMode(menu)
        userSelectBeverage = VM.SelectMenuOrEnterAdminMode(menu)
        if userSelectBeverage == "종료":
            VM.ReturnChangeMoney()
            break
        if userSelectBeverage:
            userSelectCount = VM.CountOrder(userSelectBeverage)

            if userSelectCount:
                
                # 이거 돈 적게 넣으면 그거에 맞는 피드백 넣어야함
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

    # menu.addBeverage("콜라")
    # menu.addBeverage(1)

