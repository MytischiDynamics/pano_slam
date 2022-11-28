#include "lie_groups_base.h"

namespace lier {

    template <typename LieSubgroup>
    LieSubgroup& LieGroupBase<LieSubgroup>::subgroup() & {
        return *static_cast<LieSubgroup*>(this);
    }

    template <typename LieSubgroup>
    const LieSubgroup& LieGroupBase<LieSubgroup>::subgroup() const & {
        return *static_cast<const LieSubgroup*>(this);
    }

    template <typename LieSubgroup>
    LieSubgroup LieGroupBase<LieSubgroup>::inverse() const {
        return subgroup().inverse();
    }

    template <typename LieSubgroup>
    LieSubgroup LieGroupBase<LieSubgroup>::rplus(const LieSubgroup& rhs) const {
        return subgroup().rplus(rhs);
    }
}

