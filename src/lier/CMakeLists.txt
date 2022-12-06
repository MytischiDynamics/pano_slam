add_library (lier
             src/lie_groups_base.cc
             src/so2/so2_base.cc
             src/so2/so2.cc)

target_include_directories (lier PUBLIC ${CMAKE_CURRENT_SOURCE_DIR}/include)