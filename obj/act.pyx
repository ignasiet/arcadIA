# distutils: language = c++
from . cimport action
from libcpp cimport bool
from libcpp.vector cimport vector

cdef bint boolean_variable = True
# Create a Cython extension type which holds a C++ instance
# as an attribute and create a bunch of forwarding methods
# Python extension type.
cdef class PyAction:
    cdef Action c_act  # Hold a C++ instance which we're wrapping

    def __cinit__(self, int size, String name):
        self.c_act = Action(size, name)

    def print(self):
        return self.c_act.print()

    def checkpreconditions(self, state):
        cdef vector[int] vect = state
        cdef bool b = self.c_act.checkpreconditions(vect)
        return b
