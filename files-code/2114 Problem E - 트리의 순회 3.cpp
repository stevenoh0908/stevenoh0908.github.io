///2114 Problem E - 트리의 순회 3 Solution
//후위 순회 문제이다.

#include <iostream>
using namespace std;

void postorder_visit(int root, int n) {
    if(root*2 <= n)
        postorder_visit(root*2, n);
    if(root*2+1<=n)
        postorder_visit(root*2+1, n);
    cout << (char)(root+96) << " ";
}

int main() {
    int n;
    cin >> n;
    postorder_visit(1, n);
    return 0;
}
