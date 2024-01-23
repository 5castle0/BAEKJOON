#include <iostream>
#include <queue>
using namespace std;

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int n, k;
	cin >> n >> k;
	queue<int> que;

	for (int i = 1; i <= n; i++) {
		que.push(i);
	}
	cout << "<";
	while (que.size() != 0) {
		for (int j = 1; j < k; j++) {
			que.push(que.front());
			que.pop();
		}
		cout << que.front() ;
		if (que.size() != 1) cout << ", ";
		que.pop();
	}
	cout << ">";
	return 0;
}