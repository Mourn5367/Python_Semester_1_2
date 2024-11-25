from HM_NEW_DM.DollBox import DollBox
from HM_NEW_DM.DollList import DollList
from HM_NEW_DM.Admin import Admin
from HM_NEW_DM.Product import Product
from HM_NEW_DM.Machine import Machine

class DollMachine(Machine):
    def __init__(self):
        super().__init__()
        self.dollBox = DollBox()

    def SelectMenuOrEnterAdminMode(self, dollList: DollList, admin: Admin,productsName) -> Product:
        self.dollBox.RefreshBox(dollList)
        return super().SelectMenuOrEnterAdminMode(dollList,admin,productsName)
