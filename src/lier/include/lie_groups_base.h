#ifndef LIE_GROUPS_BASE_H
#define LIE_GROUPS_BASE_H

namespace lier {
    template <typename LieSubgroup>
    struct LieGroupBase {
        LieSubgroup inverse() const /*{ return subgroup().inverse(); }*/;
        LieSubgroup rplus(const LieSubgroup& rhs) const /*{ return subgroup().rplus(rhs); }*/;

        LieSubgroup& subgroup() & /*{ return *static_cast<LieSubgroup*>(this) }*/;
        const LieSubgroup& subgroup() const & /*{ return *static_cast<const LieSubgroup*>(this); }*/;
    };
}


#endif //LIE_GROUPS_BASE_H