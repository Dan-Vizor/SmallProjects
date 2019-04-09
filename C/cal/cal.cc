#include <iostream>
#include <fstream>
using namespace std;

int help() {
	ifstream infile;
	infile.open("help.txt");
	cout << infile.rdbuf();
	infile.close();
	return 0;
}

int main() {
	char inp[10];
	int a, b;

	for( ; ; )	{
		cout << "enter your mode: ";
		cin >> inp;

		// add
		if (inp == string("add")) {
			cout << "enter first number: "; cin >> a;
			cout << "enter first second: "; cin >> b;
			cout << a + b << endl << endl;
		} 
		// subtract
		else if (inp == std::string("sub")) {
			cout << "enter first number: "; cin >> a;
			cout << "enter first second: "; cin >> b;
			cout << a - b << endl << endl;
		}
		// multiply
		else if (inp == std::string("mul")) {
			cout << "enter first number: "; cin >> a;
			cout << "enter first second: "; cin >> b;
			cout << a * b << endl << endl;
		}
		// divide
		else if (inp == std::string("div")) {
			cout << "enter first number: "; cin >> a;
			cout << "enter first second: "; cin >> b;
			cout << a / b << endl << endl;
		}
		// square
		else if (inp == std::string("squ")) {
			cout << "enter number: "; cin >> a;
			cout << a * a << endl << endl;
		}

		// exit
		else if (inp == std::string("exit") || inp == std::string("q")) {
			break;
		}
		// help menu
		else if (inp == std::string("help")) {
			help();
		} 
		else {
			cout << "Error: invald input" << endl << endl;
		}
	}
}