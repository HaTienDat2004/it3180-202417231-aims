# Changelog

Theo Keep a Changelog và Semantic Versioning.

## [Unreleased]

## [1.1.0] - 2026-11-02

### Added
- Sắp xếp giỏ hàng theo tiêu đề hoặc giá.
- Tìm DVD theo thể loại.

### Fixed
- Bao gồm bản sửa tìm kiếm tiêu đề từ dòng 1.0.1.

## [1.0.1] - 2026-11-02

### Fixed
- Tìm theo tiêu đề không phân biệt hoa thường (#18).

## [1.0.0] - 2026-11-02

### Added
- `Cart.print_cart()` và thông báo giỏ hàng trống.
- `search_by_title()` và tài liệu use case.
- `Cart.total_cost_with_discount()` và kiểm tra phần trăm hợp lệ.

### Fixed
- Từ chối DVD thứ 21 khi giới hạn giỏ hàng là 20 (#7).
- Tính số tiền sau giảm giá thay vì chỉ tính số tiền được giảm.
