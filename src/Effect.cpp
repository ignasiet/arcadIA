#include <iostream>
#include <bitset>

#include <string>
#include "Effect.h"

namespace planner {
    // Default constructor
    Effect::Effect () {}

    // Overloaded constructor
    Effect::Effect (int op) {
        this->operator=op;
    }

    /**
        * Effects operators:
        + 0
        - 1
        = 2
    */
    bool apply(int op1, int op2){
        switch(this->operator){
            case 0:
                return op1 + op2;
            case 1:
                return op1 - op2;
            case 2:
                return op2;
            default:
                cout << "Invalid Operation" << endl;
                return op1;
        }        
    }

}