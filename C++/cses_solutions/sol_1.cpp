#include <stdio.h>
#include <string>
#include <iostream>
int main(int argc, char** argv){
  unsigned long n;
  scanf("%lu",&n);
  while(true){
    printf("%lu ",n);
    if(n==1)   break;
    n = n%2==0? n/2: 3*n+1;
  }
}
