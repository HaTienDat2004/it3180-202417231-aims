# Use case AIMS-mini

Tác nhân: người sử dụng thư viện AIMS-mini hoặc chương trình minh họa CLI. `main.py` minh họa thao tác giỏ hàng; các hàm tìm kiếm được gọi qua API Python.

```mermaid
flowchart LR
    user["Người sử dụng"]
    subgraph AIMS["AIMS-mini"]
        add["Thêm DVD vào giỏ"]
        remove["Xóa DVD khỏi giỏ"]
        print["Xem chi tiết giỏ hàng"]
        total["Tính tổng tiền"]
        search["Tìm DVD theo tiêu đề"]
    end
    user --> add
    user --> remove
    user --> print
    user --> total
    user --> search
```

## Yêu cầu hành vi

- Giỏ hàng chứa tối đa 20 DVD; thêm vượt giới hạn trả về `False`.
- Xóa thành công trả về `True`; DVD không có trong giỏ trả về `False`.
- Giỏ hàng trống hiển thị `The cart is empty`.
- Tổng tiền bằng tổng `cost` của các DVD; dữ liệu mẫu có tổng 63.89 $.
- Tìm kiếm theo một phần tiêu đề; yêu cầu không phân biệt hoa thường.
- Thay đổi yêu cầu hoặc báo lỗi được theo dõi bằng Issue và Pull Request.
