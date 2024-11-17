from HW_VM.Beverage import Beverage
from HW_VM.Menu import Menu
from HW_VM.Admin import Admin


class VendingMachine:
    def __init__(self):
        self.insertMoney = 0

    # 금액 초기화
    def InsertMoneyReset(self):
        self.insertMoney = 0
    
    # 투입하여야 할 금액 표시
    def ShowOrderPrice(self,beverage:Beverage,count:int):
        print(f'{beverage.GetName()}: {beverage.GetPrice():,}원 * {count:,}개 = 총 {beverage.GetPrice()*count:,}원')
        if beverage.GetPrice()*count > self.insertMoney:
            print(f'구입하려면 {beverage.GetPrice()*count - self.insertMoney:,}원 투입하여야 합니다.')
    
    # 판매 할 재고 확인
    def CountCheck(self,menu:Menu,admin:Admin)->bool:
        count = 0
        for _, v in menu.menuDict.items():
            if v.GetCount():
                count += 1
        if count == 0:
            print("판매하고 있는 음료가 없습니다.. 관리자에게 문의 바랍니다.")
            self.ReturnChangeMoney()
            userSelect = input("아무입력을 누르시면 종료됩니다.")
            if userSelect == '999':
                return admin
            else:
                return False
        else:
            return True
    
    # 음료 선택과 관리자 모드 진입
    def SelectMenuOrEnterAdminMode(self, menu:Menu,admin:Admin)->Beverage:
        # 매진되지 않은 메뉴 출력
        print("-------판매중인 음료수 목록-------")
        menu.ShowMenuList(menu.NotSoldOutMenu())
        print(f'{len(menu.NotSoldOutMenu())+1}. 구입 종료')
        # 숫자 입력을 대비한 매진되지 않은 딕셔너리를 리스트로 변경
        tmpMenuList = list(menu.NotSoldOutMenu().items())
        
        # 유저의 입력을 담을 변수
        userSelect = ""

        # 판매대에 올라와 있는 음료가 하나도 없음.

        userSelect = input(f'원하시는 메뉴를 선택하여 주십시오.\t(현재 금액: {self.insertMoney:,}원)').replace(" ","")
        if userSelect == "999":
            return admin

        else:
            # 입력값이 메뉴의 이름(키값)과 일치할 경우
            if userSelect in menu.NotSoldOutMenu().keys():
                return menu.NotSoldOutMenu()[userSelect]
            # 메뉴의 이름도 맞지않고 양수도 아닐경우
            elif userSelect == "종료" or userSelect == "구입종료" or userSelect == str((len(menu.NotSoldOutMenu())+1)):
                return "종료"
            elif not userSelect.isdigit():
                print("잘못된 입력입니다")
                return None
            # 숫자로 주문한 경우
            elif int(userSelect):
                # 팔고 있는 메뉴의 갯수 보다 아래의 입력값을 넣을 경우 (잘 넣은 경우)
                if 1 <= int(userSelect) <= len(tmpMenuList):
                    return tmpMenuList[int(userSelect) - 1][1]
    
    # 금액 투입
    def UserInsertMoney(self)->int:
        tmpMoney = input("금액을 투입하여 주십시오.")
        if not tmpMoney.isdigit():
            print("잘못된 입력입니다.")
            return None
        else:
            print(f'{int(tmpMoney):,}원을 투입하였습니다.')
            self.insertMoney += int(tmpMoney)
            return self.insertMoney

    # 투입한 금액과 구입할 금액 비교
    def CheckChoiceAndMoney(self, userSelect:Beverage,count:int)->bool:
        if self.insertMoney < userSelect.GetPrice() * count:
            print(f'{userSelect.GetName()}을(를) {count:,}개 구입하기에는 '
                  f'{userSelect.GetPrice() * count-self.insertMoney:,}원 부족합니다')
            return False
        else:
            return True
    
    # 구입할 개수 입력
    def CountOrder(self,userSelect:Beverage)->int:
        tmpCount = input("구입할 개수를 기입하여 주십시오.:")

        if tmpCount.isdigit():
            if userSelect.GetCount() >= int(tmpCount):
                return int(tmpCount)
            else:
                print(f'재고가 {int(tmpCount) - userSelect.GetCount():,}개 만큼 부족합니다.')
                return False
        else:
            print("잘못된 입력입니다.")
            return False

    # 음료 계산, 재고 변화
    def CalculateOrder(self, userSelect:Beverage,count:int,menu:Menu)->bool:

        totalPrice = userSelect.GetPrice() * count

        self.insertMoney -= totalPrice

        userSelect.Sales(count)
        menu.totalSalesCount += count
        menu.totalPrice += totalPrice
        print(f'{userSelect.GetName()}을(를) {count:,}개 구입하여 {totalPrice:,}원 소모하였습니다')
        print(f'현재 자판기에 남아있는 금액은 {self.insertMoney:,}원입니다.')
        continueOrder = input("1. 구입한다.\t2. 종료한다.").replace(" ","").rstrip(".")
        if continueOrder == "1" or continueOrder == "구입한다":
            return True
        elif continueOrder == "2" or continueOrder == "종료한다":
            return False
        else:
            print("잘못된 입력을 하여 초기 화면으로 돌아갑니다.")
            return False
    
    # 잔돈 출력하고 입금한 기계 돈 초기화
    def ReturnChangeMoney(self):
        if self.insertMoney > 0:
            print(f'이용해 주셔서 감사합니다. 잔돈은 {self.insertMoney:,}원입니다.')
            self.InsertMoneyReset()
        else:
            print("이용해 주셔서 감사합니다.")
            return None