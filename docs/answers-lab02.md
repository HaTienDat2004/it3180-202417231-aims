# Trả lời thảo luận Lab 02

## Vì sao phải đồng bộ với `master` trước khi gửi hoặc tích hợp PR?

Nhánh tính năng có thể được tạo trước khi các PR khác cập nhật `master`. Fetch rồi tích hợp `origin/master` giúp phát hiện xung đột và lỗi tương tác ngay trên nhánh tính năng, nơi có thể sửa và chạy lại chương trình. Nhờ vậy, kết quả được review gần với kết quả sẽ tích hợp vào nhánh chính hơn. Sau thay đổi mới, cần kiểm thử lại; nếu đã cấu hình dismiss stale approvals thì phải review lại nội dung mới.

Việc đồng bộ không tự bảo đảm nhánh luôn cập nhật: `master` có thể tiếp tục thay đổi sau đó. Cần kiểm tra lại trạng thái merge và CI ngay trước khi tích hợp.

## Khi nào không nên rebase?

Rebase tạo commit mới với SHA mới. Không rebase tùy tiện `master`, `release/*` hay nhánh đã được người khác dùng làm nền, vì họ đang dựa trên lịch sử đã chia sẻ. Với nhánh cá nhân chưa chia sẻ, có thể rebase để sắp xếp lịch sử. Nếu nhánh đã push mà thật sự cần viết lại lịch sử, phải thống nhất với người liên quan và chỉ dùng `--force-with-lease` khi chính sách repo cho phép; tùy chọn này không thay thế việc phối hợp.

Theo nguyên tắc của bài thực hành, ưu tiên merge `origin/master` vào nhánh đã chia sẻ và dùng revert để hoàn tác trên lịch sử chung.

## `feature/*` khác `topic/*` ra sao?

`feature/*` dành cho khả năng mới mà người dùng có thể sử dụng, chẳng hạn in giỏ hàng hoặc tìm DVD theo tiêu đề. `topic/*` dành cho một chủ đề công việc rõ ràng, thường là tài liệu hoặc cấu hình quy trình, chẳng hạn PR template, sơ đồ use case hay cấu hình CI.

Hai loại đều là nhánh sống ngắn, thường tạo từ `master` và tích hợp qua PR vào `master`. Tên nhánh diễn đạt mục đích; Git không áp dụng cơ chế kỹ thuật khác nhau chỉ vì tiền tố tên.

## Ba kiểu merge có gì khác nhau?

- **Merge commit:** giữ các commit của nhánh và thêm một merge commit, thể hiện rõ điểm hợp nhất. Có thể revert toàn bộ merge bằng cách chỉ định parent chính với `git revert -m 1` sau khi kiểm tra lịch sử.
- **Squash and merge:** gộp thay đổi thành một commit mới trên nhánh đích. Diff cuối vẫn được giữ, nhưng chuỗi SHA ban đầu không trở thành tổ tiên của nhánh đích. Vì vậy, Git có thể không nhận nhánh nguồn là đã merge khi dùng `git branch -d`.
- **Rebase and merge:** đưa từng commit lên đầu nhánh đích theo lịch sử tuyến tính, tạo SHA mới và không thêm merge commit. Nếu muốn hoàn tác cả tính năng, cần xác định đúng các commit thuộc tính năng đó.
