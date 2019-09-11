//1431 Problem B Solution
//주어진 정의역의 범위가 작으므로, linear 탐색으로 간다.

#include <iostream>
using namespace std;

int data[100000];

int main() {
    int n, target;
    cin >> n;
    for(int i=0;i<n;i++) {
        cin >> data[i];
    }
    cin >> target;
    for(int i=0;i<n;i++) {
        if(data[i] == target) {
            cout << i+1;
            return 0;
        }
    }
    cout << -1;
    return 0;
}
