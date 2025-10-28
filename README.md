# TesteDjango

Aplica��o Django com django-ninja

## Pr�-requisitos

- Docker
- Docker Compose

## Executando com Docker

### 1. Build da imagem

```bash
docker-compose build
```

### 2. Iniciar a aplica��o

```bash
docker-compose up
```

A aplica��o estar� dispon�vel em: `http://localhost:9000`

### 3. Iniciar em modo detached (background)

```bash
docker-compose up -d
```

### 4. Ver logs da aplica��o

```bash
# Ver todos os logs
docker-compose logs

# Ver logs em tempo real
docker-compose logs -f

# Ver logs de um servi�o espec�fico
docker-compose logs -f web
```

### 5. Executar comandos Django

Para executar comandos do Django dentro do container:

```bash
# Criar um superusu�rio
docker-compose exec web uv run python manage.py createsuperuser

# Criar novas migra��es
docker-compose exec web uv run python manage.py makemigrations

# Aplicar migra��es
docker-compose exec web uv run python manage.py migrate

# Shell do Django
docker-compose exec web uv run python manage.py shell

# Acessar shell bash do container
docker-compose exec web bash
```

### 6. Parar a aplica��o

```bash
# Parar containers
docker-compose stop

# Parar e remover containers
docker-compose down

# Parar e remover containers, volumes e imagens
docker-compose down -v --rmi all
```

### 7. Rebuild (ap�s mudan�as em depend�ncias)

```bash
docker-compose down
docker-compose build --no-cache
docker-compose up
```

### 8. Comandos �teis adicionais

```bash
# Ver containers em execu��o
docker-compose ps

# Ver uso de recursos
docker stats

# Limpar volumes n�o utilizados
docker volume prune

# Reiniciar um servi�o espec�fico
docker-compose restart web
```

## Executando sem Docker

Se preferir executar localmente sem Docker:

```bash
# Instalar depend�ncias
uv sync

# Aplicar migra��es
uv run python manage.py migrate

# Iniciar servidor
uv run python manage.py runserver
```

## Estrutura do Projeto

- `config/` - Configura��es do Django
- `users/` - App de usu�rios
- `manage.py` - Script de gerenciamento do Django
- `pyproject.toml` - Depend�ncias do projeto (gerenciadas pelo uv)

## Admin

Acesse o painel admin em: `http://localhost:9000/admin`
