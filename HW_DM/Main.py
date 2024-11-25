from HW_DM.DollAdmin import DollAdmin
from HW_DM.DollList import DollList
from HW_DM.DollMachine import DollMachine
from HW_DM.DollMachineState import DollMachinState

if __name__ == '__main__':
    # 메뉴 객체 생성
    dollList = DollList()
    # 자판기 객체 생성
    dollMachine =  DollMachine()
    # 관리자 객체 생성
    dollAdmin = DollAdmin()
    # 기계 상태 객체 생성
    dollMachineState = DollMachinState()

    while True:
        dollMachineState.ActivateMachine(dollMachine,dollList,dollAdmin)