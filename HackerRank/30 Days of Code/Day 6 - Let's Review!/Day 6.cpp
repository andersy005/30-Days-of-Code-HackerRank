#include <iostream>

using namespace std;

int main() {
	int n;
	cin >> n;
	for (int i = 1; i <= n; i++) {
		for (int x = 1; x < (n - i + 1); x++) {
			cout << " ";
		}
		for (int x = 1; x < (i + 1); x++) {
			cout << "#";
		}
		cout << endl;
	}
	return 0;
}