<!-- uvicorn main:app --host 0.0.0.0 --port 8000 -->

python main.py
npm start

<!--  -->

<!-- Phân biệt thư viện và famework -->

<!-- Dùng alembic quản lý phiên bản SQL -->

alembic init alembic

alembic downgrade base
alembic upgrade head

alembic upgrade +1
alembic downgrade -1

alembic history

alembic revision --autogenerate -m "create user table"
alembic revision --autogenerate -m "add otp user table"
alembic revision --autogenerate -m "create 3 table"

<!-- CSS fe sau -->

Chỉ hiển thị không CRUD
