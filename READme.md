### Curso Técnico de Desenvolvimento de Sistemas - Senai Itapeva

# API de Charadas - Backend com Flask

Este projeto representa o backend da aplicação **Charadas - Desafie sua mente!**, desenvolvido como parte do curso Técnico em Desenvolvimento de Sistemas no SENAI Itapeva. A API foi criada utilizando **Python** com o microframework **Flask**, integrando com o banco de dados **Firestore** do Firebase para armazenar e gerenciar as charadas.

## Status do Projeto
🚀 Projeto finalizado

## Índice
- [Funcionalidades](#funcionalidades)
- [Tecnologias Utilizadas](#tecnologias-utilizadas)
- [Aprendizados](#aprendizados)
- [Veja o Frontend](#veja-o-frontend)
- [Autor](#autor)
- [Licença](#licença)

## Funcionalidades
- [GET] `/charadas` → Retorna uma charada aleatória
- [GET] `/charadas/<id>` → Retorna uma charada específica por ID
- [POST] `/charadas` → Adiciona uma nova charada
- [PUT] `/charadas/<id>` → Atualiza uma charada existente
- [DELETE] `/charadas/<id>` → Exclui uma charada por ID
- Integração com Firestore para armazenamento e consulta de dados
- Suporte a CORS para permitir requisições do frontend

## Tecnologias Utilizadas

- ![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
- ![Flask](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)
- ![Firebase](https://img.shields.io/badge/Firebase-FFCA28?style=for-the-badge&logo=firebase&logoColor=black)

## 📚 Aprendizados
Durante o desenvolvimento deste backend, foram aprofundados conhecimentos em:
- Criação de APIs RESTful com **Flask**
- Integração com banco de dados **Firebase Firestore**
- Manipulação de rotas e métodos HTTP
- Tratamento de erros e respostas JSON
- Uso de variáveis de ambiente com `dotenv`
- Boas práticas em estruturação de código backend

## Veja o Frontend
Acesse o projeto funcionando em um frontend:  
👉 [https://front-end-charada-sigma.vercel.app/](https://front-end-charada-sigma.vercel.app/)

## Autor
- Gabriel Camargo - [GitHub](https://github.com/gabrielcamargogsilva) - gabriel.cgsilva.senai@gmail.com

## Licença
Este projeto está licenciado sob a Licença MIT - veja o arquivo LICENSE para mais detalhes.
