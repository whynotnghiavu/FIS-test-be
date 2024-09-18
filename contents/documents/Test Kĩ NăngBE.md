Đề bài:

1. Xây dựng rest api với những yêu cầu sau

- Sử dụng FastAPI framework (python)
- Sử dụng thư viện sqlalchemy
- Database Sqlite

- Xây dựng các bảng 3 bảng có liên kết với nhau tùy tý có sử dụng method get/put/delete/post

<!-- ! -->

- Thêm 1 bảng user
- Xác thực bằng jwt trong jwt có xác thực thêm quyền của user
- Các đầu api được phân quyền theo quyền của user

- Password mã hóa rồi mới lưu vào database

- Phân chia các folder, file hợp lý logic

2. Thực hiện chạy trên docker
3. Test đầu api trên postman
4. Chuyển từ http sang https
Yêu cầu làm trong 1 tuần kể từ nhận đề bài.
Báo cáo 2 ngày 1 lần.
<!-- ! -->

# Kiểm tra ràng buộc khóa

1 post có nhiều category và 1 category có nhiều post (nâng cấp sau)

<!-- @ 3. Test đầu api trên postman -->

# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):

<!-- fastapi dev a.py -->


Đăng ký
Đăng nhập
Quên mật khẩu

CRUD quyền 

chỉ chủ nhân mới sửa được posts, comment
