///2112 Problem C - 트리의 순회 1 Solution
//전위 순회 문제이다.

#include <iostream>
using namespace std;

void preorder_visit(int root, int n) {
    cout << (char)(root+96) << " ";
    if(root*2 <= n)
        preorder_visit(root*2, n);
    if(root*2+1<=n)
        preorder_visit(root*2+1, n);
}

int main() {
    int n, i;
    cin >> n;
    preorder_visit(1,n);
    return 0;
}
