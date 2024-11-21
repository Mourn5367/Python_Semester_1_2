from HW_DM.Admin import Admin
from HW_DM.ProductList import ProductList
from HW_DM.Product import Product

class Machine:
    def __init__(self):
        self.insertMoney = 0

    # 금액 초기화
    def InsertMoneyReset(self):
        self.insertMoney = 0

    def ShowOrderPrice(self, Product: Product, count: int):
        print(f'{Product.GetName()}: {Product.GetPrice():,}원 * {count:,}개 = 총 {Product.GetPrice() * count:,}원')
        if Product.GetPrice() * count > self.insertMoney:
            print(f'구입하려면 {Product.GetPrice() * count - self.insertMoney:,}원 투입하여야 합니다.')

    # 판매 할 재고 확인
    def CountCheck(self, menu: ProductList, admin: Admin, productsName) -> bool:
        count = 0
        for _, v in menu.menuDict.items():
            if v.GetCount():
                count += 1
        if count == 0:
            print(f"판매하고 있는 {productsName}가 없습니다.. 관리자에게 문의 바랍니다.")
            self.ReturnChangeMoney()
            userSelect = input("아무입력을 누르시면 종료됩니다.")
            if userSelect == '999':
                return admin
            else:
                return False
        else:
            return True

    # 금액 투입
    def UserInsertMoney(self) -> int:
        tmpMoney = input("금액을 투입하여 주십시오.")
        if not tmpMoney.isdigit():
            print("잘못된 입력입니다.")
            return None
        else:
            print(f'{int(tmpMoney):,}원을 투입하였습니다.')
            self.insertMoney += int(tmpMoney)
            return self.insertMoney

    # 투입한 금액과 구입할 금액 비교
    def CheckChoiceAndMoney(self, userSelect: Product, count: int) -> bool:
        if self.insertMoney < userSelect.GetPrice() * count:
            print(f'{userSelect.GetName()}을(를) {count:,}개 구입하기에는 '
                  f'{userSelect.GetPrice() * count - self.insertMoney:,}원 부족합니다')
            return False
        else:
            return True

    # 잔돈 출력하고 입금한 기계 돈 초기화
    def ReturnChangeMoney(self):
        if self.insertMoney > 0:
            print(f'이용해 주셔서 감사합니다. 잔돈은 {self.insertMoney:,}원입니다.')
            self.InsertMoneyReset()
        else:
            print("이용해 주셔서 감사합니다.")
            return None
