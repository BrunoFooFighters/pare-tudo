# 1º vídeo: critério do ranking e fontes (proposta para aprovação)

Status: **aprovado** pelo Bruno em 10/11/2026 ("Aprovado. Pode iniciar."). Ranking calculado em `ranking.csv`; scripts em `calculo/`.

## Ajustes feitos no cálculo (10/11/2026)
- **Respostas padrão adotadas**: pesos iguais; RIDEs entram (e também a RAIDE Petrolina/Juazeiro, que é do mesmo tipo); motos entram na frota.
- **Frota**: veículos com motor = total da Senatran menos reboque, semirreboque, side-car e bonde.
- **Indicador C**: só trilhos **elétricos** (metrô, trem urbano, monotrilho e os VLTs elétricos do Rio e da Baixada Santista). Os VLTs do Nordeste (CBTU, Metrofor, Teresina) andam a diesel e parariam junto. Linhas atribuídas ao recorte que a ANPTrilhos usa (o TIC Trens conta para a RM de São Paulo, não para Jundiaí).
- **Indicador D trocado**: a distância até a base exigiria coordenadas e rotas e não seria confiável. Virou **combustível armazenado dentro da região** (tancagem autorizada da ANP em bases de distribuição, terminais e refinarias, grupo "derivados e biocombustíveis"), em litros por veículo. Mede a mesma ideia: quanto de reserva existe perto.
- **Sobreposições do IBGE**: a RM do Norte/Nordeste Catarinense saiu (seus municípios estão nas RMs de Joinville, Jaraguá do Sul e Planalto Norte, criadas pela LC 788/2021); a RM do Entorno do DF saiu (todos os 11 municípios estão na RIDE do DF); Timon fica na RIDE da Grande Teresina; Lagoa da Confusão fica na RM de Palmas. Colares, áreas de expansão e entornos metropolitanos não entram.
- **Empates**: 41 regiões não têm trilho elétrico e dividem a posição média no indicador C (21º). Regiões sem armazenagem dividem a posição 4,5 no D.

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
