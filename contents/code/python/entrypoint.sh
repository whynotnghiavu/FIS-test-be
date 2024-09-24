#!/bin/sh

python check_alembic_db.py
alembic upgrade head

python main.py
