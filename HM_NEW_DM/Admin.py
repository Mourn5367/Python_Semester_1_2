from HM_NEW_DM.Product import Product
from HM_NEW_DM.ProductList import ProductList


class Admin:
    def __init__(self,productType = "판매할 종류"):
        self.productType = productType

    def SetProductType(self, productType:str):
        self.productType = productType
    def GetProductType(self):
        return self.productType
    # 판매할 종류 판매 개수 초기화
    def Admin_SalesReset(self, menu: ProductList):

        for k, v in menu.menuDict.items():
            v.ResetSales()
        menu.totalSalesCount = 0
        menu.totalPrice = 0
        print("판매량이 초기화 되었습니다.")

    # 판매할 종류 판매량 분석
    def Admin_AnalyzeSales(self, menu: ProductList, machineTotalSalesCount, machineTotalPrice):
        ProductTotalPrice = 0
        ProductTotalsalesCount = 0
        i = 1
        for k, v in menu.menuDict.items():
            print(f'{i}. {v.GetName()} 판매 개수: {v.GetSales():,}개, 판매 금액: {v.GetSales() * v.GetPrice():,}원')
            ProductTotalPrice += v.GetSales() * v.GetPrice()
            ProductTotalsalesCount += v.GetSales()
            i += 1
        if machineTotalSalesCount != ProductTotalsalesCount:
            print(f'판매 목록에서 사라진 {self.productType} 판매 개수:{machineTotalSalesCount - ProductTotalsalesCount:,}개,'
                  f' 판매 금액:{machineTotalPrice - ProductTotalPrice:,}원')
            print("------------------------------------------")
            print(
                f'총 판매 개수는 {ProductTotalsalesCount + machineTotalSalesCount:,}개 이며 금액은 {ProductTotalPrice + machineTotalPrice:,}원 입니다.')
        else:
            print("------------------------------------------")
            print(f'총 판매 개수는 {ProductTotalsalesCount:,}개 이며 금액은 {ProductTotalPrice:,}원 입니다.')

    # 현재 판매중인 판매할 종류 출력, 보유하고 있는 판매할 종류 출력
    def Admin_ShowCount(self, menu: ProductList, menuDictOrhaveDict: dict):

        if menuDictOrhaveDict == menu.menuDict:
            # 판매대의 키값과 밸류값 받아오기
            for i, (k, v) in enumerate(menu.menuDict.items(), 1):
                # 판매대에 팔고있는 이름과 재고 수 출력
                print(f'{i}. {v.GetName()}\t판매대 재고: {v.GetCount():,}개\t', end="")
                # 등록된 판매할 종류라면 보유 재고에서 몇개 있는지 출력
                if k in menu.haveDict:
                    print(f'보유 재고: {menu.haveDict[k].GetCount():,}개\t', end="")
                # 등록되지 않은 판매할 종류 라고 출력
                else:
                    print(f"보유 재고: 등록되지 않은 {self.productType}입니다.\t", end="")
            print()  # 한줄 띄우기
        elif menuDictOrhaveDict == menu.haveDict:
            # 보유 재고의 딕셔너리를 출력
            for i, (k, v) in enumerate(menu.haveDict.items(), 1):
                print(f'{i}. {v.GetName()} {v.GetCount():,}개\t', end="")
            print()

    # 보유하지 않은 판매할 종류일 경우
    def isHaveProduct(self, product: Product, haveDict: dict) -> bool:
        if product.GetName() not in haveDict.keys():
            print(f'등록된 {self.productType} 중 {product.GetName()}는 없어 {self.productType} 재고 충전을 종료합니다.')
            return False
        else:
            return True

    # 충전 개수가 숫자값으로 들어 올 때
    def isCountDigit(self, count, product: Product, menu: ProductList):
        if count.isdigit():
            # 충전 개수만큼 보유재고가 있는지 확인
            if int(count) <= menu.haveDict[product.GetName()].GetCount():
                # 만약 충전 개수만큼 보유재고가 있다면 그만큼 해당 판매할 종류에 재고 수를 추가함.
                menu.menuDict[product.GetName()].InsertCount(int(count))
                # 추가한 재고 수 만큼 보유재고는 그만큼 차감함.
                menu.haveDict[product.GetName()].ExtractCount(int(count))
                print(f'재고가 충전되어 판매대에는 {menu.menuDict[product.GetName()].GetCount():,}개 되었고'
                      f' 보유 재고는 {menu.haveDict[product.GetName()].GetCount():,}개 되었습니다. ')
            else:
                # 보유재고가 충전 개수보다 작다면 알림을 주고 종료
                print(
                    f'{menu.haveDict[product.GetName()].GetName()}의 보유 재고({menu.haveDict[product.GetName()].GetCount():,})개 가'
                    f' 입력한 {int(count):,}개 보다 적어 재고 충전을 종료합니다.')
            # 숫자가 아니라면 종료
        else:
            print("숫자 또는 양수의 값이 입력 되지 않아 재고 충전을 종료합니다.")

    def Admin_RestockProduct(self, menu: ProductList):
        # 선택 지문 출력
        userSelect = input(f"1. {self.productType} 판매대 재고 채우기.\t"
                           f"2. {self.productType} 발주 하기(미리 {self.productType} 등록이 되어 있어야함)").replace(" ", "")
        # 판매대에 재고를 채우기 위한 입력을 받았을 때
        if userSelect == "1" or userSelect == f"{self.productType}판매대재고채우기" or userSelect == "채우기":
            # 현재 판매대의 재고현황과 보충할수있는 재고 물량 표시
            self.Admin_ShowCount(menu, menu.menuDict)
            # 1. 콜라 판매대 재고: N개 보유 재고 :N개... 출력한 뒤 무슨 판매할 종류의 재고를 넣을 것인지 입력받음
            name = input(f"재고를 채워 넣을 {self.productType} 이름을 기입하시오.")

            # 만약 입력 받은것이 양수로 입력 받았다면
            if name.isdigit():
                # 딕셔너리의 리스트 형태를 리스트로 변환함
                tmpList = list(menu.menuDict.items())
                # 입력값을 숫자로 형변환 하고 리스트의 길이보다 같거나 작게 바꿈
                # 1. 2. 3. 4. 이렇게 출력 할거라 4개라서 5해도 안되고 0해도 isdigit에 걸림
                if int(name) <= len(tmpList):
                    # 리스트를 통해서 어떤 판매할 종류인지 특정한 다음 이름(key)을 가져와서 판매대의 무슨 판매할 종류인지 가져옴
                    tmpProduct = menu.menuDict[tmpList[int(name) - 1][0]]
                    if not self.isHaveProduct(tmpProduct, menu.haveDict):
                        return
                    # 판매할 종류의 이름, 재고 수를 출력하여 몇개 넣을것인지 입력받음
                    print(f'{tmpProduct.GetName()}를 몇개 채워넣겠습니까?\n현재({tmpProduct.GetCount():,}개)', end="")
                    # 판매대에는 있고 등록되지 않은 판매할 종류일수도 있음.
                    if tmpProduct.GetName() in menu.haveDict:
                        count = input(f', 보유({menu.haveDict[tmpProduct.GetName()].GetCount():,}): ')
                    else:
                        count = input(": ")

                    # 입력받은 재고 충전 개수가 숫자인지 확인
                    self.isCountDigit(count, tmpProduct, menu)
                else:
                    print("잘못된 입력입니다. 재고 충전을 종료합니다.")

            # 입력받은 값이 key값이라면
            elif name in menu.menuDict.keys():

                # 입력받은 판매할 종류 지정
                tmpProduct = menu.menuDict[name]

                # 해당 판매할 종류가 등록되지 않은 판매할 종류라면 종료
                if not self.isHaveProduct(tmpProduct, menu.haveDict):
                    return

                # 맻개 채워 넣을지
                print(f'{tmpProduct.GetName()}를 몇개 채워넣겠습니까?\n현재({tmpProduct.GetCount():,}개)', end="")
                if tmpProduct.GetName() in menu.haveDict:
                    count = input(f', 보유({menu.haveDict[tmpProduct.GetName()].GetCount():,}): ')
                else:
                    count = input(": ")

                # 입력받은 재고 충전 개수가 숫자인지 확인
                self.isCountDigit(count, tmpProduct, menu)

            elif name not in menu.menuDict.keys():
                print(f'판매대에 {name}는 없습니다.')
                print(f"{self.productType} 재고 충전을 종료합니다.")

        # 보유 재고의 판매할 종류를 발주한다면
        elif userSelect == "2" or userSelect == f"{self.productType}발주하기" or userSelect == "발주":
            self.Admin_ShowCount(menu, menu.haveDict)
            name = input(f"발주할 {self.productType} 이름을 기입하시오.")
            # 입력을 숫자로 했다면
            if name.isdigit():
                # 딕셔너리를 리스트로 변환
                tmpList = list(menu.haveDict.items())
                # 리스트의 갯수보다 입력한 순번이 작은지 확인
                if int(name) <= len(tmpList):
                    # 판매할 종류 특정
                    tmpProduct = menu.haveDict[tmpList[int(name) - 1][0]]
                    count = input(f'{tmpProduct.GetName()}를 몇개 발주하시겠습니까?\n현재({tmpProduct.GetCount():,}개): ')
                    # 입력값이 양수라면 그만큼 충전함
                    if count.isdigit():
                        menu.haveDict[tmpProduct.GetName()].InsertCount(int(count))
                        print(f'보유 재고가 {menu.haveDict[tmpProduct.GetName()].GetCount():,}개 되었습니다.')
                    else:
                        print("숫자 또는 양수의 값이 입력 되지 않아 재고 충전을 종료합니다.")

            # 입력을 이름(key)값으로 했다면
            elif name in menu.haveDict.keys():
                # 판매할 종류 특정
                tmpProduct = menu.haveDict[name]
                count = input(f'{tmpProduct.GetName()}를 몇개 발주하시겠습니까?\n현재({tmpProduct.GetCount():,}개): ')
                if count.isdigit():
                    menu.haveDict[name].InsertCount(int(count))
                    print(f'보유 재고가 {menu.haveDict[name].GetCount():,}개 되었습니다.')
                else:
                    print("숫자 또는 양수의 값이 입력 되지 않아 재고 충전을 종료합니다.")
            # 매뉴 수보다 큰 수이거나 key값이 아닌 글자일 경우
            elif name not in menu.haveDict.keys():
                print(f'등록된 {self.productType} 중 {name}는 없습니다.')
                print(f"{self.productType} 재고 충전을 종료합니다.")
        else:
            print("잘못된 입력으로 재고 충전을 종료합니다.")

    def Admin_NewProduct(self, menu: ProductList):
        name = input(f"등록할 {self.productType} 이름을 기입하시오.")
        if name.replace(" ", "") in menu.haveDict.keys():
            print(f"이미 등록된 {self.productType}입니다. 등록을 종료합니다.")
            return
        price = input(f'{name}의 가격을 입력하시오.')
        if not price.isdigit():
            print(f"숫자 또는 양수의 값이 입력 되지 않아 {self.productType} 등록을 종료합니다.")
            return
        else:
            price = int(price)
        count = input(f'{name}의 재고량을 입력하시오.')
        if not count.isdigit():
            print(f"숫자 또는 양수의 값이 입력 되지 않아 {self.productType} 등록을 종료합니다.")
        else:
            count = int(count)

        menu.haveDict[name] = (Product(name, price, count))
        print(f'{name} {self.productType}를 등록 하였습니다.{self.productType} 메뉴 추가를 하시면 판매할 수 있습니다.')

    def Admin_DeleteProduct(self, menu: ProductList):
        menu.ShowMenuList(menu.haveDict)
        name = input(f"삭제할 {self.productType} 이름을 기입하시오")
        if name.isdigit():
            tmpList = list(menu.haveDict.items())
            if int(name) <= len(tmpList):
                tmpProduct = menu.haveDict[tmpList[int(name) - 1][0]]
                name = tmpProduct.GetName()
        elif name.replace(" ", "") not in menu.haveDict.keys():
            print(f"없는 {self.productType}입니다. {self.productType} 삭제를 종료합니다..")
            return
        menu.haveProduct.pop(name)
        print(f'{name} {self.productType}를 제거 하였습니다. {self.productType} 메뉴 제거를 하시면 판매를 종료합니다.')

    def CallAdmin(self, menu: ProductList):
        print("🛠 관리자 모드 진입 🛠")
        print("현재 메뉴")
        menu.ShowMenuList(menu.menuDict)
        print()
        adminChoice = input(
            f"1. {self.productType} 메뉴 추가\t2. {self.productType} 메뉴 제거\t"
            f"3. {self.productType} 등록\t4. {self.productType} 삭제\t"
            f"5. 재고 충전\t6. 판매량 확인\t7. 판매량 초기화\t"
            f"8. 설정 종료\t9. 기계 종료").replace(" ", "")
        if adminChoice == "1" or adminChoice == "추가" or adminChoice == f"{self.productType}메뉴추가":
            adminChoice = "추가"
            self.Admin_AddOrRemoveMenu(menu, adminChoice)
            return None
        elif adminChoice == "2" or adminChoice == "제거" or adminChoice == f"{self.productType}메뉴제거":
            adminChoice = "제거"
            self.Admin_AddOrRemoveMenu(menu, adminChoice)
            return None
        elif adminChoice == "3" or adminChoice == "등록" or adminChoice == f"{self.productType}등록":
            self.Admin_NewProduct(menu)
            return None
        elif adminChoice == "4" or adminChoice == "삭제" or adminChoice == f"{self.productType}삭제":
            self.Admin_DeleteProduct(menu)
            return None
        elif adminChoice == "5" or adminChoice == "충전" or adminChoice == "재고충전":
            self.Admin_RestockProduct(menu)
            return None
        elif adminChoice == "6" or adminChoice == "확인" or adminChoice == "판매량확인":
            self.Admin_AnalyzeSales(menu, menu.totalSalesCount, menu.totalPrice)
            return None
        elif adminChoice == "7" or adminChoice == "초기화" or adminChoice == "판매량초기화":
            self.Admin_SalesReset(menu)
            return None
        elif adminChoice == "8" or adminChoice == "설정종료":
            print("설정을 종료 하겠습니다.")
            return "설정 종료"
        elif adminChoice == "9" or adminChoice == "기계종료":
            print("자판기 판매를 종료합니다.")
            return "자판기 종료"
        else:
            print("잘못된 입력입니다.")
            return "다시"

    def Admin_AddOrRemoveMenu(self, menu: ProductList, select):
        tmpDict = {}
        tmpList = []
        adminChoice = ""

        if select == "추가":
            tmpDict = menu.haveDict
            tmpList = list(menu.haveDict.items())
            menu.ShowMenuList(tmpDict)
            adminChoice = input(f"판매할 {self.productType}를 선택하시오.")

        elif select == "제거":
            tmpDict = menu.menuDict
            tmpList = list(menu.menuDict.items())
            menu.ShowMenuList(tmpDict)

            if len(tmpDict) != 0:
                adminChoice = input(f"제거할 {self.productType}를 선택하시오.")

            else:
                print(f"제거할 {self.productType}가 없습니다.")
                return

        if adminChoice in tmpDict.keys():
            tmpProduct = tmpDict[adminChoice]
            if select == "추가":

                if adminChoice not in menu.menuDict.keys():
                    menu.menuDict[tmpProduct.GetName()] = Product(tmpProduct.GetName(), tmpProduct.GetPrice(),
                                                                    tmpProduct.GetCount())
                    menu.haveDict[tmpProduct.GetName()].ExtractCount(tmpProduct.GetCount())
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
                tmpProduct = tmpDict[adminChoice]
                if select == "추가":
                    if adminChoice not in menu.menuDict.keys():
                        menu.menuDict[tmpProduct.GetName()] = Product(tmpProduct.GetName(), tmpProduct.GetPrice(),
                                                                        tmpProduct.GetCount())
                        menu.haveDict[tmpProduct.GetName()].ExtractCount(tmpProduct.GetCount())
                    else:
                        print("이미 추가되어 있습니다.")

                elif select == "제거":
                    tmpDict.pop(adminChoice)
