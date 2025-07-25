# 📋 Cadastro de Usuários - Área de TI

Este projeto é uma aplicação web desenvolvida com **Django**, **Bootstrap** e **SQLite** que permite cadastrar, visualizar, editar e excluir usuários atuantes em diferentes áreas da Tecnologia da Informação.

---

## 🖥️ Funcionalidades

- ✅ Cadastro de novos usuários com nome, sobrenome, e-mail e área de atuação.
- 📄 Listagem de todos os usuários cadastrados.
- ✏️ Edição de usuários já existentes.
- ❌ Exclusão de usuários com confirmação.
- 🆔 Identificadores únicos via **UUID**.
- 🎨 Interface responsiva com Bootstrap.

---

## 📌 Tecnologias Utilizadas

- [Django](https://www.djangoproject.com/) – Framework web principal.
- [SQLite](https://www.sqlite.org/index.html) – Banco de dados relacional leve usado por padrão.
- [UUIDField](https://docs.djangoproject.com/en/stable/ref/models/fields/#uuidfield) – Campo utilizado como chave primária no modelo de usuário.
- [Bootstrap 4.3.1](https://getbootstrap.com/docs/4.3/getting-started/introduction/) – Framework de estilização responsiva.
- [HTML5](https://developer.mozilla.org/pt-BR/docs/Web/HTML) e [CSS3](https://developer.mozilla.org/pt-BR/docs/Web/CSS) – Estrutura e estilo da aplicação.
- [Icons8](https://icons8.com/) – Ícones para ações na interface.

---

## 📷 Layout da Aplicação

### ✅ Cadastro de Usuários
Formulário com campos para nome, sobrenome, e-mail e seleção da área de atuação em TI.

### 📄 Listagem de Usuários
Tabela exibindo os dados de todos os usuários com botões para editar ou excluir.

### ✏️ Edição e ❌ Exclusão
- Formulário com os dados pré-preenchidos para edição.
- Página de confirmação antes de excluir.

---

## 🧭 Navegação

- **`/`** → Página de cadastro de usuário.
- **`/usuarios/`** → Página de listagem de usuários.
- **`/editar/<uuid>`** → Página de edição de usuário.
- **`/excluir/<uuid>`** → Página de confirmação de exclusão.

> As rotas utilizam URLs nomeadas do Django: `home`, `listagem_usuarios`, `editar_usuario`, `excluir_usuario`.

---

## 🚀 Como Executar o Projeto Localmente

1. **Clone o repositório**:
   ```bash 
   git clone https://github.com/IsisMarieli/Cadastro-usuarios.git

   cd cadastro_usuarios

   python .\manage.py runserver