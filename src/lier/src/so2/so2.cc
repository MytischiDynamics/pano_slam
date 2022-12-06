#include "so2/so2.h"

namespace lier {
//namespace so2 {

template <typename Scalar_>
const typename SO2<Scalar_>::DataType&
SO2<Scalar_>::coeffs() const {
    return data_;
}

template <typename Scalar_>
typename SO2<Scalar_>::DataType&
SO2<Scalar_>::coeffs() {
    return data_;
}

//} // namespace so2
} // namespace lier