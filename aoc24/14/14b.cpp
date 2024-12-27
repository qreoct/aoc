#include <iostream>
#include <fstream>
#include <sstream>
#include <vector>
#include <map>
#include <string>

using namespace std;

class robot_details {
    public:
        int id;
        int start_x;
        int start_y;
        int velocity_x;
        int velocity_y;
};

int main() {
    ifstream inputFile("../in/14a.txt");

    if (!inputFile.is_open()) {
        cerr << "Error opening file" << endl;
        return 1;
    }

    map<int, robot_details> robots; 
    string line;
    int i = 0;

    int map_width = 101;
    int map_height = 103;

    map<string, int> hashes;

    // Read all lines into a vector
    while (getline(inputFile, line)) {

        int p_x, p_y, v_x, v_y;
        char ignore;

        istringstream lineStream(line);
        lineStream >> ignore >> ignore >> p_x >> ignore >> p_y >> ignore >> ignore >> v_x >> ignore >> v_y;

        robot_details rob = {i, p_x, p_y, v_x, v_y};
        robots[i] = rob;
        i++;
    }

    // print robots
    int q1 = 0, q2 = 0, q3 = 0, q4 = 0;

    map<pair<int, int>, int> final; 
    for (int x = 0; x < map_width; x++) {
        for (int y = 0; y < map_height; y++) {
            final[{x, y}] = 0;
        }
    }

    int seconds = 0;
    while (seconds < 10403) { // from cycle detection, we know that it takes 101*103 seconds to reach the same position
        int q1 = 0, q2 = 0, q3 = 0, q4 = 0;

        map<pair<int, int>, int> final; 
        for (int x = 0; x < map_width; x++) {
            for (int y = 0; y < map_height; y++) {
                final[{x, y}] = 0;
            }
        }
        for (const auto& robot : robots) {
            robot_details r = robot.second;
            int end_x = (r.start_x + r.velocity_x * seconds) % map_width;
            int end_y = (r.start_y + r.velocity_y * seconds) % map_height;

            if (end_x < 0) {
                end_x = map_width + end_x;
            }
            if (end_y < 0) {
                end_y = map_height + end_y;
            }

            final[{end_x, end_y}]++;
            // determine quadrant
            if (end_x < map_width / 2 && end_y < map_height / 2) {
                q1++;
            } else if (end_x > map_width / 2 && end_y < map_height / 2) {
                q2++;
            } else if (end_x < map_width / 2 && end_y > map_height / 2) {
                q3++;
            } else if (end_x > map_width / 2 && end_y > map_height / 2) {
                q4++;
            } else {
                continue;
            }
        }

        // go over all cells in final. count the number of cells that have neighbours
        // assume that the tree will occur with significant clustering
        int count = 0;
        for (int y = 0; y < map_height; y++) {
            for (int x = 0; x < map_width; x++) {
                if (final[{x, y}] > 0) {
                    if (final[{x, y + 1}] > 0 || final[{x, y - 1}] > 0 || final[{x + 1, y}] > 0 || final[{x - 1, y}] > 0) {
                        count++;
                    }
                }
            }
        }
        if (count > 300) {
            cout << "FOUND AT " << seconds << endl;
            cout << "q1: " << q1 << endl;
            cout << "q2: " << q2 << endl;
            cout << "q3: " << q3 << endl;
            cout << "q4: " << q4 << endl;
            break;
        }

        seconds++;
    }

    return 1;
}