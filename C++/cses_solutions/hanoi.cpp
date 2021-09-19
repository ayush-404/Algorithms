#include <iostream>

typedef unsigned long long int ull;
using namespace std;

int Pow(int a, int x) {
  int ans = 1;
  for(int i =1; i <= x; i++) {
    ans = ans * a;
  }
  return ans;
}


void hanoi(int n, string A, string B, string C) {
  if(n == 0) {
    return ;
  }
  hanoi(n-1, A, C,B);
  cout << A << " " << C << endl;
  hanoi(n-1, B, A, C);
}

int main() {
 int n;
 cin >> n;
 cout << Pow(2, n) - 1 << endl;
 hanoi(n, "1", "2" , "3");
}