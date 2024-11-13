from VendingMachine.Beverage import Beverage


class Machine2:
    def __init__(self):
        self.Menu = {1: Beverage("콜라",1000,10),
                     2: Beverage("사이다",1500,10)
                     }
        self.inputMoney = 0
        
    def InputMoney(self,money:int):
        self.inputMoney = money
    
    def PrintInputMoney(self):
        print(str(self.inputMoney) +"원")

    def ReturnMoney(self):
        tmp = self.inputMoney
        self.inputMoney = 0
        return tmp

    def ChoiceMenu(self):
        selectedMenu = int(input("메뉴를 선택하세요 : "))
        result = selectedMenu in self.Menu.keys()
        if result:
            if self.inputMoney < self.Menu[selectedMenu].getPrice():
                result = False
                print("투입된 금액이 선택한 {0}의 {1}원 보다 낮습니다.".format(self.Menu[selectedMenu].getName(),self.Menu[selectedMenu].getPrice()))
        return result, selectedMenu

    def OutProduct(self, menu):
        self.Menu[menu].sale()

        print(self.Menu[menu].getName(), "가 나왔습니다.")

        self.inputMoney -= self.Menu[menu].getPrice()
        isContinue = False

        for k, v in self.Menu.items():
            if self.inputMoney > v.getPrice():
                isContinue = True
                break

        return isContinue

    def PrintMenu(self):
        for k, v in self.Menu.items():
            str = "{0}번: {1}\t{2}원\t{3}".format(
                k,
                v.getName(),
                v.getPrice(),
                "" if v.getCount() > 0 else "품절")
            print(str +"\n")