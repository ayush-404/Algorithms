#include <stdio.h>
#include <string>
#include <vector>
#include <iostream>
using namespace std;
int main(int argc, char** argv){
    unsigned int currLen = 1, maxLen = 1;
    string input;
    getline(cin, input);
    for(int i =0; i < input.size()-1; i++) {
      if(input[i] == input[i + 1]){
        currLen++;
      }
      else
        currLen = 1;     

      if(maxLen < currLen)
        maxLen = currLen;
      
      }
    cout << maxLen;
}
