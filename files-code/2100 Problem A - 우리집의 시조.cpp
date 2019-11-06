///2100 Problem A - 우리집의 시조 Solution
//생각보다 간단한 문제이다. 시조는 부모가 없는 경우가 될 것이라는 점에 착안한다.
//별로 좋은 Solution은 아닌 듯. 길다.

#include <iostream>
using namespace std;

int main() {
    int k, n, input;
    int has_parent[1000001] = {0};
    int existence[1000001] = {0};

    cin >> k >> n;

    //건우의 존재
    existence[k]++;
    for(int i=0;i<n;i++) {
        cin >> input; //부모가 누구인지는 상관없다.
        if(!existence[input]) existence[input]++;

        //자식 1 데이터 핸들링
        cin >> input;
        if(!existence[input]) existence[input]++;
        has_parent[input]++;

        //자식 2 데이터 핸들링
        cin >> input;
        if(!existence[input]) existence[input]++;
        has_parent[input]++;
    }

    int i;
    for(i=1;i<=1000001;i++) {
        if(has_parent[i] == 0 && existence[i]) {
            cout << i;
            break;
        }
    }

    return 0;
}
