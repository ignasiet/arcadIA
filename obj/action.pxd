cdef extern from "../src/Action.cpp":
    pass

# Declare the class with cdef
cdef extern from "../src/Action.h" namespace "planner":
    cdef cppclass Action:
        Action() except +
        Action(int, string) except +
        void print()
        bool checkpreconditions(vector<int> state);
        State apply(State);