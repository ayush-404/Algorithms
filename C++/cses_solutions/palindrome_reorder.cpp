#include <iostream>
#include <map>
#include <string>
#include <utility>
using namespace std;
typedef unsigned long long int ull;

int main() {
  int arr[27] = {0};
  string input;
  cin >> input;
  int numOdds = 0;
  for(char c : input) {
    arr[c - 'A']++;
    if(arr[c - 'A'] % 2 == 1) 
      numOdds++;
    else
      numOdds--;
  }
  if(numOdds > 1) {
    cout << "NO SOLUTION";
    return 0;
  }
  char OddChar = '!';
  for(char c = 'A'; c <='Z'; c++) {
    for(int i = 0; i < arr[c - 'A'] /2 ; i++){
      cout << c;
    }
    if(arr[c- 'A'] % 2 == 1) {
      OddChar = c;
    }
  }
  if(OddChar != '!') {
    cout << OddChar;
  }
  for(char c= 'Z' ; c >= 'A' ; c--) {
    for(int i = 0 ; i < arr[c-'A']/ 2; i++) {
      cout << c;
    }
  }
}