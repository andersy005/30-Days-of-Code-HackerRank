#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
using namespace std;


int main() {
	

	double mealprice, tipperc, taxperc, finalprice;
	cin >> mealprice;
	cin >> tipperc;
	cin >> taxperc;

	double tip = mealprice * tipperc / 100;
	double tax = mealprice * taxperc / 100;
	finalprice = mealprice + tip + tax;

	cout << "The final price of the meal is $" << (int)round(finalprice) << ".";

	return 0;
}