#include <iostream>
using namespace std;

int main() {
  long long unsigned int n, f;
  cin >> n;
  for(unsigned long long int i = 1; i<=n; i++) {
    f = (((i*i)*(i*i - 1))/ 2)- 4 * (i -1) *(i-2);
    cout << f << "\n"; 
  }
}