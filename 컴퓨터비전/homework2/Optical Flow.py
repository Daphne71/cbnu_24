#Stitching.zip에서 dog_a, dog_b 두 사진을 이용해서 Good feature to Track을 추출하고 Pyramid Lucas-Kanade 알고리즘을 적용해서 Optical Flow을 구하는 코드를 작성하시오.
import numpy as np
import cv2

img_a_color = cv2.imread('stitching/dog_a.jpg')
img_b_color = cv2.imread('stitching/dog_b.jpg')

# Good Features to Track 추출
# 이미지를 그레이스케일로 변환
img_a_gray = cv2.cvtColor(img_a_color, cv2.COLOR_BGR2GRAY)
img_b_gray = cv2.cvtColor(img_b_color, cv2.COLOR_BGR2GRAY)

# Good Features to Track 추출
feature_params = dict(maxCorners=100, qualityLevel=0.3, minDistance=7, blockSize=7)
p0 = cv2.goodFeaturesToTrack(img_a_gray, mask=None, **feature_params)

# Pyramid Lucas-Kanade Optical Flow 파라미터 설정
lk_params = dict(winSize=(15, 15), maxLevel=2,
                 criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 0.03))

# Optical Flow 계산
p1, st, err = cv2.calcOpticalFlowPyrLK(img_a_gray, img_b_gray, p0, None, **lk_params)

# 좋은 포인트들만 추출
good_new = p1[st == 1]
good_old = p0[st == 1]

# Optical Flow 결과를 시각화
mask = np.zeros_like(img_a_color)  # 컬러 이미지에서 마스크 생성
for i, (new, old) in enumerate(zip(good_new, good_old)):
    a, b = new.ravel()
    c, d = old.ravel()
    mask = cv2.line(mask, (a, b), (c, d), (0, 255, 0), 2)
    img_a_color = cv2.circle(img_a_color, (a, b), 5, (0, 0, 255), -1)

output = cv2.add(img_a_color, mask)

cv2.imshow('Optical Flow', output)
cv2.waitKey(0)
cv2.destroyAllWindows()