#ifndef PRECONDITION_H
#define PRECONDITION_H

#include <iostream>
#include <bitset>

#include <string>
#include "State.h"
#include "Action.h"

namespace planner {
    class Precondition {
        public:
            Precondition();
            Precondition(int op);
            ~Precondition();
            bool check(int operator1, int operator2);
        private:
            int operator;
    };
}

#endif