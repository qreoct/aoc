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
    int x_min = x - 1;
    int x_max = x + 1;
    int y_min = y - 1;
    int y_max = y + 1;

    // if doing the search would lead us out of bounds, don't do it
    if (x_min < 0 || x_max > width || y_min < 0 || y_max > height) {
        return false;
    }
    
    // do the search for the given direction
    pair<int, int> m1 = {x + direction.first + direction.second * -1, y + direction.second + direction.first * -1};
    pair<int, int> m2 = {x + direction.first + direction.second *  1, y + direction.second + direction.first *  1};
    pair<int, int> s1 = {x + direction.first * -1 + direction.second * -1, y + direction.second * -1 + direction.first * -1};
    pair<int, int> s2 = {x + direction.first * -1 + direction.second *  1, y + direction.second * -1 + direction.first *  1};

    // cout << "direction: " << direction.first << ", " << direction.second << '\n';
    // cout << "m1: (" << m1.first << ", " << m1.second << "), m2: (" << m2.first << ", " << m2.second << ")" << '\n';
    // cout << "s1: (" << s1.first << ", " << s1.second << "), s2: (" << s2.first << ", " << s2.second << ")" << '\n';

    if (locations['M'].find(m1) == locations['M'].end() || locations['M'].find(m2) == locations['M'].end() || 
        locations['S'].find(s1) == locations['S'].end() || locations['S'].find(s2) == locations['S'].end()) {
        return false;
    }
    // cout << "CORRECT!" << '\n';
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

    // for all 'A', do a search in all directions starting from that point
    int res = 0;
    // 'M's could either be up, down, left, or right
    vector<pair<int, int>> directions = {{0, 1}, {1, 0}, {0, -1}, {-1, 0}};
    for (const auto& p : locations['A']) {
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