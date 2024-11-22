import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

# 데이터 생성

# 첫 번째 배경 이미지 로드
background_image = Image.open("bback.webp")  # 첫 번째 이미지 경로

# 두 번째 이미지 로드
doll1 = Image.open("doll1.png")  # 두 번째 이미지 경로로 변경
claw = Image.open("claw.webp")  # 두 번째 이미지 경로로 변경

# 이미지 크기 설정 (3, 3) 크기로 설정
doll1_w = 2
doll1_h = 2
claw_w = 2
claw_h = 2
# 그래프 설정
fig, ax = plt.subplots()

# 배경 이미지 설정
ax.imshow(background_image, aspect='auto', extent=[0, 10, 0, 10], zorder=0)

# x축과 y축 범위 설정
ax.set_xlim(0, 10)  # x축 범위 설정
ax.set_ylim(0, 10)  # y축 범위 설정

# 첫 번째 이미지 삽입: (x, y) 위치와 (width, height) 크기
# 예를 들어 (4, 4) 위치에 (3, 3) 크기로 삽입
doll1_x = 0
doll1_y = 0
claw_x = 0
claw_y = 8
ax.imshow(doll1, aspect='auto', extent=[doll1_x, doll1_x + doll1_w, doll1_y, doll1_y + doll1_h],
          zorder=1)
ax.imshow(claw, aspect='auto', extent=[claw_x, doll1_x + claw_w, claw_y, claw_y + claw_h],
          zorder=1)


# 모든 축 레이블, 타이틀, 범례 제거
# ax.set_xticks([])  # x축 눈금 제거
# ax.set_yticks([])  # y축 눈금 제거
ax.set_xlabel("")  # x축 레이블 제거
ax.set_ylabel("")  # y축 레이블 제거
ax.set_title("")   # 그래프 제목 제거

# 그래프 표시
plt.show()