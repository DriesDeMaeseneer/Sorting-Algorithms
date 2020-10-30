#include <vector>

std::vector<int> BubbleSort(std::vector<int> vectortosort){
    for(int i = 0;i<vectortosort.size()-1;i++){
        for (int j = 0; j<vectortosort.size()-1-i;j++){
            if (vectortosort[j]>vectortosort[j+1]){
                int temp = vectortosort[j];
                vectortosort[j] = vectortosort[j+1];
                vectortosort[j+1] = temp;
            }
        }
    }
    return vectortosort;
}
int main(){
    return 0;
}
