#include <iostream>
#include <vector>
#include <algorithm>
#include <cctype>
#include <sstream>
#include <regex>

using namespace std;

int main() {
    freopen("../in/03a.txt", "r", stdin);

    string line;
    int sum = 0;

    regex new_regex = regex("mul\\((\\d*),(\\d*)\\)|(do(n't)?)\\(\\)");
    bool is_enabled = true;

    for (string line; getline(cin, line);) {
        smatch m;
        cout << line << '\n';
        while (regex_search(line, m, new_regex)) {
            if (m[0] == "do()") {
                is_enabled = true;
            } else if (m[0] == "don't()") {
                is_enabled = false;
            } else {
                if (is_enabled) {
                    cout << m[1] << " " << m[2] << '\n';
                    sum += stoi(m[1]) * stoi(m[2]);
                }
            }
            line = m.suffix().str();
        }
    }

    cout << sum;

}