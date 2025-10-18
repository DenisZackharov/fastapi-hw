# FastApi для предсказания

## Команды для запуска

### Установка зависимостей
```shell
# установка зависимостей
uv sync

# тренировка модели
uv run train_model.py
```

### Запуск приложения
```shell
# Запуск приложения
uv run uvicorn main:app --reload

# Запуск приложения из docker
docker compose -f docker-compose.yml up
```


### Документация
http://127.0.0.1:8000/docs
