class ProductList:
    def __init__(self):
        self.menuDict = {}
        self.haveDict = {}
        self.totalSalesCount = 0
        self.totalPrice = 0

    # 매진되지 않은 메뉴 출력
    def NotSoldOutMenu(self) -> dict:
        notSoldOutMenu = {}
        for k, v in self.menuDict.items():
            if v.GetCount() > 0:
                notSoldOutMenu[k] = v
        return notSoldOutMenu

    # 매진 된 것까지 출력
    def ShowMenuList(self, selectDict: dict):
        i = 1
        for k, v in selectDict.items():
            print(f'{i}. {v.GetName()} 가격: {v.GetPrice():,}원, 재고: {v.GetCount():,}개')
            i += 1

    def SetMenuDict(self, menuDict: dict):
        self.menuDict = menuDict

    def SetHaveDict(self, haveDict: dict):
        self.haveDict = haveDict