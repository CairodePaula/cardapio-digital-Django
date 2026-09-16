# Cardápio Digital com Comanda por Mesa

Projeto acadêmico em Django + PostgreSQL. Implementa o **P1**: cadastro de
pratos, combos e mesas; abertura de comanda; adição de itens; alteração de
quantidade; cálculo de subtotal/total; fechamento da conta.

**Autor:** Cairo de Paula Cunha Gomes

## Estrutura

```
config/         -> configurações do projeto (settings, urls raiz)
restaurante/    -> model Mesa
cardapio/       -> models Prato e Combo, views de listagem
comandas/       -> models Comanda e ItemComanda, lógica de abrir/fechar conta
templates/      -> HTML de todas as páginas
```

## Como rodar

```bash
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Crie o banco no PostgreSQL e copie o `.env.example` para `.env`, ajustando usuário/senha:

```sql
CREATE DATABASE cardapio_db;
```
```bash
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser   # para acessar o Admin
python manage.py runserver
```

## Como usar o sistema

1. Em `/admin/`, cadastre **Mesas**, **Pratos** e (opcional) **Combos**.
2. Acesse `/restaurante/mesas/` e clique em **"Abrir comanda"** em uma mesa.
3. Na tela da comanda, adicione pratos/combos, altere quantidades, remova itens.
4. Clique em **"Fechar comanda"** para fechar a conta (o total é calculado automaticamente a cada item).

## Mapeamento com os requisitos (P1)

| # | Requisito                          | Onde está implementado                                 |
|---|-------------------------------------|------------------------------------------------------------|
| 1 | Cadastro de pratos                  | Django Admin (`cardapio/admin.py`)                          |
| 2 | Cadastro de combos                  | Django Admin (`cardapio/admin.py`)                          |
| 3 | Cadastro de mesas                   | Django Admin (`restaurante/admin.py`)                       |
| 4 | Abertura de comanda por mesa        | `comandas/views.py -> abrir_comanda`                        |
| 5 | Adição de pratos/combos à comanda   | `comandas/views.py -> adicionar_prato/adicionar_combo`      |
| 6 | Alteração de quantidade             | `comandas/views.py -> alterar_quantidade`                   |
| 7 | Cálculo do subtotal                 | `comandas/models.py -> ItemComanda.subtotal`                 |
| 8 | Cálculo do total da comanda         | `comandas/models.py -> Comanda.total`                        |
| 9 | Fechamento da conta                 | `comandas/views.py -> fechar_comanda`                        |
| 10| Comanda fica "fechada" após fechar  | `comandas/models.py -> Comanda.fechar()`                     |

## Problemas comuns

- **Faltando o Django / erro de import:** esqueceu de ativar o venv (`source venv/bin/activate`). Confira se o prompt mostra `(venv)`.
- **Erro lendo `SECRET_KEY`:** rode os comandos de dentro de `cardapio_digital/cardapio_digital/`, onde ficam `manage.py` e `.env`.
- **Erro de conexão com o banco:** confirme se o serviço do PostgreSQL está rodando (`pg_ctl status` ou `sudo service postgresql status`).
- **"Address already in use" na porta 8000:** feche o servidor antigo ou rode em outra porta: `python manage.py runserver 8001`.
- **Erro 405 no logout do admin:** use o botão "Sair" da tela do admin em vez de digitar `/admin/logout/` direto na URL (ela só aceita POST).

## Próximos passos (P2, ainda não implementado)

- Entidade Restaurante e multi-tenant (múltiplos restaurantes, mesas/pratos/combos vinculados a cada um).
- Vincular usuários/login a restaurantes específicos.
- Views filtrando tudo pelo restaurante do usuário logado.
- Atualização em tempo real da comanda (Django Channels ou polling via JS).
- API REST com Django REST Framework para os mesmos recursos.
