import sys

from HW_VM.Admin import Admin
from HW_VM.Menu import Menu
from HW_VM.VendingMachine import VendingMachine
from HW_VM.Beverage import Beverage


class MachineState:
    def __init__(self):
        pass
    
    # 자판기 작동
    def ActivateMachine(self,VM: VendingMachine,menu: Menu,admin: Admin):
        while True:
            self.CountCheckState(VM,menu,admin)
    # 판매할 재고가 있으면 유저가 고를 수 있는 상태로 아니면 관리자 호출 메시지.
    # 999 입력시 관리자 모드
    def CountCheckState(self, VM:VendingMachine,menu:Menu,admin:Admin):
        isCheck = VM.CountCheck(menu,admin)
        if not isCheck:
            return self.CountCheckState
        elif isinstance(isCheck,Admin):
            return self.AdminState(VM,menu,admin)
        else:
            return self.UserSelectBeverageState(VM,menu,admin)

    # 유저가 음료 고르는 상태
    def UserSelectBeverageState(self, VM:VendingMachine, menu:Menu,admin:Admin):
        userSelectBeverage = VM.SelectMenuOrEnterAdminMode(menu,admin)
        if userSelectBeverage == "종료":
            VM.ReturnChangeMoney()
            return self.CountCheckState(VM,menu,admin)
        elif isinstance(userSelectBeverage,Beverage):
            return self.UserSelectCountState(VM,menu,admin,userSelectBeverage)
        elif isinstance(userSelectBeverage,Admin):
            return self.AdminState(VM,menu,admin)
        else:
            return self.CountCheckState(VM,menu,admin)

    # 관리자 모드 
    def AdminState(self,VM:VendingMachine, menu:Menu,admin:Admin):
        adminSelect = admin.CallAdmin(menu)
        if adminSelect is None or adminSelect == "다시":
            return self.AdminState(VM,menu,admin)
        elif adminSelect == "설정 종료":
            return self.CountCheckState(VM, menu, admin)
        elif adminSelect == "자판기 종료":
            return self.DeactiavateMachine()
    
    # 관리자 모드에서 자판기 종료 가능
    def DeactiavateMachine(self):
        sys.exit()

    # 유저가 자판기에서 몇개 고를지 선택
    def UserSelectCountState(self, VM:VendingMachine, menu:Menu,admin:Admin, userSelectBeverage:Beverage):
        userSelectCount = VM.CountOrder(userSelectBeverage)
        if userSelectCount:
            return self.UserInsertMoneyState(VM,menu,admin,userSelectBeverage,userSelectCount)
        else:
            return self.CountCheckState(VM,menu,admin)
    
    # 유저가 자판기 돈 넣는 상태     
    def UserInsertMoneyState(self, VM:VendingMachine, menu:Menu,admin:Admin, userSelectBeverage:Beverage, userSelectCount:int):
        if VM.insertMoney >= userSelectCount * userSelectBeverage.GetPrice():
            isCount = VM.CheckChoiceAndMoney(userSelectBeverage, userSelectCount)
            return self.CalculateState(VM, menu, admin, userSelectBeverage, userSelectCount, isCount)
        else:
            if VM.UserInsertMoney():
                isCount = VM.CheckChoiceAndMoney(userSelectBeverage, userSelectCount)
                return self.CalculateState(VM, menu, admin,userSelectBeverage,userSelectCount, isCount)
            else:
                return self.CountCheckState(VM,menu,admin)
    
    # 자판기에서 돈 계산
    def CalculateState(self,VM:VendingMachine, menu:Menu,admin:Admin,userSelectBeverage:Beverage, userSelectCount:int,isCount:bool):
        if isCount:
            isContinue = VM.CalculateOrder(userSelectBeverage, userSelectCount, menu)
            return self.ContinueShoppingState(VM,menu,admin,isContinue)
        else:
            return self.CountCheckState(VM,menu,admin)
    
    # 계속 살건지 묻고 살 경우 잔돈 출력
    def ContinueShoppingState(self,VM:VendingMachine, menu:Menu,admin:Admin, isContinue:bool):
        if isContinue:
            return self.CountCheckState(VM,menu,admin)
        else:
            VM.ReturnChangeMoney()
            return self.CountCheckState(VM,menu,admin)
