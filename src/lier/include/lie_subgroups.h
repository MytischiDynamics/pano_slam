#ifndef LIE_SUBGROUPS_H
#define LIE_SUBGROUPS_H

#include "lie_groups_base.h"

namespace lier {
namespace SO2 {
    struct SO2 : public LieGroupBase<SO2> {
        SO2 inverse() const;

        SO2 rplus(const SO2& rhs) const;
    };
} //namespace SO2

namespace SE2 {
    struct SE2 : public LieGroupBase<SE2> {
        SE2 inverse() const;

        SE2 rplus(const SE2& rhs) const;
    };
} //namespace SE2
} //namespace lier

#endif //LIE_SUBGROUPS_H