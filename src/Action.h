#ifndef ACTION_H
#define ACTION_H

#include <iostream>
#include <bitset>

#include <string>
#include "State.h"
#include "Action.h"
#include "Precondition.h"

namespace planner {
    class Action {
        public:
            Action();
            Action(int size, String name);
            ~Action();
            void print();
            bool checkpreconditions(std::vector<int> state);
            State apply(State old);

        private:
            string _name;
            std::vector<Precondition> _operators_preconditions;
            std::vector<Effect> _operators_effects;
            std::vector<int> _precond;
            std::vector<int> _precond_values;
            std::vector<int> _effects;
            std::vector<int> _effects_values;
    };
}

#endif