
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

## Como executar localmente

### 1. (Opcional) Criar ambiente virtual
```bash
python -m venv .venv
source .venv/bin/activate       # Linux/Mac
.venv\Scripts\activate          # Windows
