#include <iostream>
using namespace std;
extern float a, b, c;
extern int count;

int main() {
	int count;
	float a, b, c;
	a = 9000.0;
	b = 2.0;
   for(;;){
	   if(count > 100000000000){
		   //cout << "test" << endl;
		   return 0;
		  }
	   c = a / b;
	   count ++;
	   }
   return 0;
}
