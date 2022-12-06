#ifndef SO2_BASE_H
#define SO2_BASE_H

#include "lie_groups_base.h"
#include "traits.h"

namespace lier {
//namespace so2 {

template <typename Derived_>
struct SO2Base : public LieGroupBase<Derived_> {
    private:
    using Base = LieGroupBase<Derived_>;
    using Type = SO2Base<Derived_>;
    using LieGroup = typename Base::LieGroup;

    public:
    using Base::coeffs;
    using Base::inverse;
    //using Base::rplus;

    protected:
    using Base::subgroup;

    public:
    LieGroup inverse() const;
    

};

//} // namespace so2
} // namespace lier

#endif //SO2_BASE_H