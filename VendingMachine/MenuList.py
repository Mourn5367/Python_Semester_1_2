from VendingMachine.Beverage import Beverage


def setBeverage():
    menuList = {}
    cola = Beverage("콜라", 2000, 15)
    cider = Beverage("사이다", 1500, 10)
    menuList[cola.getName()] = cola
    menuList[cider.getName()] = cider
    return menuList



