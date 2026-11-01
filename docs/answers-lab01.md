# Trả lời thảo luận Lab 01

## Cấu hình `--global` lưu ở đâu? Khác `--local` thế nào?

`git config --global` áp dụng cho tài khoản người dùng, thường lưu tại `~/.gitconfig` (trên Windows là `%USERPROFILE%\.gitconfig`). Git cũng hỗ trợ tệp cấu hình người dùng theo XDG tại `~/.config/git/config`. Dùng `git config --list --show-origin` để biết chính xác nguồn của từng giá trị.

`git config --local` chỉ áp dụng cho repository hiện tại và thường lưu trong `.git/config`. Khi cùng một khóa xuất hiện ở hai cấp, giá trị local ghi đè giá trị global. Ví dụ, có thể đặt email mặc định ở global và email học tập ở local cho repo môn học mà không ảnh hưởng các repo khác.

## Vì sao dùng `git mv`?

`git mv cart.py aims/cart.py` vừa di chuyển tệp vừa đưa thay đổi tên vào staging, tránh quên stage phần xóa hoặc phần thêm. Git không lưu một bản ghi đổi tên độc lập; khi so sánh các snapshot, Git nhận diện đổi tên dựa trên mức giống nhau của nội dung. Vì vậy, `mv` rồi `git add -A` cũng có thể cho cùng kết quả. Tách commit di chuyển khỏi commit sửa nội dung giúp diff dễ đọc và việc nhận diện đổi tên rõ hơn. `git log --follow -- aims/cart.py` hỗ trợ xem lịch sử trước lần đổi tên.

## `release/lab01` có phải baseline không?

Có. Trong quy trình học phần, đây là nhánh giữ trạng thái được chọn để nộp Lab 01. Khi vừa tạo từ `master`, hai nhánh phải trỏ cùng commit; có thể đối chiếu bằng `git rev-parse origin/master origin/release/lab01`. Sau khi phát triển tiếp, chúng không nhất thiết còn giống nhau.

Nhánh release có thể tiến lên khi nhận hotfix qua PR. Muốn định danh chính xác một snapshot bất biến, cần ghi commit SHA hoặc dùng annotated tag như `v0.1.0` ở Lab 04. Không di chuyển tag đã chia sẻ.

## Vì sao vẫn dùng PR khi làm một mình?

Nhánh riêng và PR tạo dấu vết gồm mục đích thay đổi, diff, kiểm thử và quyết định tích hợp. Quy trình cũng ngăn thay đổi chưa hoàn tất đi thẳng vào `master`, đồng thời tạo điểm kiểm tra trước khi cập nhật baseline. Theo đề, khi làm một mình có thể đặt số approval bắt buộc bằng 0, nhưng vẫn yêu cầu mọi thay đổi sau phần khởi tạo đi qua PR.
