// тут функции вызываются

#include <iostream>
#include "head.h"
#include <vector>
#include <chrono>
 
using namespace std;
using namespace chrono;

int main() {
    vector<int> iv;
    vector<double> dv;
    size_t n_ar;
    bool t_ar;
    cout << "Какой массив создать?\n"
            "0 - int\n"
            "1 - double" << endl;
    cout << " => ";
    cin >> t_ar;
    cout << "Введите длину массива: ";
    cin >> n_ar;
    cout << "Введите интервал случайных чисел [x, y]:" << endl;
    if (!t_ar) {
        int x, y;
        cout << "x => "; cin >> x;
        cout << "y => "; cin >> y;
        ini_ar(n_ar, x, y, iv);
        print_ar(t_ar, iv);
    } else {
        double x, y;
        cout << "x => "; cin >> x;
        cout << "y => "; cin >> y;
        ini_ar(n_ar, x, y, dv);
        print_ar(t_ar, dv);
    }
    int cnt {};
    if (!t_ar) {
        auto start = system_clock::now();
        mySortBubble(iv, cnt);
        auto end = system_clock::now();
        cout << "Количество итераций: "
             << cnt << endl;
        print_ar(t_ar, iv);
        auto elapsed = end - start;
        cout << "Скорость выполнения: "
             << duration_cast<microseconds>(elapsed).count()
             << " ���"
             << endl;
    } else {
        mySortBubble(dv, cnt);
        cout << "Количество итераций: "
             << cnt << endl;
        print_ar(t_ar, dv);
    }
    return 0;
}
