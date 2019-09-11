//1500 Problem A Solution
//주어진 정의역의 범위가 작으므로, linear 정렬로 간다.

#include <iostream>
using namespace std;

int data;

int main() {
    int max=0, idx=0;
    for(int i=0;i<9;i++) {
        cin >> data;
        if(data>max) {
            max = data;
            idx = i;
        }
    }
    cout << max << endl << idx+1 << endl;
    return 0;
}
