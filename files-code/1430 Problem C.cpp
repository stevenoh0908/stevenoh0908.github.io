//1430 Problem C Solution
//데이터가 이미 오름차순으로 정렬되어 있고, 주어진 정의역의 범위가 어느 정도 있으므로, Binary Search로 가자.

#include <iostream>
using namespace std;

int data[1000000];

//이게 Binary Search의 Body Script.
int find_data(int target, int start, int end) {
    if (target==data[(start+end)/2]) return (start+end)/2;
    if ((start-end)/2==0) return -2;
    else if (target > data[(start+end)/2]) return find_data(target, (start+end)/2, end);
    else if(target < data[(start+end)/2]) return find_data(target, 0, (start+end)/2);
}

int main() {
    int n, m, input;
    cin >> n;
    for(int i=0;i<n;i++) {
        cin >> data[i];
    }
    cin >> m;
    for(int i=0;i<m;i++) {
        cin >> input;
        cout << find_data(input, 0, n-1)+1 << " ";
    }
    return 0;
}
