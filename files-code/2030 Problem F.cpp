///2030 Problem F Solution
//큐 문제이다. judgeon 상에 문제가 있어 제출하면 WA가 뜬다. 그러나 아래는 올바른 Solution이다.

#include <iostream>
#include <queue>
using namespace std;

int main() {
    queue<char> data;
    int n;
    char input;

    cin >> n;
    for(int i=0;i<n;i++) {
        cin >> input;
        if(input != '-') data.push(input);
        else if(!data.empty()) data.pop();
        else {
            cout << "error!";
            return 0;
        }
    }

    while(!data.empty()) {
        cout << data.front() << endl;
        data.pop();
    }

    return 0;
}
