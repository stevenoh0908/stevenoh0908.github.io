///Bubble Sort Algorithm Practice
//Âü°í: https://gmlwjd9405.github.io/2018/05/06/algorithm-bubble-sort.html
#include <iostream>
using namespace std;

int main() {
    int data[100];
    int n, foo;

    cin >> n;
    for(int i=0;i<n;i++) {
        cin >> data[i];
    }

    for(int i=0;i<n;i++) {
        for(int j=0;j<n-i-1;j++) {
            if(data[j] > data[j+1]) {
                foo = data[j];
                data[j] = data[j+1];
                data[j+1] = foo;
            }
        }
    }

    for(int i=0;i<n;i++) {
        cout << data[i] << " ";
    }
    return 0;
}
