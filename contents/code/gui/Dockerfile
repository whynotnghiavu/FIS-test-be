# Sử dụng image Node chính thức từ DockerHub
FROM node:16

# Thiết lập thư mục làm việc bên trong container
WORKDIR /app

# Sao chép các file package.json và package-lock.json để cài đặt dependencies
COPY package*.json ./

# Cài đặt dependencies
RUN npm install

# Sao chép tất cả các file còn lại vào container
COPY . .

# Build ứng dụng để phục vụ cho production
RUN npm run build

# Expose port 3000 để truy cập vào ứng dụng
EXPOSE 3000

# Lệnh để chạy ứng dụng
CMD ["npm", "start"]
