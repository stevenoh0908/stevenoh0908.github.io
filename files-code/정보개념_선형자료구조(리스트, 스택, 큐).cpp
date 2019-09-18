///정보개념_선형자료구조(리스트, 스택, 큐)
//배열도 선형자료구조에 들어가나, 너무 신물나게 배운 관계로 제낀다.

/*
 > 선형 자료 구조(linear data structure)
  - 자료를 저장하고 접근하는 관계가 선형적으로 구성되는 자료 구조로서(실제로 그렇게 되는 것은 아니나, 논리적으로 추상화한 것 - 추상화 자료형. abstract data type), 배열, 리스트, 스택, 큐가 있음.
  - 배열은 신물나게 배웠으니, 설명을 제외한다. 리스트, 스택, 큐 등은 메모리의 물리적인 공간을 연속적으로 사용하는 배열과는 달리, 불연속적인 공간을 활용 가능함.
  - 또한 배열은 크기가 유동적이지 않다는 단점이 있음. - 리스트는 이의 해결이 가능함. (다음 주소만 추가시켜줌으로서 공간을 append하면 되므로)
  - 배열을 제외한 추상적 선형 자료 구조들은, std 클래스 선 지정자가 앞에 붙음. using namespace std;로 제거.

 > 리스트(list) - 탐색은 -, 자료 재구성은 +
  - 하나의 연결 관계에 따라 자료들을 한 줄로 연결시킨 형태로, 추상화된 자료구조
  - 배열과는 달리, 연결관계의 재구성만으로 중간에 자료를 삽입, 삭제 가능 - 삽입 정렬 등에서 데이터 이동에 따른 비용 절감의 효과
  - 메모리상의 연속적이지 않은 공간을 연속적인 것처럼 사용 가능
  - 그 인덱스의 원소와 다름 리스트 주소 저장(리스트에서 원소 접근 위해서는 순차적으로 접근해야 하는 단점)
  - 라이브러리: <list>
  - 생성자: std::list<자료형>
  - 주요 메서드
   -> 삽입: push_front(x): 첫번째 원소 앞에 x 삽입(연결), push_back(x): 마지막 원소 다음에 자료 x 삽입(연결) insert(k, x): k 위치 앞에 자료 x 삽입
   -> 삭제: pop_front(x): 첫번째 원소 삭제, pop_back(x): 마지막 원소 삭제, erase(k): k 위치의 자료를 삭제.
   -> 기타: begin(): 첫번째 원소 위치 반환, end(): 마지막 원소의 다음 위치(종결자) 반환(리스트 구조의 형태를 생각해보라!, 맨 마지막 다음에 종결 인자가 들어올 수 밖에 없다), size() : 리스트에 연결된 자료의 개수 반환
  - 이터레이터(iterator, 반복자): 리스트에 들어 있는 자료들의 위치를 선형적 접근이 가능하도록 해주는 자료(pointer, 주소를 16진수 형태로 출력해줌. *iterator는 그 주소에 저장된 값을 돌려준다)
   -> 생성자: std::list<자료형>::iterator -> 마치 for 문에서 int i 사용하듯이 사용 가능, iterator++로 다음 주소로 접근 가능함(iterator+=1 등은 사용할 수 없음. 전/후치 증/감 연산자만 사용 가능)
   -> 리스트 중간에 삽입하려면, 바로 k번째 위치에 k에 int 쓰면 안되고, 주소가 와야 하므로, iterator를 이동시켜서 삽입해야 한다.

 > 스택(stack) - 쌓는다
  - LIFO(Last In, First Out) 형태. 쌓아 올리는 자료 구조.
  - 이전에 저장된 자료에 접근하기 위해서는, 그 위에 쌓인 자료들 제거 필요. 즉, 삽입과 삭제는 스택의 가장 위에서만 가능.
  - 라이브러리: <stack>
  - 생성자: std::stack<자료형>
  - 주요 메서드
   -> 삽입: push(x): 스택 가장 위에 자료 x 추가.
   -> 삭제: pop(): 스택 가장 위에 있는 자료의 삭제.
   -> 기타: empty(): 스택이 비어 있는지 확인(bool return), size(): 스택의 자료 개수 return. top(): 스택의 최고 위의 값 return
   -> empty 여부를 먼저 검사하지 않고 pop을 실행하면 error raise.

 > 큐(queue) - 통과한다
  - FIFO(First In, First Out) 형태, 관을 통과하는 자료 구조.
  - 순서대로 자료를 넣으며, 넣은 순서대로 자료 접근 가능(끝에서 넣고, 앞에서 확인 - 확인은 앞과 뒤에서 가능하기는 함) - 즉, 뚫린 부분에만 접근 가능함.
  - 라이브러리: <queue>
  - 생성자: std::queue<자료형>
  - 주요 메서드
   -> 삽입: push(x): 큐의 마지막에 자료 x 추가
   -> 삭제: pop(): 큐의 처음의 자료 삭제
   -> 기타: empty(): 큐의 empty 검사(bool return), size(): 큐의 size(자료 개수) return, front(): 큐의 처음 자료 값 return, back(): 큐의 마지막 자료 값 return
   -> empty 여부를 먼저 검사하지 않고 pop을 실행하면 error raise.
*/

//list
#include <iostream>
#include <list>
using namespace std;

list<int> mylist;

//list 모두 출력
void view_list() {
    list<int>::iterator it;
    for(it=mylist.begin(); it!=mylist.end(); ++it)  {
        printf("%d", *it); //*it: it위치에 있는 리스트 값(pointer인 it)
    cout<<endl;
    }
}

int main() {
    //n개의 자료를 순서대로 list에 넣고 모두 출력
    int n, input;
    cin >> n;
    for(int i=0;i<n;i++) {
        cin >> input;
        mylist.push_back(input);
    }
    view_list();

    //다음 입력된 자료를 list의 맨 앞에 넣음
    cin >> input;
    mylist.push_front(input);

    //list의 다음 입력된 위치에 그 다음 입력된 원소를 넣음
    cin >> input;
    list<int>::iterator i;

    i = mylist.begin();
    for(int j=0;j<input;j++) i++;

    cin >> input;
    mylist.insert(i, input);

    //전체 리스트를 확인
    view_list();
    return 0;
}

/*
//stack
#include <iostream>
#include <stack>
using namespace std;

stack<int> mystack;

int main() {
    //n개의 원소를 stack에 넣음
    int n, input;
    cin >> n;
    for(int i=0;i<n;i++) {
        cin >> input;
        mystack.push(input);
    }

    //stack의 모든 원소를 출력
    while(!mystack.empty()) {
        cout << mystack.top() << endl;
        mystack.pop();
    }

    return 0;
}
*/

/*
//queue
#include <iostream>
#include <queue>
using namespace std;

queue<int> myqueue;

int main() {
    //n개의 원소를 queue에 넣음
    int n, input;
    cin >> n;
    for(int i=0;i<n;i++) {
        cin >> input;
        myqueue.push(input);
    }

    //queue의 front 자료값과 back 자료값 출력
    cout << myqueue.front() << endl << myqueue.back() << endl;

    //queue의 모든 자료값을 넣은 순서대로 출력
    while(!myqueue.empty()) {
        cout << myqueue.front() << endl;
        myqueue.pop();
    }

    return 0;
}
*/
