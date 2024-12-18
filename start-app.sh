./wait-for-it.sh postgres:5432 --timeout=60

alembic revision --autogenerate -m "init"
alembic upgrade head

python src/add_data.py

python src/main.py