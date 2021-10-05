/*
 * You are given row x col grid representing a map where grid[i][j] = 1 represents land and grid[i][j] = 0 represents water.
 * Grid cells are connected horizontally/vertically (not diagonally).
 * The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells).
 * The island doesn't have "lakes", meaning the water inside isn't connected to the water around the island.
 * One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.
*/
#include <iostream>
#include <vector>
using namespace std;

class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int n = grid.size();
        int m = grid[0].size();
        int ans = 0;
        for (int j = 0; j < m; j++) {
            ans += grid[0][j] ^ 0;       //first row with top
            ans += grid[n - 1][j] ^ 0;   //last row with bottom
        }
        for (int i = 0; i < n; i++) {
            ans += grid[i][0] ^ 0;       //first col with left
            ans += grid[i][m - 1] ^ 0;   //last col with right
        }
        for (int i = 0; i < n - 1; i++) {//grid
            for (int j = 0 ; j < m - 1; j++) {
                ans += (grid[i][j] ^ grid[i][j + 1]) + (grid[i][j] ^ grid[i + 1][j]);
            }
        }
        for (int j = 0; j < m - 1; j++) {//last row
            ans += grid[n - 1][j] ^ grid[n - 1][j + 1];
        }
        for (int i = 0; i < n - 1; i++) {//last col
            ans += grid[i][m - 1] ^ grid[i + 1][m - 1];
        }
        return ans;
    }
};

int main() {
    Solution solution;
    vector<vector<int>> grid = {{0,1,0,0},{1,1,1,0},{0,1,0,0},{1,1,0,0}};
    //vector<vector<int>> grid = {{1}};
    //vector<vector<int>> grid = {{1,0}};
    cout << solution.islandPerimeter(grid);
}

