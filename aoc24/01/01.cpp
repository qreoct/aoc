#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    freopen("../in/01a.txt", "r", stdin);

    int x;
    bool is_left = true;
    int result = 0;

    vector<int> left;
    vector<int> right;

    while (cin >> x) {
        if (is_left) {
            left.push_back(x);
            is_left = !is_left;
        } else {
            right.push_back(x);
            is_left = !is_left;
        }
    }

    sort(left.begin(), left.end());
    sort(right.begin(), right.end());

    for (int i = 0; i < left.size(); i++) {
        cout << left[i] << " " << right[i] << '\n';
        result += abs(left[i] - right[i]);
    }

    cout << result << '\n';
}