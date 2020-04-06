---
title: Machine Learning 1
updated: 2020-04-05 12:00
status: public
---

# Machine Learning 강좌노트 #1

*들어가기 전에: 이 Machine Learning 강좌노트 시리즈에서 기록하고 있는 모든 강좌 기록 내용은 다음 Coursera 강좌를 참조하였음을 알림.*

*Machine Learning, 스탠퍼드 대학교, [https://www.coursera.org/learn/machine-learning/home/welcome](https://www.coursera.org/learn/machine-learning/home/welcome)*

*[강의 슬라이드](https://d3c33hcgiwev3.cloudfront.net/_974fa7509d583eabb592839f9716fe25_Lecture1.pdf?Expires=1586217600&Signature=MbJBbE7h39m6pDhPzZ-Huq3f9k~hbDjetjbzk-X9FYjHnoSWuLEAcLbhyFKPId0ek4yzcBsryXT2efz5nulPjh1j~4Yp5eNq7-NorxyOow2cQXyFNPpXHDvgLMHjBsm0GFMijrFmdQMHqESgWivWR5H96z~3P~552Jf3qelVhas_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)*

## Machine Learning의 정의

### Arthur Samuel(1959)의 정의

Machine Learning is "Field of study that gives computers the ability to learn without being explicityly programmed"

기계 학습이란 명쾌하게 하나하나 프로그래밍 되지 않고도 컴퓨터가 스스로 학습할 수 있도록 하는 능력을 부여하는 연구 영역이다.

### Tom Mitchell(1998)의 정의

Well-posed learning problem: "A computer program is said to learn from experience E with respect to some task T and some performance measure P, if its performance on T, as measured by P, improves with experience E."

일련의 잘 정의된 학습 과제에서, 프로그램이 일정 수준의 작업 성능 P를 가지고 작업 T를 수행한다고 했을 때, 그 경험 E가 증가함에 따라 작업 T를 수행하는 성능 P가 향상될 때, 프로그램이 경험 E로부터 학습을 했다고 표현한다.

*Tom Mitchell은 학습 과제(Well-posed learning problem)를 중심으로 하여 기계 학습을 정의한 것이다.*

#### 예시

이메일 스팸 분류 프로그램은 사용자의 신고 패턴을 기억함으로써 스팸을 잘 제거하는 방법을 학습하는 머신 러닝이 도입된 프로그램에 해당한다.

이 상황에서, Tom Mitchell의 정의에서 경험 E, 작업 T, 성능 P는 다음과 같다.

경험 E: 컴퓨터가 사용자가 메일을 스팸/정상 메일로 분류하는 것을 관찰하는 것

작업 T: 스팸 메일을 선별하여 신고하는 것

성능 P: 정확하게 분류된 스팸 메일의 비율

## 지도 학습 & 비지도 학습(Supervised Learning & Unsupervised Learning)

### 지도 학습(Supervised Learning)

#### 지도 학습의 정의

지도 학습(Supervised Learning)이란 컴퓨터에게 우리가 input에 대한 답을 쌍으로 제시함으로서 input과 output 사이의 관계를 컴퓨터가 학습하도록 하는 것이다.

#### 지도 학습 문제의 분류

지도 학습 문제는 회귀(Regression) 문제와 분류(Classification) 문제로 나누어진다.

##### 회귀(Regression) 문제

회귀 문제는 주어지는 input 데이터에 대해서 연속적인 output 데이터 사이의 관계를 예측하도록 하는 문제이다.

예를 들면, 집의 면적, 집의 침실의 개수 따위의 input을 주고 집의 가격을 ouput으로 제시하는 경우가 해당할 수 있다. 집의 가격은 가산적이지 않은 실수 범위에 있기 때문이다. 집의 가격을 비쌈 / 안비쌈 이런 식으로 분류하는 것이 아니기 때문이다.

##### 분류(Classification) 문제

분류 문제는 주어지는 input 데이터에 대해서 가산적인 output 데이터 사이의 관계를 예측하도록 하는 문제이다. 다르게 말해서, input 데이터들을 몇 개의 카테고리로 분류하는 문제라고도 할 수 있다.

예를 들면, 이미지 데이터를 input으로 주고 강아지 / 고양이인지 분류하는 것을 ouput으로 제시하는 경우가 해당할 수 있다.

#### 지도 학습의 적용

지도 학습은 결과가 예측되는, 어떤 결과를 뽑아내야 할 지 명확한 문제에 손쉽게 적용할 수 있는 편이다.

### 비지도 학습(Unsupervised Learning)

#### 비지도 학습의 정의

비지도 학습은 주어지는 input 데이터에서 특이한 것이나 공통적인 구조를 찾아내는 것이라고 할 수 있다.

#### 비지도 학습 문제의 분류

지도 학습이 아닌 비지도 학습의 문제에 대한 분류는 다양하다. 그 중에서 대표적으로 2가지가 소개될 수는 있다. 하나는 군집화(Clustering) 문제이고, 다른 하나는 비군집화(Non-Clustering) 문제 중 하나인 칵테일 파티 알고리즘(Cocktail Party Algorithm)이다.

##### 군집화(Clustering) 문제

군집화 문제란 수많이 주어지는 데이터를 데이터의 유사성이나 관계성에 기반하여 몇 개의 군집으로 나누는 것을 목표로 하는 문제를 말한다.

##### 비군집화(Non-Clustering) 문제

비군집화 문제란 군집화 문제가 아닌 비지도 학습 문제를 말한다. 그것의 예로는 칵테일 파티 알고리즘(Cocktail Party Algorithm)인데, 이 알고리즘은 여러 소스가 섞여있는 환경에서 몇 개의 공통 구조를 찾아내어 뽑아내는 알고리즘이다. 마치 칵테일 파티의 혼잡한 소음 속에서 개인의 각각의 말을 추출해내는데 이용할 수 있는 알고리즘이라 이런 이름이 붙었다.

