#ifndef EFFECT_H
#define EFFECT_H

#include <iostream>
#include <bitset>

#include <string>

namespace planner {
    class Effect {
        public:
            Effect();
            Effect(int op);
            ~Effect();
            bool apply(int operator1, int operator2);
        private:
            int operator;
    };
}

#endif