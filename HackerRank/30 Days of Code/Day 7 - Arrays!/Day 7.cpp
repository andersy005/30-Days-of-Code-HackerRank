#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main() {
	int n;
	cin >> n;
	vector<int> arr(n);
	for (int arr_i = 0;arr_i < n;arr_i++) {
		cin >> arr[arr_i];
	}

	for (auto i = 0; i < n;i++)
		cout << arr[n - 1 - i] << " ";
	return 0;
}