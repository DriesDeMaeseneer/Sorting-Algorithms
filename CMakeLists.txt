cmake_minimum_required(VERSION 3.17)
project(SORTINGALG)

set(CMAKE_CXX_STANDARD 14)

add_executable(SORTING main.cpp BubbleSort/BubbleSort.cpp BubbleSort/BubbleSort.h InsertionSort/Insertionsort.cpp
        InsertionSort/Insertionsort.h SelectionSort/SelectionSort.cpp SelectionSort/SelectionSort.h
        MergeSort/MergeSort.cpp MergeSort/MergeSort.h)