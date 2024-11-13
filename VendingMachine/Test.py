from VendingMachine.Machine2 import Machine2

if __name__ == "__main__":
    VM = Machine2()
    VM.PrintMenu()
    VM.InputMoney(1000)
    VM.PrintInputMoney()

    isOk = False

    while not isOk:
        isOk, menu =VM.ChoiceMenu()

    VM.OutProduct(menu)
    VM.ReturnMoney()
    print("{0} / {1}".format(isOk, menu))
