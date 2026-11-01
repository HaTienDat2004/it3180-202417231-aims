# Changelog

Theo Keep a Changelog và Semantic Versioning.

## [Unreleased]

## [1.0.0] - 2026-11-02

### Added
- `Cart.print_cart()` và thông báo giỏ hàng trống.
- `search_by_title()` và tài liệu use case.
- `Cart.total_cost_with_discount()` và kiểm tra phần trăm hợp lệ.

### Fixed
- Từ chối DVD thứ 21 khi giới hạn giỏ hàng là 20 (#7).
- Tính số tiền sau giảm giá thay vì chỉ tính số tiền được giảm.
