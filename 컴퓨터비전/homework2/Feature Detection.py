#Stitching.zip에서 4장의 영상(boat1, budapest1, newspaper1, s1)을 선택한 후에 Canny Edge와 Harris Corner를 검출해서 결과를 출력하는 코드를 작성하시오.

import cv2
import numpy as np

images = ['boat1.jpg', 'budapest1.jpg', 'newspaper1.jpg', 's1.jpg']
image_names = ['boat1', 'budapest1', 'newspaper1', 's1']

image_paths = [f'stitching/{name}' for name in images]

for idx, img_path in enumerate(image_paths):
    img = cv2.imread(img_path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Canny Edge Detection
    edges = cv2.Canny(gray, 100, 200)

    # Harris Corner Detection
    gray_float = np.float32(gray)
    dst = cv2.cornerHarris(gray_float, 2, 3, 0.04)
    dst = cv2.dilate(dst, None)
    img_harris = img.copy()
    img_harris[dst > 0.01 * dst.max()] = [0, 0, 255]

    cv2.imshow(f'Canny Edge - {image_names[idx]}', edges)
    cv2.imshow(f'Harris Corner - {image_names[idx]}', img_harris)

cv2.waitKey(0)
cv2.destroyAllWindows()
