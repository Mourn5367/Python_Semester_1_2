from PIL import Image

from HW_DM.Doll import Doll
from HW_DM.ProductList import ProductList


class DollList(ProductList):
    def __init__(self):
        super().__init__()
        self.SetMenuDict({"A": Doll("A",1000,10,[0,0],Image.open("doll1.png"))})