#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <map>
#include <set>

using namespace std;

set<pair<int, int>> dfs(vector<vector<char>>& grid, int x, int y, int width, int height, set<pair<int, int>> visited) {
    /*
    Given grid, x, y, width, and height, return the number of valid nodes
    */
    vector<pair<int, int>> directions = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
    set<pair<int, int>> res = {};

    // if the node is invalid, return 0
    if (x < 0 || x >= width || y < 0 || y >= height ) {
        return {};
    }

    // if the node is valid, increment the result
    if (grid[y][x] == '9') {
        res.insert({y, x});
    }

    // mark the node as visited
    visited.insert({y, x});

    // for all directions, do a search
    for (const auto& direction : directions) {
        int new_x = x + direction.first;
        int new_y = y + direction.second;
        if (new_x < 0 || new_x >= width || new_y < 0 || new_y >= height) {
            continue;
        }
        if (visited.find({new_y, new_x}) == visited.end() && grid[new_y][new_x] - grid[y][x] == 1) {
            set<pair<int, int>> dfs_result = dfs(grid, new_x, new_y, width, height, visited);
            res.insert(dfs_result.begin(), dfs_result.end());
        }
    }

    return res;
}

int main() {
    freopen("../in/10.txt", "r", stdin);

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

    // for all '0', do a search in all directions starting from that point
    int res = 0;
    for (const auto& p : locations['0']) {
        set<pair<int, int>> score = dfs(grid, p.first, p.second, width, height, {});
        cout << "at " << p.first << ", " << p.second << " with score " << score.size() << '\n';
        res += score.size();
    }

    cout << res << '\n';
}