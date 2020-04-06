---
title: Machine Learning 2
updated: 2020-04-05 12:30
status: public
---

# Machine Learning 강좌노트 #2

*들어가기 전에: 이 Machine Learning 강좌노트 시리즈에서 기록하고 있는 모든 강좌 기록 내용은 다음 Coursera 강좌를 참조하였음을 알림.*

*Machine Learning, 스탠퍼드 대학교, [https://www.coursera.org/learn/machine-learning/home/welcome](https://www.coursera.org/learn/machine-learning/home/welcome)*

*[강의 슬라이드](https://d3c33hcgiwev3.cloudfront.net/_ec21cea314b2ac7d9e627706501b5baa_Lecture2.pdf?Expires=1586217600&Signature=Yios4R1JenPr4pb5RtsY0GgjRhQvVJvvlflhJ60-KSd8FJhvNLEpqbY6YSqv-6GazqiSqsg0eiSFann-ybV4gMy52QKNkzAlGdsW4zaHNKpdvuOKl~E4YZsjVa0of~uiLpKCCMP2DdTT2Fbolb5dbWaQYr5WOK1FiRzbyPd5PuE_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)*

*또한 이 부분 중 Gradient Descent 부분의 경우 Coursera 강좌와 더불어서 이 블로그의 게시물을 참고하였음을 밝힘.*

*티스토리 - 진짜공부 / 인공지능 / 06. 기울기하강 알고리즘(Gradient Descent): [https://startsecure.tistory.com/48](https://startsecure.tistory.com/48)*

## Machine Learning 학습을 위한 기호 약속

$x^{(i)}$: i 번째의 input 데이터를 칭한다.

$y^{(i)}$: i 번째의 ouput 데이터를 칭한다. (지도 학습의 경우 정의됨, 즉 목표로 하는, 학습시키고 싶어 하는 input 데이터에 대한 답에 해당)

트레이닝 예시(Training Example): 지도 학습에서 트레이닝 예시라 함은 input 데이터와 output 데이터의 쌍이다. 즉, $(x^{(i)}, y^{(i)})$인 셈이다.

트레이닝 세트(Training Set): 지도 학습에서 트레이닝 세트는 $m$개의 트레이닝 예시의 집합이다. 곧, $(x^{(i)}, y^{(i)}); i = 1, 2, ..., m$에 해당한다.

$X$: input 값들이 들어오는 영역을 지칭한다.

Y: output 값이 제시되는 영역을 지칭한다.

## Machine Learning의 동작 구조: 지도 학습

![지도 학습의 동작 구조](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/H6qTdZmYEeaagxL7xdFKxA_2f0f671110e8f7446bb2b5b2f75a8874_Screenshot-2016-10-23-20.14.58.png?expiry=1586217600000&hmac=BuPHdJFnQINWDmP07iyhI1P2RPWGWeFsLIJWHkWwTrI)

위 그림에서 보이는 바와 같이 지도 학습은 트레이닝 세트로 경험을 획득하여, 어떤 input 데이터 x에서 비교적 정확한 output y를 예측하는 중간 함수 h를 찾아내는 것이다. 이 중간 함수인 h를 가설(hypothesis)이라 한다.

결과값 y가 연속적이면 이 문제는 회귀 문제에 해당하며, 가산적이면 분류 문제에 해당한다.

## 비용 함수(Cost Function)

### 비용 함수의 정의

비용 함수(Cost Function)란 지도 학습에서 가설의 정확성을 평가하기 위하여 사용되는 함수이다. 이 비용함수는 간단하게 말해서 실제 값과 참값의 제곱의 합을 평균낸 것에 $1 \over 2$ 한 것으로서, 다음과 같이 쓸 수 있다.

*보통 비용함수는 $J$의 기호로 표기하는 편이다.*

$J = {{1} \over {2m}} \sum\limits_{i=1}^{m}(\hat{y}_i - y_i)^2 $ 

*여기서 $\hat{y}_i$는 실제 i번째 output 값을 지시하고, $y_i$는 예측된 i번째 output 값을 지시한다.*

가설 $h$가 $y = h(x_{(i)})$의 형태로 표현됨을 고려하면, 위의 비용함수는 아래와 같은 형태로도 쓸 수 있을 것이다.

$J = {{1} \over {2m}} \sum\limits_{i=1}^{m}(\hat{y}_i - y_i)^2 = {{1} \over {2m}} \sum\limits_{i=1}^{m}(h(x_i)-y_i)^2$ 

이 비용함수는 마치 통계학의 분산과도 비슷한 느낌의 함수에 해당한다.

더 간단하게 표현해서, $\bar{x}$가 $(h(x_i) - y_i)^2$의 평균을 지시한다고 정의하면 비용함수 $J = {1 \over 2} \bar{x}$가 된다.

비용함수는 "제곱 오차 함수(Squared error function)", "평균 제곱 오차(Mean squared error)"라고도 하며, 하필 1/2을 곱하는 이유는 후에 기술할 기울기 강하법(Gradient Descent)에서의 편의를 위함이다.

비용함수의 개념은 이해하기 어려우므로 동영상 강의를 아래에 덧붙인다. 

[Cost Function Video](https://d3c33hcgiwev3.cloudfront.net/02.2-V2-LinearRegressionWithOneVariable-CostFunction.b1832fa0b22b11e49f072fa475844d6b/full/360p/index.mp4?Expires=1586217600&Signature=J128XQke7pd--TsiORgcFSSEy6bnqIcyDgreA~7n-8kKqfd2sjPWoZo0fXqjlNEBqYNeBFIZU0e8eRVtkC~7MyEOcxSV-MCz1eSaKtZZcTh7~UB~~3HCmxLQvyaj8jUjlsWm00UtxlgCST6S-7hclV959Hf9if0H3QX~5zjsO8s_&Key-Pair-Id=APKAJLTNE6QMUY6HBC5A)

### 비용 함수의 적용: 단일 Feature

지도 학습 문제에서 주된 목표는 설정한 가설에 대하여 각각의 input 변수들 앞에 붙는 미정계수를 결정하는 것이다. 그것도 실제 output과 잘 맞게끔 하도록 말이다.

우선 가장 간단한 비용 함수의 적용을 살펴보기로 하자. 가장 간단하게, 가설이 일차함수의 형태로 구현된다고 하자. 즉, 어떤 단일 input 변수(이제부터는 이들 input 변수를 feature라 한다)만이 input으로 주어진 경우를 살펴보자.

해당 가설은 일차함수의 형태이므로, 각각의 미정계수를 $\theta$로 표현하여, 가설을 다음과 같은 형태로서 나타낼 수 있다.

$h(x) = \theta_0 + \theta_1 x$

보다 상황을 간단히 하기 위해서 $\theta_0 = 0$이라 하자. 그러면 가설을 다음의 형태로 표현할 수 있다. $h(x) = \theta_1 x$

지도 학습 문제에서 설정한 가설의 각각의 미정계수가 최대한 주어진 데이터에 맞게끔 미정계수를 결정하는 것이 목적임을 상기하자.

데이터가 다음과 같이 주어졌다고 하자. $(x,y) = (1, 1), (2, 2), (3, 3)$.

이 데이터에 대하여 가설 $h(x) = \theta_1 x$의 미정계수 $\theta_1$을 결정하면 다음과 같다.

ex1) $\theta_1 = 1$이라고 가정했을 경우, 그래프에서 보이듯이 가설로 예측한 값은 그 어떤 트레이닝 예시에서도 오차를 보이지 않는다. 따라서 비용함수 $J(0) = 0$이 된다.

![if theta1 equals to 1 graph](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/_B8TJZtREea33w76dwnDIg_3e3d4433e32478f8df446d0b6da26c27_Screenshot-2016-10-26-00.57.56.png?expiry=1586217600000&hmac=xSJfv1O5f0MAQxe7c37QmeX3AIZl7lCvQ19uX7rg5pk)

ex2) $\theta_1 = 0.5$라고 가정했을 경우, 그래프에서 보이듯이 가설로 예측한 값과 트레이닝 예시의 참값이 오차를 보인다. 비용함수 $J$의 정의에 따라 계산하면, $J(1) = {{(0.5)^2 + 1^2 + (1.5)^2} \over {2 \times 3}} = 0.58$이다.

![if theta1 equals to 0.5 graph](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/8guexptSEeanbxIMvDC87g_3d86874dfd37b8e3c53c9f6cfa94676c_Screenshot-2016-10-26-01.03.07.png?expiry=1586217600000&hmac=mvLCM_m9H2uEOpmmmBxhGIS1eaa5Xfv2pBVu0svJU6I)

다른 몇몇 값을 따라 나머지 몇몇 $J(\theta_1)$을 계산해보면 그 그래프는 아래와 같다.

![J 계산 그래프](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/fph0S5tTEeajtg5TyD0vYA_9b28bdfeb34b2d4914d0b64903735cf1_Screenshot-2016-10-26-01.09.05.png?expiry=1586217600000&hmac=hdhYZQsMKbqzU46LPv2OycWEBiL9jTpo0Z7PBSCXNfE)

비용함수 $J$는 미정계수의 결정에 따른 예측값과 참값의 오차를 보여주는 함수이므로, 비용함수 $J$가 최소화되도록 미정계수인 $\theta_1$을 정해야 한다. 위 그래프에서 볼 수 있듯이, 비용함수는 $\theta_1 = 1$일 때 최소가 된다. 따라서 $\theta_1 = 1$이다.

### 비용 함수의 적용: 복수 Feature

Feature가 여러개일 경우는 상황이 복잡하다. Feature가 2개인 경우만 하더라도 단순히 선형적으로 표현되었다고 가정해도 가설 $h$를 표현하는데 2차원 좌표평면이 필요하며 비용함수 $J$를 도식해도 3차원 공간이 필요하다.

![Feature가 여러개인 경우 그래프](https://d3c33hcgiwev3.cloudfront.net/imageAssetProxy.v1/N2oKYp2wEeaVChLw2Vaaug_d4d1c5b1c90578b32a6672e3b7e4b3a4_Screenshot-2016-10-29-01.14.37.png?expiry=1586217600000&hmac=JJJsBG2Bl5uimt5zTS2chYSq4NILP1sS6rastF9DH8Q)

이런 경우 비용함수 $J$의 도식은 3차원 그래프나 등고선을 이용한 2차원 평면 상에 도식하게 된다. 그러나 복수 Feature의 비용 함수더라도 그 값을 최소화하는 것이 목적임에는 변함이 없다.

## 기울기 하강 알고리즘(Gradient Descent Algorithm)

### 기울기 하강 알고리즘의 정성적(기하적) 이해

기울기 하강 알고리즘(Gradient Descent Algorithm)이란 비용함수 $J$의 최솟값을 구하는데 자주 이용되는 알고리즘이다. 단순히 선형회귀에서만 사용되는 것 만이 아니고, 머신 러닝의 다양한 분야에서 다채롭게 활용되고 있다.

가장 정성적으로 기울기 하강 알고리즘을 이해하는 방법은 다음의 그림으로서 가능할 것이다. 비용함수가 두 Features만 가지고 있다고 하여, $J(\theta_0, \theta_1)$의 형태로 표현된다고 하자. 3차원 좌표공간 상에 $J(\theta_0, \theta_1)$, $\theta_0$, $\theta_1$를 축으로 하여 도식하여 다음의 그래프가 나타났다고 하자.

![기울기 하강 알고리즘 3차원 그래프](https://t1.daumcdn.net/cfile/tistory/996B21355B49CDF71F)

이러한 형태에서 $J(\theta_0, \theta_1)$을 최소화하기 위한 기울기 하강 알고리즘의 동작 방식은 마치 나 자신이 산의 어느 지점에 올라와 있는데, 경사진 쪽을 따라서 가장 고도가 낮은 곳으로 내려가려 하는 것과 비슷하다.

한 편, 이러한 기울기 하강 알고리즘은 모든 비용함수 $J$에 대해서 전역적 최솟값을 구할 수 있는 것은 아니다. 위의 그래프가 하나의 반례로서, 아래 그림과 같은 위치에서 시작할 경우 위와는 전혀 다른 위치에 도달하게 된다.

![기울기 하강 알고리즘 3차원 그래프 2](https://t1.daumcdn.net/cfile/tistory/99E40F3E5B49CE4530)

즉, 기울기 하강 알고리즘은 일반적으로는 비용함수 $J$에 대해서 지역적 최솟값을 찾아주며, 이 알고리즘을 통해 발견할 수 있는 지역적 최솟값은 초기 시작 위치에 따라 달라지게 된다. 다만 비용함수 $J$가 볼록함수에 해당할 경우 반드시 전역적 최솟값을 기울기 하강 알고리즘을 통해 찾을 수 있다.

당연하게도, 비용함수 $J$가 볼록함수가 아닌 경우에는 초기 시작 위치에 따라 다양한 지역적 최솟값을 찾을 수 있으며, 이 최솟값 중 가장 작은 것을 이용하여 학습의 정확도를 높일 수 있다.

### 기울기 하강 알고리즘의 수학적 이해

#### 과정의 설명

다음은 기울기 하강 알고리즘의 수학적 정의이다. 편미분이 사용된다. 생각보다 아주 간단하다.

![기울기 하강 알고리즘 수식](https://t1.daumcdn.net/cfile/tistory/99F9C24F5B49F6C011)

말로 설명해보도록 하자. 위의 말을 간단하게 이야기하면, 기울기 하강 알고리즘을 적용하려고 하는 비용함수 $J$의 모든 파라미터 $\theta$ 각각에 대하여 비용함수를 그 파라미터로 편미분 한 것에 일정 양의 상수를 곱한 것을 뺀 것을 다시 집어넣는다는 것이다.  

그리고 중요한 것, 실제 알고리즘의 적용 혹은 구현에서 자주 실수하는 것이니 반드시 주의해야 할 부분은,

**모든 $\theta$를 동시에 재대입(업데이트), 즉 Simultaneous Update 해 주어야 한다는 것이다.**

그러니까 예를 들어 먼저 $\theta_0$을 Gradient Descent로 바꿔버린다면 뒤의 $\theta_1$의 계산에서는 함수가 원래와 다르게 바뀌어버리므로 알고리즘이... _와장창_

위의 알고리즘의 동작을 대략적으로 살펴보도록 하자. 간단하게 논증하기 이위해서, 아래와 같이 비용함수가 단 하나의 파라미터 $\theta_1$으로 구성된다고 하자.

비용함수 $J$를 파라미터 $\theta_1$으로 편미분한 결과인 ${{\partial}\over{\partial \theta_1}} J(\theta_1)$의 부호에 따라서 어떤 방식으로 동작하게 되는지를 살펴보자.

![기울기 하강 알고리즘 수학적 타당성 설명](https://t1.daumcdn.net/cfile/tistory/9971DF3D5B49F8631B)

위의 그림을 보자. 첫 번째로 위쪽, ${{\partial}\over{\partial \theta_1}} J(\theta_1) > 0$인 경우를 보면, 양의 실수 $\alpha$와 곱해져 빼지므로 $\theta_1$은 감소하여 최솟값 부근으로 다가가게 된다.

두 번째로 아래쪽  ${{\partial}\over{\partial \theta_1}} J(\theta_1) < 0$인 경우를 보면, 양의 실수 $\alpha$와 곱해져 빼지므로 $\theta_1$은 증가하여 최솟값 부근으로 다가가게 된다.

어떤 함수의 편미분은 그 변수의 증감에 따른 함수의 증감 효과를 조사하는 것이므로 위와 같은 논증이 일반적으로 다수개의 Features를 가지고 있는 복잡한 비용함수에 대해서도 적용된다.

다만, 위에서도 지적하였듯이 이들 다수 Features를 동시에 업데이트해야 알고리즘이 정상적으로 동작함에 주의해야 한다.

#### $\alpha$의 의미

위의 알고리즘에서 임의의 양의 실수 $\alpha$는 Learning Rate라고 해서, 알고리즘의 학습 속도를 조절하는 역할을 한다. $\alpha$의 값에 따라서 학습에 걸리는 시간이나, 학습의 정확도가 달라질 수 있다.

아래 그림을 보자.

![alpha](https://t1.daumcdn.net/cfile/tistory/994B9D425B49FA3818)

우선 $\alpha$가 너무 작으면 그래프에 보인 바와 같이 뽈뽈 조금씩 기어내려가게 되어서 Gradient Descent 과정이 너무 오래 걸리게 된다. 이는 알고리즘의 효율성에서 좋지 못한 방법이다.

다른 한 편, $\alpha$가 너무 크면 그래프에 보인 바와 같이 너무 많이 이동하는 바람에 지속적으로 지역적 최솟값에 다가가지 못하고 크게 벗어나게 되는 경우가 생긴다.

따라서 Gradient Descent 알고리즘에서는 이 Learning Rate인 $\alpha$의 값을 적절하게 조작해주는 것이 효율을 올리는 비결이라고 할 수도 있겠다.