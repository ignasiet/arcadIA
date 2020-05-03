#ifndef STATE_H
#define STATE_H

#include <vector>
#include <unordered_map>

namespace planner {
    class State {
        public:
            State();
            State(int size);
            ~State();
            void print();
            State expand(Action a);
            int getValue(int position);
        
        private:
            std::bitset<size>() _repr;
            std::vector<int> _vars;
            std::unordered_map<int, int> _values;
    };
}

#endif