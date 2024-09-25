
<!-- NodeJS MSA có post comment -->
# Coding:

Hàm routers = def (): thì để `):` bên dưới
Xóa thì chỉ return `204 No Content`
HTTP status=404, detail
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

<!-- Thêm validate: -->
<!-- dùng field_validator -->
<!-- và regex -->

<!-- !regex -->

<!-- Chuyển từ http sang https -->
<!-- !SSL -->

<!-- Dùng alembic quản lý SQL -->
<!-- Quản lý SQL .v1 .v2 Migration: Dùng `alembic` -->

alembic init alembic

alembic downgrade base
alembic upgrade head

alembic upgrade +1
alembic downgrade -1

alembic history

alembic revision --autogenerate -m "add description"

<!-- !alembic -->
<!-- @ Muốn dùng lệnh -->
<!-- alembic upgrade head -->
<!-- trong docker nhưng db chưa khởi động -->
<!-- dùng file .sh -->

Thêm admin đầu tiên
Cấu hình trong .env

IF count == 0 thì tạo admin
Phân quyền chỉ admin mới đăng ký tk mới

<!-- @ Có dùng trực tiếp trong app/api -->
<!-- https://gist.github.com/jsmsalt/26bf25844870d59eee17997727e3a631 -->

Xử lý OTP: Dùng thư viện pyotp
https://it-tools.tech/otp-generator

<!-- !pyotp -->
<!-- https://pyauth.github.io/pyotp -->
<!-- !Học thuật toán HOTP, TOTP -->
<!-- https://www.onelogin.com/learn/otp-totp-hotp -->

<!-- https://pinonote.wordpress.com/2018/11/27/thuat-toan-hmac-based-one-time-password-algorithm-hotp-va-time-based-one-time-password-totp-trong-google-authenticator/ -->

Thêm logging logger
xóa sau một giờ, 7 ngày 30 60 90.... env

logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.error("This is an error message.")
logger.warning("This is a warning message.")

<!-- ################### -->

Test đầu api trên postman: Làm lại sau

{{url_api_v1}}/users/login
{{url_api_v1}}/users/generate-qr
{{url_api_v1}}/users/verify-otp

{{url_api_v1}}/categories
{{url_api_v1}}/categories/{category_id}

{{url_api_v1}}/posts
{{url_api_v1}}/posts/{post_id}

{{url_api_v1}}/posts/{post_id}/comments
{{url_api_v1}}/posts/{post_id}/comments/{comment_id}

<!-- ! Postman -->
<!-- Gọi API với Postman? -->
Gọi {{baseUrl}} để lấy JWT 


Thêm gửi email quên mật khẩu: Dùng mailhong
Thêm đổi mật khẩu 

<!-- Thêm gợi ý DTO có thể dùng fAker -->

Cách loại bỏ thông tin DTO từ Base (ví dụ bỏ thông tin password)

1 post có nhiều category và 1 category có nhiều post (có 1 bảng trung gian)

Thêm 2 class Minxi chung: Tên bảng và thời gian create_at, update_at

utils check Auto check exits Kiểm tra ràng buộc khóa

Truy vấn bị lỗi do server: dùng ExceptionMiddleware return
`Chưa làm được`

<!-- @Nhưng tất cả lỗi DB đều bị return -->





Anh Đăng bảo:
thêm  isEnableOTP: true, false
thêm khôi phục quên OTP như github????


ẢNh base64 nên làm 
hàm phụ hình ảnh tạo hình ảnh?
hàm phụ hoặc router2

Tạo báo cáo