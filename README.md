# Controle de Gastos - Backend API

Uma API REST desenvolvida em Django para controle de gastos pessoais.

## Funcionalidades

- **Autenticação de Usuários**: Sistema de login e registro
- **Gestão de Categorias**: Criar e gerenciar categorias para gastos e receitas
- **Controle de Gastos**: Registrar, editar e visualizar gastos
- **Controle de Receitas**: Registrar, editar e visualizar receitas
- **API REST**: Endpoints completos para todas as operações

## Tecnologias Utilizadas

- **Django**: Framework web principal
- **Django REST Framework**: Para criação da API REST
- **SQLite**: Banco de dados (pode ser alterado para PostgreSQL em produção)
- **Python 3.x**: Linguagem de programação

## Instalação Local

1. Clone o repositório:
```bash
git clone https://github.com/Scsant/ControleGastosBackend.git
cd ControleGastosBackend
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
```

3. Instale as dependências:
```bash
pip install -r requirements.txt
```

4. Execute as migrações:
```bash
python manage.py makemigrations
python manage.py migrate
```

5. Crie um superusuário:
```bash
python manage.py createsuperuser
```

6. Execute o servidor:
```bash
python manage.py runserver
```

## Endpoints da API

### Autenticação
- `POST /api/auth/login/` - Login
- `POST /api/auth/logout/` - Logout
- `POST /api/auth/register/` - Registro

### Categorias
- `GET /api/categorias/` - Listar categorias
- `POST /api/categorias/` - Criar categoria
- `GET /api/categorias/{id}/` - Detalhes da categoria
- `PUT /api/categorias/{id}/` - Atualizar categoria
- `DELETE /api/categorias/{id}/` - Deletar categoria

### Gastos
- `GET /api/gastos/` - Listar gastos
- `POST /api/gastos/` - Criar gasto
- `GET /api/gastos/{id}/` - Detalhes do gasto
- `PUT /api/gastos/{id}/` - Atualizar gasto
- `DELETE /api/gastos/{id}/` - Deletar gasto

### Receitas
- `GET /api/receitas/` - Listar receitas
- `POST /api/receitas/` - Criar receita
- `GET /api/receitas/{id}/` - Detalhes da receita
- `PUT /api/receitas/{id}/` - Atualizar receita
- `DELETE /api/receitas/{id}/` - Deletar receita

## Estrutura do Projeto

```
meu_controle_gastos/
├── manage.py
├── requirements.txt
├── meu_controle_gastos/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── usuarios/
│   ├── models.py
│   ├── views.py
│   └── admin.py
└── financas/
    ├── models.py
    ├── serializers.py
    ├── views.py
    ├── urls.py
    └── admin.py
```

## Deploy

Este projeto pode ser facilmente deployado em plataformas como:

- **Heroku**
- **Railway**
- **PythonAnywhere**
- **DigitalOcean**
- **AWS**

## Contribuição

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença

Este projeto está sob a licença MIT.
