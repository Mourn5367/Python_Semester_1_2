from HW_VM.Beverage import Beverage

class Menu:
    def __init__(self):
        self.menuDict = {"콜라":Beverage("콜라",2000,0),
                         "사이다":Beverage("사이다",1500,0),
                         "보리차":Beverage("보리차",2000,0)}
        self.haveBeverage = {"콜라":Beverage("콜라",2000,150),
                             "사이다":Beverage("사이다",1500,100),
                             "보리차":Beverage("보리차",2000,100),
                             "포카리":Beverage("포카리",3000,200)}
        self.totalSalesCount = 0
        self.totalPrice = 0
    
    # 매진되지 않은 메뉴 출력
    def NotSoldOutMenu(self)->dict:
        notSoldOutMenu = {}
        for k, v in self.menuDict.items():
            if v.GetCount() > 0:
                notSoldOutMenu[k] = v
        return notSoldOutMenu

    # 매진 된 것까지 출력
    def ShowMenuList(self, selectDict:dict):
        i = 1
        for k, v in selectDict.items():
            print(f'{i}. {v.GetName()} 가격: {v.GetPrice():,}원, 재고: {v.GetCount():,}개')
            i += 1
