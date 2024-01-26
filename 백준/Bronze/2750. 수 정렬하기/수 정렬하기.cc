#include<iostream>
#include<vector>
#include<algorithm>
using namespace std;

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N;
    cin >> N;
    vector<int> vec;
    int num;
    for (int i = 0; i < N; i++) {
        cin >> num;
        vec.push_back(num);
    }

    sort(vec.begin(), vec.end());

    for (int i : vec) cout << i << '\n';
    return 0;
}
