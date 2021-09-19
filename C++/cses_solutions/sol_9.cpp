#include <iostream>
using namespace std;
typedef unsigned long long int ull;
int main() {
  ull n;
  cin >> n;
  ull ans = 1;
  for(ull i = 1 ;i<=n ;i++ ) {
    ans = 2*ans % 1000000007;
  }
  cout << ans;
}