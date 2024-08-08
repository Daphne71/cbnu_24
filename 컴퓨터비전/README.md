# cbnu_24 컴퓨터 비전

# Middle Project 이미지 처리 프로젝트

이 프로젝트는 OpenCV와 NumPy를 사용하여 이미지에 모폴로지 연산 및 워터쉐드 분할을 수행하는 파이썬 코드입니다. 이 README 파일은 코드에 대한 설명과 함께 각 함수의 역할을 설명합니다.

## 파일 구조

- `main.py`: 메인 코드 파일로, 이미지를 읽고 처리하는 모든 작업을 포함합니다.
- `README.md`: 프로젝트 설명 파일입니다.
- `DRIVE/training/images/21_training.tif`: 테스트에 사용된 이미지 파일입니다.
- 결과 이미지 파일들 (`original_image2.jpg`, `opening_result2.jpg`, `gradient_result2.jpg`, `eroded2.jpg`, `dilated2.jpg`): 각각의 처리 결과를 저장한 파일들입니다.

## 필요 조건

이 프로젝트를 실행하기 위해서는 다음의 파이썬 라이브러리가 필요합니다:

- `opencv-python`
- `numpy`

이 라이브러리들은 다음 명령어로 설치할 수 있습니다:

```bash
pip install opencv-python numpy



#  Home Work


## 1번: 히스토그램 평탄화 (homework/1번.py)
목적: 입력된 컬러 이미지에서 사용자가 선택한 채널(R, G, B)에 대해 히스토그램을 그리고 평탄화를 수행합니다. 또한, HSV 컬러 스페이스로 변환하여 V 채널에 대해 평탄화를 수행합니다.

## 2번: 공간 도메인 필터링 (homework/2번.py)
목적: 입력 영상에 노이즈를 추가하고, Gaussian, Median, Bilateral 필터를 적용하여 노이즈를 제거합니다. 필터링 전후의 차이 이미지를 계산하여 출력합니다.

## 3번: 주파수 도메인 필터링 (homework/3번.py)
목적: DFT를 사용하여 입력 영상을 주파수 도메인으로 변환하고, 사용자로부터 입력받은 반지름을 기반으로 band pass 필터링을 수행합니다.

## 4번: 모폴로지 필터 (homework/4번.py)
목적: Otsu 기반의 이진화와 Adaptive 이진화(median)를 선택하여 결과를 출력하고, Erosion, Dilation, Opening, Closing 중 선택하여 결과를 출력합니다.

## Feature Detection (homework2/Feature Detection.py)
목적: Canny Edge와 Harris Corner를 검출하여 결과를 출력합니다.

## Matching (homework2/Matching.py)
목적: SIFT, SURF, ORB를 사용하여 특징점을 추출하고 매칭 및 RANSAC을 통해 호모그래피를 계산하여 이미지를 warping합니다.

## Optical Flow (homework2/Optical Flow.py)
목적: Good feature to Track을 추출하고 Pyramid Lucas-Kanade 알고리즘을 적용하여 Optical Flow를 계산합니다.

## Panorama (homework2/Panorama.py)
목적: CreaterStitcher 함수를 사용하여 여러 이미지를 파노라마로 합칩니다.





