<!-- Học thư viện pydantic -->
<!-- Học thư viện datetime -->
<!-- Học thư viện faker -->
<!-- Học thư viện typing python -->
<!-- Học Git -->
<!-- Học NodeJS MSA có post comment -->
<!-- mongodb -->

# Coding:

Xóa thì chỉ return `204 No Content`
Dùng password_hash trong db cho rõ nghĩa
HTTP status=404, detail
Hàm def (): thì để `):` bên dưới
Quy trình chung: Tạo mới, Lấy tất cả, Lấy theo id, Xóa bỏ, Cập nhật
Mã HTTP: 401 user

# Công việc:

<!-- Sử dụng FastAPI framework (python) -->

<!-- !FastAPI -->

<!-- Sử dụng thư viện SQLAlchemy -->
<!-- Xây dựng 3 bảng -->

<!-- !SQLAlchemy -->
<!-- !ORM -->

<!-- Sử dụng method get/put/delete/post -->

<!-- Xác thực và phân quyền: -->
<!-- Thêm 1 bảng user -->
<!-- role là 1 hàng trong bảng với 2 loại "admin" và "user" -->
<!-- Password mã hóa rồi mới lưu vào database -->

<!-- Xác thực bằng jwt -->
<!-- jwt có xác thực thêm quyền của user -->
<!-- Các đầu api được phân quyền theo quyền của user -->

<!-- Phân quyền: -->
<!-- Admin all và CRUD thể loại -->
<!-- Thêm sửa xóa (posts, comment) chỉ chủ nhân -->

<!-- !jwt -->
<!-- !json -->
<!-- !hash -->

<!-- Sử dụng docker -->
<!-- Sử dụng mysql trong docker -->

<!-- !docker -->

<!-- Xử lý connect db với: -->
<!-- retry_delay: Thời gian chờ thử lại -->
<!-- retries: Số lần thử lại -->

Truy vấn bị lỗi do server: dùng ExceptionMiddleware return

<!-- @Nhưng tất cả lỗi DB đều bị return -->

<!-- Thêm validate: -->
<!-- dùng field_validator -->
<!-- và regex -->

<!-- !regex -->

<!-- Chuyển từ http sang https -->

<!-- !SSL -->

Quản lý SQL .v1 .v2 Migration: Dùng `alembic`

pip install alembic
alembic init alembic

alembic upgrade head
alembic upgrade +1
alembic downgrade -1


alembic revision --autogenerate -m "first init"
<!-- # -->

<!-- ! -->

Test đầu api trên postman:
Làm lại sau
postman: test

<!-- ! Học Postman -->

Thêm admin đầu tiên, đăng ký là admin
Có admin đầu tiên và login ở đăng ký mới
.env User_name default: admin password default: admin
IF count =0 thì tạo user admin, password admin

<!-- -->

login đúng : otp qr
k có jwt ,

<!-- -->

user: email, password, role, xác nhận is2Fa = False; Enable
tokent: user_id,

<!-- -->

<!--  -->

Jwt và auth
Postman và các tạo test

Thêm 2 class Minxi chung: Tên bảng và thời gian create_at, update_at

<!-- -->

thêm sub id trong jwt

Thử hết hạn jwt?

utils check Auto check exits Kiểm tra ràng buộc khóa

1 post có nhiều category và 1 category có nhiều post (có 1 bảng trung gian)

Thêm gửi email quên mật khẩu, qr, ... tokent

Thêm logging xóa sau một giờ

<!-- ! Học thư viện log -->

Cách loại bỏ thông tin DTO

Thêm gợi ý DTO

<!-- !Kiến thức cần học: -->

Thư viện uvicorn
Thư viện FastAPI

Thư viện Sqlaichemy: ORM
