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
