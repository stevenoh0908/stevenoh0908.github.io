///1170 Problem A Solution with list
//이는 배열을 활용하는 문제이나 굳이 리스트로 풀면 아래와 같다.

#include <iostream>
#include <list>
using namespace std;

int main() {
    int n, input;
    list<int> numbers;
    list<int>::iterator it;

    cin >> n;
    for(int i=0;i<n;i++) {
        cin >> input;
        numbers.push_front(input);
    }

    for(it=numbers.begin(); it!=numbers.end(); it++) cout << *it << " ";

    return 0;
}
