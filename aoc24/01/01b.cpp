#include <iostream>
#include <vector>
#include <algorithm>
#include <map>

using namespace std;

int main() {
    freopen("../in/01a.txt", "r", stdin);

    int x;
    bool is_left = true;
    int result = 0;

    map<int, int> left;
    map<int, int> frequency;

    while (cin >> x) {
        if (is_left) {
            left[x]++;
            is_left = !is_left;
        } else {
            frequency[x]++;
            is_left = !is_left;
        }
    }

    for (auto &i : left) {
        result += abs(i.first * i.second * frequency[i.first]);
    }

    cout << result << '\n';
}