#include <iostream>
#include <iomanip>
#include <cmath>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <string>

using namespace std;

struct machine {
    int id;
    int a_x;
    int a_y;
    int b_x;
    int b_y;
    double prize_x;
    double prize_y;
};

double determinant(double a, double b, double c, double d) {
    return (a * d - b * c);
}

pair<double, double> solveLinearEquations(double a1, double b1, double c1, double a2, double b2, double c2) {
    double det = determinant(a1, b1, a2, b2);

    if (det != 0) { // Unique solution (det != 0)
        double x = determinant(c1, b1, c2, b2) / det;
        double y = determinant(a1, c1, a2, c2) / det;
        cout << fixed << setprecision(2);
        cout << "Unique solution: a = " << x << ", b = " << y << endl;
        return {x, y};
    } else {
        // Check ranks for no solution or infinitely many solutions
        double rank1 = determinant(a1, b1, a2, b2);
        double rank2 = determinant(a1, c1, a2, c2);

        if (fabs(rank1) < 1e-9 && fabs(rank2) > 1e-9) {
            cout << "No solution exists." << endl;
            return {-1, -1};
        } else {
            cout << fixed << setprecision(2);
            if (fabs(a1) > 1e-9) { // Assume a = 0, solve for b
                double b = c1 / b1;
                cout << "Infinitely many solutions. One valid solution: a = 0.00, b = " << b << endl;
                return {0, b};
            } else { // Assume b = 0, solve for a
                double a = c2 / a2;
                cout << "Infinitely many solutions. One valid solution: a = " << a << ", b = 0.00" << endl;
                return {a, 0};
            }
        }
    }
}

int main() {
    ifstream inputFile("../in/13a.txt");

    if (!inputFile.is_open()) {
        cerr << "Error opening file" << endl;
        return 1;
    }

    map<int, machine> machines;
    string line;
    int id = 0;

    while (getline(inputFile, line)) {
        if (line.empty()) continue;

        machine m;
        m.id = id;

        // Parse Button A
        istringstream issA(line);
        string temp;
        char ignore;
        issA >> temp >> temp >> ignore >> m.a_x >> temp >> ignore >> m.a_y;

        // Parse Button B
        if (getline(inputFile, line)) {
            istringstream issB(line);
            issB >> temp >> temp >> ignore >> m.b_x >> temp >> ignore >> m.b_y;
        }

        // Parse Prize
        if (getline(inputFile, line)) {
            istringstream issP(line);
            issP.ignore(9);
            issP >> m.prize_x;
            issP.ignore(4);
            issP >> m.prize_y;
            m.prize_x += 10000000000000; // PART 2
            m.prize_y += 10000000000000; // PART 2
        }

        machines[id] = m;
        id++;
    }

    double totalRes = 0;

    // Print the machines to verify
    pair<double, double> solution;
    for (const auto& pair : machines) {
        const machine& m = pair.second;
        solution = solveLinearEquations(m.a_x, m.b_x, m.prize_x, m.a_y, m.b_y, m.prize_y);
        if (solution.first == -1 && solution.second == -1) {
            cout << "no solution" << endl;
        } else if (floor(solution.first) != solution.first || floor(solution.second) != solution.second) {
            cout << "solution is not a whole number" << endl;
        } else {
            totalRes += 3 * solution.first + solution.second;
        }
    }

    cout << "part1: " << totalRes << endl;

    return 0;
}
