Apresentação — Notas para os Apresentadores (Speaker Notes)
Slide 1 — Introdução (Leonardo Melo Pelicano)

Explicar rapidamente o objetivo da A3.

Apresentar o problema do código legado: monolítico, confuso e difícil de manter.

Contextualizar por que a refatoração é necessária.

Slide 2 — Problemas Identificados (Carlos Eduardo dos Santos Junior)

Mostrar (ou citar) exemplos do código original.

Destacar problemas como:

condicionais muito grandes

duplicação de lógica

ausência de testes

mistura de responsabilidades

Enfatizar por que esse código é ruim para manutenção.

Slide 3 — Refatoração e Arquitetura (Pedro Henrique Hôrtencio de Oliveira)

Explicar a escolha dos padrões Strategy + Factory.

Mostrar como o conversor foi dividido em classes independentes.

Falar sobre as unidades base (Kelvin, Metro, Quilo) e por que isso facilita tudo.

Destacar como agora é fácil adicionar novas unidades.

Slide 4 — Testes (Leonardo)

(Como deixamos só 3 membros, Leonardo assume essa parte também — sem problemas)

Explicar que os testes foram implementados com pytest.

Mostrar (ou contar) que cobrimos:

temperatura

comprimento

peso

entradas inválidas

Explicar a importância dos testes na refatoração.

(Removi GitHub Actions, já que com 3 membros é opcional e não necessário para nota)

Slide 5 — Conclusão (Todos)

Cada um fala uma frase curta:

Leonardo: impacto de Clean Code no projeto.

Carlos: como o código ficou mais simples de evoluir.

Pedro: o que poderia ser melhorado em versões futuras.
