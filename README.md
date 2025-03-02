# Arquitetura Hexagonal

Objetivos: os objetivos dessa arquitetura é separar regras de negócio das dependências externas,
tornando o sistema mais modular, testável e flexível.

Ports: interfaces que definem como o domínio se comunica com o mundo externo

Adapter: são as implementações dessas interfaces

📌 Por que usar a Arquitetura Hexagonal?

    Desacoplamento: A lógica de negócio não depende diretamente de frameworks, bancos de dados ou APIs externas.

    Testabilidade: Como a lógica está isolada, fica mais fácil criar testes unitários e mocks para dependências externas.

    Flexibilidade: Você pode mudar a camada de persistência (banco de dados) ou a interface de entrada (HTTP, CLI, eventos) sem impactar a lógica principal.

## Estrutura do projeto

```
/seu_projeto
│── app/
│   │── core/                # Regras de negócio (Aplicação)
│   │   ├── services/        # Casos de uso (regras de negócio)
│   │   ├── models/          # Modelos de entidades (domain models)
│   │   ├── repositories/    # Interfaces dos repositórios
│   │── infrastructure/      # Implementações das interfaces
│   │   ├── db/              # Conexões com banco de dados
│   │   ├── repositories/    # Repositórios concretos (implementações)
│   │   ├── external_apis/   # Comunicação com APIs externas
│   │── adapters/            # Adaptadores (Entrada e Saída)
│   │   ├── api/             # Controllers e Rotas FastAPI
│   │   ├── cli/             # Interface via terminal
│   │── config.py            # Configurações do projeto
│   │── main.py              # Ponto de entrada da aplicação
│── tests/                   # Testes unitários e de integração
│── requirements.txt         # Dependências do projeto
│── Dockerfile               # Arquivo Docker para containerização
```
