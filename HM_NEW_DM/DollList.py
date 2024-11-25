from PIL import Image
from HM_NEW_DM.Doll import Doll
from HM_NEW_DM.ProductList import ProductList

class DollList(ProductList):
    def __init__(self):
        super().__init__()
        self.SetMenuDict({"A": Doll("A", 1000, 1, 0, Image.open("dollImg/doll1.png")),
                          "B": Doll("B", 1000, 1, 3, Image.open("dollImg/doll2.webp")),
                          "C": Doll("C", 1000, 1, 6, Image.open("dollImg/doll3.webp"))})

        self.SetHaveDict({"A": Doll("A", 1000, 10, 0, Image.open("dollImg/doll1.png")),
                          "B": Doll("B", 1000, 10, 3, Image.open("dollImg/doll2.webp")),
                          "C": Doll("C", 1000, 10, 6, Image.open("dollImg/doll3.webp"))})