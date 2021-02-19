// This file will be edited soon.
#include <vector>
#include <iostream>

std::pair<int,int> Largest(std::vector<int> vector){
  int a {0};
  int index{0};
  for (int i{0};i<vector.size();i++){
    if (a<vector[i]){
      a = vector[i];
      index = i;
    }
  }
  return{a, index};
}

std::vector<int> SelectionSort(std::vector<int>& array){
  std::vector<int> sorted;
  std::pair<int,int> largestAndIndex;
  for (int i{0};i<array.size();i++){
      largestAndIndex = Largest(array);
      sorted.insert(sorted.begin(), largestAndIndex.first);
      array.erase(array.begin()+largestAndIndex.second);
  }
  return sorted;
}
