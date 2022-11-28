cmake_minimum_required(VERSION 3.25.0)
project(pano C CXX)

set(CMAKE_CXX_STANDARD 20)

#include(dependencies.cmake)

add_subdirectory(src)
add_subdirectory(test)
