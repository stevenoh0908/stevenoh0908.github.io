///2011 Problem E Solution
//스택 문제이다 문제의 조건대로 간다.

#include <iostream>
#include <stack>
using namespace std;

int main() {
    stack<int> data;
    int n;
    int s = 0;

    cin >> n;
    for(int i=1;i<=n;i++) {
        s += i;
        data.push(s);
    }

    while(!data.empty()) {
        cout << data.top() << " ";
        data.pop();
    }

    return 0;
}
