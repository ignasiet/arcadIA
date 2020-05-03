#include <iostream>
#include <bitset>

#include <string>
#include "Precondition.h"

namespace planner {
    // Default constructor
    Precondition::Precondition () {}

    // Overloaded constructor
    Precondition::Precondition (int op) {
        this->operator=op;
    }

    /**
        * Comparison operators:
        >= 0
        > 1
        == 2
        <= 3
        < 4
    */
    bool check(int op1, int op2){
        switch(this->operator){
            case 0:
                return op1 >= op2;
            case 1:
                return op1 > op2;
            case 2:
                return op1 == op2;
            case 3:
                return op1 <= op2;
            case 4:
                return op1 < op2;
            default:
                cout << "Invalid Operation" << endl;
                return False;
        }        
    }

}