# Локальный поисковик. Версия 2.

# Установка программы

## Скачивание

Скачиваем себе проект.
```
git clone https://github.com/prog815/loc-index-2.git
```
Получится каталог с файлами. Переходим в него.
```
cd loc-index-2/
```

## Создание образа

Теперь создадим контейнер из скачанного образа:

```
docker build --pull --rm -f "Dockerfile" -t locindex2:latest .
```

# Контейнер

## Запуск контейнера

```
docker run -d -p80:5000 --mount type=bind,source="$(pwd)"/files,target=/app/static/files,readonly --name locindex2 locindex2
```

## Список запущенных контейнеров

```
docker container ls
```

## Удалить контейнер

```
docker rm -f locindex2
```

## Подключиться к контейнеру

```
docker exec -it locindex2 /bin/sh
```

# Работа с программой

Запускаем в браузере http://localhost и в поисковой строке пишем через пробелы последовательности символов которые должны быть в пути к файлу. Жмем "искать". Видим результат перед собой.