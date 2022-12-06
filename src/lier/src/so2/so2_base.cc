#include "so2/so2_base.h"

namespace lier {
//namespace so2 {

template <typename Derived_>
typename SO2Base<Derived_>::LieGroup
SO2Base<Derived_>::inverse() const {
    return LieGroup {};
}

//} //namespace so2
} // namespace lier