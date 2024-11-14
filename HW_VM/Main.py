
from HW_VM.Menu import Menu
from HW_VM.VendingMachine import VendingMachine

if __name__ == '__main__':
    menu = Menu()
    VM =  VendingMachine()
    #menu.setBeverage()\
    while True:
       # ㅁㄴㅇ= VM.SelectMenuOrEnterAdminMode(menu)
        menu.RestockBeverage()
    # menu.addBeverage("콜라")
    # menu.addBeverage(1)

