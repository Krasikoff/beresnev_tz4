# beresnev_tz4

## запуск приложения.

- Клонируем репозиторий.

```shell
git@github.com:Krasikoff/beresnev_tz4.git
```

- Запуск postgres. Переходим в соотвтетствующую директрорию.
(предположительно докер установлен)
```shell
cd postgres
docker compose up -d
```

Проверка БД.
```shell
psql -h localhost -p 5432 -U postgres -W postgres
cd ..
```
- Запуск redis. Переходим в соотвтетствующую директрорию.
```shell
cd redis
docker compose up -d
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

## запуск приложения в docker режиме.

```shell
docker build -t tz4 .
docker run -d --name tz4 -p 8000:8000 tz4
docker exec -it tz4 alembic upgrade head
```


```shell
docker compose up -d
```

## в develop режиме.
- Устанавливаем окружение.
```shell
git push -u origin main && source venv/bin/activate
```
- Устанавливаем заисимости.
```shell
python -m pip install --upgrade pip
pip install -r requirements.txt
```

- Запуск приложения.
```shell
uvicorn app.main:app --reload 
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
