# Trả lời thảo luận Lab 03

## Merge base là gì?

Merge base là tổ tiên chung tốt nhất của hai đầu lịch sử. Git dùng nó làm mốc để so sánh thay đổi ở mỗi phía trong phép merge ba chiều. Lệnh `git merge-base master feature/discount` có thể tìm mốc chung giữa hai nhánh. Trong lịch sử phức tạp có thể tồn tại nhiều merge base tốt nhất.

Nếu hai phía sửa cùng một vùng nội dung theo cách không tự kết hợp được, Git báo conflict. Cần hiểu ý đồ của cả hai thay đổi, sửa thành nội dung thống nhất, xóa marker và chạy test trước khi hoàn tất merge.

## Vì sao `master` và `release/*` dùng revert?

Đây là các nhánh có lịch sử dùng chung hoặc đã dùng làm baseline. `git revert` tạo commit đảo ngược thay đổi nhưng giữ nguyên lịch sử, nên người khác vẫn có thể đồng bộ bình thường và kiểm toán được ai đã thay đổi, vì sao phải hoàn tác. Commit revert cũng phải đi qua nhánh sửa lỗi và PR theo chính sách của đề.

Ngược lại, `reset` dời con trỏ nhánh; `amend` và `rebase` viết lại commit. Nếu áp dụng rồi force push lên lịch sử đã chia sẻ, các bản clone khác có thể mất đồng bộ và các tham chiếu cũ không còn phản ánh lịch sử của nhánh.

## Hoàn tác merge commit thế nào?

Merge commit có nhiều parent. `git revert -m 1 <merge-sha>` chọn parent thứ nhất làm đường chính và đảo phần thay đổi mà merge đã đưa vào so với parent đó. Phải kiểm tra parent trước; không áp dụng số 1 một cách máy móc cho mọi lịch sử.

Revert merge không xóa sự kiện merge khỏi lịch sử. Nếu muốn đưa lại tính năng đó, cần thiết kế thay đổi mới hoặc revert commit revert theo tình huống, thay vì cho rằng merge lại cùng nhánh sẽ tự phục hồi mọi thay đổi.

## `reset` và `reflog` dùng trong nhánh nháp ra sao?

- `reset --soft` đưa con trỏ về commit trước và giữ thay đổi trong staging.
- `reset --mixed` giữ thay đổi ở working tree, đồng thời đặt lại staging.
- `reset --hard` đặt lại cả working tree; chỉ thực hành với thay đổi nháp có chủ đích và đã bảo vệ dữ liệu cần giữ.
- `reflog` ghi các lần di chuyển tham chiếu ở bản clone hiện tại, giúp tìm lại commit vừa bị bỏ khỏi đầu nhánh. Reflog là dữ liệu cục bộ, có thời hạn lưu và không phải cơ chế sao lưu lâu dài.

## Vì sao commit test phải đứng trước commit fix?

Chạy test trước khi sửa phải tái hiện đúng lỗi dự kiến, chẳng hạn giỏ chấp nhận đĩa thứ 21. Sau khi sửa, cùng test phải pass. Hai trạng thái FAIL rồi PASS chứng minh test bắt được lỗi thay vì chỉ tình cờ luôn thành công. Với lỗi trên nhánh tính năng, PR bugfix phải chọn đúng base là nhánh tính năng; từ khóa đóng Issue thường chỉ đóng Issue khi thay đổi được merge vào nhánh mặc định.
## Thao tác đã thực hiện trên repo bài

- Issue [#7](https://github.com/HaTienDat2004/it3180-202417231-aims/issues/7) ghi lỗi giới hạn giỏ hàng và đã tự đóng khi PR [#8](https://github.com/HaTienDat2004/it3180-202417231-aims/pull/8) merge vào master. Commit regression test nằm trước commit fix; test thất bại trước sửa vì đĩa thứ 21 được chấp nhận, sau đổi điều kiện từ lớn hơn thành lớn hơn hoặc bằng thì pass.
- PR [#9](https://github.com/HaTienDat2004/it3180-202417231-aims/pull/9) có base feature/discount; sau khi merge vào nhánh tính năng, PR [#10](https://github.com/HaTienDat2004/it3180-202417231-aims/pull/10) tích hợp tính năng đã sửa vào master.
- PR [#11](https://github.com/HaTienDat2004/it3180-202417231-aims/pull/11) đưa thông báo tiếng Việt vào trước. Nhánh feature/show-added-title được tạo từ master cũ, merge master vào nhánh đó và gặp conflict thật tại cùng dòng của aims/cart.py. PR [#12](https://github.com/HaTienDat2004/it3180-202417231-aims/pull/12) giữ cả hai ý trong thông báo Đã thêm đĩa '<title>' vào giỏ hàng.
- Sau khi xác nhận chỉ cần thông báo tiếng Việt, dùng git revert -m 1 trên nhánh sửa riêng rồi merge qua PR [#13](https://github.com/HaTienDat2004/it3180-202417231-aims/pull/13). Master hiện có Đã thêm đĩa vào giỏ hàng, không còn phần thêm tiêu đề. Bốn test đều pass.
- reset --soft, --mixed và --hard được tập trên nhánh local chưa push topic/undo-practice. reflog tìm lại commit 8a5c28d; nhánh cứu hộ khôi phục được tệp trước hard reset. Sau khi xác minh, các nhánh nháp đã được xóa.
