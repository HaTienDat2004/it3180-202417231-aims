# Trả lời thảo luận Lab 05

## Vì sao không merge cả nhánh hotfix vào `master`?

Hotfix của dòng `1.0.x` có hai mục đích tách biệt: sửa hành vi tìm kiếm và tăng phiên bản lên `1.0.1`. `master` đang phát triển `1.1.0`, nên nhận cả nhánh có thể gây xung đột hoặc làm sai phiên bản. Tách commit sửa lỗi khỏi commit tăng phiên bản cho phép dùng `cherry-pick -x` để đưa đúng phần sửa vào `master` và `release/lab05`; phần ghi chú phát hành được cập nhật theo ngữ cảnh của từng dòng.

Tùy chọn `-x` thêm SHA commit nguồn vào message, hỗ trợ truy vết. Cherry-pick tạo commit mới nên SHA của bản sửa ở các dòng phiên bản có thể khác nhau.

## Vì sao chưa gắn tag `v1.1.0` ở phần A?

`release/lab05` được tạo trước để làm dòng chuẩn bị phát hành, nhưng vẫn phải nhận bản sửa tìm kiếm trước khi chốt baseline. Đợi đến khi bản sửa được review và kiểm thử mới tạo annotated tag `v1.1.0`. Nếu tag đó đã được chia sẻ cho người dùng, không di chuyển tag để che thay đổi; bản vá sau phát hành phải dùng phiên bản mới như `v1.1.1`.

## Upstream first so với release first

Với **upstream first**, sửa lỗi trên dòng phát triển chính trước rồi backport sang các release bị ảnh hưởng. Cách này giảm nguy cơ quên sửa ở phiên bản tương lai, giữ nguồn sửa chung rõ ràng và phù hợp sản phẩm phát triển liên tục. Tuy nhiên, mã trên dòng chính có thể đã khác nhiều so với bản ổn định, khiến backport phải chỉnh sửa hoặc xử lý conflict.

Với **release first**, sửa từ đúng bản đang lỗi giúp tái hiện sự cố và phát hành patch có phạm vi nhỏ, ít kéo theo tính năng mới. Đổi lại, phải chủ động đưa bản sửa sang `master` và mọi release còn bị ảnh hưởng; bỏ sót một dòng sẽ để lỗi tiếp tục tồn tại. Bài thực hành chọn release first để minh họa việc bảo trì đồng thời nhiều baseline.

## Nếu quên lan truyền sang `release/lab05`, kiểm tra nào phát hiện?

Kiểm tra hành vi tìm `lion` trong `The Lion King` trên `v1.0.1`, `v1.1.0` và `master` là phép kiểm tra trực tiếp: cả ba phải tìm được một DVD. Nếu bản Lab 05 vẫn trả về 0 hoặc test hồi quy tìm kiếm thất bại, bản sửa chưa có hiệu lực ở dòng đó.

Các lệnh kiểm toán lịch sử cần được đọc cùng nhau:

- Tìm message `cherry picked from commit <FIX_SHA>` dự kiến cho thấy hai bản lan truyền. Tuy nhiên, grep trên `--all` chỉ tìm commit ở bất kỳ ref nào; commit tồn tại trên nhánh hotfix chưa merge không chứng minh release đã nhận sửa. Cần kiểm tra riêng lịch sử `master` và `release/lab05`, đồng thời đối chiếu PR.
- `git cherry -v master release/lab04` có thể nhận diện patch tương đương ở `master` bằng dấu `-`, dù SHA khác. Commit chỉ tăng phiên bản cho dòng `1.0.x` có thể hiện dấu `+` một cách có chủ đích. Lệnh này không tự kiểm tra `release/lab05`; cần đối chiếu riêng dòng đó nếu muốn kiểm toán bản vá tương đương.
- `git tag --contains <FIX_SHA>` kiểm tra quan hệ tổ tiên của chính SHA nguồn. Nó có thể liệt kê `v1.0.1` nhưng không liệt kê `v1.1.0` khi bản sửa được cherry-pick. Đây là hành vi đúng: lệnh không phát hiện patch tương đương.

Do đó, cần kết hợp truy vết commit, trạng thái PR và test hành vi trên từng phiên bản; chỉ đếm message hoặc chỉ xem `tag --contains` đều chưa đủ.

## CI hỗ trợ quy trình như thế nào?

Workflow chạy unit test trên PR vào `master` và `release/**` giúp phát hiện lỗi trước khi tích hợp. Để CI thực sự chặn merge, branch protection phải yêu cầu đúng status check `test`; chỉ có tệp workflow chưa tự tạo ra điều kiện bắt buộc. Một PR cố ý làm hỏng tính tổng chỉ dùng để chứng minh CI chặn lỗi và phải được sửa hoặc đóng, không được tích hợp mã lỗi vào baseline.


## Kết quả thực hiện trong repository

- Issue #18 theo dõi lỗi tìm kiếm hoa thường và được đóng khi PR #22 vào master được merge.
- PR #21 phát hành hotfix trên release/lab04; commit sửa lỗi ở GitHub là c065dcc33552e3e155fbe25174feac2bec2bd126.
- Cùng bản sửa được cherry-pick có ghi nguồn vào master qua PR #22 và release/lab05 qua PR #23.
- Đã chạy 8 test trên master và release/lab05; tìm lion trả về The Lion King.
