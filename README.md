
# UniversalConverter – Projeto A3 Completo

Este repositório contém todo o projeto completo e totalmente estruturado da atividade A3:

- `codigo-original/` : código legado propositalmente confuso (versão “antes”)
- `codigo-refatorado/` : pacote limpo, modular e organizado utilizando os padrões Strategy e Factory
- `Relatorio_A3_detalhado.pdf` : relatório completo do projeto (na raiz)
- `Apresentacao_speaker_notes.md` : orientações do que cada membro pode falar na apresentação
- `tests/` : suíte de testes unitários usando PyTest

## Funcionalidades
- Conversões entre Temperatura, Comprimento e Peso
- Uso de unidades canônicas internas (Kelvin, Metro e Quilograma)
- Separação clara de responsabilidades (SOLID)
- Interface de linha de comando (CLI) e endpoint opcional em Flask
- Testes unitários completos cobrindo múltiplos cenários

## Grupo e Linha do Tempo de Desenvolvimento

- **GRUPO:**

- **Leonardo Melo Pelicano - 823127961**
- **Pedro Henrique Hortêncio de Oliveira- 823117300**
- _Carlos Eduardo dos Santos Junior-823125602_

  ---

- **15/09 – Início do projeto e criação do código legado**
- **20/09 – Implementação das versões iniciais do código original**
- **30/09 – Publicação do código original no GitHub**
- **05/10 – Início da refatoração (Strategy, Factory e organização modular)**
- **10/10 – Implementação das classes de conversão**
- **17/10 – Implementação da fábrica de conversores**
- **25/10 – Criação do serviço central de conversão**
- **03/11 – Implementação da CLI**
- **12/11 – Criação dos testes unitários**
- **20/11 – Documentação e organização do repositório**
- **26/11 – Conclusão e entrega final do projeto**

## Como executar localmente

### 1. (Opcional) Criar ambiente virtual
```bash
python -m venv .venv
source .venv/bin/activate       # Linux/Mac
.venv\Scripts\activate          # Windows
