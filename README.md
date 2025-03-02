# Arquitetura Hexagonal no FastAPI

Este projeto implementa a **Arquitetura Hexagonal** com **FastAPI**, separando claramente **regras de negócio** de **dependências externas**. Isso torna o sistema **modular, testável e flexível**.

---

## 🔥 **Objetivo da Arquitetura Hexagonal**
A Arquitetura Hexagonal (Ports & Adapters) busca desacoplar as regras de negócio das tecnologias externas, permitindo:

✅ **Modularidade** → Separação clara entre domínio e infraestrutura  
✅ **Testabilidade** → Facilidade para criar testes unitários e mocks  
✅ **Flexibilidade** → Possibilidade de trocar banco de dados, APIs externas ou interface de usuário sem afetar o núcleo do sistema  

---

## 🚀 **Conceitos da Arquitetura Hexagonal**
A arquitetura se baseia em dois conceitos principais:

### 🔹 **Ports (Portas)**
Interfaces que definem **como** o domínio se comunica com o mundo externo. Elas garantem que as regras de negócio permaneçam independentes da implementação concreta.

- **Exemplo:** `order_repository.py` define uma interface para persistência de pedidos.

### 🔸 **Adapters (Adaptadores)**
São as implementações concretas das **Ports**. Eles traduzem chamadas externas para o formato esperado pelo domínio.

- **Exemplo:** `order_repository_concrete.py` implementa a interface e salva pedidos no banco de dados.

---

## 📂 **Estrutura do Projeto**

```
├── app
│   ├── adapter
│   │   ├── controller
│   │   │   ├── __init__.py
│   │   │   └── order_controller.py
│   │   ├── dto
│   │   │   ├── __init__.py
│   │   │   └── order_schema.py
│   │   └── __init__.py
│   ├── core
│   │   ├── __init__.py
│   │   ├── model
│   │   │   ├── __init__.py
│   │   │   └── order.py
│   │   ├── repository
│   │   │   ├── __init__.py
│   │   │   └── order_repository.py
│   │   └── service
│   │       ├── __init__.py
│   │       └── order_service.py
│   ├── infra
│   │   ├── db
│   │   │   ├── database.py
│   │   │   └── __init__.py
│   │   ├── __init__.py
│   │   └── repository_concrete
│   │       ├── __init__.py
│   │       └── order_repository_concrete.py
│   ├── __init_.py
│   ├── __init__.py
│   └── main.py
├── README.md
└── tests
│── requirements.txt         # Dependências do projeto
```
