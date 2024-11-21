import sys

from HW_DM.Admin import Admin
from HW_DM.ProductList import ProductList
from HW_DM.Machine import Machine
from HW_DM.Product import Product


class MachineState:
    def __init__(self):
        pass

    # 자판기 작동
    def ActivateMachine(self, machine: Machine, productList: ProductList, admin: Admin):
        while True:
            self.CountCheckState(machine, productList, admin)

    # 판매할 재고가 있으면 유저가 고를 수 있는 상태로 아니면 관리자 호출 메시지.
    # 999 입력시 관리자 모드
    def CountCheckState(self, machine: Machine, productList: ProductList, admin: Admin):
        isCheck = machine.CountCheck(productList, admin,admin.GetProductType())
        if not isCheck:
            return self.CountCheckState
        elif isinstance(isCheck, Admin):
            return self.AdminState(machine, productList, admin)
        else:
            return self.UserSelectBeverageState(machine, productList, admin)

    # 유저가 음료 고르는 상태
    def UserSelectBeverageState(self, machine: Machine, productList: ProductList, admin: Admin):
        userSelectBeverage = machine.SelectMenuOrEnterAdminMode(productList, admin)
        if userSelectBeverage == "종료":
            machine.ReturnChangeMoney()
            return self.CountCheckState(machine, productList, admin)
        elif isinstance(userSelectBeverage, Product):
            return self.UserSelectCountState(machine, productList, admin, userSelectBeverage)
        elif isinstance(userSelectBeverage, Admin):
            return self.AdminState(machine, productList, admin)
        else:
            return self.CountCheckState(machine, productList, admin)

    # 관리자 모드
    def AdminState(self, machine: Machine,  productList: ProductList, admin: Admin):
        adminSelect = admin.CallAdmin(productList)
        if adminSelect is None or adminSelect == "다시":
            return self.AdminState(machine, productList, admin)
        elif adminSelect == "설정 종료":
            return self.CountCheckState(machine, productList, admin)
        elif adminSelect == "자판기 종료":
            return self.DeactiavateMachine()

    # 관리자 모드에서 자판기 종료 가능
    def DeactiavateMachine(self):
        sys.exit()

    # 유저가 자판기에서 몇개 고를지 선택
    def UserSelectCountState(self, machine: Machine,  productList: ProductList, admin: Admin, userSelectBeverage: Product):
        userSelectCount = machine.CountOrder(userSelectBeverage)
        if userSelectCount:
            return self.UserInsertMoneyState(machine, productList, admin, userSelectBeverage, userSelectCount)
        else:
            return self.CountCheckState(machine, productList, admin)

    # 유저가 자판기 돈 넣는 상태
    def UserInsertMoneyState(self, machine: Machine, productList: ProductList, admin: Admin, userSelectBeverage: Product,
                             userSelectCount: int):
        machine.ShowOrderPrice(userSelectBeverage, userSelectCount)
        if machine.insertMoney >= userSelectCount * userSelectBeverage.GetPrice():
            isCount = machine.CheckChoiceAndMoney(userSelectBeverage, userSelectCount)
            return self.CalculateState(machine, productList, admin, userSelectBeverage, userSelectCount, isCount)
        else:
            if machine.UserInsertMoney():
                isCount = machine.CheckChoiceAndMoney(userSelectBeverage, userSelectCount)
                return self.CalculateState(machine, productList, admin, userSelectBeverage, userSelectCount, isCount)
            else:
                return self.CountCheckState(machine, productList, admin)

    # 자판기에서 돈 계산
    def CalculateState(self, machine: Machine, productList: ProductList, admin: Admin, userSelectBeverage: Product,
                       userSelectCount: int, isCount: bool):
        if isCount:
            isContinue = machine.CalculateOrder(userSelectBeverage, userSelectCount, productList)
            return self.ContinueShoppingState(machine, productList, admin, isContinue)
        else:
            return self.CountCheckState(machine, productList, admin)

    # 계속 살건지 묻고 살 경우 잔돈 출력
    def ContinueShoppingState(self, machine: Machine, productList: ProductList, admin: Admin, isContinue: bool):
        if isContinue:
            return self.CountCheckState(machine, productList, admin)
        else:
            machine.ReturnChangeMoney()
            return self.CountCheckState(machine, productList, admin)
