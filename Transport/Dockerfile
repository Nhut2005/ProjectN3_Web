# For more information, please refer to https://aka.ms/vscode-docker-python
FROM python:3.13-slim

RUN adduser --disabled-password --gecos '' appuser

# Đặt thư mục làm việc 
WORKDIR /app

# Cài đặt các gói cần thiết cho mysqlclient
# RUN apt-get update && apt-get install -y \
#     pkg-config \
#     libmysqlclient-dev \
#     build-essential
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

   
# Copy tập yêu cầu và cài đặt dependencies 
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy mã nguồn dự án
COPY . .

# Expose cổng 8000
EXPOSE 8000

# Chạy lệnh khởi động server Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
