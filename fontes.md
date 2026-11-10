# Fontes dos dados

Toda cifra usada nos roteiros entra aqui com fonte, data e link. Ainda vazio.

Fontes candidatas: IBGE (municípios, população, frota), Senatran/Denatran (frota de veículos), ANP (postos e combustíveis), ANTT (transporte), ONS e Aneel (energia), ANA e SNIS (água e saneamento), Anatel (telecom).

## Conjuntos de dados identificados (10/11/2026; nenhuma cifra extraída ainda)
- IBGE, recortes metropolitanos e aglomerações urbanas (composição por município, arquivos de 2025 corrigidos em 16/06/2026): https://www.ibge.gov.br/geociencias/organizacao-do-territorio/divisao-regional/18354-recortes-metropolitanos-e-aglomeracoes-urbanas.html
- Senatran, frota por município e tipo: https://www.gov.br/transportes/pt-br/assuntos/transito/conteudo-Senatran/frota-de-veiculos-2023
- ANP, dados cadastrais dos revendedores varejistas de combustíveis automotivos: https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/dados-cadastrais-dos-revendedores-varejistas-de-combustiveis-automotivos

## Vídeo 1: combustível (levantado em 10/11/2026)
Tabela completa, com todas as cifras por região: `videos/01-combustivel/ranking.csv`. Cálculo: `videos/01-combustivel/calculo/`.

| Dado | Fonte | Referência | Link |
|---|---|---|---|
| Composição das RMs e RIDEs | IBGE, Composicao_RM_2025_v2 | 2025, versão corrigida | https://geoftp.ibge.gov.br/organizacao_do_territorio/estrutura_territorial/municipios_por_regioes_metropolitanas/Situacao_2020a2029/Composicao_RM_2025_v2.xls |
| População por município | IBGE, Censo 2022 (população total, 2ª apuração) | 22/12/2023 | https://ftp.ibge.gov.br/Censos/Censo_Demografico_2022/Populacao_e_domicilios_Primeiros_resultados/Resultados_da_2a_apuracao_20231027/CD2022_Populacao_Coletada_Imputada_e_Total_Municipio_e_UF_20231222.xlsx |
| Frota por município e tipo | Senatran | setembro/2026 | https://www.gov.br/transportes/pt-br/assuntos/transito/conteudo-Senatran/frota-de-veiculos-2026-2/Frota_por_municipio_e_tipo_Setembro_2026.xlsx/@@download/file |
| Postos (revendedores varejistas) | ANP, dados cadastrais | arquivo baixado em 10/11/2026 | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-dados-cadastrais-dos-revendedores-varejistas-de-combustiveis-automotivos/dados-cadastrais-revendedores-varejistas-combustiveis-automoveis.csv |
| Combustível armazenado (tancagem autorizada) | ANP, tancagem do abastecimento nacional | 30/10/2026 | https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/arquivos-tancagem-do-abastecimento-nacional-de-combustiveis/dados-abertos/2026/outubro.csv |
| Km de trilhos por modo e UF | ANPTrilhos, Balanço do Setor 2025 (gráfico 10, IN-002-a) e tabela 1 (sistemas por recorte) | 31/12/2025 | https://anptrilhos.org.br/wp-content/uploads/2026/04/anptrilhos-balanco-setor-2025-5.pdf |
| VLTs da CBTU (Natal, João Pessoa, Maceió, Recife) são a diesel | CBTU, especificação técnica de VLTs (consulta pública 2026) | 2026 | https://www.gov.br/cbtu/pt-br/acesso-a-informacao/participacao-social-1/audiencia-e-consultas-publicas/consulta-publica-2026/01.4.Especificaes_Tcnicas_VLTs.pdf |
| VLTs do Ceará (Oeste, Parangaba-Mucuripe, Cariri, Sobral) não são eletrificados | O Povo, 30/07/2024 | 2024 | https://www.opovo.com.br/noticias/ceara/2024/07/30/amp/e-metro-ou-vlt-entenda-a-diferenca-dos-meios-de-transporte-sobre-trilhos-no-ceara.html |
| VLT de Teresina é a diesel | Railway Gazette (trens diesel Marcopolo para Teresina) | — | https://www.railwaygazette.com/traction-and-rolling-stock/marcopolo-rail-to-supply-dmus-for-teresina-suburban-rail/69754.article |

Km elétricos por região (ANPTrilhos 2025): RM São Paulo 377,4 (trem 273,2 + metrô 89,7 + monotrilho 14,5); RM Rio de Janeiro 285,9; RM Porto Alegre 42,9; RIDE DF 42,4; RM Recife 37,7 (metrô); RM Salvador 34,4; RM Belo Horizonte 28,1; RM Fortaleza 24,1 (metrô Linha Sul); RM Baixada Santista 19,5 (VLT elétrico). O VLT de Salvador (4 km, 2026) não entra porque a referência é 2025.

Cifras citadas no roteiro (todas em `ranking.csv`):
- Totais das 50 regiões: 109,7 milhões de habitantes; 74,3 milhões de veículos com motor; 18.522 postos.
- Piracicaba (1º): 1.519.024 hab.; 1.331.911 veículos; 876,8 por mil hab.; 338 postos; 3.940,6 veículos/posto; 0 km; 1.737 m³ (1,3 L/veículo).
- Curitiba: 954,7 veículos/mil hab. (maior); 5.269,6 por posto; 1.193.997 m³.
- Belo Horizonte: 6.205,1 veículos por posto (maior); 28,1 km; 5.128.282 hab.
- São Paulo: 6.019,3 por posto; 16.294.302 veículos; 377,4 km.
- Rio de Janeiro: 285,9 km; 23,8 km por milhão; 5.017,8 por posto.
- Baixada Santista: 2.711.396 m³ (2.524 L/veículo, maior).
- Salvador (50º): 453,9 veículos/mil hab.; 34,4 km; 1.913.744 m³.
- Maceió: 419,5 veículos/mil hab. (menor).
- Sobral: 1.732,3 veículos por posto (menor).
