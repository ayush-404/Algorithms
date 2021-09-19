#include <iostream>
using namespace std;
int main() {
  unsigned long long n;
  cin >> n;
  unsigned long long prev=0, curr=0, ans=0, diff=0;
  cin >> prev;

  for(int i = 1 ; i < n; i++) {
    cin >> curr;
    diff = prev > curr ? prev - curr : 0;
    ans += diff;
    prev = curr + diff;
  }
  printf("%llu", ans);
}