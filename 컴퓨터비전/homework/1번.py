'''
1. 히스토그램 평탄화

사용자로부터 R, G, B 중의 하나의 채널을 입력받고 입력받은 채널에 대한 히스토그램을 그리고 평탄화를 한 후에 다시 그 영상을 출력하시오.
입력받은 컬러 영상을 HSV 컬러 스페이스로 변경한 후에 V 채널에 대한 평탄화를 한 후에 다시 그 영상을 출력하시오.
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt
# 사용자로부터 채널 선택

img = cv2.imread('../data/Lena.png')
while True:
    channel_input = input("채널을 고르시오 (R, G, or B): ")
    if channel_input.upper() == 'R':
        channel = 2
        break
    elif channel_input.upper() == 'G':
        channel = 1
        break
    elif channel_input.upper() == 'B':
        channel = 0
        break
    else:
        print("RGB중에 선택하세요.")

channel_image = img[:,:,channel]

hist = cv2.calcHist([channel_image], [0], None, [256], [0, 256])
# 히스토그램 그리기
hist, bins = np.histogram(channel_image.flatten(), 256, [0, 256])
plt.fill_between(range(256), hist, 0)
plt.title('Histogram')
plt.xlabel('Pixel Value')
plt.ylabel('Frequency')
plt.show()

# 채널 평탄화 적용
equalized_channel = cv2.equalizeHist(channel_image)

# 평탄화된 이미지와 원본 이미지를 병합
equalized_image = img.copy()
equalized_image[:,:,channel] = equalized_channel

cv2.imshow('Equalized Image', equalized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#HSV 컬러 스페이스로 변경
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
v_channel = hsv[:,:,2]

# 채널 평탄화 적용
equalized_v_channel = cv2.equalizeHist(v_channel)
hsv[:,:,2] = equalized_v_channel

from_hsv = cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)
cv2.imshow('from_hsv', from_hsv)
cv2.waitKey()
cv2.destroyAllWindows()