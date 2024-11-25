from HM_NEW_DM import DollBox
from HW_DM import Machine, ProductList, Admin, Product
from HW_DM.MachineState import MachineState


class DollMachinState(MachineState):
    def __init__(self):
        super().__init__()

    # 자판기 작동
    def ActivateMachine(self, machine: Machine, productList: ProductList, admin: Admin,dollBox:DollBox):
        while True:
            self.CountCheckState(machine, productList, admin,dollBox)

    # 판매할 재고가 있으면 유저가 고를 수 있는 상태로 아니면 관리자 호출 메시지.
    # 999 입력시 관리자 모드
    def CountCheckState(self, machine: Machine, productList: ProductList, admin: Admin,dollBox:DollBox):
        isCheck = machine.CountCheck(productList, admin,admin.GetProductType())
        if not isCheck:
            self.CountCheckState(machine, productList, admin,dollBox)
        elif isinstance(isCheck, Admin):
            self.AdminState(machine, productList, admin)
        else:
            self.UserSelectBeverageState(machine, productList, admin,dollBox)

    # 유저가  고르는 상태
    def UserSelectBeverageState(self, machine: Machine, productList: ProductList, admin: Admin,dollBox:DollBox):
        dollBox.RefreshBox(productList)
        userSelectBeverage = machine.SelectMenuOrEnterAdminMode(productList, admin,admin.GetProductType())
        if userSelectBeverage == "종료":
            machine.ReturnChangeMoney()
            self.CountCheckState(machine, productList, admin,dollBox)
        elif isinstance(userSelectBeverage, Product):
            self.UserSelectCountState(machine, productList, admin, userSelectBeverage)
        elif isinstance(userSelectBeverage, Admin):
            self.AdminState(machine, productList, admin)
        else:
            self.CountCheckState(machine, productList, admin,dollBox)

    # 관리자 모드
    def AdminState(self, machine: Machine,  productList: ProductList, admin: Admin):
        adminSelect = admin.CallAdmin(productList)
        if adminSelect is None or adminSelect == "다시":
            self.AdminState(machine, productList, admin)
        elif adminSelect == "설정 종료":
            self.CountCheckState(machine, productList, admin)
        elif adminSelect == "자판기 종료":
            self.DeactiavateMachine()

    # 유저가 자판기에서 몇개 고를지 선택
    def UserSelectCountState(self, machine: Machine,  productList: ProductList, admin: Admin, userSelectBeverage: Product):
        userSelectCount = machine.CountOrder(userSelectBeverage)
        if userSelectCount:
            self.UserInsertMoneyState(machine, productList, admin, userSelectBeverage, userSelectCount)
        else:
            self.CountCheckState(machine, productList, admin)

    # 유저가 자판기 돈 넣는 상태
    def UserInsertMoneyState(self, machine: Machine, productList: ProductList, admin: Admin, userSelectBeverage: Product,
                             userSelectCount: int):
        machine.ShowOrderPrice(userSelectBeverage, userSelectCount)
        if machine.insertMoney >= userSelectCount * userSelectBeverage.GetPrice():
            isCount = machine.CheckChoiceAndMoney(userSelectBeverage, userSelectCount)
            self.CalculateState(machine, productList, admin, userSelectBeverage, userSelectCount, isCount)
        else:
            if machine.UserInsertMoney():
                isCount = machine.CheckChoiceAndMoney(userSelectBeverage, userSelectCount)
                self.CalculateState(machine, productList, admin, userSelectBeverage, userSelectCount, isCount)
            else:
                self.CountCheckState(machine, productList, admin)

    # 자판기에서 돈 계산
    def CalculateState(self, machine: Machine, productList: ProductList, admin: Admin, userSelectBeverage: Product,
                       userSelectCount: int, isCount: bool):
        if isCount:
            isContinue = machine.CalculateOrder(userSelectBeverage, userSelectCount, productList)
            self.ContinueShoppingState(machine, productList, admin, isContinue)
        else:
            self.CountCheckState(machine, productList, admin)

    # 계속 살건지 묻고 살 경우 잔돈 출력
    def ContinueShoppingState(self, machine: Machine, productList: ProductList, admin: Admin, isContinue: bool):
        if isContinue:
            self.CountCheckState(machine, productList, admin)
        else:
            machine.ReturnChangeMoney()
            self.CountCheckState(machine, productList, admin)
