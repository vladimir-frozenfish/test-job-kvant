# Тестовое задание на вакансию Python Разработчик (ФГУП "НИИ "Квант")

## По условиям задания:
- создано приложение Projects
- создана модель Projects с необходимыми полями: приоритет, статус, время создания, исполнители
- написаны view-функции: create, destroy, choose

## URLS проекта:
- localhost/ - главная страница проекта - выводится все созданные проекты
- localhost/create/ - создание проекта
- localhost/project/<project_id>/ - выводится детальная информация о конкретном проекте
- localhost/project/<project_id>/destroy/ - удаление проекта
- localhost/project/<project_id>/edit/ - редактирование проекта
- localhost/choose/ - выводит страницу приоритетного проекта 

### <span style="color:red"> В связи с тем, что данный проект является тестовым заданием - секретный ключ и другие возможные секретные данные не выносились в переменные окружения </span> 

### Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/.../
```
Cоздать и активировать виртуальное окружение:
```
python3 -m venv env
. env/bin/activate (для linux)
sourse env/Scripts/activate (для Windows)
```
Установить зависимости из файла requirements.txt:
```
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```
Выполнить миграции:
```
python3 manage.py migrate
```
Для доступа в admin-панель создать суперюзера:
```
python3 manage.py createsuperuser
```
Запустить проект:
```
python3 manage.py runserver
```

