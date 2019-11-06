///2101 Problem B - 힙의 구성 Solution
#include <iostream>
using namespace std;

int main() {
    int n, temp, child;
    int data[1001];
    int heap[1001];

    cin >> n;
    for(int i=1;i<=n;i++)
        cin >> data[i];

    //최대 힙 구성
    for(int i=1; i<=n; i++) {
        heap[i] = data[i];
        for(int child = i, parent=child/2; parent>0 && heap[parent] < heap[child]; parent/=2, child/=2) {
            temp = heap[child];
            heap[child] = heap[parent];
            heap[parent] = temp;
        }
    }

    //최대 힙 출력
    for(int i=1;i<=n;i++)
        cout << heap[i] << " ";

    cout << endl;

    //최소 힙 구성
    for(int i=1; i<=n; i++) {
        heap[i] = data[i];
        for(int child = i, parent = child/2; parent>0 && heap[parent] > heap[child]; parent/=2, child/=2) {
            temp = heap[child];
            heap[child] = heap[parent];
            heap[parent] = temp;
        }
    }

    //최소 힙 출력
    for(int i=1;i<=n;i++)
        cout << heap[i] << " ";

    return 0;
}
