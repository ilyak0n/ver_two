// тут реализованы функции

#include "head.h"
#include <vector>
#include <chrono>
#include <random>
 
using namespace std;
using namespace chrono;

int Rnd (int a, int b) {
    int seed = system_clock::now().time_since_epoch().count();
    static default_random_engine rnd(seed);
    static uniform_int_distribution<int> d(a, b);
    return d(rnd);
}
double Rnd (double a, double b) {
    int seed = system_clock::now().time_since_epoch().count();
    static default_random_engine rnd(seed);
    static uniform_real_distribution<double> d(a, b);
    return d(rnd);
}

void mySortBubble(vector<int> &mas, int &r) {
    for (size_t i = 0; i < mas.size() - 2; i++)
        for (size_t j = 0; j < mas.size() - i - 1; j++) {
            r++;
            if (mas[j] > mas[j + 1]) {
                int buf = mas[j];
                mas[j] = mas[j + 1];
                mas[j + 1] = buf;
            }
        }
}
 
void mySortBubble(vector<double> &mas, int &r) {
    for (size_t i = 0; i < mas.size() - 2; i++)
        for (size_t j = 0; j < mas.size() - i - 1; j++) {
            r++;
            if (mas[j] > mas[j + 1]) {
                double buf = mas[j];
                mas[j] = mas[j + 1];
                mas[j + 1] = buf;
            }
        }
}

void myQsort(vector<int> &mas, size_t l, size_t r, int &k) {
    size_t L = l, R = r;
    int M = mas[(l + r) / 2];
    do {
        k++;
        while (mas[l] < M) l++;
        while (mas[r] > M) r--;
        if (l <= r) {
            int buff = mas[l];
            mas[l]   = mas[r];
            mas[r]   = buff;
            l++;
            r--;
        }
    } while (l < r);
    if (L < r) myQsort(mas, L, r, k);
    if (l < R) myQsort(mas, l, R, k);
}

void myQsort(vector<double> &mas, size_t l, size_t r, int &k) {
    size_t L = l, R = r;
    int M = mas[(l + r) / 2];
    do {
        k++;
        while (mas[l] < M) l++;
        while (mas[r] > M) r--;
        if (l <= r) {
            int buff = mas[l];
            mas[l]   = mas[r];
            mas[r]   = buff;
            l++;
            r--;
        }
    } while (l < r);
    if (L < r) myQsort(mas, L, r, k);
    if (l < R) myQsort(mas, l, R, k);
}

size_t myBinSearch(vector<int> &mas, int &r, int x) {
    size_t L = 0, R = mas.size(), q;
    do {
        q = (R + L) / 2;
        if (mas[q] > x)
            R = q;
        else
            L = q;
        r++;
    } while (L < R - 1);
    return L;
}

size_t myBinSearch(vector<double> &mas, int &r, int x) {
    size_t L = 0, R = mas.size(), q;
    do {
        q = (R + L) / 2;
        if (mas[q] > x)
            R = q;
        else
            L = q;
        r++;
    } while (L < R - 1);
    return L;
}
