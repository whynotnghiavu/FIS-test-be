Đề bài:

1. Xây dựng rest api với những yêu cầu sau

- Sử dụng FastAPI framework (python)
- Sử dụng thư viện sqlalchemy
- Database Sqlite

- Xây dựng các bảng 3 bảng có liên kết với nhau tùy tý có sử dụng method get/put/delete/post

- Thêm 1 bảng user
- Xác thực bằng jwt trong jwt có xác thực thêm quyền của user
- Các đầu api được phân quyền theo quyền của user

- Password mã hóa rồi mới lưu vào database

- Phân chia các folder, file hợp lý logic

2. Thực hiện chạy trên docker

<!-- ! -->


Yêu cầu làm trong 1 tuần kể từ nhận đề bài.
Báo cáo 2 ngày 1 lần.

<!-- @ -->
<!-- @ -->
<!-- @ -->

<!-- role là 1 hàng trong bảng? -->

<!-- fastapi dev a.py -->

<!-- !Nâng cấp sau: -->

<!-- Sử dụng mysql -->
<!-- Sử dụng phpmyadmin -->

<!-- sqlalchemy connect:  -->
<!-- retry_delay: Thời gian chờ thử lại  -->
<!-- retries: Số lần thử lại   -->

<!-- Truy vấn bị lỗi do server: dùng ExceptionMiddleware -->

<!-- Thêm validate: field_validator -->

3. Test đầu api trên postman

<!-- 4. Chuyển từ http sang https -->

Lấy người dùng hiện tại?
QUYỀN: chỉ chủ nhân mới sửa được posts, comment??? get user
<!-- posts liên kết user -->


<!-- ! -->

Quản lý SQL:
v1 v2 Migration:
pip install alembic  
alembic init alembic


utils check Auto check exits Kiểm tra ràng buộc khóa?
Auto CRUD?


 



1 post có nhiều category và 1 category có nhiều post (có 1 bảng trung gian)




Thêm gửi email quên mật khẩu, qr, ...

logging

Thêm gợi ý đầu vào 