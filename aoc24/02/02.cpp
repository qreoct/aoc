#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

int main() {
    freopen("../in/02a.txt", "r", stdin);

    int x;
    string line;
    int result = 0;

    while (getline(cin, line)) {
        cout << line << '\n';
        istringstream iss(line);

        int c;
        int prev = -1;
        int seen = -1;
        bool is_valid = true;
        bool overall_direction;

        while (iss >> c) {
            seen++;
            // on first int, set previous
            if (seen == 0) {
                prev = c;
                continue;
            }

            // on second int, set direction
            if (seen == 1) {
                overall_direction = c > prev;
            }

            // check for diff range
            int diff = abs(c - prev);
            if (diff < 1 || diff > 3) {
                is_valid = false;
                break;
            }

            // check for consistent direction
            bool direction = c > prev;
            if (direction != overall_direction) {
                is_valid = false;
                break;
            }

            prev = c;
        }

        if (is_valid) {
            result++;
        }

    }
    cout << result << '\n';
}