import os
import cv2
import numpy as np

def read_images(image_folder):
    image_files = os.listdir(image_folder)
    images = []
    for image_file in image_files:
        image_path = os.path.join(image_folder, image_file)
        image = cv2.imread(image_path)
        if image is not None:
            images.append(image)
        else:
            print("이미지를 읽을 수 없습니다.")
    return images

def watershed_segmentation(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    dist_transform = cv2.distanceTransform(thresh, cv2.DIST_L2, 5)
    ret, sure_fg = cv2.threshold(dist_transform, 0.8 * dist_transform.max(), 255, 0)
    sure_fg = np.uint8(sure_fg)
    unknown = cv2.subtract(thresh, sure_fg)
    ret, markers = cv2.connectedComponents(sure_fg)
    markers = markers + 1
    markers[unknown == 255] = 0
    markers = cv2.watershed(image, markers)
    image[markers == -1] = [255, 0, 0]
    return image


image_path = "DRIVE/training/images/21_training.tif"
image = cv2.imread(image_path)

#모폴로지 연산
# for image in images:
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# 모폴로지 연산을 위한 구조 요소 생성 (커널)
kernel_size = (3,3)  # 커널 사이즈 설정
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernel_size)

# 모폴로지 연산 적용
eroded = cv2.erode(gray_image, None, iterations = 1)
dilated = cv2.dilate(gray_image, None, iterations = 1)
opening = cv2.morphologyEx(gray_image, cv2.MORPH_OPEN, kernel)
closing = cv2.morphologyEx(gray_image, cv2.MORPH_CLOSE, kernel)
gradient = cv2.morphologyEx(gray_image, cv2.MORPH_GRADIENT, kernel)

# 결과 출력
cv2.imshow('Original Image', image)
cv2.imshow('Opening', opening)
cv2.imshow('Gradient', gradient)
cv2.imshow('eroded', eroded)
cv2.imshow('dilated', dilated)

cv2.imwrite('original_image2.jpg', image)
cv2.imwrite('opening_result2.jpg', opening)
cv2.imwrite('gradient_result2.jpg', gradient)
cv2.imwrite('eroded2.jpg', eroded)
cv2.imwrite('dilated2.jpg', dilated)
cv2.waitKey(0)
cv2.destroyAllWindows()