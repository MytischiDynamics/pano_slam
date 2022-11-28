//#include "lie_groups_base.h"
#include "lie_subgroups.h"

#include <iostream>

namespace lier {
namespace SO2 {

    SO2 SO2::inverse() const {
        std::cout << "From SO2.inverse()" << std::endl;
        return SO2{};
    }

    SO2 SO2::rplus(const SO2& rhs) const {
        std::cout << "From SO2.rplus()" << std::endl;
        return rhs;
    }
} // namespace SO2

namespace SE2 {

    SE2 SE2::inverse() const {
        std::cout << "From SE2.inverse()" << std::endl;
        return SE2{};
    }


    SE2 SE2::rplus(const SE2& rhs) const {
        std::cout << "From SE2.rplus()" << std::endl;
        return rhs;
    }
} // namespace SE2
} // namespace lier