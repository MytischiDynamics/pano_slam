add_library (lier
             src/lie_groups_base.cc
             src/lie_subgroups.cc)

target_include_directories (lier PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)