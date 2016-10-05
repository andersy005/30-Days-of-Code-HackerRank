/*
ID: axbanih1
PROG: ride
LANG: C++                
*/
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
	ofstream fout("ride.out");
	ifstream fin("ride.in");
	int a, b;
	fin >> a >> b;
	fout << a + b << endl;
	return 0;
}