#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <sstream>

using namespace std;

int check_validity(vector<int> arr) {
    int prev = -1;
    int seen = -1;
    bool is_valid = true;
    bool overall_direction;
    int size = arr.size() - 1;

    while (seen < size) {
        seen++;
        // on first int, set previous
        if (seen == 0) {
            prev = arr[seen];
            continue;
        }

        // on second int, set direction
        if (seen == 1) {
            overall_direction = arr[seen] > prev;
        }

        // check for diff range
        int diff = abs(arr[seen] - prev);
        if (diff < 1 || diff > 3) {
            is_valid = false;
            break;
        }

        // check for consistent direction
        bool direction = arr[seen] > prev;
        if (direction != overall_direction) {
            is_valid = false;
            break;
        }

        prev = arr[seen];
    }

    return is_valid;
}


// Naive solution
// Check array as a whole, then check all possible subarrays
// O(m * n^3) time complexity since
// 1. check array as a whole is O(n)
// 2. check all possible subarrays is O(n^2)
// This happens for every line, so O(n^3) * O(m) where m is the number of lines

int main() {
    freopen("../in/02a.txt", "r", stdin);

    int x;
    string line;
    int result = 0;

    // 1. read the whole line
    // 2. don't take the first number, and do a normal check for the rest. if ok, then pass
    // 3. take the first number, and do a conditional check for the rest. allow myself to drop at most once. if drop twice, fail. if drop at most once, pass

    while (getline(cin, line)) {
        cout << "line now: " << line << '\n';
        istringstream iss(line);

        int number;
        vector<int> numbers;
        while (iss >> number) {
            numbers.push_back(number);
        }

        bool is_whole_true = check_validity(numbers);

        if (is_whole_true) {
            result++;
            cout << "is valid: " << line << '\n';
            continue;
        }

        else {
            // skip exactly one element and try on the subarrays
            vector<int> subarray;
            for (int i = 0; i < numbers.size(); i++) {
                subarray.clear();
                for (int j = 0; j < numbers.size(); j++) {
                    if (j == i) {
                        continue;
                    }
                    subarray.push_back(numbers[j]);
                }

                if (check_validity(subarray)) {
                    result++;
                    cout << "is valid: ";
                    for (int k = 0; k < subarray.size(); k++) {
                        cout << subarray[k] << " ";
                    }
                    cout << "\n";
                    break;
                }
            }

        }

    }
    cout << result << '\n';
}