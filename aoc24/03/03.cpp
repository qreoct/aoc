#include <iostream>
#include <vector>
#include <algorithm>
#include <cctype>
#include <sstream>
#include <regex>

using namespace std;

int main() {
    freopen("../in/03a.txt", "r", stdin);

    // parse the entire file as one line as a string
    // run regex mul\((\d*),(\d*)\)
    // for each match, get int(group 1) * int(group 2) and add result to sum
    // return sum
    string line;
    int sum = 0;

    regex r = regex("mul\\((\\d*),(\\d*)\\)");
    for (string line; getline(cin, line);) {
        smatch m;
        while (regex_search(line, m, r)) {
            sum += stoi(m[1]) * stoi(m[2]);
            cout << m[1] << " " << m[2] << '\n';
            line = m.suffix().str();
        }
    }

    cout << sum;

}