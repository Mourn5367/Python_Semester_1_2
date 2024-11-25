import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from HM_NEW_DM.Doll import Doll
from HM_NEW_DM.DollList import DollList
from matplotlib.axes import Axes
from HM_NEW_DM.Claw import Claw

class DollBox:
    def __init__(self):
        self.Xaxis = 10
        self.Yaxis = 10
        self.ax = None
        self.fig = None
        self.background_image = Image.open("backImg/bg.jpg")
        self.claw = Claw()

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
    def DrawClaw(self,ax: Axes):
        ax.imshow(self.claw.GetImgPath(), aspect='auto', extent=[self.claw.GetW(), self.claw.GetW() + self.claw.GetSize()[0],
                                                            self.claw.GetH(), self.claw.GetH() +self.claw.GetSize()[1]],
                  zorder=1)

    def RefreshBox(self,dollList: DollList):
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
        self.DrawClaw(self.GetAx())

        self.GetAx().set_xticks([])
        self.GetAx().set_yticks([])
        self.GetAx().set_title("Doll Machine")
        plt.draw()
        plt.pause(0.1)