# 🎉 LocaFesta — Sistema de Gestão de Aluguel de Equipamentos para Festas e Eventos

## 📑 Índice

- [Descrição do Projeto](#-descrição-do-projeto)
- [Principais Funcionalidades](#️-principais-funcionalidades)
- [Regras e Padrões de Desenvolvimento](#-regras-e-padrões-de-desenvolvimento)
- [Padrões de Comentários](#-padrões-de-comentários)
- [Boas Práticas na Codificação](#-boas-práticas-na-codificação)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Orientador](#-orientador)
- [Autores](#-autores)

## 📘 Descrição do Projeto

A **LocaFesta** é uma empresa especializada no aluguel de equipamentos para festas e eventos, como mesas, tendas e sistemas de iluminação. Atualmente, a empresa enfrenta desafios significativos devido ao controle manual de agendamentos e estoque, resultando em conflitos de reserva, perdas de equipamentos por falta de manutenção e atrasos no atendimento ao cliente.

## 🛠️ Principais Funcionalidades

- Autenticação Segura: Sistema de login com validação para acesso diferenciado de funcionários e administradores.
- Gestão de Funcionários: Possibilidade de cadastrar novos funcionários.
- Gerenciamento de Clientes: Permite adicionar, editar, excluir e consultar informações de clientes.
- Controle de Equipamentos: Permite adicionar, editar, excluir e consultar informações de equipamentos disponíveis.
- Gerenciamento de Reservas: Permite adicionar, editar, excluir e consultar reservas feitas por clientes para determinado equipamento.

**Obs:** A exclusão só pode ser realizada por um perfil de Administrador!

## 📏 Regras e padrões de Desenvolvimento

Esta seção foi criada para garantir organização e consistência no uso do GitHub e no desenvolvimento do projeto.

    🗂️ Estrutura de Pastas
        - Diagramas/: Armazena todos os diagramas do projeto.
        - Padrões Adotados/: Contém os padrões utilizados para nomenclatura dos requisitos e regras para elaboração do Documento de Requisitos.
        - Projeto/: Pasta destinada a todo o código-fonte do sistema.
        - Requisitos/: Armazena o Documento de Requisitos, incluindo os Requisitos Funcionais (RF) e Não Funcionais (RNF).
        - Testes/: Contém os testes realizados no sistema.

- Os nomes dos commits devem ser completos e seguir o padrão que encontramos [nesse repositório](https://github.com/iuricode/padroes-de-commits);

## 💬 Padrões de comentários

- Comentários devem ser curtos, claros e objetivos.
- Comentar blocos de código complexos ou que envolvam lógica importante.
- Toda função deve conter um comentário explicando sua finalidade.

## 🧠 Boas Práticas na Codificação

- A branch principal do projeto é a master. Ela deve conter apenas o código estável e testado.
- Para alteração no projeto crie uma nova branch de desenvolvimento seguindo o padrão:
    - feature/nome-da-funcionalidade
    - fix/nome-do-bug
    - improvement/nome-da-melhoria
- Declarar variáveis no início das funções sempre que possível.
- Usar nomes de variáveis descritivos que representem bem seu conteúdo, utilizando PascalCase para Classes e camelCase para os demais tipos de variáveis e funções.
- Indentar o código corretamente para manter a legibilidade.
- Evitar duplicação de código (SRP - SOLID).
- Antes de fazer push, garantir que a branch de desenvolvimento esteja atualizada com a main.

## 💻 Tecnologias Utilizadas

- HTML: HTML5
- CSS: CSS3
- JavaScript: ECMAScript 2024 (ES15)
- Bootstrap: 5.3.6
- Python: 3.13.2
- MySQL: 8.0.41
- Servidor Local: Utilização de servidor local (localhost) para testes do aplicativo.
- Ambiente de Desenvolvimento: Visual Studio Code versão 1.100.0

## 👨‍🏫 Orientador

Prof. Antônio Maria Pereira de Resende — UFLA

> Projeto desenvolvido para o Trabalho Prático Final da disciplina GCC188 - Engenharia de Software da Universidade Federal de Lavras.

## 👥 Autores

| [<img src="https://avatars.githubusercontent.com/u/136363953?v=4" width="100px"><br><sub>@DPontello</sub>](https://github.com/DPontello) | [<img src="https://avatars.githubusercontent.com/u/109813431?v=4" width="100px"><br><sub>@luapxb</sub>](https://github.com/luapxb) | [<img src="https://avatars.githubusercontent.com/u/123120658?v=4" width="100px"><br><sub>@SamuVanoni</sub>](https://github.com/SamuVanoni) |
| :---: | :---: | :---: |