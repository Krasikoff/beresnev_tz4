# beresnev_tz4

## запуск приложения в dev режиме.

- Клонируем репозиторий.

```shell
git@github.com:Krasikoff/beresnev_tz4.git
```
- Устанавливаем окружение.
```shell
git push -u origin main && source venv/bin/activate
```
- Устанавливаем заисимости.
```shell
python -m pip install --upgrade pip
pip install -r requirements.txt
```
- Запуск контейнера с postgres
```shell
docker compose up -d
```

- Запуск приложения.
```shell
uvicorn app.main:app --reload 
```

## запуск приложения в docker режиме.
    (предположительно докер установлен)
```shell
docker compose up -d
```

to be continued....

### Команды alembic - справочно 

```shell
alembic init --template async alembic
alembic revision --autogenerate -m "First migration" 
alembic upgrade head
```
Проверка БД.
```shell
psql -h localhost -p 5432 -U postgres -W postgres
```

```shell
redis://username:password@193.3.298.206:6380/0
```
