
from HW_VM.Beverage import Beverage

class Menu:
    def __init__(self):
        self.menuDict = {"콜라":Beverage("콜라",2000,2000),
                         "사이다":Beverage("콜라",2000,0),
                         "사이다1":Beverage("콜라",2000,2000)}
        self.haveBeverage = {"콜라":Beverage("콜라",2000,15),
                             "사이다":Beverage("사이다",1500,10),
                             "생수":Beverage("생수",1000,20)}


    # def setBeverage(self):
    #     i = 1
    #     for k, v in self.haveBeverage.items():
    #         print(f'{i}. {v.getName()} 가격: {v.getPrice()}, 재고: {v.getCount()}')
    #         i += 1
    #     haveBeverageList = list(self.haveBeverage.items())
    #
    #     adminChoice = input("판매할 음료수를 선택하시오.")
    #
    #     if adminChoice in self.haveBeverage.keys():
    #         self.addBeverage(adminChoice)
    #     elif int(adminChoice):
    #         if 1 <= int(adminChoice) <= len(haveBeverageList):
    #             adminChoice = int(adminChoice) - 1
    #             adminChoice = haveBeverageList[adminChoice][0] #이때 String 타입변경
    #             self.addMenuBeverage(adminChoice)
    #         else:
    #             print("그런 음료수는 없습니다.")
    #     else:
    #         print("그런 음료수는 없습니다.")

    def NewBeverage(self):
        name = input("추가할 음료수 이름을 기입하시오")
        price = input(f'{name}의 가격을 입력하시오.')
        if not price.isdigit():
            print("숫자 또는 양수의 값이 입력 되지 않아 음료 추가를 종료합니다.")
            return
        else:
            price = int(price)
        count = input(f'{name}의 재고량을 입력하시오.')
        if not count.isdigit():
            print("숫자 또는 양수의 값이 입력 되지 않아 음료 추가를 종료합니다.")
        else:
            count = int(count)
        self.haveBeverage[name] = (Beverage(name,price, count))

    def CallAdmin(self):
        print("🛠 관리자 모드 진입 🛠")
        print("현재 메뉴")
        self.Admin_ShowMenuList(self.menuDict)
        print()
        adminChoice = input("1. 음료수 추가\t2. 음료수 제거\t3. 종료").replace(" ","")
        if adminChoice == "1" or adminChoice == "추가" or adminChoice == "음료수추가":
            adminChoice = "추가"
            self.Admin_AddOrRemoveMenu(adminChoice)
        elif adminChoice == "2" or adminChoice == "제거" or adminChoice == "음료수제거":
            adminChoice = "제거"
            self.Admin_AddOrRemoveMenu(adminChoice)
        elif adminChoice == "3" or adminChoice == "종료":
            print("설정을 종료 하겠습니다.")
        else:
            print("잘못된 입력입니다.")

    def Admin_ShowMenuList(self, selectDict:dict):
        i = 1
        if len(selectDict) != 0:
            for k, v in selectDict.items():
                    print(f'{i}. {v.getName()} 가격: {v.getPrice()}, 재고: {v.getCount()}')
                    i += 1
        else:
            print("비어있습니다.")
    def ShowMenuList(self, selectDict:dict):
        i = 1
        if len(selectDict) != 0:
            for k, v in selectDict.items():
                if not v.getCount() <= 0:
                    print(f'{i}. {v.getName()} 가격: {v.getPrice()}, 재고: {v.getCount()}')
                i += 1
        else:
            print("비어있습니다.")
    def Admin_AddOrRemoveMenu(self, select):
        tmpDict = {}
        tmpList = []
        adminChoice = ""

        if select == "추가":
            tmpDict =  self.haveBeverage
            tmpList =  list(self.haveBeverage.items())
            self.Admin_ShowMenuList(tmpDict)
            adminChoice = input("판매할 음료수를 선택하시오.")

        elif select == "제거":
            tmpDict = self.menuDict
            tmpList = list(self.menuDict.items())
            self.Admin_ShowMenuList(tmpDict)

            if len(tmpDict) != 0:
                adminChoice = input("제거할 음료수를 선택하시오.")

            else:
                print("제거할 음료수가 없습니다.")
                return

        if adminChoice in tmpDict.keys():
            if select == "추가":

                if adminChoice not in self.menuDict.keys():
                    self.menuDict[adminChoice] = tmpDict[adminChoice]
                else:
                    print("이미 추가되어 있습니다.")

            elif select == "제거":
                tmpDict.pop(adminChoice)

        elif int(adminChoice):
            if 1 <= int(adminChoice) <= len(tmpList):
                adminChoice = int(adminChoice) - 1
                adminChoice = tmpList[adminChoice][0]  # 이때 String 타입변경

                if select == "추가":
                    if adminChoice not in self.menuDict.keys():
                        self.menuDict[adminChoice] = tmpDict[adminChoice]
                    else:
                        print("이미 추가되어 있습니다.")

                elif select == "제거":
                    tmpDict.pop(adminChoice)
    def RemoveZeroCount(self):
        for i, v in self.menuDict.items():
            if v.getCount() == 0:
                self.menuDict.pop(i)
    # def addMenuBeverage(self):
    #     haveBeverageList = list(self.haveBeverage.items())
    #     adminChoice = input("판매할 음료수를 선택하시오.")
    #
    #     if adminChoice in self.haveBeverage.keys():
    #         self.menuDict[adminChoice] = self.haveBeverage[adminChoice] # 이때 변경됨
    #     elif int(adminChoice):
    #         if 1 <= int(adminChoice) <= len(haveBeverageList):
    #             adminChoice = int(adminChoice) - 1
    #             adminChoice = haveBeverageList[adminChoice][0] #이때 String 타입변경
    #             self.menuDict[adminChoice] = self.haveBeverage[adminChoice] # 이때 변경됨
    #         else:
    #             print("그런 음료수는 없습니다.")
    #     else:
    #         print("그런 음료수는 없습니다.")
    #
    # def removeMenuBeverage(self):
    #     menuList = list(self.menuDict.items())
    #     if  len(menuList) != 0:
    #         adminChoice = input("제거할 음료수를 선택하시오.")
    #
    #         if adminChoice in self.menuDict.keys():
    #             self.menuDict.pop(adminChoice)
    #         elif int(adminChoice):
    #             if 1 <= int(adminChoice) <= len(menuList):
    #                 adminChoice = int(adminChoice) - 1
    #                 adminChoice = menuList[adminChoice][0] #이때 String 타입변경
    #                 self.menuDict.pop(adminChoice)
    #             else:
    #                 print("그런 음료수는 없습니다.")
    #         else:
    #             print("그런 음료수는 없습니다.")
    #     else:
    #         print("제거할 음료수가 없습니다.")
