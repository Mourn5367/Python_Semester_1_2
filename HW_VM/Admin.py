from HW_VM.Beverage import Beverage
from HW_VM.Menu import Menu


class Admin:
    def __init__(self):
        pass
    def Admin_SalesReset(self,menu:Menu):

        for k , v in menu.menuDict.items():
            v.ResetSales()
        menu.totalSalesCount = 0
        menu.totalPrice = 0
        print("판매량이 초기화 되었습니다.")

    def Admin_AnalyzeSales(self,menu:Menu, machineTotalSalesCount, machineTotalPrice):
        beverageTotalPrice = 0
        beverageTotalsalesCount = 0
        i = 1
        for k, v in menu.menuDict.items():
            print(f'{i}. {v.GetName()} 판매 개수: {v.GetSales():,}개, 판매 금액: {v.GetSales()*v.GetPrice():,}원')
            beverageTotalPrice += v.GetSales()*v.GetPrice()
            beverageTotalsalesCount += v.GetSales()
            i += 1
        if machineTotalSalesCount != beverageTotalsalesCount:
            print(f'판매 목록에서 사라진 음료 판매 개수:{machineTotalSalesCount - beverageTotalsalesCount:,}개,'
                  f' 판매 금액:{machineTotalPrice - beverageTotalPrice:,}원')
        print("------------------------------------------")
        print(f'총 판매 개수는 {beverageTotalsalesCount + machineTotalSalesCount:,}개 이며 금액은 {beverageTotalPrice + machineTotalPrice:,}원 입니다.')

    def Admin_RestockBeverage(self,menu:Menu):
        # 선택 지문 출력
        userSelect = input("1. 음료수 판매대 재고 채우기.\t2. 음료수 발주 하기(미리 음료수 등록이 되어 있어야함)").replace(" ", "")
        name = ""
        count = 0
        # 판매대에 재고를 채우기 위한 입력을 받았을 때
        if userSelect == "1" or userSelect == "음료수판매대재고채우기" or userSelect == "채우기":
            i = 1  # 순번을 넣기 위한 i
            # 판매대의 키값과 밸류값 받아오기
            for k, v in menu.menuDict.items():
                # 판매대에 팔고있는 이름과 재고 수 출력
                print(f'{i}. {v.GetName()}\t판매대 재고: {v.GetCount():,}개\t', end="")
                # 등록된 음료수라면 보유 재고에서 몇개 있는지 출력
                if k in menu.haveBeverage:
                    print(f'보유 재고: {menu.haveBeverage[k].GetCount():,}개\t', end="")
                # 등록되지 않은 음료수라고 출력
                else:
                    print("보유 재고: 등록되지 않은 음료수입니다.\t", end="")
                i += 1

            print()  # 한줄 띄우기

            # 1. 콜라 판매대 재고: N개 보유 재고 :N개... 출력한 뒤 무슨 음료수의 재고를 넣을 것인지 입력받음
            name = input("재고를 채워 넣을 음료수 이름을 기입하시오.")

            # 만약 입력 받은것이 양수로 입력 받았다면
            if name.isdigit():
                # 딕셔너리의 리스트 형태를 리스트로 변환함
                tmpList = list(menu.menuDict.items())
                # 입력값을 숫자로 형변환 하고 리스트의 길이보다 같거나 작게 바꿈
                # 1. 2. 3. 4. 이렇게 출력 할거라 4개라서 5해도 안되고 0해도 isdigit에 걸림
                if int(name) <= len(tmpList):
                    # 리스트를 통해서 어떤 음료수인지 특정한 다음 이름(key)을 가져와서 판매대의 무슨 음료인지 가져옴
                    tmpBeverage = menu.menuDict[tmpList[int(name) - 1][0]]
                    if tmpBeverage.GetName() not in menu.haveBeverage.keys():
                        print(f'등록된 음료수 중 {tmpBeverage.GetName()}는 없어 음료 재고 충전을 종료합니다.')
                        return
                    # 음료수의 이름, 재고 수를 출력하여 몇개 넣을것인지 입력받음
                    print(f'{tmpBeverage.GetName()}를 몇개 채워넣겠습니까?\n현재({tmpBeverage.GetCount():,}개)', end="")
                    # 판매대에는 있고 등록되지 않은 음료수일수도 있음.
                    if tmpBeverage.GetName() in menu.haveBeverage:
                        count = input(f', 보유({menu.haveBeverage[tmpBeverage.GetName()].GetCount():,}): ')
                    else:
                        count = input(": ")

                    # 입력받은 재고 충전 개수가 숫자인지 확인

                    if count.isdigit():
                        # 충전 개수만큼 보유재고가 있는지 확인
                        if int(count) <= menu.haveBeverage[tmpBeverage.GetName()].GetCount():
                            # 만약 충전 개수만큼 보유재고가 있다면 그만큼 해당 음료수에 재고 수를 추가함.
                            menu.menuDict[tmpBeverage.GetName()].InsertCount(int(count))
                            # 추가한 재고 수 만큼 보유재고는 그만큼 차감함.
                            menu.haveBeverage[tmpBeverage.GetName()].ExtractCount(int(count))
                            print(f'충전되어 판매대에는 {menu.menuDict[tmpBeverage.GetName()].GetCount():,}개 되었고'
                                  f' 보유 재고는 {menu.haveBeverage[tmpBeverage.GetName()].GetCount():,}개 되었습니다. ')
                        else:
                            # 보유재고가 충전 개수보다 작다면 알림을 주고 종료
                            print(
                                f'{menu.haveBeverage[tmpBeverage.GetName()].GetName()}의 보유 재고({menu.haveBeverage[tmpBeverage.GetName()].GetCount():,})가'
                                f' 입력한 {count}보다 적어 재고 충전을 종료합니다.')
                    # 숫자가 아니라면 종료
                    else:
                        print("숫자 또는 양수의 값이 입력 되지 않아 재고 충전을 종료합니다.")
                else:
                    print("잘못된 입력입니다. 재고 충전을 종료합니다.")

            # 입력받은 값이 key값이라면
            elif name in menu.menuDict.keys():

                # 입력받은 음료수 지정
                tmpBeverage = menu.menuDict[name]

                # 해당 음료가 등록되지 않은 음료수라면 종료
                if tmpBeverage.GetName() not in menu.haveBeverage.keys():
                    print(f'등록된 음료수 중 {tmpBeverage.GetName()}는 없어 음료 재고 충전을 종료합니다.')
                    return

                # 맻개 채워 넣을지
                print(f'{tmpBeverage.GetName()}를 몇개 채워넣겠습니까?\n현재({tmpBeverage.GetCount():,}개)', end="")
                if tmpBeverage.GetName() in menu.haveBeverage:
                    count = input(f', 보유({menu.haveBeverage[tmpBeverage.GetName()].GetCount():,}): ')
                else:
                    count = input(": ")

                if count.isdigit():
                    if int(count) <= menu.haveBeverage[tmpBeverage.GetName()].GetCount():
                        menu.menuDict[tmpBeverage.GetName()].InsertCount(int(count))
                        menu.haveBeverage[tmpBeverage.GetName()].ExtractCount(int(count))
                        print(f'충전되어 판매대에는 {menu.menuDict[tmpBeverage.GetName()].GetCount():,}개 되었고'
                              f' 보유 재고는 {menu.haveBeverage[tmpBeverage.GetName()].GetCount():,}개 되었습니다. ')
                    else:
                        print(
                            f'{menu.haveBeverage[tmpBeverage.GetName()].GetName()}의 보유 재고({menu.haveBeverage[tmpBeverage.GetName()].GetCount():,})가'
                            f' 입력한 {count:,}개 보다 적어 재고 충전을 종료합니다.')
                else:
                    print("숫자 또는 양수의 값이 입력 되지 않아 재고 충전을 종료합니다.")
            elif name not in menu.menuDict.keys():
                print(f'판매대에 {name}는 없습니다.')
                print("음료 재고 충전을 종료합니다.")

        # 보유 재고의 음료를 발주한다면
        elif userSelect == "2" or userSelect == "음료수발주하기" or userSelect == "발주":
            i = 1
            # 보유 재고의 딕셔너리를 출력
            for k, v in menu.haveBeverage.items():
                print(f'{i}. {v.GetName()} {v.GetCount():,}개\t', end="")
                i += 1
            print()
            name = input("발주할 음료수 이름을 기입하시오.")
            # 입력을 숫자로 했다면
            if name.isdigit():
                # 딕셔너리를 리스트로 변환
                tmpList = list(menu.haveBeverage.items())
                # 리스트의 갯수보다 입력한 순번이 작은지 확인
                if int(name) <= len(tmpList):
                    # 음료수 특정
                    tmpBeverage = menu.haveBeverage[tmpList[int(name) - 1][0]]
                    count = input(f'{tmpBeverage.GetName()}를 몇개 발주하시겠습니까?\n현재({tmpBeverage.GetCount():,}개): ')
                    # 입력값이 양수라면 그만큼 충전함
                    if count.isdigit():
                        menu.haveBeverage[tmpBeverage.GetName()].InsertCount(int(count))
                        print(f'보유 재고가 {menu.haveBeverage[tmpBeverage.GetName()].GetCount():,}개 되었습니다.')
                    else:
                        print("숫자 또는 양수의 값이 입력 되지 않아 재고 충전을 종료합니다.")

            # 입력을 이름(key)값으로 했다면
            elif name in menu.haveBeverage.keys():
                # 음료수 특정
                tmpBeverage = menu.haveBeverage[name]
                count = input(f'{tmpBeverage.GetName()}를 몇개 발주하시겠습니까?\n현재({tmpBeverage.GetCount():,}개): ')
                if count.isdigit():
                    menu.haveBeverage[name].InsertCount(int(count))
                    print(f'보유 재고가 {menu.haveBeverage[name].GetCount():,}개 되었습니다.')
                else:
                    print("숫자 또는 양수의 값이 입력 되지 않아 재고 충전을 종료합니다.")
            # 매뉴 수보다 큰 수이거나 key값이 아닌 글자일 경우
            elif name not in menu.haveBeverage.keys():
                print(f'등록된 음료수 중 {name}는 없습니다.')
                print("음료 재고 충전을 종료합니다.")
        else:
            print("잘못된 입력으로 재고 충전을 종료합니다.")


    def Admin_NewBeverage(self,menu:Menu):
        name = input("등록할 음료수 이름을 기입하시오.")
        if name.replace(" ", "") in menu.haveBeverage.keys():
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

        menu.haveBeverage[name] = (Beverage(name,price, count))
        print(f'{name} 음료를 등록 하였습니다. 음료수 메뉴 추가를 하시면 판매할 수 있습니다.')

    def Admin_DeleteBeverage(self,menu:Menu):
        name = input("삭제할 음료수 이름을 기입하시오")
        if name.replace(" ", "") not in menu.haveBeverage.keys():
            print("없는 음료수입니다. 음료 삭제를 종료합니다..")
            return
        menu.haveBeverage.pop(name)
        print(f'{name} 음료를 제거 하였습니다. 음료수 메뉴 제거를 하시면 판매를 종료합니다.')

    def CallAdmin(self,menu:Menu):
        print("🛠 관리자 모드 진입 🛠")
        print("현재 메뉴")
        menu.ShowMenuList(menu.menuDict)
        print()
        adminChoice = input("1. 음료수 메뉴 추가\t2. 음료수 메뉴 제거\t3. 음료수 등록\t4. 음료수 삭제\t5. 재고 충전\t6. 판매량 확인\t7. 판매량 초기화\t8. 종료").replace(" ","")
        if adminChoice == "1" or adminChoice == "추가" or adminChoice == "음료수메뉴추가":
            adminChoice = "추가"
            self.Admin_AddOrRemoveMenu(adminChoice)
        elif adminChoice == "2" or adminChoice == "제거" or adminChoice == "음료수메뉴제거":
            adminChoice = "제거"
            self.Admin_AddOrRemoveMenu(adminChoice)
        elif adminChoice == "3" or adminChoice == "등록" or adminChoice == "음료수등록":
            self.Admin_NewBeverage(menu)
        elif adminChoice == "4" or adminChoice == "삭제" or adminChoice == "음료수삭제":
            self.Admin_DeleteBeverage(menu)
        elif adminChoice == "5" or adminChoice == "충전" or adminChoice == "재고충전":
            self.Admin_RestockBeverage(menu)
        elif adminChoice == "6" or adminChoice == "확인" or adminChoice == "판매량확인":
            self.Admin_AnalyzeSales(menu,menu.totalSalesCount,menu.totalPrice)
        elif adminChoice == "7" or adminChoice == "초기화" or adminChoice == "판매량초기화":
            self.Admin_SalesReset(menu)
        elif adminChoice == "8" or adminChoice == "종료":
            print("설정을 종료 하겠습니다.")
        else:
            print("잘못된 입력입니다.")

    def Admin_AddOrRemoveMenu(self,menu:Menu, select):
        tmpDict = {}
        tmpList = []
        adminChoice = ""

        if select == "추가":
            tmpDict =  menu.haveBeverage
            tmpList =  list(menu.haveBeverage.items())
            menu.ShowMenuList(tmpDict)
            adminChoice = input("판매할 음료수를 선택하시오.")

        elif select == "제거":
            tmpDict = menu.menuDict
            tmpList = list(menu.menuDict.items())
            menu.ShowMenuList(tmpDict)

            if len(tmpDict) != 0:
                adminChoice = input("제거할 음료수를 선택하시오.")

            else:
                print("제거할 음료수가 없습니다.")
                return

        if adminChoice in tmpDict.keys():
            if select == "추가":

                if adminChoice not in menu.menuDict.keys():
                    menu.menuDict[adminChoice] = tmpDict[adminChoice]
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
                    if adminChoice not in menu.menuDict.keys():
                        menu.menuDict[adminChoice] = tmpDict[adminChoice]
                    else:
                        print("이미 추가되어 있습니다.")

                elif select == "제거":
                    tmpDict.pop(adminChoice)
