from HW_VM.Beverage import Beverage
from HW_VM.Menu import Menu



class VendingMachine:
    def __init__(self):
        self.insertMoney = 0



    def SelectMenuOrEnterAdminMode(self, menu:Menu)->Beverage:
        menu.ShowMenuList(menu.NotSoldOutMenu())
        tmpMenuList = list(menu.NotSoldOutMenu().items())

        userSelect = ""

        if len(menu.menuDict) == 0:
            print("관리자에게 문의 바랍니다.")
        else:
            userSelect = input("원하시는 메뉴를 선택하여 주십시오.").replace(" ","")
            if userSelect == "999":
                menu.CallAdmin()

            else:
                if userSelect in menu.NotSoldOutMenu().keys():
                    return menu.NotSoldOutMenu()[userSelect]
                elif not userSelect.isdigit():
                    print("잘못된 입력입니다")
                elif int(userSelect):
                    if 1 <= int(userSelect) <= len(tmpMenuList):
                        return tmpMenuList[int(userSelect) - 1][1]

    def UserInsertMoney(self):
        tmpMoney = input("금액을 투입하여 주십시오.")
        if not tmpMoney.isdigit():
            print("잘못된 입력입니다.")
        else:
            self.insertMoney += int(tmpMoney)


    def CheckChoiceAndMoney(self, userSelect:Beverage,count:int)->bool:
        if self.insertMoney <= userSelect.GetPrice() * count:
            return False
        else:
            return True

    def CountOrder(self,userSelect:Beverage)->int:
        tmpCount = input("구입할 개수를 기입하여 주십시오.:")

        if tmpCount.isdigit():
            if userSelect.GetCount() >= int(tmpCount):
                return int(tmpCount)
            else:
                print(f'재고가 {int(tmpCount) - userSelect.GetCount()} 만큼 부족합니다.')
                return False
        else:
            print("잘못된 입력입니다.")
            return False

    def CalculateOrder(self, userSelect:Beverage):
        count =  self.CountOrder(userSelect)
        if not count: return
        self.UserInsertMoney()

        isAcceptable = False
        isAcceptable = self.CheckChoiceAndMoney(userSelect,count)
