<!-- Các chức năng: -->
 

Xác minh OTP
Thể loại, Bài viết, Bình luận
Postman
<!-- refresh token? -->

Quên mật khẩu

<!-- Lý thuyết: -->

JWT token
Mail Mailhong
Back end + Font end
 



<!-- Sử dụng FastAPI framework (python) -->
<!-- Sử dụng method get/put/delete/post -->

<!-- Sử dụng thư viện SQLAlchemy -->
<!-- Xây dựng 3 bảng -->

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

<!-- Sử dụng docker -->
<!-- Sử dụng mysql trong docker -->

<!-- Xử lý connect db với: -->
<!-- retry_delay: Thời gian chờ thử lại -->
<!-- retries: Số lần thử lại -->

<!-- Thêm validate: -->
<!-- dùng field_validator -->
<!-- và regex -->

<!-- Chuyển từ http sang https -->


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

<!-- Xử lý OTP: Dùng thư viện pyotp -->

Thêm logging logger
xóa sau một giờ, 7 ngày 30 60 90.... env

logger.debug("This is a debug message.")
logger.info("This is an info message.")
logger.error("This is an error message.")
logger.warning("This is a warning message.")

isEnableOTP: true, false

<!-- Lưu ảnh vào bảng user -->
<!-- check lại -->

phân quyền check otp

<!-- đổi login như hướng dẫn -->

https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/?h=jwt#hash-and-verify-the-passwords

<!-- @Khi đăng ký và xác thực otp thì làm sao để tự động gắn lại JWT? -->

thêm khôi phục quên OTP như github????
otp-recovery

<!-- # Thay đổi  ảnh khi quên OTP (mất điện thoại) -->

<!-- !Tạo FE -->
<!-- ################### -->

npx create-react-app gui
cd gui
npm start

<!-- !Lỗi chưa OTP tạo thể loại thì bị báo lỗi JWTT?! -->
<!-- ################### -->

<!-- Gọi API với Postman? -->

<!-- @Gọi {{baseUrl}} để lấy JWT -->

<!-- Thêm đổi mật khẩu -->
<!-- Thêm gửi email quên mật khẩu: Dùng mailhong -->

<!-- Thêm gợi ý DTO có thể dùng fAker -->

Cách loại bỏ thông tin DTO từ Base (ví dụ bỏ thông tin password)

1 post có nhiều category và 1 category có nhiều post (có 1 bảng trung gian)

Thêm 2 class Minxi chung: Tên bảng và thời gian create_at, update_at

utils check Auto check exits Kiểm tra ràng buộc khóa

Truy vấn bị lỗi do server: dùng ExceptionMiddleware return
`Chưa làm được`

<!-- @Nhưng tất cả lỗi DB đều bị return -->

<!-- Anh Đăng bảo: -->
<!-- thêm isEnableOTP: true, false -->
<!-- thêm khôi phục quên OTP như github???? -->

<!-- ẢNh base64 nên làm -->
<!-- hàm phụ hình ảnh tạo hình ảnh? -->
<!-- hàm phụ hoặc router2 -->

<!-- Tạo báo cáo -->

refresh_token
