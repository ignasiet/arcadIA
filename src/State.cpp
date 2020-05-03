#include <iostream>
#include <bitset>

#include <string>
#include "State.h"
#include "Action.h"
#include "Effect.h"

namespace planner {

    // Default constructor
    State::State () {}

    // Overloaded constructor
    State::State (int size) {
        this->_repr=new std::bitset<size>();
        this->_vars=new std::vector<int>(size);
        this->_values=new std::unordered_map<int, int>(size);
    }

    // Destructor
    State::~State () {}

    // Get the size of the rectangle.
    // Put the size in the pointer args
    void State::print () {
        cout << "State : " << this->_vars <<endl;
    }

    int getValue(int position){
        return state._vars[position]
    }
}