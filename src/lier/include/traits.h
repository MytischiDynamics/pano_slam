#ifndef LIER_TRAITS_H
#define LIER_TRAITS_H

namespace lier {
namespace internal {
    template <typename T> struct traits;

    // define that traits<const T> == traits<T>
    template<typename T> struct traits<const T> : traits<T> {};
    
} // namespace internal
} // namespace lier



#endif // LIER_TRAITS_H