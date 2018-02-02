#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string binary(int x, string res) {
    if(!x) {
        int s = res.size();
        while (s < 7) { res += "0"; s++; }
        return string(res.rbegin(), res.rend());
    }
    
    res += to_string(x % 2);
    return binary(x / 2, res);
}

string binary(string s) {
    string res = "";
    int size = s.size();
    
    for (int i = 0; i < size; i++) {
        res += binary((int) s.at(i), "");
    }
    
    return res;
}

string encode(string s) {
    string r = "";
    
    int i = 1;
    int size = s.size();
    
    char p = s.at(0);
    r += p == '1' ? "0 0" : "00 0";
    
    while (i < size) {
        char c = s.at(i);
        
        if (c == p) {
            r += "0";
        } else {
            r += " ";
            p = c;

            r += c == '1' ? "0 0" : "00 0";
        }
        
        i++;
    }
    
    return r;   
}

int main()
{
    string MESSAGE;
    getline(cin, MESSAGE);
    int s = MESSAGE.size();
    
    cout << encode(binary(MESSAGE)) << endl;
    
    return 0;
}
