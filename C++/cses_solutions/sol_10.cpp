#include <iostream>
using namespace std;
typedef unsigned long long int ull;
int main() {
  ull n;
  cin >> n;
  ull count = 0;
  for(int i = 5 ; n/i >= 1; i *=5) {
    count += n/i;
  }
  cout <<  count;
}