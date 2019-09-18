///1186 Problem B Solution
//배열을 사용해서 푸는 문제이다. 이미 풀어본 바가 있다(일차원 배열 연습에서)

#include <iostream>
using namespace std;

int main() {
    int n, a, b;
    int data[50];

    cin >> n;
    for(int i=0;i<n;i++) {
        cin >> data[i];
    }
    cin >> a >> b;

    int foo = data[b-1];
    for(int i=b-1;i>=a-1;i--) data[i] = data[i-1];
    data[a-1] = foo;

    for(int i=0;i<n;i++) {
        cout << data[i] << " ";
    }

    return 0;
}
