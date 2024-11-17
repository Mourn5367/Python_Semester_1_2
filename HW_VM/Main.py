# 2024_11_18_파이썬_기초_실습_과제
# 한국폴리텍대학_서울정수캠퍼스_인공지능소프트웨어과
# 2401110252_박지수
# 자판기 만들기
# https://github.com/Mourn5367/Python_Semester_1_2/tree/master/HW_VM
from HW_VM.Admin import Admin
from HW_VM.MachineState import MachineState
from HW_VM.Menu import Menu
from HW_VM.VendingMachine import VendingMachine

if __name__ == '__main__':
    # 메뉴 객체 생성
    menu = Menu()
    # 자판기 객체 생성
    VM =  VendingMachine()
    # 관리자 객체 생성
    admin = Admin()
    # 기계 상태 객체 생성
    machineState = MachineState()

    while True:
        machineState.ActivateMachine(VM,menu,admin)


