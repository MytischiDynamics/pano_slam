#ifndef LIE_GROUPS_BASE_H
#define LIE_GROUPS_BASE_H

#include "traits.h"

namespace lier {
    template <typename LieSubgroup>
    struct LieGroupBase {
        public:
        using Scalar = typename internal::traits<LieSubgroup>::Scalar;
        using LieGroup = typename internal::traits<LieSubgroup>::LieGroup;
        using DataType = typename internal::traits<LieSubgroup>::DataType;

        LieGroup inverse() const;

        DataType& coeffs();
        const DataType& coeffs() const;
        //LieSubgroup rplus(const LieSubgroup& rhs) const;

        protected:
        LieSubgroup& subgroup() &;
        const LieSubgroup& subgroup() const &;
    };
}


#endif //LIE_GROUPS_BASE_H