Notas de Apresentação (Speaker Notes)

Este documento descreve a divisão dos slides e os pontos principais que cada integrante apresentará durante a apresentação do projeto.

Slide 1 — Introdução (Leonardo Melo Pelicano)

-Explicar o objetivo geral da A3.
-Destacar a importância de Clean Code e boas práticas.
-Apresentar o contexto do código original: estrutura monolítica e difícil manutenção.
-Introduzir a motivação para realizar a refatoração.

Slide 2 — Problemas Identificados (Carlos Eduardo dos Santos Junior)

-Apontar os principais problemas do código original.

Destacar:
-Condicionais aninhadas.
-Funções extensas e sem responsabilidade única.
-Ausência de testes.
-Mistura de lógica, prints e validações.
-Explicar como esses problemas dificultavam evolução e manutenção.

Slide 3 — Refatoração e Arquitetura (Pedro Henrique Hôrtencio de Oliveira)

-Explicar a utilização dos padrões Strategy e Factory.
-Apresentar como o código foi modularizado em classes e pacotes.
-Comentar sobre o uso de unidades base (Kelvin, Metro, Quilograma).
-Mostrar como a nova arquitetura facilita a extensão do sistema.

Slide 4 — Testes Unitários (Leonardo Melo Pelicano)

-Explicar que os testes foram implementados com pytest.
-Apresentar o que foi testado:
-Conversões de temperatura.
-Conversões de comprimento.
-Conversões de peso.
-Tratamento de valores inválidos.
-Reforçar a importância dos testes para garantir comportamento do código refatorado.

Slide 5 — Conclusão (Todos os Membros)

-Leonardo: comentar o impacto da refatoração e das boas práticas no resultado final.
-Carlos: destacar como o código ficou mais limpo e fácil de manter.
-Pedro: sugerir melhorias futuras (novas unidades, interface, mais testes).
