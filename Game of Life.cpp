//
//  Lab01.cpp
//  Labs
//
//  Created by Brittany Ng on 9/6/18.
//  Copyright © 2018 Brittany Ng. All rights reserved.
//

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

int main() {
    ifstream life("life.txt");
    if (!life) {
        cerr << "failed to open up life";
        exit(1);
    }
    string line;
    vector<string> pastGen;
    
    while (getline(life, line)) {
        pastGen.push_back(line);
    }
    life.close();


    // creates vector of the provided life.txt
    cout << "Initial World" << endl;
    cout << "========================================" << endl;

    for (size_t row = 0; row < pastGen.size(); ++row) {
        for (size_t col = 0; col < pastGen[row].size(); ++col) {
            cout << pastGen[row][col] << ' ';
        }
        cout << endl;
    }
    cout << "========================================" << endl;

    
    // creates a clean slate of the vector
    for (int gen = 1; gen < 11; ++gen) {
        vector<string> newGen;
        for (size_t row = 0; row < pastGen.size(); ++row) {
            string new_line;
            for (size_t col = 0; col < pastGen[row].size(); ++col) {
                int neighbours = 0;
                
                // counts the amount of neighbors around each cell
                for (int i = -1; i < 2; ++i) {
                    for (int k = -1; k < 2; ++k) {
                        if (pastGen[row+i][col+k] == '*')
                            ++ neighbours;
                    }
                }
                // takes into account whether the cell that is being checked is alive or not,
                // if it's alive, it'll subtract 1 from neighbor count so that it doesn't count itself as a neighbour
                if (pastGen[row][col] == '*') {
                    --neighbours;
                }
                
                // adds alive/dead cells onto the clean slate of the vector based on neighbour count
                if (pastGen[row][col] == '*') {
                        if (neighbours == 2 || neighbours == 3) {
                            new_line += '*';
                        } else if (neighbours < 2 || neighbours > 3) {
                            new_line += '-';
                        }
                    }
                    
                if (pastGen[row][col] == '-') {
                        if (neighbours == 3) {
                            new_line += '*';
                        } else {
                            new_line += '-';
                        }
                    }
//                newGen.push_back(new_line);
            }
            newGen.push_back(new_line);
            
        }
//    cout << "newGen" << endl;
        
        // creates the new generation
        cout << "Generation #" << gen << endl;
        for (size_t row = 0; row < newGen.size(); ++row) {
            for (size_t col = 0; col < newGen[row].size(); ++col) {
                cout << newGen[row][col] << ' ';
            }
            cout << endl;
        }
        cout << "========================================" << endl;

        // updates the old generation each time 
        pastGen = newGen;

    }

}


            
                
        
        
    
        


