# 손실함수

## batch_norm_test.py
목적: 배치 정규화(Batch Normalization)의 효과를 테스트합니다.
설명:
MultiLayerNetExtend 클래스를 사용하여 배치 정규화를 포함한 신경망과 포함하지 않은 신경망을 각각 학습합니다.
여러 초기 가중치 스케일 값에 대해 두 신경망의 학습 정확도를 비교합니다.

## optimizer_compare_mnist.py
목적: 다양한 최적화 알고리즘의 성능을 비교합니다.
설명:
SGD, Momentum, AdaGrad, Adam 최적화 알고리즘을 비교합니다.
MultiLayerNet 클래스를 사용하여 각 알고리즘에 대해 신경망을 학습합니다.

## overfit_dropout.py
목적: 오버피팅을 방지하기 위해 드롭아웃(Dropout)을 적용합니다.
설명:
작은 데이터셋으로 신경망을 학습시켜 오버피팅을 재현합니다.
드롭아웃을 적용한 경우와 적용하지 않은 경우를 비교합니다.

## train_neuralnet.py
목적: 2층 신경망을 학습합니다.
설명:
TwoLayerNet 클래스를 사용하여 2층 신경망을 구현하고 학습합니다.
학습 데이터와 테스트 데이터에 대한 정확도를 출력합니다.

## two_layer_net.py
목적: 2층 신경망을 구현합니다.
설명:
입력층, 은닉층, 출력층으로 구성된 2층 신경망을 구현합니다.
순전파, 손실 계산, 정확도 계산, 역전파를 포함합니다.

## sigmoid&step_function.py
목적: 시그모이드 함수와 계단 함수를 구현합니다.

## sigmoid.py
목적: 소프트맥스 함수 구현 및 테스트
설명:
softmax: 입력 배열을 소프트맥스 함수로 변환하여 반환

## squared_error.py
목적: 손실 함수 구현
설명:
sum_squares_error: 제곱 오차 손실 함수
cross_entropy_error: 교차 엔트로피 손실 함수
##
