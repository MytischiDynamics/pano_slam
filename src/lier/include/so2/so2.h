#ifndef SO2_H
#define SO2_H

#include "Eigen/Dense"
#include "so2/so2_base.h"

namespace lier {
namespace internal {

template <typename Scalar_> struct SO2;

template <typename Scalar_>
struct traits <SO2<Scalar_>> {
    using Scalar = Scalar_;

    static constexpr int RepSize = 2;

    using LieGroup = SO2<Scalar_>;

    using Base = SO2Base<SO2<Scalar_>>;
    using Type = SO2<Scalar_>;

    using DataType = Eigen::Matrix<Scalar, RepSize, 1>;
};

} // namespace internal

//namespace so2 {

template <typename Scalar_>
struct SO2 : SO2Base<SO2<Scalar_>> {
    using Base = SO2Base<SO2<Scalar_>>;
    using Type = SO2<Scalar_>;

    using DataType = typename Base::DataType;

    DataType& coeffs();
    const DataType& coeffs() const;

    protected:
    DataType data_;
};

//} // namespace so2
} // namespace lier

#endif // SO2_H