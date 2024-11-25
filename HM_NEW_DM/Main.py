# 2024_11_25_파이썬_기초_실습_과제
# 한국폴리텍대학_서울정수캠퍼스_인공지능소프트웨어과
# 2401110252_박지수
# 인형 자판기 만들기
# https://github.com/Mourn5367/Python_Semester_1_2/tree/master/HM_NEW_DM

from HM_NEW_DM.DollAdmin import DollAdmin
from HM_NEW_DM.DollList import DollList
from HM_NEW_DM.DollMachine import DollMachine
from HM_NEW_DM.DollMachineState import DollMachinState

if __name__ == '__main__':
    # 인형 객체 생성
    dollList = DollList()
    # 인형 자판기 객체 생성
    dollMachine =  DollMachine()
    # 인형 관리자 객체 생성
    dollAdmin = DollAdmin()
    # 인형 기계 상태 객체 생성
    dollMachineState = DollMachinState()

    while True:
        dollMachineState.ActivateMachine(dollMachine,dollList,dollAdmin)