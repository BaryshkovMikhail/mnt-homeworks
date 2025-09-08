# Домашнее задание к занятию 3 «Использование Ansible» - Барышков Михаил

## Подготовка к выполнению

1. Подготовьте в Yandex Cloud три хоста: для `clickhouse`, для `vector` и для `lighthouse`.
2. Репозиторий LightHouse находится [по ссылке](https://github.com/VKCOM/lighthouse).

## Основная часть

1. Допишите playbook: нужно сделать ещё один play, который устанавливает и настраивает LightHouse.
2. При создании tasks рекомендую использовать модули: `get_url`, `template`, `yum`, `apt`.
3. Tasks должны: скачать статику LightHouse, установить Nginx или любой другой веб-сервер, настроить его конфиг для открытия LightHouse, запустить веб-сервер.
4. Подготовьте свой inventory-файл `prod.yml`.
5. Запустите `ansible-lint site.yml` и исправьте ошибки, если они есть.
6. Попробуйте запустить playbook на этом окружении с флагом `--check`.
7. Запустите playbook на `prod.yml` окружении с флагом `--diff`. Убедитесь, что изменения на системе произведены.
8. Повторно запустите playbook с флагом `--diff` и убедитесь, что playbook идемпотентен.
9. Подготовьте README.md-файл по своему playbook. В нём должно быть описано: что делает playbook, какие у него есть параметры и теги.
10. Готовый playbook выложите в свой репозиторий, поставьте тег `08-ansible-03-yandex` на фиксирующий коммит, в ответ предоставьте ссылку на него.

---

### Как оформить решение задания

Выполненное домашнее задание пришлите в виде ссылки на .md-файл в вашем репозитории.

---


# Решение

Ansible Playbook: Clickhouse + Lighthouse

Этот playbook настраивает:
- Clickhouse — аналитическую СУБД
- Lighthouse — веб-интерфейс для просмотра логов (через Nginx)
- Поддержка Ubuntu 20.04/22.04

## Структура

- `site.yml` — основной playbook
- `inventory/prod.yml` — инвентарь
- `group_vars/clickhouse/vars.yml` — переменные Clickhouse
- `templates/lighthouse.conf.j2` — шаблон Nginx

## Clickhouse
- `clickhouse_version`: версия пакета (по умолчанию `22.3.3.44`)

## Lighthouse (в play)
- `lighthouse_repo`: URL репозитория
- `lighthouse_path`: путь к статике
- `nginx_vhost`, `nginx_link`: пути к конфигу Nginx

## Теги
- `clickhouse` — только установка Clickhouse
- `lighthouse` — только установка Lighthouse


![img1](img/img1.png)
![img2](img/img2.png)
![img3](img/img3.png)
![img4](img/img4.png)