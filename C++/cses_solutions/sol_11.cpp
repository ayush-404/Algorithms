#include <iostream>
using namespace std;
typedef unsigned long long int ull;
int main() {
  ull t, a, b, nR, nL;
  cin >> t;
  for (int i = 1; i <= t; i++) {
    cin >> a;
    cin >> b;
    nR = 2*a - b / 3;
    nL = (a- nR) / 2;
    if((2*a - b) % 3 == 0 && nR >= 0 ){
      if(a - nR % 2 ==0 && nL >= 0)
        cout << "YES" << endl;
      else 
        cout << "NO" << endl;
    }
    else {
      cout << "NO" << endl;
    }
  }
}