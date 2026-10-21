# Prompts adicionais para o Lovable — conteúdos novos do Pente Fino

Use depois dos prompts iniciais (`docs/PROMPT_LOVABLE.md`). Cada bloco é um prompt independente: cole um por vez, espere o Lovable terminar e confira antes do próximo.

Ordem recomendada: **A → B → C → D → E → F → G → H → I**. O bloco A é obrigatório antes dos outros, porque cria os novos tipos de dados.

Tudo continua lendo de `https://raw.githubusercontent.com/matheushexsel/pentefino/master/data/`. Enquanto os arquivos novos não existirem em `data/`, usar exemplos marcados com `"exemplo": true` e a faixa "DADO DE EXEMPLO — ainda não verificado". Nunca inventar número como se fosse real.

---

## PROMPT A — Novos tipos de dados (rodar primeiro)

```
Leia o Knowledge do projeto. Vamos ampliar o módulo src/lib/data/ com cinco novos tipos de registro, todos validados com zod em schema.ts, com hooks próprios e com entradas em data/index.json (chaves "eventos", "falas", "historias", "temas_em_alta", "medidas"). Registros inválidos geram console.warn e são descartados, nunca quebram a página. Crie exemplos em public/data-snapshot/ marcados com "exemplo": true.

1) data/eventos/<id>.json — um debate, sabatina, entrevista, podcast, live ou discurso.
{
  "id": "debate-band-2turno-2026-10-18",
  "tipo": "debate" | "sabatina" | "entrevista" | "podcast" | "live" | "discurso" | "propaganda",
  "nome": "Debate da Band – 2º turno",
  "data": "2026-10-18",
  "veiculo": "Band",
  "participantes": ["flavio-bolsonaro", "lula"],
  "url_video": "https://...",
  "url_transcricao": "https://...",
  "resumo_uma_frase": "...",
  "placar": { "flavio-bolsonaro": { "checadas": 20, "por_veredito": { "verdadeiro": 8, "falso": 3, "...": 0 } }, "lula": { "checadas": 22, "por_veredito": { "..." : 0 } } },
  "falas": ["fala-0001", "fala-0002"],
  "checagens_externas": [ { "veiculo": "Lupa", "url": "https://...", "resumo": "8 falsas de X, 2 de Y" } ],
  "fontes": [ ... ],
  "atualizado_em": "2026-10-21",
  "exemplo": false
}

2) data/falas/<id>.json — UMA frase dita por um candidato ou aliado em um evento.
{
  "id": "fala-0001",
  "slug": "flavio-lula-recebeu-74-por-cento-dos-votos-dos-presos",
  "evento_id": "debate-band-2turno-2026-10-18",
  "candidato": "flavio-bolsonaro",
  "lado": "oposicao-flavio-pl",
  "minuto": "01:12:40",
  "frase_literal": "…",
  "literal": true,
  "tema": "seguranca",
  "veredito": "falta-contexto",
  "resumo_uma_frase": "Presos com condenação definitiva não votam; quem vota em presídios são presos provisórios e adolescentes internados, um grupo de X mil eleitores.",
  "explicacao_simples": ["...", "...", "..."],
  "o_que_e_verdade": ["..."],
  "o_que_nao_se_sustenta": ["..."],
  "numeros": [ { "rotulo": "...", "valor": 0, "unidade": "...", "periodo": "...", "fonte": { "nome": "...", "url": "https://...", "acesso_em": "2026-10-21" } } ],
  "base_legal": [ { "norma": "Constituição, art. 15, III", "o_que_diz": "...", "url": "https://..." } ],
  "checagens_externas": [ { "veiculo": "Aos Fatos", "veredito_original": "Falso", "url": "https://...", "data": "2026-10-18" } ],
  "checagem_slug": "lula-recebeu-74-por-cento-dos-votos-dos-presos",
  "fontes": [ ... ],
  "atualizado_em": "2026-10-21",
  "exemplo": false
}
Regra: toda fala com veredito diferente de "opiniao" deve apontar para uma checagem completa (checagem_slug) ou carregar seus próprios números e fontes.

3) data/historias/<id>.json — história longa em formato de linha do tempo com capítulos (ex.: a prisão de Lula; a privatização da Eletrobras; a fraude do INSS; o 8 de janeiro).
{
  "id": "prisao-de-lula",
  "titulo": "Por que Lula foi preso, e por que a condenação foi anulada",
  "pergunta_principal": "Lula foi preso por quê? Quem o prendeu? O que aconteceu depois?",
  "resposta_curta": ["...", "...", "..."],
  "periodo": { "inicio": "2014-03-17", "fim": "2026-10-21" },
  "personagens": [ { "id": "sergio-moro", "nome": "Sergio Moro", "papel_na_historia": "juiz da 13ª Vara Federal de Curitiba; depois ministro da Justiça de Bolsonaro; hoje senador", "partido_atual": "União Brasil" } ],
  "capitulos": [
    { "id": "1", "titulo": "A acusação do tríplex", "periodo": "2016", "texto_md": "...",
      "eventos": [ { "data": "2016-09-14", "fato": "Coletiva do MPF com PowerPoint", "citacao_literal": "…", "quem_disse": "Deltan Dallagnol", "url": "https://...", "tipo": "declaracao" | "decisao" | "fato" | "documento" } ],
      "o_que_a_acusacao_dizia": "...", "o_que_a_defesa_dizia": "...",
      "numeros": [ ... ] }
  ],
  "glossario_local": [ { "termo": "incompetência do juízo", "definicao_simples": "..." } ],
  "o_que_cada_lado_diz_hoje": { "lado_a": { "quem": "Flávio Bolsonaro", "frase": "...", "veredito": "...", "checagem_slug": "..." }, "lado_b": { "quem": "Lula", "frase": "...", "veredito": "...", "checagem_slug": "..." } },
  "perguntas_frequentes": [ { "pergunta": "Lula foi inocentado ou 'descondenado'?", "resposta": "..." } ],
  "fontes": [ ... ],
  "nota_bruta_url": "https://github.com/matheushexsel/pentefino/blob/master/research_notes/...",
  "atualizado_em": "2026-10-21"
}

4) data/temas_em_alta.json — temas mais buscados/mencionados, com a evidência e o dado por trás.
[
  { "id": "flavio-miliciano", "termo": "Flávio miliciano", "lado_que_impulsiona": "governo-lula-pt", "evidencia": [ { "fonte": "Google Trends via Poder360", "metrica": ">500 mil buscas em 4h", "data": "2026-10-18", "url": "https://..." } ], "o_que_e": "...", "o_que_os_dados_dizem": "...", "checagem_slug": "...", "historia_id": null, "atualizado_em": "2026-10-21" }
]

5) data/medidas/<id>.json — uma medida de governo (imposto, benefício, lei) com quem ganha e quem paga, usada pelo simulador e pela página "Impostos: quem paga?".
{
  "id": "lei-15270-2025-isencao-ir",
  "nome": "Isenção do IR até R$ 5 mil e IR mínimo para altas rendas",
  "tipo": "imposto" | "beneficio" | "lei-trabalhista" | "tarifa" | "privatizacao" | "outro",
  "governo": "lula-3",
  "lado": "governo-lula-pt",
  "norma": { "nome": "Lei 15.270/2025", "data": "2025-11-26", "url": "https://...", "vigencia": "2026-01-01" },
  "status": "em-vigor" | "proposta" | "aprovada-aguarda" | "revogada" | "caducou" | "suspensa-stf",
  "o_que_faz_simples": ["..."],
  "quem_ganha": { "descricao": "...", "pessoas": 16000000, "faixa_renda": "até R$ 7.350/mês", "fonte": {...} },
  "quem_paga": { "descricao": "...", "pessoas": 141400, "faixa_renda": "acima de R$ 50 mil/mês", "fonte": {...} },
  "custo_ou_arrecadacao": { "valor": 25.8, "unidade": "R$ bilhões/ano", "fonte": {...} },
  "regra_simulador": { "tipo": "tabela" | "percentual" | "fixo" | "nenhuma", "parametros": { } },
  "mitos": [ { "mito": "O governo criou um imposto sobre o Pix", "fato": "...", "fontes": [...] } ],
  "fontes": [ ... ],
  "atualizado_em": "2026-10-21"
}

Crie os hooks useEventos(), useEvento(id), useFalas(filtros), useFala(slug), useHistorias(), useHistoria(id), useTemasEmAlta(), useMedidas(filtros). Atualize scripts/fetch-data.mjs e os testes de schema.
```

---

## PROMPT B — Seção "Falas e debates"

```
Crie a seção "O que eles disseram" com as rotas:

/falas — todas as falas checadas. Topo: PlacarEquilibrio por candidato (total de falas checadas e distribuição por veredito, lado a lado, mesmo tamanho). Filtros: candidato, evento, tema, veredito, período, "só literais". Busca por texto da frase. Ordenação por data ou por veredito. Cada card mostra: aspas com a frase, candidato (iniciais em círculo cinza, sem foto), evento e data, SeloVeredito, resumo em uma frase.

/falas/:slug — página de uma fala: breadcrumb; H1 = a frase entre aspas; quem, onde, quando, minuto e botão "ver no vídeo" (link com timestamp); SeloVeredito grande; "Em 3 frases"; cards de números com fonte; "Base legal" quando houver (norma, o que diz, link); "O que é verdade" | "O que não se sustenta"; "O que outras agências disseram"; link para a checagem completa (checagem_slug) e para a história relacionada (historia_id) quando existir; fontes; compartilhar; "achou um erro?".

/eventos — lista de debates, sabatinas e entrevistas em ordem cronológica, com placar por candidato em cada card.
/eventos/:id — página do evento: dados do evento, placar por candidato (barras empilhadas por veredito, mesma escala para os dois), lista de falas na ordem do minuto, com filtro por candidato; link para transcrição e checagens externas.

/candidatos/:slug/falas — todas as falas daquele candidato, com o placar dele e um gráfico de barras por tema.

SEO: title no formato "[frase curta] — é verdade? | Pente Fino"; description com veredito e um número; JSON-LD ClaimReview em /falas/:slug (claimReviewed = frase_literal, itemReviewed.author = candidato, itemReviewed.datePublished = data do evento, itemReviewed.appearance.url = url_video) e Event + ItemList em /eventos/:id; breadcrumbs; canonical; pré-renderização de todas as rotas.
```

---

## PROMPT C — Seção "Histórias" (linhas do tempo longas)

```
Crie /historias e /historias/:id para os registros de data/historias/.

/historias — cards com título, pergunta principal, período e número de capítulos.

/historias/:id — layout de leitura longa, mobile first:
- H1 = título; abaixo, a "resposta curta" em 3 frases dentro de um destaque.
- Barra de progresso de leitura e índice lateral (desktop) ou menu suspenso (mobile) com os capítulos.
- Linha do tempo vertical: cada evento com data, tipo (ícone: declaração, decisão judicial, fato, documento), texto e link para a fonte. Citações literais aparecem em bloco de aspas com o nome de quem disse e link; se "literal": false, exibir rótulo "paráfrase".
- Em cada capítulo, duas caixas lado a lado "O que a acusação dizia" | "O que a defesa dizia".
- Componente "Personagens" com cards (nome, papel na história, partido atual) e, ao clicar, os eventos daquele personagem destacados na linha do tempo.
- Glossário local em tooltips (ex.: "incompetência do juízo", "suspeição", "trânsito em julgado", "absolvição de mérito", "prescrição").
- Seção final "O que cada lado diz hoje": a frase de cada lado com SeloVeredito e link para a checagem.
- Perguntas frequentes (FAQPage).
- Fontes numeradas e botão "ver nota bruta no GitHub".
SEO: title = pergunta principal; description = resposta curta resumida; JSON-LD Article + FAQPage + BreadcrumbList; H2 = títulos dos capítulos formulados como perguntas quando fizer sentido.
Primeira história a estruturar (quando os dados chegarem): "prisao-de-lula". Prepare também os ids "privatizacao-da-eletrobras", "fraude-do-inss", "8-de-janeiro-e-condenacao-de-bolsonaro", "banco-master" e "pix-taxacao-janeiro-2025".
```

---

## PROMPT D — Página "Pix: vão taxar?" e "Impostos: quem paga?"

```
Crie duas páginas a partir de data/medidas/ e da história "pix-taxacao-janeiro-2025":

/impostos — "Impostos: quem paga cada um?". Topo: seletor de governo (Bolsonaro 2019-2022 | Lula 3 2023-2026 | propostas 2026 de cada candidato). Lista de medidas em cards com: nome, status, o que faz em uma frase, duas barras lado a lado "quem ganha" e "quem paga" (nº de pessoas e faixa de renda, com fonte), custo ou arrecadação, e botão "detalhes". Filtros: tipo, status, "atinge quem ganha até R$ 5 mil?" (derivado de quem_paga.faixa_renda). Inclua um gráfico de pizza "de cada R$ 100 arrecadados, de onde vem" quando a série existir, e a faixa "Carga tributária total por ano" com fonte.
/impostos/:id — detalhe da medida: norma com link, o que faz, quem ganha, quem paga, custo, mitos e fatos, fontes, medidas relacionadas, e um mini simulador "e para quem ganha R$ X?" quando regra_simulador existir.
/pix — explicador dedicado: resposta curta no topo ("Não existe e nunca existiu imposto sobre o Pix. Veja o que a norma de 2024 fazia, o que foi revogado e o que vale hoje."), linha do tempo da história "pix-taxacao-janeiro-2025", caixa "O que a norma dizia de fato" com trechos literais e link para o DOU, gráfico do volume de Pix por mês (série do Banco Central) com marcador em janeiro de 2025, bloco "Quem espalhou e quem desmentiu" com links, bloco "E em 2026?" e perguntas frequentes.
SEO: /pix deve ranquear para "pix vai ser taxado", "taxação do pix", "imposto do pix", "pix taxado 2026": use essas expressões no title, H1, H2 e primeiro parágrafo, com canonical único; JSON-LD ClaimReview (claimReviewed = "O governo vai taxar o Pix") + FAQPage.
```

---

## PROMPT E — "Temas em alta" na Home e página própria

```
Crie /temas-em-alta a partir de data/temas_em_alta.json e um bloco na Home "O que o Brasil está buscando agora". Cada tema mostra: termo, qual lado impulsiona (ícone neutro, sem cor partidária), evidência (fonte da métrica e data), "o que é" em uma frase, "o que os dados dizem" em até 3 frases e link para a checagem ou história. Filtro por lado e por período. Ordenar por data da evidência. Mostre sempre pelo menos um tema de cada lado na Home. SEO: title "Os assuntos políticos mais buscados do Brasil, explicados com dados | Pente Fino"; JSON-LD ItemList.
```

---

## PROMPT F — Espectro político e glossário (completar)

```
Complete /espectro-politico com os dados de data/partidos.json (campo posicao_espectro.bls_score, escala de -1 a +1 das Brazilian Legislative Surveys, com fonte e ano) e de data/glossario.json:
- EspectroInterativo: linha horizontal de -1 (esquerda) a +1 (direita) com os partidos posicionados pelo bls_score; ao tocar, mostra sigla, nome, score, ano e fonte. Abaixo, segundo eixo (social: autoritário-libertário) só quando houver dado; se não houver, exibir "sem medida acadêmica disponível".
- Cards por ideologia (comunismo, socialismo, social-democracia, trabalhismo, liberalismo econômico, liberalismo social, conservadorismo, nacionalismo, populismo, fascismo, libertarianismo, direita radical) com: definição simples, origem histórica, exemplos reais de países e partidos, "o que NÃO é", fontes.
- Seção "Teste o rótulo": o usuário escolhe um rótulo e um partido ou candidato; o site lista os critérios acadêmicos do rótulo (do glossário) e, para cada critério, o que os dados do partido mostram (texto e fonte), terminando com "se aplica / se aplica em parte / não se aplica" e um aviso de que a classificação é dos estudos citados, não do site.
- Linha do tempo "Esquerda e direita no Brasil" (PCB 1922, 1935, 1937, 1964-85, PT 1980, PL 1985, 2018, 2021) a partir de uma história "esquerda-e-direita-no-brasil".
SEO: a página deve responder "o que é comunismo", "o que é extrema direita", "o PT é comunista?", "o PL é de extrema direita?" em H2 com resposta direta no primeiro parágrafo de cada seção; JSON-LD DefinedTermSet + FAQPage.
```

---

## PROMPT G — Simulador "Quanto você ganha?" ligado a data/medidas

```
Refaça /quanto-voce-ganha para usar data/medidas/ (campo regra_simulador) e data/simuladores/renda.json (distribuição por décimo e percentil, salário mínimo vigente). Fluxo: a pessoa informa renda mensal individual (slider + campo) e, opcionalmente, número de pessoas na casa; o site mostra "você está entre os X% dos brasileiros" (com a fonte IBGE e o período), a mediana e o décimo em que a pessoa está num gráfico de barras com a posição marcada. Em seguida, as medidas de ambos os lados intercaladas, cada uma com: efeito mensal estimado para aquela renda (ganho, perda ou "não te afeta"), quem paga, status, fonte da simulação e botão "ver conta" com o cálculo passo a passo. Rodapé fixo: "Simulação simplificada com base em regras públicas; não substitui cálculo oficial." Toggle "mostrar só o que está em vigor". Compartilhar resultado como card (sem expor a renda, só o décimo).
```

---

## PROMPT H — Fichas dos candidatos (completar)

```
Complete /candidatos/:slug com, na mesma ordem e com o mesmo layout para todos: resumo neutro em 3 frases; cargos e período; patrimônio declarado ao TSE (valor total e lista itemizada com link para o divulgacandcontas); votações relevantes como senador/deputado quando houver (nome do projeto, data, voto, link para a votação nominal); processos e inquéritos em tabela com colunas caso, status_categoria, tribunal, data, link, sempre com legenda da escala (investigado, denunciado, réu, condenado em 1ª/2ª instância, condenação definitiva, anulada, absolvido, arquivado, prescrito); mudanças de posição documentadas (antes/depois com links); placar de falas checadas (link para /candidatos/:slug/falas); doações e fundo eleitoral recebidos (fonte TSE); programa de governo (link e resumo por eixo). Nenhuma foto; iniciais em círculo cinza.
```

---

## PROMPT I — Auditoria de equilíbrio e SEO

```
Crie uma página interna /auditoria (noindex) que calcula e exibe, a partir dos dados carregados: nº de checagens, falas, histórias e medidas por lado; distribuição de vereditos por lado; nº de registros sem fonte, sem URL, sem atualizado_em, marcados como exemplo; lista de slugs duplicados; páginas sem title ou description. Em seguida, rode a auditoria de SEO em todas as rotas novas (falas, eventos, historias, impostos, pix, temas-em-alta, espectro, simulador, candidatos): title, description, canonical, OG, JSON-LD válido, inclusão no sitemap.xml, pré-renderização. Corrija o que falhar e me mostre o relatório.
```

---

## Observação para você

Os arquivos de `data/` ainda não existem; eles serão gerados a partir das notas de `research_notes/` seguindo exatamente estes esquemas. Até lá, o Lovable vai construir tudo com exemplos marcados. Quando `data/` entrar no repositório, rode de novo o prompt 1 da sequência original ("Dados reais") para trocar o snapshot de exemplo pelos dados verificados.
