# Briefing: canal Pare Tudo

Cole este texto no início da conversa nova.

## Contexto
Pare Tudo é um canal novo do YouTube sobre cidades brasileiras, separado do Cine Comics. O dono é o Bruno. Repositório: github.com/BrunoFooFighters/pare-tudo (ler `CLAUDE.md`, `projeto.md` e `andamento.md` antes de começar). Mídias pesadas ficam no Google Drive, pasta "Pare Tudo" (https://drive.google.com/drive/folders/1vaR4iFqMuBx4UHDIwEt0BVN04o42sP8f).

## Estrutura base do título (o padrão do canal)
"Se [X] ficasse sem [recurso], estas seriam as primeiras a parar — o ranking das 50 [unidades]"

- [X]: o sistema ou serviço que falha (os postos de gasolina, a energia elétrica, a água encanada, a internet).
- [recurso]: o que falta (combustível, energia, água, sinal). Quando o X já é o recurso, a frase fica "Se a energia elétrica acabasse".
- [unidades]: o que é ranqueado. Exemplo: "das 50 maiores cidades do Brasil".
- Sempre com "estas seriam as primeiras a parar" e o travessão antes de "o ranking das 50".

Primeiro vídeo: "Se os postos de gasolina ficassem sem combustível, estas cidades seriam as primeiras a parar — o ranking das 50 maiores do Brasil"
Segundo (sugestão): "Se a energia elétrica acabasse, estas cidades seriam as primeiras a parar — o ranking das 50 maiores do Brasil"
Futuros possíveis: água encanada, internet e celular, gás de cozinha, transporte público.

## Decisão em aberto: a unidade do ranking
O Brasil tem 5.570 municípios (50 cidades é viável), mas só 26 estados + DF. Opções: cidades (50), capitais (27), estados + DF (27), regiões metropolitanas (~50), locais específicos (aeroportos, portos, hospitais). Recomendação: cidades, para manter o "50". O Bruno ainda não escolheu.

## Formato do vídeo
- ~10 minutos, roteiro de 1.400 a 1.600 palavras.
- Ranking de 50 itens, contado do menos para o mais dependente (ou o inverso), com explicação do critério no início.
- Narrado com a voz clonada do Bruno (ferramenta de voz provavelmente Speko; confirmar ferramenta e voz salva).

## Regras de conteúdo
- Dados reais e citados. Nada inventado. Toda cifra usada tem a fonte registrada em `fontes.md`.
- Fontes candidatas: IBGE, Senatran/Denatran, ANP, ANTT (combustível); ONS, Aneel (energia); ANA, SNIS (água); Anatel (telecom).
- Explicar o critério do ranking de forma simples e honesta, sem exagero sensacionalista.

## Entregas por vídeo
1. Roteiro (~10 min)
2. Narração com a voz do Bruno
3. Thumbnail 1280x720
4. Material de postagem (título, descrição, tags)

## Entregas únicas do canal
- Banner 2560x1440 (área segura 1546x423)
- Avatar 800x800

## Pendências
1. Bruno escolher a unidade do ranking e confirmar o título do 2º vídeo.
2. Confirmar a ferramenta de voz e a voz clonada.
3. Depois: propor o critério do ranking e a lista de dados com fontes, para aprovação, e só então escrever o roteiro do 1º vídeo.

## Como trabalhar
- Tudo fica salvo no repositório pare-tudo; ao fim de cada etapa atualizar `andamento.md`, commit e push em `main`.
- Roteiros em `videos/<nome-do-video>/`.
