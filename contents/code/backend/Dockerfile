# Sử dụng image Python
FROM python:3.9-slim

# Đặt thư mục làm việc
WORKDIR /app

# Copy các file cần thiết
COPY ./requirements.txt /app/requirements.txt

# Cài đặt các thư viện
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

# Copy mã nguồn vào container
COPY ./ /app

# Lệnh khởi chạy ứng dụng FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
