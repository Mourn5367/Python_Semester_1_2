
from HW_VM.Beverage import Beverage

class Menu:
    def __init__(self):
        self.menuDict = {"콜라":Beverage("콜라",2000,2000),
                         "사이다":Beverage("사이다",2000,0),
                         "사이다1":Beverage("사이다1",2000,2000)}
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
    def RestockBeverage(self, count):
        userSelect = input("1. 음료수 판매대 재고 채우기.\t2. 음료수 발주 하기(미리 음료수 등록이 되어 있어야함)").replace("", " ")
        name = ""
        if userSelect == "1" or userSelect == "음료수판매대재고채우기" or userSelect == "채우기":
            name = input("재고를 채워 넣을 음료수 이름을 기입하시오.")
            if name not in self.menuDict.keys():
                print(f'판매대에 {name}의 음료수는 없습니다.')
                
        elif userSelect == "2"or userSelect == "음료수발주하기" or userSelect == "발주":
            name = input("발주할 음료수 이름을 기입하시오.")
            if name not in self.haveBeverage.keys():
                print(f'{name} 음료수는 등록되지 않은 음료수입니다.')


    def NotSoldOutMenu(self)->dict:
        notSoldOutMenu = {}
        for k, v in self.menuDict.items():
            if v.getCount() > 0:
                notSoldOutMenu[k] = v
        return notSoldOutMenu

    def NewBeverage(self):
        name = input("등록할 음료수 이름을 기입하시오.")
        if name.replace(" ", "") in self.haveBeverage.keys():
            print("이미 등록된 음료수입니다. 등록을 종료합니다.")
            return
        price = input(f'{name}의 가격을 입력하시오.')
        if not price.isdigit():
            print("숫자 또는 양수의 값이 입력 되지 않아 음료 등록을 종료합니다.")
            return
        else:
            price = int(price)
        count = input(f'{name}의 재고량을 입력하시오.')
        if not count.isdigit():
            print("숫자 또는 양수의 값이 입력 되지 않아 음료 등록을 종료합니다.")
        else:
            count = int(count)
        self.haveBeverage[name] = (Beverage(name,price, count))
        print(f'{name} 음료를 등록 하였습니다. 음료수 메뉴 추가를 하시면 판매할 수 있습니다.')
    def DeleteBeverage(self):
        name = input("삭제할 음료수 이름을 기입하시오")
        if name.replace(" ", "") not in self.haveBeverage.keys():
            print("없는 음료수입니다. 음료 삭제를 종료합니다..")
            return
        self.haveBeverage.pop(name)
        print(f'{name} 음료를 제거 하였습니다. 음료수 메뉴 제거를 하시면 판매를 종료합니다.')
    def CallAdmin(self):
        print("🛠 관리자 모드 진입 🛠")
        print("현재 메뉴")
        self.ShowMenuList(self.menuDict)
        print()
        adminChoice = input("1. 음료수 메뉴 추가\t2. 음료수 메뉴 제거\t3. 음료수 등록\t4. 음료수 삭제\t5. 종료").replace(" ","")
        if adminChoice == "1" or adminChoice == "추가" or adminChoice == "음료수메뉴추가":
            adminChoice = "추가"
            self.Admin_AddOrRemoveMenu(adminChoice)
        elif adminChoice == "2" or adminChoice == "제거" or adminChoice == "음료수메뉴제거":
            adminChoice = "제거"
            self.Admin_AddOrRemoveMenu(adminChoice)
        elif adminChoice == "3" or adminChoice == "등록" or adminChoice == "음료수등록":
            self.NewBeverage()
        elif adminChoice == "4" or adminChoice == "삭제" or adminChoice == "음료수삭제":
            self.DeleteBeverage()
        elif adminChoice == "5" or adminChoice == "종료":
            print("설정을 종료 하겠습니다.")
        else:
            print("잘못된 입력입니다.")

    def ShowMenuList(self, selectDict:dict):
        i = 1
        for k, v in selectDict.items():
            print(f'{i}. {v.getName()} 가격: {v.getPrice()}, 재고: {v.getCount()}')
            i += 1
    def Admin_AddOrRemoveMenu(self, select):
        tmpDict = {}
        tmpList = []
        adminChoice = ""

        if select == "추가":
            tmpDict =  self.haveBeverage
            tmpList =  list(self.haveBeverage.items())
            self.ShowMenuList(tmpDict)
            adminChoice = input("판매할 음료수를 선택하시오.")

        elif select == "제거":
            tmpDict = self.menuDict
            tmpList = list(self.menuDict.items())
            self.ShowMenuList(tmpDict)

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

        elif not adminChoice.isdigit():
            print("잘못된 입력입니다.")

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
