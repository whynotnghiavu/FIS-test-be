# Sử dụng image Node.js
FROM node:16-alpine

# Đặt thư mục làm việc
WORKDIR /app

# Copy package.json và cài đặt các dependencies
COPY package.json /app

RUN npm install

# Copy mã nguồn vào container
COPY . /app

# Chạy ứng dụng React
CMD ["npm", "start"]
