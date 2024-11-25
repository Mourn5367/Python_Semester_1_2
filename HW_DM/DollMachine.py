from HM_NEW_DM import DollBox
from HW_DM import ProductList, Admin, Product
from HW_DM.Machine import Machine


class DollMachine(Machine):
    def __init__(self):
        super().__init__()

    def SelectMenuOrEnterAdminMode(self, productList: ProductList, admin: Admin,productsName,dollBox:DollBox) -> Product:
        dollBox.RefreshBox()
        super().SelectMenuOrEnterAdminMode(productList,admin,productsName)

