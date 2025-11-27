##Slide 1 — Introdução

Apresentador: Leonardo Melo Pelicano

Pontos-chave para falar:

Objetivo da A3: criar um código legado, depois refatorar com boas práticas.

Importância de Clean Code e manutenção de software.

Contexto inicial: código monolítico, confuso e difícil de evoluir.

Explicar que o objetivo é melhorar a qualidade sem mudar o comportamento.

Slide 2 — Problemas Identificados

Apresentador: Carlos Eduardo dos Santos Junior

Pontos-chave para falar:

Código original tinha diversos problemas estruturais:

Condicionais enormes (ifs aninhados).

Funções longas e de responsabilidade múltipla.

Ausência total de testes.

Mistura de cálculos, prints e validações.

Explicar por que isso dificulta manutenção, testes e evolução.

Reforçar necessidade real de refatoração.

##Slide 3 — Refatoração e Arquitetura

Apresentador: Pedro Henrique Hôrtencio de Oliveira

Pontos-chave para falar:

Decisão de utilizar os padrões Strategy + Factory.

Separação das conversões em classes individuais.

Uso de unidades base internas:

Kelvin

Metro

Quilograma

Como a nova estrutura facilita adicionar novos conversores.

Destaque: baixa dependência entre módulos.

##Slide 4 — Testes Unitários

Apresentador: Leonardo Melo Pelicano

Pontos-chave para falar:

Testes escritos com pytest.

O que foi coberto:

Temperatura

Comprimento

Peso

Casos inválidos

Importância dos testes na refatoração:

Garantir que comportamento antigo não foi quebrado.

Segurança para evoluir.

Código mais confiável.

##Slide 5 — Conclusão

Apresentadores: Todos os membros

Cada um fala uma frase curta:

Leonardo: reforçar o impacto do Clean Code e da arquitetura aplicada.

Carlos: comentar como o código se tornou mais legível e sustentável.

Pedro: falar brevemente sobre possíveis melhorias futuras (ex: interface web mais completa, mais unidades, testes extras).
