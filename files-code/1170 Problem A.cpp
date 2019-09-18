///1170 Problem A Solution
//이는 배열을 활용하는 문제이다. 문제의 도움말에도 쓰여 있듯이 배열에 저장하고 거꾸로 출력하면 된다.

#include <iostream>
using namespace std;

int main() {
    int n;
    int numbers[10000];

    cin >> n;
    for(int i=0;i<n;i++) cin >> numbers[i];

    for(int i=n-1;i>=0;i--) cout << numbers[i] << " ";

    return 0;
}
