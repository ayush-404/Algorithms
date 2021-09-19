#include <iostream>
// The algorithm is to find the gray code for lenght n-1. 
// Then gray code is 1 appened to the reverse of gray code of n-1.
#include <string>
#include <vector>
using namespace std;
int Pow(int a, int x) {
  int ans = 1;
  for(int i =1; i <= x; i++) {
    ans = ans * a;
  }
  return ans;
}
int main() {
  int n;
  cin >> n;
  vector<string> ans;

  if(n == 1) {
    cout << "0\n1";
    return 0;
  }  
  string s;
  s.insert(0, n, '0');
  ans.push_back(s);
    cout << s << endl;
  s[n-1] = '1';
  ans.push_back(s);
    cout << s << endl;
  s[n-2] = '1';
  ans.push_back(s);
    cout << s << endl;
  s[n-1] = '0';
  ans.push_back(s);
    cout << s << endl;
  string curr;
  for(int i = 2; i < n; i++) {
    for(int j = Pow(2, i) - 1; j >= 0; j--) {
      curr = ans[j];
      curr[n - i - 1] = '1';
      ans.push_back(curr);
      cout << curr << endl;
    }
  }
}
