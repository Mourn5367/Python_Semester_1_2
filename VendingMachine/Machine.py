from VendingMachine.Beverage import Beverage
from VendingMachine.MenuList import setBeverage


class Machine:
    def __init__(self):
        self.machineName = "ㅇ"
        self.menuList = setBeverage()
        self.inputMoney = 0
        self.changeMoney = 0

    def showMenu(self):
        i = 0
        for k,v in self.menuList.items():
            print(f'{i}번: {v.GetName()}\t', end="")
            i += 1
        print()

    def showStock(self):
        for k,v in self.menuList.items():
            print(f'{k} 재고: {v.GetCount()}개\t', end="")
        print()

    def inputMoney(self,inputMoney: int):
        self.inputMoney += inputMoney

    # 돈 크기 조건 미리
    def getChangeMoney(self,price: int):
        return self.inputMoney - price

m = Machine()

m.showMenu()
m.showStock()






