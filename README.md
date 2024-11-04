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
- Запуск postgres. Переходим в соотвтетствующую директрорию.
```shell
cd postgres
docker compose up -d
```

Проверка БД.
```shell
psql -h localhost -p 5432 -U postgres -W postgres
cd ..
```
запуск redis.
```shell
cd redis
redis://username:password@193.3.298.206:6380/0
```

Прверка redis.
```shell
redis-cli -h 127.0.0.1 -p 6379 -a redis
cd ..
```

- Запуск aiohttp. Переходим в соотвтетствующую директрорию.
```shell
cd aiohttp
docker compose up -d
```

проверка aiohttp
```shell
http://localhost:8080
cd ..
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


Проверка redis.

```shell
redis-cli -h 127.0.0.1 -p 6379 -a redis
```
```shell
redis> set test:1:string "my binary safe string" OK
```
```shell
redis> get test:1:string "my binary safe string"
```
