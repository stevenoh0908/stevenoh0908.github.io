#include <iostream>
using namespace std;

int n;

//Print Array
//배열 left~right 인덱스 원소 출력

void print(int data[], int left, int right) {
    for(int i=left;i<=right;i++) cout << data[i] << " ";
    cout << endl;
    return;
}

//Bubble sort(소스 이상, 고칠것!)
//버블 정렬은 인접한 두 원소의 대소를 비교하여 정렬이 완료될 때까지 자리를 바꾸는 정렬이다.

void bubble_sort(int data[], int left, int right) {
    int temp;
    for(int i=left;i<=right-1;i++) {
        for(int j=left;j<=right-i-1;j++) {
            if(data[j]>data[j+1]) {
                temp = data[j];
                data[j] = data[j+1];
                data[j+1] = temp;
            }
        }
    }
    return;
}

//Insertion sort
//삽입 정렬은 그 원소가 들어가야 할 위치를 찾아 그 위치에 원소를 삽입하는 정렬이다.

void insertion_sort(int data[], int left, int right) {
    for(int i=left+1;i<=right;i++) {
        int key = data[i];
        int idx;
        for(idx=i-1;idx>=0&&data[idx]>=key;idx--) {
            data[idx+1] = data[idx];
        }
        data[idx+1] = key;
    }
    return;
}

//Selection sort
//선택 정렬은 그 인덱스에 들어가야할 원소를 찾아 그 위치에 원소를 넣는 방법이다.

void selection_sort(int data[], int left, int right) {
    int temp;
    for(int i=left;i<=right;i++) {
        int min_idx = i;
        for(int j=i; j<=right;j++) {
            if(data[min_idx] >= data[j]) min_idx = j;
        }
        temp = data[i];
        data[i] = data[min_idx];
        data[min_idx] = temp;
    }
    return;
}

//Quick sort
//0. pivot을 선정한다.(임의적, 보통 가장 왼쪽이나 가장 우측, 중앙, 랜덤으로 설정하는 편이다, 이 코드에서는 가장 왼쪽을 기준으로 선정)
//1. 왼쪽 인덱스 i, 오른쪽 인덱스 j에 대하여, 각각 배열에서 순, 역방향으로 진행하면서 i는 pivot 보다 큰 원소를, j는 pivot 보다 작은 원소를 찾아 i, j의 원소를 교환한다.
//2. 리스트가 pivot보다 작은 원소들과, pivot보다 큰 원소들로 나누어진다. 각각에 대해서 다시 피벗 선정하고 진행한다.
//3. 피벗을 어떻게 잡느냐에 따라서 정렬이 완료될 때의 idx 위치가 달라짐에 유의해야 한다.

void quick_sort(int data[], int left, int right) {
    int pivot = data[left];
    int i=left+1, j=right;
    int temp;
    while(i<=j) {
        cout << i << endl;
        /* 나누기(partition) */
        while(pivot>data[i]) i++; //left 탐색에서 걸리는 idx 찾기
        while(pivot<data[j]) j--; //right 탐색에서 걸리는 idx 찾기
        if(i<=j) {
            //교환
            temp = data[i];
            data[i] = data[j];
            data[j] = temp;
            i++;
            j--;
        }
    }
    //끝나고 피벗과 교차점의 원소를 교환하여 분할을 완료한다.
    temp = data[left];
    data[left] = data[j];
    data[j] = temp;

    /* 재귀 호출(recursion) */
    if(left < j) quick_sort(data, left, j);
    if(j+1 < right) quick_sort(data, j+1, right);
    return;
}

int main() {
    int data[100];
    cin >> n;
    for(int i=0;i<n;i++) {
        cin >> data[i];
    }
    bubble_sort(data, 0, n-1);
    for(int i=0;i<n;i++) {
        cout << data[i] << " ";
    }
    return 0;
}
