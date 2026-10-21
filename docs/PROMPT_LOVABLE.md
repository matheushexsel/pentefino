# Prompt para o Lovable — site "Pente Fino"

Este arquivo tem três partes:

1. **Knowledge** — texto para colar em *Project Settings → Knowledge* do Lovable (contexto permanente que o Lovable relê a cada geração).
2. **Prompt mestre** — o primeiro prompt, que constrói a fundação inteira.
3. **Prompts de sequência** — prompts curtos, numerados, para rodar em ordem depois do mestre (o Lovable trabalha melhor em passos).

Os dados do site vêm deste repositório: `https://github.com/matheushexsel/pentefino`. A pasta `data/` (formato JSON descrito abaixo) é a fonte de verdade. A pasta `research_notes/` guarda as notas brutas com todas as fontes. Enquanto `data/` não existir, o site deve rodar com arquivos de exemplo que sigam exatamente o mesmo esquema.

---

## PARTE 1 — KNOWLEDGE (colar em Project Settings → Knowledge)

```
PROJETO: Pente Fino — site apartidário, didático e verificável sobre política, economia e serviços públicos no Brasil.

MISSÃO: qualquer pessoa leiga abre o site, digita ou clica em uma frase que ouviu ("o Lula quebrou o Brasil", "vão taxar o Pix", "o Bolsonaro privatizou a Eletrobras", "a conta de luz subiu por culpa do governo") e em menos de 30 segundos entende: o que é verdade, o que é falso, o que falta de contexto, qual é o número real, de onde ele veio e quem é responsável por aquilo. Sempre com os dois lados tratados com o mesmo rigor.

PRINCÍPIOS NÃO NEGOCIÁVEIS
1. Apartidário de verdade: mesma profundidade, mesmo tom e mesma escala de veredito para PT/Lula e PL/Flávio Bolsonaro e para qualquer outro partido. Nunca usar vermelho para PT nem azul/verde-amarelo para PL. Cores dos partidos só aparecem como pequeno marcador neutro, nunca como cor de layout.
2. Só fonte confiável e verificável: órgãos oficiais (IBGE, Banco Central, Tesouro, ANEEL, ANP, TSE, STF, MPF, PF, DATASUS, INEP, INPE), organismos multilaterais (FMI, Banco Mundial, FAO, OCDE), institutos de pesquisa reconhecidos (IPEA, FGV, Dieese, FBSP, Transparência Internacional) e agências de checagem (Lupa, Aos Fatos, Comprova, Estadão Verifica, UOL Confere, G1 Fato ou Fake, AFP Checamos). Todo número exibido tem: valor, período de referência, nome da fonte, URL clicável e data de acesso.
3. Linguagem: português do Brasil, simples, direta, sem jargão. Frases curtas. Quando houver termo técnico, link para o Glossário. Nunca usar "mentira", "mentiroso", "golpista", "petralha", "bolsominion" ou qualquer palavra de torcida. Vereditos usam a escala fixa do projeto.
4. Didático e lúdico: todo dado tem versão "em uma frase" e versão "quero entender a fundo". Gráficos simples, com marcadores de governo. Comparações em unidades do dia a dia (litros de gasolina por salário mínimo, meses de salário, "para cada R$ 100").
5. Nada é inventado: se um dado não está em data/, o componente mostra "dado ainda não verificado" em vez de inventar. Nunca gerar número fictício em produção.
6. Transparência: página de Metodologia, página de Fontes, política de correções, histórico de alterações de cada checagem (campo atualizado_em e changelog), link para a nota bruta em research_notes/ no GitHub.

ESCALA DE VEREDITO (fixa, em ordem; cada um tem ícone, cor neutra-semântica e rótulo):
- verdadeiro — a frase é confirmada pelos dados oficiais.
- verdadeiro-mas — o número está certo, mas a conclusão ou a culpa atribuída não se sustenta sem contexto.
- impreciso — o número está errado em magnitude ou período, mas a direção está certa.
- exagerado — a direção está certa, o tamanho não.
- falta-contexto — omite informação que muda a leitura.
- insustentavel — não há dado público que permita afirmar ou negar.
- falso — contradito pelos dados oficiais.
- opiniao — juízo de valor, não checável; o site mostra apenas os dados relacionados.

LADOS (campo lado): "governo-lula-pt", "oposicao-flavio-pl", "outro", "ambos". Toda listagem permite filtrar por lado e sempre mostra o contador de checagens por lado e por veredito para evidenciar o equilíbrio.

STACK E DADOS
- Front-end React + TypeScript + Vite + Tailwind + shadcn/ui, sem backend próprio. Sem login, sem banco.
- Dados: fetch dos JSON em https://raw.githubusercontent.com/matheushexsel/pentefino/master/data/ (manifesto em data/index.json). No build, baixar todos os JSON para gerar páginas estáticas; em runtime, revalidar com ETag e cache de 1 hora; se o GitHub falhar, usar a cópia do build. Nunca travar a tela por falta de rede.
- Gráficos: Recharts. Markdown: react-markdown + remark-gfm. Meta tags: react-helmet-async. Rotas estáticas pré-renderizadas no build (vite-react-ssg ou equivalente) para que cada página exista como HTML completo para o Google.
- Idioma único pt-BR. lang="pt-BR" no html.

SEO É PRIORIDADE DE PRODUTO (ver Prompt mestre, seção SEO).
```

---

## PARTE 2 — PROMPT MESTRE (primeiro prompt no chat do Lovable)

```
Construa o site "Pente Fino", um portal apartidário, didático e verificável sobre política, economia e serviços públicos no Brasil, voltado para pessoas leigas. Leia o Knowledge do projeto antes de qualquer coisa e siga todos os princípios dele.

======================================================================
1. OBJETIVO DO SITE
======================================================================
Uma pessoa ouve uma frase na campanha eleitoral (ex.: "o Lula quebrou o Brasil", "o governo vai taxar o Pix", "o Bolsonaro vendeu a Eletrobras", "a conta de luz subiu por causa do governo federal", "Lula e o PT são comunistas", "Flávio Bolsonaro foi investigado por rachadinha"), entra no site, encontra a frase em segundos e vê: veredito na escala fixa, explicação em 3 frases, os números reais com gráfico, quem é responsável pelo assunto (presidente, Congresso, STF, Banco Central, agência reguladora, estado, município, empresa privada), as fontes oficiais com link e as checagens de outras agências. Os dois lados da eleição de 2026 (Lula/PT e Flávio Bolsonaro/PL) e todos os partidos recebem exatamente o mesmo tratamento.

======================================================================
2. FONTE DE DADOS: GITHUB
======================================================================
Repositório: https://github.com/matheushexsel/pentefino (branch master).
Base raw: https://raw.githubusercontent.com/matheushexsel/pentefino/master/

Crie um módulo src/lib/data/ com:
- client.ts: função fetchJson<T>(path) que busca em raw.githubusercontent.com, usa cache em memória + localStorage com ETag e TTL de 1 hora, com fallback para a cópia embutida no build (pasta public/data-snapshot/ copiada no build a partir do GitHub por um script scripts/fetch-data.mjs rodado no "prebuild").
- schema.ts: tipos TypeScript e validadores zod para TODOS os esquemas abaixo. Registros inválidos são descartados com console.warn, nunca quebram a página.
- hooks: useManifest(), useChecagens(filtros), useChecagem(slug), useSerie(id), useGovernos(), useEscandalos(), useGlossario(), useExplicadores(), useSimuladorRenda(), useCandidatos(), usePartidos(), useFontes(), useTemas().

Enquanto a pasta data/ não existir no repositório, crie public/data-snapshot/ com 6 checagens de exemplo, 4 séries, os 5 governos, 2 escândalos, 10 termos de glossário, 2 explicadores, 1 simulador — TODOS marcados com "exemplo": true e exibidos com faixa "DADO DE EXEMPLO — ainda não verificado". Não invente números apresentados como reais.

ESQUEMA DOS ARQUIVOS (pasta data/):

data/index.json
{
  "versao": "1.0.0",
  "atualizado_em": "2026-10-21T12:00:00-03:00",
  "arquivos": {
    "checagens": ["checagens/lula-quebrou-o-brasil.json", "..."],
    "series": ["series/pib-anual.json", "..."],
    "escandalos": ["escandalos/lava-jato.json", "..."],
    "explicadores": ["explicadores/conta-de-luz-quem-decide.json", "..."],
    "simuladores": ["simuladores/renda.json"],
    "governos": "governos.json",
    "glossario": "glossario.json",
    "candidatos": "candidatos.json",
    "partidos": "partidos.json",
    "fontes": "fontes.json",
    "temas": "temas.json"
  }
}

data/checagens/<slug>.json
{
  "id": "chk-0001",
  "slug": "lula-quebrou-o-brasil",
  "frase": "O Lula quebrou o Brasil",
  "frase_normalizada": "lula quebrou o brasil",
  "variantes": ["Lula quebrou o país", "o PT quebrou o Brasil"],
  "autor": { "nome": "Flávio Bolsonaro", "partido": "PL", "cargo": "candidato à Presidência" },
  "lado": "oposicao-flavio-pl",
  "alvo": { "nome": "Lula", "partido": "PT" },
  "data": "2026-10-18",
  "onde": "Debate da Band",
  "url_declaracao": "https://...",
  "temas": ["economia", "divida-publica"],
  "tags": ["pib", "inflacao", "divida"],
  "veredito": "falta-contexto",
  "resumo_uma_frase": "Nenhum critério objetivo de país quebrado (calote, hiperinflação, recessão, reservas) está presente em 2026, mas a dívida pública está em nível recorde.",
  "explicacao_simples": ["frase 1", "frase 2", "frase 3"],
  "explicacao_completa_md": "## O que significa 'quebrar um país'\n...",
  "o_que_e_verdade": ["A dívida bruta está em 82,9% do PIB, recorde."],
  "o_que_nao_se_sustenta": ["Não há calote, as reservas são de US$ 362 bi..."],
  "quem_e_responsavel": [
    { "ator": "Presidência/Ministério da Fazenda", "papel": "propõe o orçamento e a meta fiscal", "peso": "alto" },
    { "ator": "Congresso Nacional", "papel": "aprova o orçamento e as emendas", "peso": "alto" },
    { "ator": "Banco Central (autônomo desde 2021)", "papel": "define a taxa Selic", "peso": "alto" }
  ],
  "numeros": [
    { "rotulo": "Dívida bruta do governo geral", "valor": 82.87, "unidade": "% do PIB", "periodo": "ago/2026",
      "fonte": { "nome": "Banco Central – SGS 13762", "url": "https://...", "acesso_em": "2026-10-21" },
      "comparacao": { "rotulo": "dez/2022", "valor": 71.7 } }
  ],
  "series": ["divida-bruta-pib", "pib-anual", "ipca-anual"],
  "checagens_externas": [ { "veiculo": "Aos Fatos", "veredito_original": "Verdadeiro (sobre R$ 11 tri)", "url": "https://...", "data": "2026-10-20" } ],
  "fontes": [ { "nome": "...", "url": "https://...", "tipo": "oficial", "acesso_em": "2026-10-21" } ],
  "nota_bruta_url": "https://github.com/matheushexsel/pentefino/blob/master/research_notes/.../01_macroeconomia_por_governo.md",
  "perguntas_frequentes": [ { "pergunta": "O Brasil deu calote?", "resposta": "Não. ..." } ],
  "relacionadas": ["divida-de-11-trilhoes", "menor-desemprego-da-historia"],
  "atualizado_em": "2026-10-21",
  "changelog": [ { "data": "2026-10-21", "o_que_mudou": "publicação" } ],
  "exemplo": false
}

data/series/<id>.json
{
  "id": "pib-anual",
  "titulo": "Crescimento do PIB",
  "descricao_simples": "Quanto a economia do país cresceu ou encolheu a cada ano.",
  "unidade": "% ao ano",
  "tipo_grafico": "barra",
  "frequencia": "anual",
  "fonte": { "nome": "IBGE – Contas Nacionais", "url": "https://...", "acesso_em": "2026-10-21" },
  "pontos": [ { "periodo": "2003", "valor": 1.1 }, { "periodo": "2004", "valor": 5.8 } ],
  "faixas_referencia": [ { "rotulo": "meta", "valor": 3.0 } ],
  "notas_metodologicas": ["Série revisada pelo IBGE em ..."],
  "ultimo_periodo": "2025"
}

data/governos.json
[
  { "id": "lula-1-2", "presidente": "Luiz Inácio Lula da Silva", "partido": "PT", "inicio": "2003-01-01", "fim": "2010-12-31", "vice": "José Alencar", "resumo_uma_frase": "...", "contexto_externo": ["boom das commodities", "crise de 2008"] },
  { "id": "dilma", "...": "..." },
  { "id": "temer", "...": "..." },
  { "id": "bolsonaro", "...": "..." },
  { "id": "lula-3", "...": "...", "fim": null }
]

data/escandalos/<id>.json
{
  "id": "lava-jato",
  "nome": "Operação Lava Jato / Petrolão",
  "periodo": { "inicio": "2014-03-17", "fim": "2021-02-03" },
  "governos_em_que_ocorreram_os_fatos": ["lula-1-2", "dilma"],
  "governos_em_que_foi_investigado": ["dilma", "temer", "bolsonaro"],
  "resumo_simples": ["..."],
  "valores": [ { "rotulo": "Prejuízo reconhecido pela Petrobras", "valor": 6.2, "unidade": "R$ bilhões", "fonte": {...} } ],
  "partidos": [ { "partido": "PT", "citados": 93, "denunciados": 0, "condenados_1a_instancia": 0, "condenados_definitivo": 0, "condenacoes_anuladas": 0, "fonte": {...} } ],
  "pessoas": [ { "nome": "...", "partido_na_epoca": "PT", "cargo": "...", "crime": "...", "tribunal": "...", "data_condenacao": "2017-07-12", "pena": "9 anos e 6 meses", "status_atual": "anulada pelo STF em 2021", "status_categoria": "anulada", "url": "https://..." } ],
  "linha_do_tempo": [ { "data": "2014-03-17", "evento": "Primeira fase", "url": "https://..." } ],
  "o_que_dizem_os_dois_lados": { "acusacao": "...", "defesa": "..." },
  "status_atual_md": "...",
  "fontes": [ ... ],
  "atualizado_em": "2026-10-21"
}
status_categoria é enum: investigado | denunciado | reu | condenado-1a | condenado-2a | condenado-definitivo | absolvido | arquivado | prescrito | anulada | cumprindo-pena | pena-cumprida.

data/explicadores/<id>.json  ("Quem decide isso?")
{
  "id": "conta-de-luz-quem-decide",
  "pergunta": "Por que a conta de luz subiu e quem é responsável?",
  "resposta_curta": "...",
  "cadeia_de_responsabilidade": [
    { "ator": "ANEEL (agência reguladora federal)", "o_que_controla": "autoriza o reajuste anual de cada distribuidora", "o_que_nao_controla": "...", "peso": "alto", "url": "https://..." },
    { "ator": "Enel SP (empresa privada)", "o_que_controla": "...", "peso": "medio" },
    { "ator": "Governo federal", "o_que_controla": "encargos da CDE, Tarifa Social, MME pode pedir caducidade", "o_que_nao_controla": "não fixa a tarifa nem manda na Eletrobras (privatizada em 2022)", "peso": "medio" },
    { "ator": "Governo estadual", "o_que_controla": "ICMS", "peso": "medio" }
  ],
  "composicao": [ { "rotulo": "Geração", "percentual": 41.6 }, { "rotulo": "Distribuição", "percentual": 31 } ],
  "linha_do_tempo": [ ... ],
  "numeros": [ ... ],
  "mitos_e_fatos": [ { "mito": "O presidente pode baixar a conta de luz por decreto", "fato": "...", "fontes": [...] } ],
  "fontes": [ ... ],
  "atualizado_em": "2026-10-21"
}

data/simuladores/renda.json
{
  "id": "renda",
  "salario_minimo": { "valor": 1621, "ano": 2026, "fonte": {...} },
  "distribuicao": [ { "faixa_max": 1621, "rotulo": "até 1 salário mínimo", "pessoas": 0, "percentual_acumulado": 0, "fonte": {...} }, ... ],
  "medidas": [
    { "id": "isencao-ir-5mil", "nome": "Isenção do IR até R$ 5 mil", "lado": "governo-lula-pt", "status": "em vigor desde 2026", "tipo": "beneficio_mensal",
      "regra": { "tipo": "tabela", "faixas": [ { "ate": 5000, "ganho_mensal": "ir_devido_anterior" }, { "ate": 7350, "ganho_mensal": "reducao_linear" } ] },
      "quem_paga": "renda acima de R$ 50 mil/mês (IR mínimo)", "custo_anual": 25.8, "unidade_custo": "R$ bilhões", "fonte": {...}, "simulacao_de": "Ministério da Fazenda" },
    { "id": "congelamento-salario-minimo-2019-2022", "lado": "oposicao-flavio-pl", "...": "..." }
  ]
}

data/glossario.json: [ { "termo": "Comunismo", "slug": "comunismo", "definicao_simples": "...", "definicao_completa_md": "...", "exemplos_historicos": [...], "o_que_nao_e": "...", "fontes": [...] } ]
data/candidatos.json: ficha de cada candidato (nome, partido, vice, cargos, patrimônio declarado TSE com url, processos [{caso, status_categoria, tribunal, url}], votações relevantes, programa_url).
data/partidos.json: sigla, nome, fundação, posição_espectro {bls_score, fonte}, presidente, bancadas, cor_marcador_neutra.
data/fontes.json: registro de fontes com "tier": "oficial" | "multilateral" | "academico" | "checagem" | "imprensa".
data/temas.json: lista de temas com slug, nome, ícone, descrição e ordem.

======================================================================
3. ARQUITETURA DE PÁGINAS (todas pré-renderizadas em HTML no build)
======================================================================
/                                   Home
/checagem/:slug                     Página de uma checagem
/checagens                          Lista + busca + filtros (lado, veredito, tema, autor, período)
/tema/:slug                         Hub de um tema (economia, emprego, energia, combustíveis, segurança, saúde, educação, corrupção, impostos, pix, eleição-2026, ideologias...)
/governos                           Comparador por governo (Lula 1-2, Dilma, Temer, Bolsonaro, Lula 3)
/governos/:id                       Ficha de um governo
/indicador/:id                      Página de uma série (gráfico grande + tabela + fontes + download CSV)
/escandalos                         Mapa dos escândalos (linha do tempo + por partido)
/escandalos/:id                     Ficha de um escândalo com tabela de condenados por partido e status
/quem-decide/:id                    Explicadores "quem é responsável" (conta de luz, gasolina, juros, impostos...)
/quanto-voce-ganha                  Simulador de renda e impacto das medidas
/espectro-politico                  Explicador didático de esquerda/direita + glossário de ideologias + onde estão os partidos
/glossario e /glossario/:slug
/candidatos/:slug                   Ficha dos candidatos (Lula, Flávio Bolsonaro e demais)
/eleicao-2026                       Resultado do 1º turno, calendário, regras, pesquisas (com fonte)
/metodologia                        Escala de veredito, critérios de fonte, política de correção
/fontes                             Todas as fontes usadas, com tier
/sobre                              Quem faz, por quê, como contribuir (link para o GitHub)
/busca?q=                           Resultado de busca
/404 amigável com busca

======================================================================
4. HOME (acima da dobra, mobile first)
======================================================================
- Título: "Ouviu uma frase na campanha? Cheque aqui, com os números oficiais."
- Campo de busca gigante com autocomplete pela frase_normalizada e variantes (fuse.js, fuzzy, tolerante a acento e erro de digitação). Abaixo: chips com as 8 frases mais buscadas.
- Faixa "Placar de equilíbrio": contador de checagens por lado e por veredito, para mostrar que o site olha os dois lados. Sempre visível.
- Bloco "Os dois lados hoje": duas colunas lado a lado (governo-lula-pt | oposicao-flavio-pl), cada uma com 3 cards de checagem recentes; o mesmo tamanho, a mesma hierarquia visual.
- Bloco "Quem decide?": cards para conta de luz, gasolina, juros, impostos, Pix, segurança.
- Bloco "Compare os governos": mini gráficos (PIB, inflação, desemprego, dívida, pobreza) com marcadores de governo em cinza neutro e tooltip.
- Bloco "Quanto você ganha?" com CTA para o simulador.
- Bloco "Esquerda, direita, centro: o que isso quer dizer de verdade?" com CTA para /espectro-politico.
- Rodapé: metodologia, fontes, correções, GitHub, licença (dados CC BY 4.0, código MIT), aviso de que o site não tem vínculo com partidos ou candidatos.

======================================================================
5. PÁGINA DE CHECAGEM (o coração do site)
======================================================================
Ordem fixa:
1. Breadcrumb (Início > Tema > Frase).
2. H1 = a frase entre aspas. Abaixo: quem disse, partido, cargo, onde, quando, link da declaração.
3. Selo do veredito (grande, com ícone, cor semântica neutra e rótulo) + "resumo em uma frase".
4. "Em 3 frases" (explicacao_simples).
5. Cards de números: valor grande, unidade, período, fonte com link e comparação (seta e delta).
6. Gráfico(s) das séries referenciadas, com marcadores dos governos e botão "ver tabela" e "baixar CSV".
7. Duas colunas: "O que é verdade" | "O que não se sustenta".
8. "Quem é responsável por isso?" — lista de atores com barra de peso e link para o explicador.
9. "Quero entender a fundo" (accordion com explicacao_completa_md renderizada).
10. Perguntas frequentes (accordion; vira FAQPage JSON-LD).
11. "O que outras agências disseram" (checagens externas com veredito original e link).
12. Fontes (lista numerada, tier, data de acesso) + botão "ver nota bruta no GitHub".
13. Checagens relacionadas (mesmo tema, e sempre pelo menos 1 do lado oposto).
14. Rodapé da checagem: atualizado em, changelog, "achou um erro? abra uma issue no GitHub" (link pré-preenchido).
15. Botões de compartilhar: WhatsApp, X, Telegram, copiar link, e "baixar card" (imagem PNG gerada no cliente com html-to-image: frase, veredito, 1 número, fonte, URL).

======================================================================
6. COMPARADOR DE GOVERNOS
======================================================================
Tabela e gráficos lado a lado dos 5 governos para: PIB médio, inflação média e anos fora da meta, Selic média, desemprego no fim, dívida/PIB início e fim, resultado primário, pobreza, Gini, salário mínimo real, emprego formal gerado, desmatamento, homicídios. Toggle "mostrar contexto externo" (commodities, crise 2008, Covid, guerra, tarifaço). Cada célula com tooltip de fonte. Botão "o que é bom/ruim aqui?" com explicação neutra do indicador. Nunca ranquear governos com nota; apenas mostrar os números.

======================================================================
7. SIMULADOR "QUANTO VOCÊ GANHA?"
======================================================================
Slider de renda mensal (R$ 0 a R$ 60 mil, com teclas e input numérico). Mostra: "você está entre os X% que ganham até isso" (distribuição IBGE/Receita, com fonte). Em seguida, lista de medidas (de ambos os lados, intercaladas, ordem por impacto absoluto) com o efeito estimado para aquela renda: ganho/perda mensal, quem paga, status (em vigor, proposta, revogada), fonte da simulação e premissas. Botão "ver conta" abre o cálculo passo a passo. Rodapé: "simulação simplificada, não substitui cálculo oficial".

======================================================================
8. ESPECTRO POLÍTICO (didático)
======================================================================
Linha interativa de extrema esquerda a extrema direita com dois eixos (econômico e social/autoritário-libertário). Cards por ideologia: o que defende, origem histórica, exemplos reais de países/partidos, "o que NÃO é". Posição dos partidos brasileiros segundo pesquisas acadêmicas (Brazilian Legislative Surveys / V-Party), com fonte e ano. Seção "Teste o rótulo": o usuário escolhe um rótulo ("comunista", "fascista", "liberal", "social-democrata") e o site mostra os critérios acadêmicos e o que os dados sobre o partido mostram, lado a lado. Linguagem neutra: "o rótulo X se aplica? Os critérios são A, B, C; o partido faz A, não faz B e C".

======================================================================
9. SEO — REQUISITOS OBRIGATÓRIOS (tráfego orgânico é a meta de negócio)
======================================================================
a) Pré-renderização: toda rota vira HTML estático completo no build (vite-react-ssg ou equivalente). Gere uma página por checagem, série, escândalo, explicador, termo do glossário, governo, tema e candidato. Nada de conteúdo só via JS após o load.
b) react-helmet-async em cada página com: <title> único (até 60 caracteres, começando pela frase ou pergunta exatamente como as pessoas buscam, ex.: "Lula quebrou o Brasil? Veja os números oficiais | Pente Fino"), meta description única (até 155 caracteres, com o veredito e um número), canonical absoluto, og:title, og:description, og:image (1200x630 gerada no build para cada checagem com a frase + veredito), og:type article, twitter:card summary_large_image, article:published_time, article:modified_time, lang pt-BR, robots index,follow.
c) JSON-LD (schema.org) por tipo de página:
   - Checagem: ClaimReview (claimReviewed = frase, itemReviewed.author = quem disse, reviewRating com ratingValue mapeado da escala 1-6 e alternateName = rótulo do veredito, author = Organization "Pente Fino", url, datePublished, dateModified) + FAQPage com as perguntas_frequentes + BreadcrumbList.
   - Série: Dataset (name, description, creator = fonte oficial, temporalCoverage, distribution CSV).
   - Explicador e glossário: Article + FAQPage + DefinedTerm.
   - Escândalo e governo: Article + BreadcrumbList.
   - Site: WebSite com SearchAction (sitelinks searchbox) e Organization com logo e sameAs (GitHub).
d) URLs: minúsculas, com hífen, sem acento, sem stopwords desnecessárias, com a frase exata (ex.: /checagem/lula-quebrou-o-brasil, /quem-decide/por-que-a-conta-de-luz-subiu, /checagem/pix-vai-ser-taxado). Redirect 301 para variantes com e sem barra final.
e) sitemap.xml gerado no build a partir de data/index.json, com lastmod = atualizado_em; robots.txt permitindo tudo e apontando o sitemap; sitemap de imagens para os cards OG.
f) Conteúdo on-page: H1 único com a frase; H2 com perguntas em linguagem natural ("Lula quebrou o Brasil?", "Quem privatizou a Eletrobras?", "Por que a gasolina subiu em 2026?"); primeiro parágrafo responde a pergunta em até 2 frases (featured snippet); tabelas HTML reais (não imagens) para os números; alt text descritivo em todo gráfico (gere um resumo em texto do gráfico abaixo dele, visível).
g) Links internos: cada checagem linka para pelo menos 3 relacionadas, 1 explicador, 1 governo e o glossário; hubs de tema linkam para tudo do tema; breadcrumbs em todas as páginas.
h) Performance (Core Web Vitals): LCP < 2 s em 4G, CLS ~0, fontes locais com font-display swap, imagens WebP com width/height, code splitting por rota, gráficos carregados com lazy loading abaixo da dobra, sem bibliotecas pesadas desnecessárias. Lighthouse acima de 95 em todas as categorias.
i) Página /busca indexável somente quando houver resultado; páginas de filtro com noindex para evitar conteúdo duplicado.
j) Acessibilidade = SEO: contraste AA, navegação por teclado, aria-labels, skip link, foco visível, prefers-reduced-motion respeitado.
k) Dados estruturados de atualização: exibir "Atualizado em" visível e no dateModified.
l) Gere automaticamente páginas "Perguntas" para variantes populares de busca (campo variantes), todas com canonical apontando para a checagem principal.
m) Preparar para Google Search Console e Bing: meta de verificação configurável por variável de ambiente; arquivo humans.txt; manifest.json PWA com ícones.

======================================================================
10. DESIGN
======================================================================
- Mobile first. Tipografia legível (Inter ou similar, 17-18px base). Espaço em branco generoso.
- Paleta neutra institucional: fundo claro, texto quase preto, um tom de destaque não partidário (ex.: roxo/ametista ou teal) e as cores semânticas do veredito (verde para verdadeiro, âmbar para intermediários, cinza para insustentável/opinião, vinho para falso). Nunca vermelho-PT nem azul/verde-amarelo-PL em layout. Dark mode automático.
- Ícones Lucide. Ilustrações simples em SVG inline, sem fotos de políticos (evitar viés visual). Avatares dos candidatos substituídos por iniciais em círculo cinza.
- Microinterações leves (contadores animados, barras preenchendo), respeitando prefers-reduced-motion.
- Componentes: SeloVeredito, CardChecagem, CardNumero, GraficoSerie (com marcadores de governo), CadeiaResponsabilidade, PlacarEquilibrio, LinhaDoTempo, TabelaCondenadosPorPartido, SliderRenda, EspectroInterativo, CaixaFonte, BotaoCompartilhar, FaixaExemplo.

======================================================================
11. QUALIDADE E REGRAS DE CONTEÚDO
======================================================================
- Nunca gere textos com números que não venham de data/. Em caso de dado ausente, renderize "dado ainda não verificado".
- Toda ocorrência de número no texto deve ter a fonte a um clique.
- Teste automatizado (vitest) para: validação do schema de todos os JSON do snapshot, geração de slugs, mapa de veredito para rating, geração do sitemap.
- Script scripts/fetch-data.mjs: baixa data/ do GitHub para public/data-snapshot/ e falha o build se index.json estiver inválido.
- README do projeto explicando como os dados chegam do GitHub e como contribuir.

Entregue primeiro: estrutura, módulo de dados com validação, Home, página de checagem, lista de checagens, comparador de governos básico, metodologia, SEO completo (helmet + JSON-LD + sitemap + pré-renderização). Depois iteramos página a página.
```

---

## PARTE 3 — PROMPTS DE SEQUÊNCIA (rodar um por vez, depois do mestre)

1. **Dados reais.** "A pasta data/ já existe no repositório. Remova o snapshot de exemplo, rode scripts/fetch-data.mjs, valide todos os arquivos com o schema zod e me liste os registros rejeitados com o motivo. Não altere os dados; só reporte."
2. **Busca.** "Implemente a busca com fuse.js sobre frase, variantes, tags, autor e tema, tolerante a acento e erro de digitação, com autocomplete na Home e página /busca. Destaque o trecho encontrado. Registre as 20 buscas mais feitas em localStorage apenas para sugerir chips (sem enviar a servidor)."
3. **Gráficos.** "Crie o componente GraficoSerie com Recharts: barras ou linhas conforme tipo_grafico, faixa sombreada por governo em cinza com rótulo, linha de meta quando houver faixas_referencia, tooltip com fonte, botão 'ver tabela' e 'baixar CSV', e resumo textual automático do gráfico abaixo dele para acessibilidade e SEO."
4. **Comparador de governos.** "Monte /governos com a tabela comparativa descrita no prompt mestre, usando as séries de data/series e os marcos de data/governos.json. Toggle de contexto externo. Nenhuma nota ou ranking."
5. **Escândalos.** "Monte /escandalos (linha do tempo horizontal com filtros por partido e governo) e /escandalos/:id com a TabelaCondenadosPorPartido, que separa claramente citados, denunciados, condenados em 1ª e 2ª instância, condenação definitiva, anulada, absolvido e arquivado. Inclua o bloco 'o que dizem os dois lados'."
6. **Quem decide.** "Monte /quem-decide/:id com a CadeiaResponsabilidade (atores, o que controlam, o que não controlam, peso), gráfico de composição (donut) e seção mitos e fatos. Priorize conta de luz, gasolina, juros, impostos e Pix."
7. **Simulador.** "Monte /quanto-voce-ganha conforme o prompt mestre, lendo data/simuladores/renda.json. Cada medida mostra ganho/perda mensal, quem paga, status e fonte. Botão 'ver conta' com o passo a passo."
8. **Espectro.** "Monte /espectro-politico com o EspectroInterativo de dois eixos, cards de ideologia, posição dos partidos com fonte e a seção 'Teste o rótulo'."
9. **Candidatos e eleição.** "Monte /candidatos/:slug e /eleicao-2026 lendo data/candidatos.json e as séries de pesquisas/resultados. Mesmo layout e mesma profundidade para todos os candidatos."
10. **Compartilhamento.** "Implemente o 'baixar card' (PNG 1080x1350 para stories e 1200x630 para link) com html-to-image, com frase, veredito, um número, fonte e URL. Gere também as imagens OG no build."
11. **SEO final.** "Audite todas as rotas: title, description, canonical, OG, JSON-LD válido (teste com o validador do schema.org), sitemap.xml, robots.txt, pré-renderização de todas as páginas, Lighthouse > 95. Corrija tudo que falhar e me mostre o relatório."
12. **Correções e contribuição.** "Adicione em cada página o link 'achou um erro?' que abre uma issue no GitHub já preenchida com a URL da página e o id do registro, e a página /metodologia com a escala de veredito, critérios de fonte e política de correção."

---

## Observações para você (não colar no Lovable)

- Conecte o GitHub no Lovable apenas para o **código do site**. Os **dados** são lidos pelo site direto da URL raw do repositório `pentefino`, então o site e os dados podem viver em repositórios diferentes ou no mesmo.
- O domínio ideal contém a palavra que as pessoas digitam (ex.: `pentefino.org`, `pentefino.com.br`). Depois de publicar, cadastre no Google Search Console e envie o sitemap.
- As checagens em `data/checagens/` precisam de um JSON por frase. Eu vou gerar esses arquivos a partir das notas de `research_notes/` como próximo passo, seguindo exatamente o esquema acima.
