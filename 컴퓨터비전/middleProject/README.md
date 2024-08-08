
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
