
#include "Insertionsort.h"

void vectorPrint(std::vector<int>& vectortoprint){
    std::cout<<"---\n";
    for(std::vector<int>::iterator it = vectortoprint.begin();it!=vectortoprint.end();it++){
        std::cout<<*it<<std::endl;
    }
    std::cout<<"---\n";
}

void InsertionSort(std::vector<int>& vectortosort){
//    std::iter_swap(vectortosort.begin(), vectortosort.begin()+1);
    for(int i{1};i<vectortosort.size();i++){
        int tmp = vectortosort[i];
        int j = i-1;
        while(j>=0 and tmp<vectortosort[j]){
            vectortosort[j+1] = vectortosort[j];
            j--;
        }
        vectortosort[j+1] = tmp;
    }
}