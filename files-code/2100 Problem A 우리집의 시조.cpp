///2100 Problem A 우리집의 시조 Solution.. 미완성

#include <iostream>
using namespace std;

struct DATA {
    int parent=0;
    int child1=0, child2=0;
};

int main() {
    int k, n;
    cin >> k >> n;
    DATA data[100];

    int parent, child1, child2;
    for(int i=0;i<n;i++) {
        cin >> parent >> child1 >> child2;
        data[parent].child1 = child1;
        data[parent].child2 = child2;
        data[child1].parent = parent;
        data[child2].parent = parent;
    }

    while(1) {
        if(data[k].parent != 0) {
            k = parent;
        }
        else break;
    }

    cout << k;
    return 0;
}

//진우 필기: 부모가 없는 데이터가 조상임.
