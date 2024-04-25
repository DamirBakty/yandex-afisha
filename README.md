# Куда пойти - Проект по Джанго

Тестовый проект по Django о самых интересных местах в Москве.
<br>
[Сайт](https://pythonenjoyer228.pythonanywhere.com/)
<br>
[Источник](https://github.com/devmanorg/where-to-go-frontend/?tab=readme-ov-file)

![&#x41A;&#x443;&#x434;&#x430; &#x43F;&#x43E;&#x439;&#x442;&#x438;](.gitbook/assets/site.png)

## Как запустить

* Скачайте код
* Перейдите в корневую папку проекта
* Создайте виртуальное окружение
* Установите зависимости

```bash
$ pip install -r requirements.txt
```

* Создайте .env файл и скопируйте содержимое из .env.example
* Поменяйте данные под свой проект
* * SECRET_KEY - набор из случайных символов для защиты от CSRF
* * DEBUG - Значение которое включает и выключает режим отладки проекта. Варианты: True или False
* Экспортируйте переменные из .env в переменные окружения
* Сделайте миграцию в базу данных

```bash
$ python manage.py migrate
```

* Создайте супер пользователя для админки

```bash
$ python manage.py createsuperuser
```

* Запустите проект
```bash
$ python manage.py runserver
```

* Заходим в админку по пути /admin
* Заполняем локации:
* * Название Локации
* * Короткое описание
* * Полное описание
* * Координаты в формате JSON, Пример: 
* ```json
  {
  "lng": "37.64912239999976", 
  "lat": "55.77754550000014"
  }

* Автоматическая загрузка данных
* Пишем команду в терминале python manage.py load_place [url]
* Данные берем по [ссылке](https://github.com/devmanorg/where-to-go-places)
* В папке places лежат JSON файлы, читаем в формате Raw и копируем ссылку
* Пример:
```bash
python manage.py load_place https://raw.githubusercontent.com/devmanorg/where-to-go-places/master/places/%D0%90%D1%80%D1%82-%D0%BF%D1%80%D0%BE%D1%81%D1%82%D1%80%D0%B0%D0%BD%D1%81%D1%82%D0%B2%D0%BE%20%C2%AB%D0%91%D1%83%D0%BD%D0%BA%D0%B5%D1%80%20703%C2%BB.json
```


## Настройки

![debug mode](.gitbook/assets/debug-option.png)

Настройки сохраняются в Local Storage браузера и не пропадают после обновления страницы. Чтобы сбросить настройки, удалите ключи из Local Storage с помощью Chrome Dev Tools —&gt; Вкладка Application —&gt; Local Storage.

Если что-то работает не так, как ожидалось, то начните с включения отладочного режима логгирования.

<a href="#" id="data-sources"></a>

## Источники данных
Фронтенд получает данные из базы данных. <br> 
* Сперва передает общая информация о всех места с координатами в HTML. И ссылку на детальную информацию о месте, передав id локации. 
Пример: /places/1 <br>
* Нажимая на одну из точек можно получить более детальную информацию о месте, делая запрос по id локации

## Используемые библиотеки
* [Django](https://www.djangoproject.com/)
* [django-admin-sortable2](https://pypi.org/project/django-admin-sortable2/)
* [pillow](https://pypi.org/project/pillow/)
* [django-tinymce](https://pypi.org/project/django-tinymce/)
