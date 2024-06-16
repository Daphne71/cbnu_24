#CreaterStitcher 함수를 이용하여 4개의 영상 셋에 대해서 파노라마 이미지를 만드는 방법을 구현하시오.
import cv2
import numpy as np

# 이미지 경로 설정
image_paths = [
    'stitching/newspaper1.jpg',
    'stitching/newspaper2.jpg',
    'stitching/newspaper3.jpg',
    'stitching/newspaper4.jpg'
]

# 이미지 읽기
images = [cv2.imread(image_path) for image_path in image_paths]

# Stitcher 객체 생성
stitcher = cv2.createStitcher()

# 파노라마 생성
status, pano = stitcher.stitch(images)

if status == cv2.Stitcher_OK:
    print("Stitching completed successfully.")
    cv2.imshow('Panorama', pano)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Stitching failed. Error code: ", status)
