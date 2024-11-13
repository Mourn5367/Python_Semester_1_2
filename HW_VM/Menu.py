from urllib.response import addbase

from HW_VM.Beverage import Beverage

class Menu:
    def __init__(self):
        self.menuList = {}
        self.haveBeverage = {"콜라":Beverage("콜라",2000,15),
                             "사이다":Beverage("사이다",1500,10),
                             "생수":Beverage("생수",1000,20)}


    def setBeverage(self):
        i = 1
        for k, v in self.haveBeverage.items():
            print(f'{i}. {v.getName()} 가격: {v.getPrice()}, 재고: {v.getCount()}')
            i += 1
        haveBeverageList = list(self.haveBeverage.items())

        adminChoice = input("판매할 음료수를 선택하시오.")

        if adminChoice in self.haveBeverage.keys():
            self.addBeverage(adminChoice)
        elif int(adminChoice):
            if 1 <= int(adminChoice) <= len(haveBeverageList):
                adminChoice = int(adminChoice) - 1
                adminChoice = haveBeverageList[adminChoice][0] #이때 String 타입변경
                self.addBeverage(adminChoice)
            else:
                print("그런 음료수는 없습니다.")
        else:
            print("그런 음료수는 없습니다.")

    def newBeverage(self):
        name = input("추가할 음료수 이름을 기입하시오")
        price = int(input(f'{name}의 가격을 입력하시오.'))
        count = int(input(f'{name}의 재고량을 입력하시오.'))
        self.haveBeverage[name] = (Beverage(name,price, count))

    def addBeverage(self,choice):
        self.menuList[choice] = self.haveBeverage[choice]