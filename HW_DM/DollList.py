from PIL import Image

from HW_DM.Doll import Doll
from HW_DM.ProductList import ProductList


class DollList(ProductList):
    def __init__(self):
        super().__init__()
        self.SetMenuDict({"A": Doll("A", 1000, 1, 0, Image.open("dollImg/doll1.png")),
                          "B": Doll("B", 1000, 1, 3, Image.open("dollImg/doll2.webp")),
                          "C": Doll("C", 1000, 1, 6, Image.open("dollImg/doll3.webp"))})

    def ShowMenuList(self, selectDict: dict):
        i = 1
        price = 0
        for k, v in selectDict.items():
            print(f'{i}. {v.GetName()}, 재고: {v.GetCount():,}개')
            i += 1
            price = v.GetPrice()
        print(f"1회당 {price}원 입니다. 뽑고 싶은 인형이 있다면 선택하여 주십시오.")

    def GetTotalCount(self) -> int:
        totalCount = 0
        for k , v in self.menuDict.items():
            totalCount += v.GetCount()
        return totalCount