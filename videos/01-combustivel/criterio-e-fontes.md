# 1º vídeo: critério do ranking e fontes (proposta para aprovação)

Status: **proposta**, aguardando aprovação do Bruno (10/11/2026). Nenhum número foi levantado ainda.

## 1. Quem entra no ranking
- As **50 regiões metropolitanas mais populosas**, pela composição oficial do IBGE (arquivo de 2025, corrigido em 16/06/2026) e pela população do Censo 2022.
- Entram também as **RIDEs**. Sem elas, Brasília e Teresina ficam de fora.
- Ficam de fora as aglomerações urbanas, que são só três e não são regiões metropolitanas.
- Cálculo: somar a população dos municípios de cada RM, ordenar e pegar as 50 primeiras.

## 2. O que mede "parar primeiro" (Índice Pare Tudo)
Não é uma simulação. É uma medida de **quanto a região depende de combustível nas ruas e de quanta folga ela tem**. São quatro indicadores, todos por RM:

| # | Indicador | Por que importa | Fonte |
|---|---|---|---|
| A | Veículos por 1.000 habitantes | Quanto mais carros e motos por pessoa, mais a rotina depende do posto | Senatran (frota por município) ÷ IBGE (Censo 2022) |
| B | Veículos por posto de combustível | Mais veículos por posto = filas e tanques vazios mais cedo | Senatran ÷ ANP (cadastro de revendedores varejistas) |
| C | Km de metrô, trem ou VLT por milhão de habitantes | Os trilhos são elétricos e continuam rodando sem diesel nem gasolina | ANPTrilhos / operadores |
| D | Distância até a base de distribuição de combustível mais próxima | Quanto mais longe a base, mais demora o reabastecimento | ANP (bases de distribuição autorizadas) |

- Cada RM recebe uma posição de 1 a 50 em cada indicador. A nota final é a **média das quatro posições**, com pesos iguais, o que é simples de explicar no vídeo.
- Desempate: o indicador B (veículos por posto).
- Se o indicador D for difícil de medir de forma confiável, sai, e o índice fica com A, B e C.

## 3. Como explicar no vídeo (rascunho de 2 frases)
"Não dá para prever o futuro, mas dá para medir quem depende mais do tanque cheio. Juntamos quatro dados oficiais: carros por habitante, carros por posto, trilhos elétricos e distância até o combustível."

## 4. Arquivos a baixar (com data de referência)
- IBGE: composição das RMs/RIDEs (2025, versão corrigida) e população municipal do Censo 2022.
- Senatran: frota por município e tipo (mês mais recente disponível).
- ANP: dados cadastrais dos revendedores varejistas e bases de distribuição.
- ANPTrilhos: extensão das redes de passageiros por região.

## 5. Perguntas para o Bruno
1. Aprova os quatro indicadores com peso igual?
2. Inclui as RIDEs (Brasília, Teresina)?
3. Conta motos na frota ou só automóveis?
