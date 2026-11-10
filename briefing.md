# Briefing para a próxima sessão (10/11/2026)

Cole na nova conversa: **"Leia o `briefing.md` e o `andamento.md` do repositório pare-tudo e continue de onde parou."**

## O que é
- **Pare Tudo**: canal do YouTube sobre cidades brasileiras. Repositório `BrunoFooFighters/pare-tudo`, push em `main`.
- Regras no `CLAUDE.md`:
  - dados reais com fonte em `fontes.md`;
  - roteiro com 1.400 a 1.600 palavras;
  - atualizar `andamento.md` e dar push a cada etapa;
  - alertar o Bruno para mandar `/compact` a cada 3 mensagens dele.
- Mídias ficam no Drive, na pasta **Pare Tudo**, subpasta `01-primeiro-video/`.

## Vídeo 1: combustível (`videos/01-combustivel/`)
- **Tema:** ranking das 50 maiores regiões metropolitanas por vulnerabilidade à falta de combustível.
- **Índice Pare Tudo:** média das posições em 4 indicadores (desempate pelo B):
  - A: veículos por mil habitantes (Senatran set/2026 + Censo 2022);
  - B: veículos por posto (ANP out/2026);
  - C: km de trilho **elétrico** por milhão de habitantes (ANPTrilhos 2025);
  - D: litros de combustível armazenado na região por veículo (tancagem ANP).
- **Resultado:**
  - Top 5: 1º Piracicaba, 2º Jundiaí, 3º Vale Europeu, 4º Sorocaba, 5º Joinville.
  - Último (50º): Salvador.
- **Arquivos:**
  - `roteiro.md`: v1, 1.562 palavras. **Falta o Bruno revisar.**
  - `narracao.txt`: 1.589 palavras, escrito como se fala, sem algarismos. É o texto para colar no VoiceStudio.
  - `ranking.csv`
  - `criterio-e-fontes.md`
  - `calculo/rm.py` e `calculo/indice.py`
- **Próximo vídeo:** e se faltasse energia elétrica?

## Pendências, em ordem
1. **Bruno revisa o roteiro.** Se mudar algo, refazer o `narracao.txt` junto.
2. **Narração com a voz clonada no VoiceStudio.**
   - Precisa de sessão **local** no PC do Bruno, porque a nuvem não alcança o programa. Não há conector do VoiceStudio, e a conta Speko não tem voz clonada.
   - Como fazer: Claude Desktop → aba Code → sessão local na pasta `pare-tudo` → permitir computer use no VoiceStudio.
   - Colar `narracao.txt`, gerar o áudio e salvar em `Pare Tudo/01-primeiro-video/`.
3. **Thumbnail 1280x720, cartelas do ranking e texto de descrição** (tabela completa e fontes). Pode ser feito na nuvem ou localmente.
4. **Montagem e render.** Sessão local.
5. **Postagem no canal numa nova janela do Chrome.** Sessão local, com o **ok final do Bruno antes de publicar**.
