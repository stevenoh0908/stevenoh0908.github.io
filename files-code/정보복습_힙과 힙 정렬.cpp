///정보복습 - 힙과 힙 정렬: 2진 힙에 대하여, 2019-11-20. 7교시

//최대 히프 구성
#include <iostream>
using namespace std;

int Heap[100];

int main() {
    int n, temp;
    cin >> n;
    for(int i=0;i<n;i++) {
        cin >> Heap[i];
        for(int child = i, parent = child/2; Heap[parent]<Heap[child] && parent>0; parent/=2, child/=2) {
            temp = Heap[child];
            Heap[child] = Heap[parent];
            Heap[parent] = temp;
        }
    }

    for(int i=0;i<n;i++) {
        cout << Heap[i] << " ";
    }
    return 0;
}

//힙 정렬은 최대 히프를 구성하고 루트 노드만 빼고 나머지 노드들에 대하여 최대 힙을 계속 구성하는 과정을 반복하면 된다.
//최소 히프에 대해서는 비교문만 반대이다.
