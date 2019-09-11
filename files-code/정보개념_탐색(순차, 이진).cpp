/*
> 순차 탐색(Squential Search)
 - 리스트 처음부터 끝까지 차례대로 모든 요소를 비교해서 자료를 찾는 탐색 알고리즘
 - 한 쪽 방향으로만 탐색을 수행한다고 해서 선형 탐색(Linear Search)이라고 부르기도 한다.

> 자기 구성 순차 탐색
 - 전진 이동법(한번 검색된 데이터는 데이터집합의 가장 앞으로 이동)
 - 전위법(탐색된 항목을 바로 이전 항목과 교환)
 - 빈도 계수법(탐색된 횟수 정보를 저장하고, 탐색된 횟수가 높은 순으로 재구성)

> 이진 탐색(Binary Search)
 - 정렬된 데이터 집합에서 사용할 수 있는 고속 탐색 방법
 - 탐색 범위를 1/2씩 줄여나가는 방식
 - 이진 탐색의 시간 복잡도는 O(log2 n)이다.

> 이진 탐색 알고리즘(Binary Search Algorithm)
 0. 데이터를 정렬해놓고 탐색을 수행한다.
 1. 데이터 집합의 중앙에 위치한 요소를 고른다.(인덱스가 중앙이라는 것이다)
 2. 중앙 요소의 값과 찾고자 하는 목표값을 비교한다.
 3. 목표 값이 중앙 요소의 값보다 작다면 중앙을 기준으로 데이터 집합의 왼편에 대해, 크다면 오른편에 대해 이진 탐색을 수행
 4. 데이터 나올 때까지 1~3을 수행

> 이진 탐색 성능 분석
 - 탐색 대상의 범위가 1/2, 1/4, 1/8, 1/16 ...
 - 데이터 집합의 크기를 n, 탐색 반복 횟수를 x라 한다면,
 - 1 = n X (1/2)^x
 - x = log_2 n
*/

//아래 Binary Search Algorithm은 1430 Problem C의 Solution에서 들고 왔다.

#include <iostream>
using namespace std;

int data[10000];

int find_linear(int target, int start, int end) {
    for(int i=0;i<n;i++) {
        if(data[i] == target) return i;
    }
    return -1;
}

//Binary Search의 재귀함수형
//아래 함수는 찾아진 원소의 index를 return 한다.
int find_binary(int target, int start, int end) {
    int mid = (start+end)/2
    if (target==data[mid]) return mid;
    if ((start-end)/2==0) return -1;
    else if (target > data[mid]) return find_binary(target, mid, end);
    else if(target < data[mid]) return find_binary(target, 0, mid);
}

//이건 KYH 선생님의 while문으로 Binary Search 구현한 코드
int BinarySearch(int data[], int n, int key) {
    int left=0, right=n-1, mid;
    while(left<=right) {
        mid=(left+right)/2;
        if(key==data[mid])
            return mid;
        else if(key<data[mid])
            right=mid-1;
        else
            left=mid+1;
    }
    return -1;
}

//n개의 data를 입력해서 그 중에 찾고자 하는 m개의 input이 몇 번째 원소인지 출력한다.(index는 0부터 시작)
int main() {
    int n, m, input;
    cin >> n;
    for(int i=0;i<n;i++) {
        cin >> data[i];
    }
    cin >> m;
    for(int i=0;i<m;i++) {
        cin >> input;
        cout << find_binary(input, 0, n-1) << " ";
    }
    return 0;
}
