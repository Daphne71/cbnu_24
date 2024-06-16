'''
2. 공간 도메인 필터링

입력 영상에 대해서 임의의 노이즈를 입히고, Gaussian Filtering, Median Filtering, Bilateral Filtering 알고리즘을 적용해서 결과를 출력하시오.
각 결과를 입력 영상(노이즈 입히기 전)과 절대값 차이를 취해서 그 결과를 출력하시오.
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../data/Lena.png').astype(np.float32) / 255
#노이즈
noised = (img + 0.2*np.random.rand(*img.shape).astype(np.float32))
noised = noised.clip(0,1)
plt.imshow(noised[:,:,[2,1,0]])
plt.show()

#Gaussian Filtering
gauss = cv2.GaussianBlur(noised, (7,7), 0)
plt.imshow(gauss[:,:,[2,1,0]])
plt.title('Gaussian')
plt.show()

#Median Filtering
median = cv2.medianBlur((noised * 255).astype(np.uint8), 7).astype(np.float32) / 255
plt.imshow(median[:,:,[2,1,0]])
plt.title('Median')
plt.show()

#Bilateral Filtering
bilat = cv2.bilateralFilter(noised, -1, 0.3, 10)
plt.imshow(bilat[:,:,[2,1,0]])
plt.title('Bilateral')
plt.show()

# 입력 이미지와 각각의 필터링 결과의 절대값 차이 계산 및 출력
def difference(original, filtered, title):
    difference = np.abs(original - filtered)
    plt.imshow(difference[:, :, [2, 1, 0]])
    plt.title(title)
    plt.show()

difference(img, gauss, 'Difference Gaussian')

difference(img, median, 'Difference Median')

difference(img, bilat, 'Difference Bilateral')
