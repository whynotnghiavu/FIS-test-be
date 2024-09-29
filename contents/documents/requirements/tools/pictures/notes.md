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

<!--  -->
npx create-next-app@latest my-app
cd my-app
npx create-next-app@latest my-next-app
cd my-next-app
npm run dev

npx shadcn@latest add "https://v0.dev/chat/b/b_CTLbpNp1F5c?token=eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..tIVtR9TBrCzEjXNH.qbHSYQnNIprGtdXDEXDqGmyWGvuj7R9kjWhy_OeLbHDkk4vH7e2QYoQ2N_Q.vxvcLmT_HlRvl9JPCmUnuw"