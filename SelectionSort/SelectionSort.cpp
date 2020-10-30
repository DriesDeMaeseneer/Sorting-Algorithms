// This file will be edited soon.
#include <vector>
#include <iostream>

int Largest(std::vector<int> vector){
  int a {0};
  for (int i:vector){
    if (a<i){
      a =i;
    }
  }
  return a;
}

int main(){
  return 0;
}
