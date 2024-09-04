

if __name__ == '__main__':
    VM_Menu = {"1. 사이다" : 1000, "2. 콜라" : 1500, "3. 쿠키" : 2000 , "4. 레몬에이드" : 2500}
    VM_Wallet = 0
    VM_State = 1

    while VM_State != 0:

        print(VM_Menu)

        if VM_State == 1:
            try:
                VM_Wallet = int(input("금액을 투입해 주세요"))
            except TypeError:
                print("정수의 숫자만 입력해 주세요")
                continue
            VM_State = 2

        #elif VM_State == 2:


