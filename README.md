# TesteDjango

Aplicação Django com django-ninja

## Pré-requisitos

- Docker
- Docker Compose

## Executando com Docker

### 1. Build da imagem

```bash
docker-compose build
```

### 2. Iniciar a aplicação

```bash
docker-compose up
```

A aplicação estará disponível em: `http://localhost:9000`

### 3. Iniciar em modo detached (background)

```bash
docker-compose up -d
```

### 4. Ver logs da aplicação

```bash
# Ver todos os logs
docker-compose logs

# Ver logs em tempo real
docker-compose logs -f

# Ver logs de um serviço específico
docker-compose logs -f web
```

### 5. Executar comandos Django

Para executar comandos do Django dentro do container:

```bash
# Criar um superusuário
docker-compose exec web uv run python manage.py createsuperuser

# Criar novas migrações
docker-compose exec web uv run python manage.py makemigrations

# Aplicar migrações
docker-compose exec web uv run python manage.py migrate

# Shell do Django
docker-compose exec web uv run python manage.py shell

# Acessar shell bash do container
docker-compose exec web bash
```

### 6. Parar a aplicação

```bash
# Parar containers
docker-compose stop

# Parar e remover containers
docker-compose down

# Parar e remover containers, volumes e imagens
docker-compose down -v --rmi all
```

### 7. Rebuild (após mudanças em dependências)

```bash
docker-compose down
docker-compose build --no-cache
docker-compose up
```

### 8. Comandos Úteis adicionais

```bash
# Ver containers em execução
docker-compose ps

# Ver uso de recursos
docker stats

# Limpar volumes não utilizados
docker volume prune

# Reiniciar um serviço específico
docker-compose restart web
```

## Executando sem Docker

Se preferir executar localmente sem Docker:

```bash
# Instalar dependências
uv sync

# Aplicar migrações
uv run python manage.py migrate

# Iniciar servidor
uv run python manage.py runserver
```

## Estrutura do Projeto

- `config/` - Configurações do Django
- `users/` - App de usuários
- `manage.py` - Script de gerenciamento do Django
- `pyproject.toml` - Dependências do projeto (gerenciadas pelo uv)

## Admin

Acesse o painel admin em: `http://localhost:9000/admin`
