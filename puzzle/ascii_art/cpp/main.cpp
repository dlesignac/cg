#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

int main()
{
    int L;
    int H;
    
    cin >> L; cin.ignore();
    cin >> H; cin.ignore();
    
    string T;
    getline(cin, T);
    int S = T.size();
    
    string answer = "";
    
    for (int i = 0; i < H; i++) {
        string ROW;
        getline(cin, ROW);
        
        for (int j = 0; j < S; j++) {
            int ascii = (int) T.at(j);
            
            if (ascii >= 65 && ascii <= 90) { ascii -= 65; }
            else if (ascii >= 97 && ascii <= 122)   { ascii -= 97; }
            else { ascii = 26; }
            
            answer += ROW.substr(ascii * L, L);
        }
        
        answer += "\n";
    }

    cout << answer;
}
