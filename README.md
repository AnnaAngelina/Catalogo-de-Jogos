# Playlist — Catálogo de Jogos

Projeto desenvolvido para a atividade prática de **Programação para Internet**.

## Tema

Catálogo de Jogos.

## Tecnologias utilizadas

- Python
- Django 5
- SQLite
- HTML e CSS

## Modelos

O projeto possui três modelos:

- **Jogo:** armazena nome, descrição, ano de lançamento, desenvolvedora e plataforma.
- **Desenvolvedora:** armazena o nome da empresa responsável pelo jogo.
- **Plataforma:** armazena o nome da plataforma em que o jogo está disponível.

Cada jogo possui relacionamento com uma desenvolvedora e uma plataforma por meio de `ForeignKey`.

## Funcionalidades

- Listagem dos jogos cadastrados, mostrando nome, descrição, ano, desenvolvedora e plataforma.
- Pesquisa pelo nome do jogo. A consulta utiliza `nome__icontains`.
- Filtro por desenvolvedora.
- Filtro por plataforma.
- Os dois filtros podem ser usados separadamente ou junto com a pesquisa.
- Paginação com 5 jogos por página.
- Os parâmetros de pesquisa e filtros são mantidos nos links de navegação entre páginas.

## Como executar o projeto

É necessário ter Python instalado.

1. Extraia o arquivo ZIP e abra a pasta `catalogo_jogos` no terminal.
2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   ```

   No Linux:

   ```bash
   source venv/bin/activate
   ```

   No Windows:

   ```bash
   venv\Scripts\activate
   ```

3. Instale o Django:

   ```bash
   pip install -r requirements.txt
   ```

4. Crie as tabelas e cadastre os dados iniciais:

   ```bash
   python manage.py migrate
   ```

   A migração inicial cria os modelos e insere 24 jogos, 6 desenvolvedoras e 4 plataformas.

5. Inicie o servidor:

   ```bash
   python manage.py runserver
   ```

6. Acesse no navegador:

   http://127.0.0.1:8000/

## Django Admin

Os modelos também estão registrados no painel administrativo. Para acessar, crie um superusuário:

```bash
python manage.py createsuperuser
```

Depois, entre em:

http://127.0.0.1:8000/admin/

## Organização das pastas

```text
catalogo_jogos/
├── catalogo_jogos/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── jogos/
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── templates/
│   │   └── jogos/
│   │       └── listar_jogos.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   └── views.py
├── static/
│   └── css/
│       └── style.css
├── templates/
│   └── base.html
├── manage.py
└── requirements.txt
```