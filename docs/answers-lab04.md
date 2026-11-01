# Trả lời thảo luận Lab 04

## Vì sao chuẩn bị phát hành trên `master` trước khi tạo release?

Phiên bản, banner chương trình và CHANGELOG là thay đổi cần kiểm thử, review và tích hợp qua PR như mã nguồn. Chuẩn bị chúng trên nhánh topic rồi merge vào `master` giúp nhánh phát triển chính chứa đầy đủ trạng thái đã được duyệt. Từ đó tạo `release/lab04` để đóng băng đúng snapshot. Nếu chỉ sửa trên release, `master` sẽ thiếu thông tin phát hành và hai dòng phiên bản có thể lệch nhau ngay từ đầu.

## Vì sao `release/*` không merge ngược vào `master`?

Trong Release Flow của học phần, release là dòng bảo trì của bài đã nộp. Các commit riêng như tăng patch từ `1.0.0` lên `1.0.1` không được làm lùi phiên bản `1.1.0` đang phát triển trên `master`. Khi release cần hotfix, chọn riêng commit sửa lỗi bằng `cherry-pick -x` rồi đưa qua PR vào các dòng bị ảnh hưởng. Nhờ vậy, chỉ lan truyền thay đổi phù hợp và có dấu vết nguồn gốc.

Đây là chính sách của quy trình đang áp dụng, không phải giới hạn kỹ thuật của Git. Git vẫn có thể merge các nhánh, nhưng làm vậy có thể mang theo thay đổi không phù hợp với mục tiêu bài thực hành.

## So sánh với GitFlow

GitFlow thường có nhánh phát triển dài hạn `develop` và nhánh phát hành chính `main`/`master`; các nhánh release hoặc hotfix được đưa trở lại các dòng liên quan theo quy trình GitFlow. Bài thực hành dùng `master` làm dòng tích hợp và giữ các nhánh `release/labXX` để nộp bài, bảo trì nhiều baseline. Không có nhánh `develop`, và bản sửa được lan truyền có chọn lọc thay vì merge cả release trở lại `master`.

## Vì sao phát hành `1.0.0` thay vì `0.4.0`?

Theo SemVer, `0.y.z` biểu thị giai đoạn phát triển ban đầu, giao diện và hành vi còn có thể thay đổi. `1.0.0` thể hiện quyết định xác lập giao diện và hành vi công khai đầu tiên để bắt đầu quản lý tương thích. Trong đề, Lab 04 được chọn làm mốc ổn định đó. Không có quy tắc rằng hoàn thành bốn lab thì bắt buộc phải tăng từ `0.3.0` lên `0.4.0`; phiên bản phải phản ánh ý nghĩa phát hành.

## Tag khác nhánh release thế nào?

Annotated tag xác định một snapshot và kèm thông tin phát hành; tag đã chia sẻ không được di chuyển. Nhánh release là một tham chiếu có thể tiến lên khi nhận hotfix được duyệt. Vì vậy, ngay lúc phát hành `v1.0.0` trùng đầu `release/lab04`, nhưng sau hotfix đầu nhánh có thể là `v1.0.1`, còn `v1.0.0` phải giữ nguyên.

Kiểm toán một tag cần đối chiếu phiên bản trong mã nguồn, CHANGELOG, danh sách tệp được theo dõi và kết quả test trên chính tag đó. Chạy test chỉ ở `master` không chứng minh được bản phát hành cũ hoạt động đúng.
