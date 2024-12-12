
#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <fstream>
#include <sstream>

using namespace std;

vector<pair<int, int>> calc_antinodes(pair<int, int> p1, pair<int, int> p2, int height, int width) {
    int x_distance = p1.first - p2.first;
    int y_distance = p1.second - p2.second;

    // generate all pairs that lie along the same line as p1 and p2
    vector<pair<int, int>> antinodes;
    for (int k = 1; k < max(height, width); k++) {
        pair<int, int> a1 = {p1.first + k * x_distance, p1.second + k * y_distance};
        pair<int, int> a2 = {p2.first - k * x_distance, p2.second - k * y_distance};
        antinodes.push_back(a1);
        antinodes.push_back(a2);
    }
    return antinodes;
}

vector<pair<int, int>> accept_valid_nodes(vector<pair<int, int>> antinodes, int height, int width) {
    vector<pair<int, int>> valid_nodes;
    for (auto &node : antinodes) {
        if (node.first >= 0 && node.first < width && node.second >= 0 && node.second < height) {
            valid_nodes.push_back(node);
        }
    }
    return valid_nodes;   
}

int main() {
    freopen("../in/08a.txt", "r", stdin);

    int x;
    int x_coord = 0;
    int y_coord = 0;
    int width = 0;
    int height = 0;

    int part1 = 0;
    int part2 = 0;

    map<char, vector<pair<int, int>>> locations;
    vector<vector<char>> grid;
    vector<string> lines;
    string line;
    set<pair<int, int>> all_valid_nodes;

    // Read all lines into a vector
    while (getline(cin, line)) {
        lines.push_back(line);
        width = max(width, static_cast<int>(line.size()));
        height++;
    }

    // Resize the grid to the correct dimensions
    grid.resize(height, vector<char>(width, ' '));

    // Fill in the grid using the stored lines
    for (int y = 0; y < height; y++) {
        for (int x = 0; x < lines[y].size(); x++) {
            char c = lines[y][x];
            grid[y][x] = c;
            if (c != '.') {
                locations[c].push_back({x, y});
            }
        }
    }

    // print antennae
    for (auto &elem : locations) {
        cout << elem.first << ": ";
        for (auto &pair : elem.second) {
            cout << "(" << pair.first << ", " << pair.second << ") ";
        }
        cout << '\n';
    }

    for (auto &elem : locations) {
        vector<pair<int, int>> coords = elem.second;
        for (int i = 0; i < coords.size() - 1; i++) {
            for (int j = i + 1; j < coords.size(); j++) {
                pair<int, int> p1 = coords[i];
                pair<int, int> p2 = coords[j];
                vector<pair<int, int>> antinodes = calc_antinodes(p1, p2, height, width);
                vector<pair<int, int>> valid_nodes = accept_valid_nodes(antinodes, height, width);

                all_valid_nodes.insert(valid_nodes.begin(), valid_nodes.end());
                for (auto &valid_node : valid_nodes) {
                    grid[valid_node.second][valid_node.first] = '#';
                }
            }
        }
    }
    // print grid
    for (int i = 0; i < height; i++) {
        for (int j = 0; j < width; j++) {
            cout << grid[i][j] << ' ';
        }
        cout << '\n';
    }
    part1 = all_valid_nodes.size();
    cout << "part1: " << part1 << '\n';

    for (auto &elem : locations) {
        vector<pair<int, int>> antennae = elem.second;
        if (antennae.size() > 1) {
            for (auto &antenna : antennae) {
                all_valid_nodes.insert(antenna);
            }
        }
    }
    part2 = all_valid_nodes.size();
    cout << "part2: " << part2;

    return 1;

}