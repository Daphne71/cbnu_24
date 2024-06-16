'''
4. 모폴로지 필터
사용자의 입력을 받아서 Otsu 기반의 이진화와 Adaptive 이진화 (median)를 선택해서 그 결과를 출력하고, Erosion, Dilation, Opening, Closing에 대한 선택과 횟수를 입력받아서 해당 결과를 출력하시오.
'''

import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('../data/tomato.png',0)

while True:
    input_binary = input("Otsu = O or Adaptive = A :")
    if input_binary == 'O':
        ret, binary = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
        break
    elif input_binary == 'A':
        median_image = cv2.medianBlur(img, 5)
        binary = cv2.adaptiveThreshold(median_image, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 2)
        break
    else:
        print('다시 입력해주세요')

cv2.imshow('binary img', binary)
cv2.waitKey(0)
cv2.destroyAllWindows()

while True:
    choice = input('Erosion = E, Dilation = D, Opening = O, Closing = C : ')
    iteration = int(input('iterations num : '))

    if choice == 'E':
        result = cv2.morphologyEx(binary, cv2.MORPH_ERODE, (3,3), iterations=iteration)
        break
    elif choice == 'D':
        result = cv2.morphologyEx(binary, cv2.MORPH_DILATE, (3, 3), iterations=iteration)
        break
    elif choice == 'O':
        result = cv2.morphologyEx(binary, cv2.MORPH_OPEN, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5, 5)), iterations=iteration)
        break
    elif choice == 'C':
        result = cv2.morphologyEx(binary, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5, 5)), iterations=iteration)
        break
    else:
        print('다시 입력해주세요')

plt.imshow(result, cmap='gray')
plt.show()