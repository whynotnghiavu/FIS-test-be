#!/bin/sh

while ! mysqladmin ping -h"mysql" --silent; do
  sleep 1
done

alembic upgrade head

python main.py

# 1. **`#!/bin/sh`**
#    - Đây là một "shebang", cho hệ điều hành biết rằng đoạn mã này sẽ được thực thi bởi shell (`sh`).

# 2. **`while ! mysqladmin ping -h"database" --silent; do`**
#    - `mysqladmin ping` là lệnh để kiểm tra xem MySQL server có sẵn sàng chấp nhận kết nối hay không.
#    - `-h"database"` chỉ định host của cơ sở dữ liệu. Thay thế `"database"` bằng địa chỉ host thật (ví dụ: `localhost` hoặc tên container trong Docker).
#    - `--silent` chỉ định không in ra thông báo.
#    - `!` phủ định, tức là sẽ lặp lại cho đến khi `mysqladmin ping` trả về thành công (nghĩa là MySQL đã sẵn sàng).
#    - Vòng lặp `while ... do ... done` sẽ lặp lại lệnh trong thân vòng lặp nếu điều kiện của `while` là đúng. 

# 3. **`sleep 1`**
#    - Nếu MySQL chưa sẵn sàng, script sẽ tạm dừng 1 giây trước khi thử lại. Điều này giúp tránh việc script kiểm tra liên tục gây tốn tài nguyên.

# 4. **`done`**
#    - Kết thúc vòng lặp `while`.

