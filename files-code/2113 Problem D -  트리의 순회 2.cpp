///2113 Problem D - 트리의 순회 2 Solution
//중위 순회 문제이다.

#include <iostream>
using namespace std;

void inorder_visit(int root, int n) {
    if(root*2 <= n)
        inorder_visit(root*2, n);
    cout << (char)(root+96) << " ";
    if(root*2+1<=n)
        inorder_visit(root*2+1, n);
}

int main() {
    int n;
    cin >> n;
    inorder_visit(1, n);
    return 0;
}
