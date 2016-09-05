#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	
	int T;
	cin >> T;

	for (int i = 0; i < T; i++)
	{

		int N, a, b;
		cin >> a >> b >> N;

		int j = 0;
		int sum = a;
		while (j < N)
		{
			sum += (pow(2, j) * b);
			cout << sum << " ";
			j++;
		}
		cout << endl;

	}
	return 0;
}
