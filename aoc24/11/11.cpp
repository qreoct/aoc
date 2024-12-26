#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <string>

using namespace std;

vector<long long> apply_rule(vector<long long> numbers) {
    vector<long long> new_numbers;
    for (int i = 0; i < numbers.size(); i++) {
        if (numbers[i] == 0) {
            new_numbers.push_back(1);
        } else if (to_string(numbers[i]).length() % 2 == 0) {
            string left_half = to_string(numbers[i]).substr(0, to_string(numbers[i]).length() / 2);
            string right_half = to_string(numbers[i]).substr(to_string(numbers[i]).length() / 2, to_string(numbers[i]).length());
            new_numbers.push_back(stoll(left_half));
            new_numbers.push_back(stoll(right_half));
        } else {
            new_numbers.push_back(numbers[i] * 2024);
        }
    }
    return new_numbers;
}

map<pair<int, int>, long long> memo; // (index, step) -> value

long long resolve(vector<long long> numbers, int step) {
    // cout << "step " << step << endl;
    // for (long long num : numbers) {
    //     cout << num << " ";
    // }
    // cout << endl;
    if (step == 0) {
        return 1;
    } else {
        long long sum = 0;
        for (int i = 0; i < numbers.size(); i++) {
            if (memo.find({numbers[i], step}) != memo.end()) {
                sum += memo[{numbers[i], step}];
            } else {
                long long ans = resolve(apply_rule({numbers[i]}), step - 1);
                sum += ans;
                memo[{numbers[i], step}] = ans;
            }
        }
        return sum;
    }
}

int main() {
    ifstream inputFile("../in/11a.txt");
    int p1_step_limit = 26;
    int p2_step_limit = 76;

    // read entire line, split by space, into vector<int>
    string line;
    getline(inputFile, line);
    vector<long long> numbers;
    stringstream ss(line);
    for (long long i; ss >> i;) {
        numbers.push_back(i);
        if (ss.peek() == ' ') {
            ss.ignore();
        }
    }

    cout << "p1: " << resolve(numbers, p1_step_limit) << endl;
    cout << "p2: " << resolve(numbers, p2_step_limit) << endl;

    return 0;
}