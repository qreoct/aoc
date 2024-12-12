#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <fstream>
#include <map>


using namespace std;

int main() {
    ifstream inputFile("../in/07a.txt");

    string line;
    map<long long, vector<long long>> input;
    long long part2 = 0;

    while (getline(inputFile, line)) {
        istringstream ss(line);
        string token;

        cout << line << '\n';

        ss >> token;
        long long target = stoll(token.substr(0, token.size() - 1));

        vector<long long> results = vector<long long>();
        vector<long long> layer = vector<long long>();

        while (ss >> token) {
            long long rhToken = stoll(token);
            results.clear();
            if (layer.size() == 0) {
                layer.push_back(rhToken);
                continue;
            }

            for (long long &it3 : layer) {
                if (it3 * rhToken <= target) {
                    results.push_back(it3 * rhToken);
                } 
                if (it3 + rhToken <= target) {
                    results.push_back(it3 + rhToken);
                }
                if (stoll(to_string(it3) + to_string(rhToken)) <= target) {
                    results.push_back(stoll(to_string(it3) + to_string(rhToken))); // part 2
                }
            }
            layer = results; 
        }

        for (long long &elem : results) {
            if (elem == target) {
                cout << "   YES" << endl;
                part2 += target;
                break;
            }
        }
    }

    cout << "part2: " << part2 << '\n';

    return 1;
}