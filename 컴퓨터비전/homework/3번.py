'''
3. 주파수 도메인 필터링

DFT를 통해서 입력 영상을 주파수 도메인으로 바꿔서 출력한 후에 사용자로부터 반지름을 두 개 입력 받은 후에 영상의 중심을 원의 중심으로 하는 두 개의 원을 각각 그린 후에 그 두 원 사이의 값을 통과시키고, 나머지 부분은 다 지워버리는 band pass 필터링을 구현하여 출력하시오.
'''


import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../data/tomato.png',0).astype(np.float32) / 255

#주파수 도메인
dft = cv2.dft(img, flags=cv2.DFT_COMPLEX_OUTPUT)

dft_shift = np.fft.fftshift(dft, axes=[0,1])
magnitude = cv2.magnitude(dft_shift[:,:,0], dft_shift[:,:,1])
magnitude = np.log(magnitude)

plt.imshow(magnitude, cmap='gray')
plt.colorbar()
plt.show()

height, width = img.shape
center_y, center_x = height // 2, width // 2

#circle 2개 입력
inner_circle = int(input('inner circle: '))
outer_circle = int(input('outer circle: '))

#band pass
inner_circle_mask = np.zeros((height, width), np.uint8)
cv2.circle(inner_circle_mask, (center_x, center_y), inner_circle, 255, -1)
outer_circle_mask = np.zeros((height, width), np.uint8)
cv2.circle(outer_circle_mask, (center_x, center_y), outer_circle, 255, -1)

circle_circle = outer_circle_mask ^ inner_circle_mask

plt.imshow(circle_circle, cmap='gray')
plt.show()