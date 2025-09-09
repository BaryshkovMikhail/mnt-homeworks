# Ansible Role: Lighthouse

Устанавливает и настраивает веб-интерфейс Lighthouse через Nginx.

## Требования

- Ubuntu 20.04/22.04/24.04
- Ansible 2.10+

## Переменные

| Переменная | Описание | По умолчанию |
|-----------|---------|-------------|
| `lighthouse_repo` | URL репозитория Lighthouse | `https://github.com/VKCOM/lighthouse.git` |
| `lighthouse_path` | Путь к статике | `/var/www/lighthouse` |
| `nginx_vhost` | Путь к конфигу Nginx | `/etc/nginx/sites-available/lighthouse` |
| `nginx_link` | Ссылка в enabled-sites | `/etc/nginx/sites-enabled/lighthouse` |

## Зависимости

Нет.

## Пример использования

```yaml
- hosts: lighthouse
  roles:
    - lighthouse-role
```

### Лицензия 

MIT      

## Автор 

**Барышков Михаил**

Роль создана в рамках домашнего задания по курсу "DevOps: с нуля до профи".

Можно использовать и модифицировать свободно. 

