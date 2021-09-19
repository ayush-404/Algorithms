#include <iostream>
using namespace std;
#include <set>
typedef unsigned long long int ull;
int main() {
  long long unsigned int n;
  cin >> n;
  set<unsigned long long int> set;    
  long long unsigned int sum = (n*(n+1)) / 2;
  long long unsigned int halfSum = sum /2;
  long long unsigned int lasti;
  if(sum % 2 == 1 ) {
    cout << "NO"; 
    return 0;
  } 
  else {
    cout << "YES" <<endl;
    for(unsigned long long int i = n ; i <= halfSum ; i--) {
      halfSum = halfSum - i;
      lasti = i;
      set.insert(i);
    }
    if(halfSum != 0) {
      set.insert(halfSum);
    }
    cout << set.size() << endl;
    for (ull i : set) {
      cout << i << " ";
    }
    cout << endl;
    cout << lasti - 1 << endl;
    for(ull i = 1 ; i < lasti; i++) {
      if(i == halfSum)  continue;
      cout << i << " ";
    }
  }
  return 0;
  
}