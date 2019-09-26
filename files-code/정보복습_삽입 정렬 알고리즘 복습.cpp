///Insertion Sort Algorithm Practice
//Âü°í: https://gmlwjd9405.github.io/2018/05/06/algorithm-insertion-sort.html
#include <iostream>
using namespace std;

int main() {
    int n;
    int data[10000];

    cin >> n;
    for(int i=0;i<n;i++) {
        cin >> data[i];
    }
    for(int i=1;i<n;i++) {
        int j;
        int key = data[i];
        for(j=i-1;j>=0&&data[j]>=key; j--) {
            data[j+1] = data[j];
        }
        data[j+1] = key;
    }
    for(int i=0;i<n;i++) {
        cout << data[i] << " ";
    }
    return 0;
}
