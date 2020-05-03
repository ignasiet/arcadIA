#include <iostream>
#include <bitset>
#include <vector>
#include "State.h"
#include "Action.h"
#include "Precondition.h"

namespace planner {

    // Default constructor
    Action::Action () {}

    // Overloaded constructor
    Action::Action (int size, String Name) {
        this->_name=Name;
        this->_vars=new std::vector<int>(size);
    }

    // Destructor
    State::~State () {}

    // Get the size of the rectangle.
    // Put the size in the pointer args
    void State::print () {
        cout << "Action : " << this->_name <<endl;
    }

    bool checkpreconditions(std::vector<int> state){
        /* While iterating the values, we must also iterate the operators
        */
        int i = 0;
        for(std::vector<int>::iterator it = this->_precond.begin(); it != _precond.end(); ++it) {
            /* std::cout << *it; ... */
            Precondition pre = this->_operators_preconditions[i];
            if(!pre.check(state.getValue(i), this->_precond_values[*it], state)){
                return False;
            }
            i++;
        }
        return True;
    }

    State apply(State old){
        /* While iterating the values, we must also iterate the operators
        */
        State state = new State(this->_effects_values.size());
        int i = 0;
        for(std::vector<int>::iterator it = this->_effects.begin(); it != _effects.end(); ++it) {
            Effect eff = this->_operators_effects[i];
            state.setValue(i, eff.apply(state.getValue(i), this->_effect_values[*it]));
            i++;
        }
        return state;
    }
}