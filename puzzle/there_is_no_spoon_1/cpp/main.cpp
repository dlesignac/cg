#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int width; // the number of cells on the X axis
    cin >> width; cin.ignore();
    int height; // the number of cells on the Y axis
    cin >> height; cin.ignore();
    
    string map = "";
    
    for (int i = 0; i < height; i++) {
        string line; // width characters, each either 0 or .
        getline(cin, line);
        map += line;
    }
    
    int s = width * height;
    
    for (int i = 0; i < s; i++) {
        if(map.at(i) == '0') {
            int x = i % width;
            int y = i / width;
            string node = to_string(x) + " " + to_string(y) + " ";

            int _x = x + 1;
            int _y = y + 1;
            int found = 0;
            
            while (!found && _x < width) {
                if (map.at(y * width +_x) == '0') {
                    node += to_string(_x) + " " + to_string(y);
                    found = 1;
                }
                
                _x++;
            }
            
            if (found)  { found = 0; }
            else { node += to_string(-1) + " " + to_string(-1); }
                
            node += " ";
            
            while (!found && _y < height) {
                if (map.at(_y * width +x) == '0') {
                    node += to_string(x) + " " + to_string(_y);
                    found = 1;
                }
                
                _y++;
            }
            
            if (!found)  { node += to_string(-1) + " " + to_string(-1); }
            
            cout << node << endl;
        }
    }
}
