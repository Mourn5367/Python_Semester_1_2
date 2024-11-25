import random

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from HW_DM.Doll import Doll
from DollList import DollList
from matplotlib.axes import Axes

from HW_DM.Claw import Claw

class DollBox:
    def __init__(self):
        self.Xaxis = 10
        self.Yaxis = 10
        self.ax = None
        self.fig = None
        self.background_image = Image.open("backImg/bg.jpg")
        self.probability = random.random()
        self.__chance = 5
        self.currentChance = 0

    def GetXaxis(self):
        return self.Xaxis

    def GetYaxis(self):
        return self.Yaxis

    def ResetPlt(self):
        self.fig, self.ax = plt.subplots()

    def GetAx(self):
        return self.ax
    def GetFig(self):
        return self.fig


    # 이미지 설정 함수
    def DrawDoll(self,ax: Axes, imgPath: str, dollPosition: int, menuLen: int):
        for i in range(menuLen):
            ax.imshow(imgPath, aspect='auto',
                      extent=[dollPosition, dollPosition + Doll.GetSize(), 0,
                              Doll.GetSize()],
                      zorder=1)

    # 인형 그리기 함수
    def SettingDoll(self,ax: Axes, dollList: DollList):
        for k, v in dollList.menuDict.items():
            if v.GetCount() != 0:
                self.DrawDoll(ax, v.GetImgPath(), v.GetPosition(), len(dollList.menuDict))

    # 클로 그리기 함수
    def DrawClaw(self,ax: Axes, claw: Claw):
        ax.imshow(claw.GetImgPath(), aspect='auto', extent=[claw.GetW(), claw.GetW() + claw.GetSize()[0],
                                                            claw.GetH(), claw.GetH() + claw.GetSize()[1]],
                  zorder=1)

    def MoveClaw(self,claw: Claw, dollList: DollList):
        userSelect = input("A는 좌측, S는 뽑기, D는 우측입니다.")
        if userSelect.isdigit():
            print("잘못된 입력입니다.")
            return False
        elif userSelect.upper() == 'A':
            if claw.GetW() == 0:
                print("더 이상 좌측으로 움직일 수 없습니다.")
                return False
            else:
                claw.SetW(claw.GetW() - claw.GetTick())
                return True
        elif userSelect.upper() == 'S':
            tmpDoll = self.SelectDoll(dollList, claw.GetW())
            if isinstance(tmpDoll, Doll):
                tmpDoll.Sales()
            claw.RestW()
        elif userSelect.upper() == 'D':
            if claw.GetW() == self.GetXaxis():
                print("더 이상 우측으로 움직일 수 없습니다.")
            else:
                claw.SetW(claw.GetW() + claw.GetTick())
                return True

    def SelectDoll(self,dollList: DollList, claw_x):
        tmpList = []
        tmpDoll = Doll

        for k, v in dollList.menuDict.items():
            if claw_x == v.GetPosition():
                tmpList.append(v)

            if tmpList:
                tmpDoll = tmpList[random.randint(0, len(tmpList) - 1)]
            else:
                return False

            if self.probability <= 1:
                return tmpDoll
            else:
                return False

    def RefreshBox(self,dollList: DollList, claw: Claw):
        plt.close('all')  # 상태 초기화
        self.ResetPlt()  # 새로 생성

        # 축 범위 설정
        self.GetAx().set_xlim(0, self.GetXaxis())
        self.GetAx().set_ylim(0, self.GetYaxis())

        # 배경 이미지 표시
        self.GetAx().imshow(np.array(self.background_image), aspect='auto',
                               extent=[0, self.GetXaxis(), 0, self.GetYaxis()], zorder=0)

        # 인형 및 클로 그리기
        self.SettingDoll(self.GetAx(), dollList)
        self.DrawClaw(self.GetAx(), claw)

        plt.draw()
        plt.pause(0.1)