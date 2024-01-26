#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    vector<int> A;
    vector<int> B;
    int input;
    int sum = 0;
    for (int i = 0; i < N; i++) {
        cin >> input;
        A.push_back(input);
    }
    for (int i = 0; i < N; i++) {
        cin >> input;
        B.push_back(input);
    }
    sort(A.begin(), A.end());
    sort(B.begin(), B.end(), greater<>());

    for (int i = 0; i < N; i++) {
        sum += A[i] * B[i];
    }
    cout << sum;
}
