///2010 Problem D Solution
//스택 문제이다. 스택을 사용해서 연산 후의 결과값을 출력한다는 것이다. 문제의 조건대로 코딩하자.

#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> data;
    int n, k;

    cin >> n;
    for(int i=0;i<n;i++) {
        cin >> k;
        data.push(k);
    }

    int sum = 0;
    int foo;
    sum = foo = data.top();
    data.pop();

    while(!data.empty()) {
        if(data.top()<foo) sum -= data.top();
        else sum += data.top();
        foo = data.top();
        data.pop();
    }

    cout << sum;

    return 0;
}
