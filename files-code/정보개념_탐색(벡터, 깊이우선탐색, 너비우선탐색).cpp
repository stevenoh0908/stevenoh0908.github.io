///정보개념_탐색(벡터, 깊이우선탐색, 너비우선탐색)
//Vector 참고자료: https://blockdmask.tistory.com/70

/*
#Vector(벡터)
> 리스트와 배열의 중간쯤 되는 느낌의 선형자료구조로서, 자동으로 메모리가 할당되는 배열이라고 생각하면 된다.
> 배열과는 달리, 중간에 값을 삽입하거나 삭제할 수 있다.
> 배열기반이기 때문에 삽입과 삭제가 빈번하게 일어나면 비효율적이기는 하다.
> v.front()와 v.back()이 존재하며, push_back()과 pop_back()으로 맨 뒤쪽에서 삽입과 삭제가 가능하다.

#Vector의 사용
> 벡터의 사용은 <vector> 헤더 파일을 추가하여야 한다.
> using namespace std;를 해주면 편리하다.
> vector의 선언은 vector<data type> name이다.
>> ex) vector<int> v;

#Vector의 생성자와 연산자(편의상 data type는 int로 고정)
> vector<int> v; - 비어있는 vector v 생성
> vector<int> v(5); - 기본값(0)으로 초기화된 5개의 원소를 가지는 vector v를 생성
> vector<int> v(5, 2); - 2로 초기화된 5개의 원소를 가지는 vector v를 생성
> vector<int> v2(v1); - vector v2를 v1 벡터를 복사하여 생성한다.

#Vector의 멤버함수
> v.assign(5, 2); - 2의 값으로 5개의 원소를 할당한다.
> v.at(index); - index번째의 원소를 참조한다(범위 점검, 안전 느림)
> v[index] - index번째의 원소를 참조(범위 무점검, 불안전 빠름)
> v.front(); - 1번째 원소를 참조
> v.back(); - 마지막 원소를 참조
> v.clear(); - 모든 원소를 제거한다. 단, 원소만 제거하고 메모리는 남아있으므로, size만 감소하고 capacity는 그대로이다.
> v.push_back(n); - 마지막 원소 뒤에 원소 n을 삽입
> v.pop_back(); - 마지막 원소를 제거
> v.begin() - 1번째 원소를 가리킴(iterator 사용/리스트와 동일)
> v.end() - 마지막의 "다음"을 가리킴(iterator 사용/리스트와 동일)
> v.rebegin() - reverse begin(역순 1번째 원소)를 가리킴(iterator 사용)
> v.rend() - reverse end(역순 마지막 다음)을 가리킴(iterator 사용)
> v.reserve(n) - n개의 원소를 저장할 위치를 예약(동적할당)
> v.resize(n) - vector의 크기를 n으로 변경하며, 더 커진 경우 새로 생긴 공간들은 default 값인 0으로 초기화됨
> v.resize(n, 3) - vector의 크기를 n으로 변경하며, 더 커졌을 경우 새로 생긴 공간들은 3으로 초기화
> v.size() - vector의 원소의 개수를 리턴
> v.capacity() - vector에 할당된 공간의 크기를 리턴/공간 할당의 기준은 점점 커지면서 capacity를 할당(push_back이 일어날때마다 동적할당을 하면 비효율적이므로, 정해둔만큼 동적 할당을 한꺼번에)
> v2.swap(v1) - v1, v2의 vector의 capacity를 스왑한다(모든 것을 스왑)
>> v1의 capacity를 없앨 때(할당한 메모리를 프로그램이 끝나기 전에 없애고 싶을 때) 사용하기도 한다.: vector<int>().swap(v1);
> v.insert(2, 3, 4)- 2번째 위치에 3개의 4를 삽입(뒤로 밀면서)
> v.insert(2, 3)- 2번째 위치에 3 삽입하고, 삽입한 곳의 iterator를 반환
> v.erase(iterator) - iterator가 가리키는 원소를 제거한다. size만 줄어들고 capacity는 그대로 남는다. erase는 파라미터 하나를 받을 때와 두개를 받을 때 다르다.
> v.empty() - vector가 비었으면 true를 리턴하며, 기준은 size
*/
