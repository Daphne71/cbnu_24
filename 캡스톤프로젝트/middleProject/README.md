지능화 캡스톤 프로젝트 

<프로젝트 목표>
스마트 공장 내 실시간 넘어짐 감지 모니터링 시스템 개발​

<middleProject>
프로젝트 관련 논문 선정 및 구현
Fall Detection and Activity Recognition Using Human Skeleton Features
영상 데이터에서 AlphaPose를 이용해 프레임에서 골격 좌표를 추출한 후 4가지 머신러닝을 적용하여 넘어짐을 판단하는 방법론 제안 논문
  
  1. Alpha Pose를 통해 추출된 Skeleton 기반 json 형식 데이터 전처리 수행
  2. 다중 인물이 등장하는 경우, score 점수 가장 높은 것 제외하고 모두 제거
  3. 17개의 keypoints (x, y, confidence) 17x3 = 51차원 특징 벡터 구성
  4. 데이터 라벨링 1 - 5, 11 : FALL 6 - 10 : NOT FALL
  5. 4가지 머신러닝을 통해 이진 분류 진행

4가지 머신러닝 모델 적용
    - RF(Random Forest)
    - SVM(Support Vector Machine)
    - MLP(Multilayer Perceptron)
    - KNN(K-Nearest Neighbor)

