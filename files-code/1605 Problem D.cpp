//1605 Problem D Solution
//데이터가 이미 오름차순으로 정렬되어 있고, 주어진 정의역의 범위가 얼마 없으므로, Linear Search로 간다.
//같은 수가 여러 개 존재할 수 있음에 유의해야 한다.
//Binary Search는 그 특성상 중복값에 약하므로, 최초로 등장하는 범위를 알 수 있는 방법은 혼용을 하던가, Linear Search로 구현해야 할 것이다

#include <iostream>
using namespace std;

int data[500000];

int main() {
    int n, k;
    cin >> n;
    for(int i=0;i<n;i++) {
        cin >> data[i];
    }
    cin >> k;

    for(int i=0;i<n;i++) {
        if(data[i] >= k) {
            cout << i+1;
            return 0;
        }
    }

    cout << n+1;
    return 0;
}
