# import random
#
# import matplotlib.pyplot as plt
# import numpy as np
# from PIL import Image
# from HW_DM.Doll import Doll
# from DollList import DollList
# from matplotlib.axes import Axes
#
# from HW_DM.Claw import Claw
# from HW_DM.DollBox import DollBox
#
# # 데이터 생성
# # 첫 번째 배경 이미지 로드
# background_image = Image.open("backImg/bg.jpg")  # 첫 번째 이미지 경로
# probability = random.random()
# dollList = DollList()
# claw = Claw()
# dollBox = DollBox()
#
# # 이미지 설정 함수
# def DrawDoll(ax: Axes, imgPath: str, dollPosition: int, menuLen:int):
#     for i in range(menuLen):
#         ax.imshow(imgPath, aspect='auto',
#                   extent=[dollPosition, dollPosition + Doll.GetSize(), 0,
#                           Doll.GetSize()],
#                   zorder=1)
# # 인형 그리기 함수
# def SettingDoll(ax: Axes,dollList: DollList):
#     for k, v in dollList.menuDict.items():
#         if v.GetCount() != 0:
#             DrawDoll(ax, v.GetImgPath(), v.GetPosition(), len(dollList.menuDict))
#
# # 클로 그리기 함수
# def DrawClaw(ax: Axes, claw: Claw):
#     ax.imshow(claw.GetImgPath(), aspect='auto', extent=[claw.GetW(), claw.GetW() + claw.GetSize()[0],
#                                                         claw.GetH(), claw.GetH() + claw.GetSize()[1]],
#               zorder=1)
#
# def MoveClaw(claw: Claw,dollList: DollList,dollBox: DollBox):
#     userSelect = input("A는 좌측, S는 뽑기, D는 우측입니다.")
#     if userSelect.isdigit():
#         print("잘못된 입력입니다.")
#         return False
#     elif userSelect.upper() == 'A':
#         if claw.GetW() == 0:
#             print("더 이상 좌측으로 움직일 수 없습니다.")
#             return False
#         else:
#             claw.SetW(claw.GetW()-claw.GetTick())
#             return True
#     elif userSelect.upper() == 'S':
#         tmpDoll = SelectDoll(dollList,claw.GetW())
#         if isinstance(tmpDoll,Doll):
#             tmpDoll.Sales()
#         claw.RestW()
#     elif userSelect.upper() == 'D':
#         if claw.GetW() == dollBox.Xaxis:
#             print("더 이상 우측으로 움직일 수 없습니다.")
#         else:
#             claw.SetW(claw.GetW()+claw.GetTick())
#             return True
#
# def SelectDoll(dollList:DollList, claw_x):
#     tmpList = []
#     tmpDoll = Doll
#
#     for k , v in dollList.menuDict.items():
#         if claw_x == v.GetPosition():
#             tmpList.append(v)
#
#         if tmpList:
#             tmpDoll = tmpList[random.randint(0, len(tmpList) - 1)]
#         else:
#             return False
#
#         if probability <= 1:
#             return tmpDoll
#         else:
#             return False
#
#
# def RefreshBox(dollList: DollList, dollBox: DollBox, claw: Claw):
#     plt.close('all')  # 상태 초기화
#     dollBox.ResetPlt()  # 새로 생성
#
#     # 축 범위 설정
#     dollBox.GetAx().set_xlim(0, dollBox.GetXaxis())
#     dollBox.GetAx().set_ylim(0, dollBox.GetYaxis())
#
#     # 배경 이미지 표시
#     dollBox.GetAx().imshow(np.array(background_image), aspect='auto',
#               extent=[0, dollBox.GetXaxis(), 0, dollBox.GetYaxis()], zorder=0)
#
#     # 인형 및 클로 그리기
#     SettingDoll(dollBox.GetAx(), dollList)
#     DrawClaw(dollBox.GetAx(), claw)
#
#     plt.draw()
#     plt.pause(0.1)
#
#
# # 실행
# RefreshBox(dollList, dollBox, claw)
# MoveClaw(claw, dollList, dollBox)
# RefreshBox(dollList, dollBox, claw)
# MoveClaw(claw, dollList, dollBox)
# RefreshBox(dollList, dollBox, claw)