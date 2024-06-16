#Stitching.zip에서 각 영상셋(boat, budapest, newspaper, s1~s2)에서 두장을 선택하고 각 영상에서 각각 SIFT, SURF, ORB를 추출한 후에 매칭 및 RANSAC을 통해서 두 장의 영상 간의 homography를 계산하고, 이를 통해 한 장의 영상을 다른 한 장의 영상으로 warping하는 코드를 작성하시오.
import cv2
import numpy as np

# 이미지 경로 설정
image_pairs = [
    ('stitching/boat1.jpg', 'stitching/boat2.jpg'),
    ('stitching/budapest1.jpg', 'stitching/budapest2.jpg'),
    ('stitching/newspaper1.jpg', 'stitching/newspaper2.jpg'),
    ('stitching/s1.jpg', 'stitching/s2.jpg')
]

def find_homography_and_warp(img1, img2, detector_name='SIFT'):
    if detector_name == 'SIFT':
        detector = cv2.xfeatures2d.SIFT_create()
    elif detector_name == 'SURF':
        detector = cv2.xfeatures2d.SURF_create()
    elif detector_name == 'ORB':
        detector = cv2.ORB_create()
    else:
        raise ValueError("Unsupported detector. Choose from 'SIFT', 'SURF', or 'ORB'.")

    # 특징점 검출 및 서술자 계산
    kp1, des1 = detector.detectAndCompute(img1, None)
    kp2, des2 = detector.detectAndCompute(img2, None)

    # BFMatcher로 매칭
    if detector_name == 'ORB':
        bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    else:
        bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    print(f"Number of matches found: {len(matches)} for detector {detector_name}")

    if len(matches) < 10:
        raise ValueError(f"Not enough matches are found - {len(matches)}/{10}")

    # 매칭된 특징점들 추출
    pts1 = np.float32([kp1[m.queryIdx].pt for m in matches])
    pts2 = np.float32([kp2[m.trainIdx].pt for m in matches])

    # RANSAC을 사용한 Homography 계산
    H, mask = cv2.findHomography(pts1, pts2, cv2.RANSAC, 5.0)

    if H is None:
        raise ValueError("Homography could not be computed.")

    print(f"Homography matrix:\n{H}")

    # img1을 img2로 warping
    height, width = img2.shape[:2]
    warped_img = cv2.warpPerspective(img1, H, (width, height))

    return warped_img, matches, kp1, kp2, mask

# 이미지 쌍을 순회하며 특징점 추출, 매칭, 호모그래피 계산, 그리고 warping 수행
for (img1_path, img2_path) in image_pairs:
    img1 = cv2.imread(img1_path)
    img2 = cv2.imread(img2_path)

    for detector in ['SIFT', 'SURF', 'ORB']:
        try:
            warped_img, matches, kp1, kp2, mask = find_homography_and_warp(img1, img2, detector)

            # 매칭 결과 시각화
            try:
                print(f"Drawing matches for {detector} with {img1_path} and {img2_path}")
                if mask is not None:
                    mask = mask.ravel().tolist()
                else:
                    mask = [0] * len(matches)
                match_img = cv2.drawMatches(img1, kp1, img2, kp2, matches[:50], None, matchesMask=mask[:50],
                                            flags=cv2.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
                cv2.imshow(f'{detector} Matches - {img1_path} & {img2_path}', match_img)
                cv2.imshow(f'{detector} Warped Image - {img1_path}', warped_img)
            except Exception as e:
                print("Error ")
        except Exception as e:
            print("Error")

cv2.waitKey(0)
cv2.destroyAllWindows()
