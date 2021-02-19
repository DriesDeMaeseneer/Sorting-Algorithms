#include "MergeSort.h"

void MergeStep(std::vector<int>& mergeInto, std::vector<int>& v1, std::vector<int>& v2){
    while(!v1.empty() and !v2.empty()){
        if(v1[0]<v2[0]){
            mergeInto.push_back(v1[0]);
            v1.erase(v1.begin()+0);
        }
        else{
            mergeInto.push_back(v2[0]);
            v2.erase(v2.begin()+0);
        }
    }
    if(v1.empty()){
        if(!v2.empty()){
            while(!v2.empty()){
                mergeInto.emplace_back(v2[0]);
                v2.erase(v2.begin() + 0);
            }
        }
    }
    else if(v2.empty()){
        while(!v1.empty()) {
            mergeInto.emplace_back(v1[0]);
            v1.erase(v1.begin() + 0);
        }
    }
}


void MergeSort(std::vector<int>& to_sort){
    if(to_sort.size()>2){
        std::vector<int> v1(to_sort.begin()+0, to_sort.begin()+to_sort.size()/2);
        std::vector<int> v2(to_sort.begin()+to_sort.size()/2, to_sort.end());
        MergeSort(v1);
        MergeSort(v2);
        to_sort.clear();
        MergeStep(to_sort, v1, v2);
    }
    else{
        if(to_sort.size()==2){
            if(to_sort[0]>to_sort[1]){
                int tmp = to_sort[0];
                to_sort[0] = to_sort[1];
                to_sort[1] = tmp;
            }
        }
    }
}