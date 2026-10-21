#include <stdio.h>
#include <pybind11/pybind11.h>
#include <cmath>

int read_accel(double g) {
    double raw = std::round(g * 16384.0);
    if (raw > 32767) raw = 32767;
    if (raw < -32768) raw = -32768;
    return (int)raw;
}

PYBIND11_MODULE(accel,m){
    m.def("read_accel", &read_accel);
}