#include <iostream>
#include <vector>
#include <algorithm>
#include <sstream>
#include <map>
#include <set>

using namespace std;

bool search(map<char, set<pair<int, int>>> locations, pair<int, int> start, pair<int, int> direction, int width, int height) {
    /*
    Given locations, start, and direction, return if search is successful
    */
    int x = start.first;
    int y = start.second;
    int end_x = x + 3 * direction.first;
    int end_y = y + 3 * direction.second;

    // if doing the search would lead us out of bounds, don't do it
    if (end_x < 0 || end_x >= width || end_y < 0 || end_y >= height) {
        return false;
    }

    // do the search for the given direction
    for (int i = 1; i <= 3; i++) {
        x += direction.first;
        y += direction.second;
        if (i == 1) {
            if (locations['M'].find({x, y}) == locations['M'].end()) {
                return false;
            }
        } else if (i == 2) {
            if (locations['A'].find({x, y}) == locations['A'].end()) {
                return false;
            }
        } else if (i == 3) {
            if (locations['S'].find({x, y}) == locations['S'].end()) {
                return false;
            }
        }
    }
    return true;

}

int main() {
    freopen("../in/04a.txt", "r", stdin);

    int x;
    int x_coord = 0;
    int y_coord = 0;
    int width;
    int height;

    map<char, set<pair<int, int>>> locations;

    // for loop to traverse grid cell by cell
    for (string line; getline(cin, line);) {
        x_coord = 0;
        for (char c : line) {
            locations[c].insert({x_coord, y_coord});
            x_coord++;
            width = x_coord;
        }
        y_coord++;
    }
    height = y_coord;


    // print all locations
    for (auto it = locations.begin(); it != locations.end(); ++it) {
        char key = it->first;
        const set<pair<int, int>>& value = it->second;
        cout << key << ": ";
        for (const auto& p : value) {
            int x = p.first;
            int y = p.second;
            cout << "(" << x << ", " << y << ") ";
        }
        cout << '\n';
    }

    // for all 'X', do a search in all directions starting from that point
    int res = 0;
    vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}, {-1, -1}, {1, 1}, {1, -1}, {-1, 1}};
    for (const auto& p : locations['X']) {
        int x = p.first;
        int y = p.second;
        for (const auto& d : directions) {
            if (search(locations, {x, y}, d, width, height)) {
                res++;
            }
        }
    }

    cout << res << '\n';


    return 1;
}