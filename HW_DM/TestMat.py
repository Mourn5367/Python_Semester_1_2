import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.image as mpimg

img = mpimg.imread('js.png')

# 이미지 데이터 정규화 (0-1 범위로 변환)
if img.dtype == np.uint8:  # 0-255 범위의 정수형
    img = img / 255.0  # 0-1 범위로 변환
# 3D 플롯 생성
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
# X축 면
x = np.array([[0, 1], [0, 1]])
y = np.array([[0, 0], [1, 1]])
z = np.array([[0, 0], [0, 0]])
#ax.plot_surface(x, y, z, color='red', alpha=1)
ax.plot_surface(x, y, z, rstride=1, cstride=1, facecolors=img/255.0, alpha=1)

ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_zlim(0,1)

# 그래프 표시
plt.show()