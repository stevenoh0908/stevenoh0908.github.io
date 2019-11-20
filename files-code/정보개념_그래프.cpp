///정보개념 - 그래프 2019-11-20. 6교시

//2차원 배열을 이용한 인접 행렬로서의 그래프 저장: 무방향/무가중치
//메모리를 아끼기 위하여 약간의 변형을 가했음.
/*
#include <iostream>
using namespace std;

int v, e, G[10][10];

int main() {
    int v1, v2;
    cin >> v >> e;

    //v1->v2, v2->v1 연결관계 1, 0 저장
    for(int i=0; i<e ; i++) {
        cin >> v1 >> v2;
        G[v1-1][v2-1] = G[v2-1][v1-1] = 1;
    }

    //연결 관계를 저장한 인접 행렬 2차원 배열의 출력
    for(int i=0;i<v;i++) {
        for(int j=0;j<v;j++)
            cout << G[i][j] << " ";
        cout << endl;
    }

    return 0;
}
*/

//2차원 배열을 이용한 인접 행렬로서의 그래프의 저장: 유방향/유가중치
//메모리를 아끼기 위하여 약간의 변형을 가함.
/*
#include <iostream>
#define NO_CONNECTION 0
using namespace std;

int v, e;
int G[10][10] = {NO_CONNECTION};

int main() {
    int v1, v2, w;
    cin >> v >> e;

    //v1->v2 간선에 대한 가중치의 저장
    for(int i=0;i<e;i++) {
        cin >> v1 >> v2 >> w;
        G[v1-1][v2-1] = w;
    }

    //모든 간선의 연결에 대한 가중치의 연결 정보
    for(int i=0;i<v;i++) {
        for(int j=0;j<v;j++)
            cout << G[i][j] << " ";
        cout << endl;
    }

    return 0;
}
*/

//Vector의 이용
/*
#include <iostream>
#include <vector>
using namespace std;

vector<int> vect;

int main() {
    int n;
    cin >> n;
    for(int i=0; i<n; i++)
        vect.push_back(i*10);
    for(int i=0; i<vect.size(); i++)
        cout << vect[i] << " ";
    return 0;
}
*/

//Vector를 이용한 인접 리스트로서의 그래프 저장: 무방향성/무가중치
/*
#include <iostream>
#include <vector>
using namespace std;

int v, e;
vector<int> G[10];

int main() {
    int v1, v2;
    cin >> v >> e;

}
*/

//Vector를 이용한 인접 리스트로서의 그래프 저장: 유방향성/유가중치
/*
#include <iostream>
#include <vector>
using namespace std;

int v, e;
struct NODE {
    int vn;
    int w;
};
vector<NODE> G[10];
NODE node;

int main() {
    int v1, v2, w;
    cin >> v >> e;

    //v1->v2 간선에 대한 가중치의 저장
    for(int i=0;i<e;i++) {
        cin >> v1 >> v2 >> w;
        node.vn = v2;
        node.w = w;
        G[v1-1].push_back(node);
    }

    //v1->v2 간선에 대한 모든 연결 출력
    for(int i=0;i<v;i++) {
        cout << G[i].size() << ": ";
        for(int j=0;j<G[i].size();j++) {
            cout << G[i][j].w << " ";
        }
        cout << endl;
    }

    return 0;
}
*/


/*
수행평가는 Judgeon 트리의 순회 3까지의 모든 문제 중 5문 랜덤
시험은 2학기 배운 전 범위
*/
