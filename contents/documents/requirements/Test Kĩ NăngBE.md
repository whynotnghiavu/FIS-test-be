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

<!-- @ -->
<!-- @ -->
<!-- @ -->

<!-- role là 1 hàng trong bảng? -->

<!-- fastapi dev a.py -->

<!-- !Đã làm thêm: -->

Sử dụng mysql
Sử dụng phpmyadmin

sqlalchemy connect:
retry_delay: Thời gian chờ thử lại
retries: Số lần thử lại

Truy vấn bị lỗi do server: dùng ExceptionMiddleware return

Thêm validate: field_validator

4. Chuyển từ http sang https

posts liên kết user:
comments liên kết user:

Phân quyền:
Admin all
Thêm sửa xóa (posts, comment) chỉ chủ nhân

Xóa thì chỉ return `204 No Content`

Quản lý SQL .v1 .v2 Migration: thêm cột mô tả
Dùng `alembic`
pip install alembic
alembic init alembic

alembic revision -m "Add a column description"

alembic upgrade +1
alembic downgrade -1

<!-- !Nâng cấp sau: -->

`Test đầu api trên postman`

utils check Auto check exits Kiểm tra ràng buộc khóa

1 post có nhiều category và 1 category có nhiều post (có 1 bảng trung gian)

Thêm gửi email quên mật khẩu, qr, ... tokent

Thêm logging

Thêm gợi ý DTO

<!-- !Câu hỏi: -->

Auto CRUD?

<!-- !Kiến thức cần học: -->

Fastapi
Sqlaichemy
Jwt
Alembic
Docker
Postman
