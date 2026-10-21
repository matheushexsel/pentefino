# Contas públicas e dívida por governo (Lula 1-2, Dilma, Temer, Bolsonaro, Lula 3) — dossiê numérico, posição em 21/10/2026

Convenções: valores em R$ correntes salvo indicação; "% PIB" = percentual do PIB nominal acumulado em 12 meses, no critério do Banco Central (BCB). Sinal: "superávit" = receitas primárias > despesas primárias; "déficit" = o contrário. Último dado mensal disponível de cada série está marcado como **[últ.: mês/ano]**. Séries do BCB foram baixadas diretamente da API do Sistema Gerenciador de Séries Temporais (SGS) em 21/10/2026; a série do Tesouro foi lida da planilha oficial "Série Histórica RTN" (versão jul/2026, publicada 27/08/2026).

## Conceitos básicos: o que medem resultado primário, nominal, dívida bruta e dívida líquida

### Takeaway
Resultado primário é receita menos despesa sem contar juros; resultado nominal inclui os juros; a Dívida Bruta do Governo Geral (DBGG) soma os passivos de União, estados e municípios (excluindo BC e estatais) e é o indicador usado em comparações internacionais; a Dívida Líquida do Setor Público (DLSP) desconta ativos como reservas internacionais e créditos do Tesouro junto ao BNDES.

### Cited Findings
- Definição oficial da DBGG (BCB): "abrange os passivos internos e externos do Governo Federal, dos Estados e dos Municípios. Esse conceito, que segue padrões internacionais, exclui do seu escopo, portanto, o BCB e as empresas estatais". Estrutura: dívida mobiliária do Governo Federal em mercado (−) aplicações de estados, municípios e fundos federais em títulos (+) operações compromissadas (+) dívida bancária (+) dívida assumida pela União – Lei 8.727/1993 (+) dívida externa bruta — [BCB, Nota Técnica 47 (jul/2018), p. 3-4](https://www.bcb.gov.br/content/publicacoes/notastecnicas/47_notas_tecnicas_julho_2018.pdf)
- Mudança metodológica de 2008: na metodologia anterior (até 2007) a DBGG incluía todos os títulos na carteira do BC; a partir de 2008 (série iniciada em dez/2006) passou a incluir as operações compromissadas do BC e a excluir os "títulos livres" na carteira do BC. Objetivo declarado: "maior aderência entre a DBGG e o resultado fiscal primário" — [BCB, Nota Técnica 47](https://www.bcb.gov.br/content/publicacoes/notastecnicas/47_notas_tecnicas_julho_2018.pdf)
- A diferença metodológica explica por que o FMI reporta dívida bruta do Brasil em 93,3% do PIB (2025) enquanto o BCB reporta 78,6%: o FMI inclui a totalidade dos títulos na carteira do BC (Tabela A15 do Fiscal Monitor, nota metodológica "Brazil") — [FMI, Fiscal Monitor abr/2026, Tabela A15 e notas](https://www.imf.org/-/media/files/publications/fiscal-monitor/2026/april/english/text.pdf); comparação explícita entre as duas métricas (83,6% BCB/PLDO x 96,5% FMI para 2026) — [CNN Brasil](https://www.cnnbrasil.com.br/blogs/lucinda-pinto/economia/money/macroeconomia/divida-do-brasil-pode-chegar-a-100-do-pib-no-primeiro-ano-do-novo-governo/)
- Resultado primário = receitas − despesas primárias (sem juros); resultado nominal = primário − juros nominais; a diferença entre o nominal e o primário é exatamente a conta de juros, como mostram as séries do BCB (ex.: dez/2015: nominal 10,22% − primário 1,86% ≈ juros 8,37%) — [BCB/SGS série 5727 (nominal)](https://api.bcb.gov.br/dados/serie/bcdata.sgs.5727/dados?formato=json), [série 5793 (primário)](https://api.bcb.gov.br/dados/serie/bcdata.sgs.5793/dados?formato=json), [série 5760 (juros)](https://api.bcb.gov.br/dados/serie/bcdata.sgs.5760/dados?formato=json)
- "Acima da linha" (Tesouro/RTN: soma de receitas e despesas) x "abaixo da linha" (BCB: variação do endividamento) produzem números ligeiramente diferentes para o mesmo governo central — ex.: 2025, Tesouro R$ −61,69 bi; BCB R$ −58,69 bi — [Agência Brasil (BCB)](https://agenciabrasil.ebc.com.br/economia/noticia/2026-01/contas-publicas-tem-deficit-de-r-55021-bilhoes-em-2025); [Tesouro, Série Histórica RTN (xlsx)](https://www.tesourotransparente.gov.br/ckan/dataset/ab56485b-9c40-4efb-8563-9ce3e1973c4b/resource/527ccdb1-3059-42f3-bf23-b5e3ab4c6dc6/download/seriehistoricajul26.xlsx)

### Inferences
- Para checagens, use sempre a mesma métrica ao comparar governos: a DBGG do BCB (série 13762) começa em dez/2006, portanto não cobre o início do governo Lula 1; para 2003-2006 só existe a DLSP (série 4513) ou a DBGG na metodologia antiga.

### Gaps
- Não acessei o Manual de Estatísticas Fiscais do BCB (link citado na NT 47) para detalhar o tratamento de swaps cambiais nos juros.

## Resultado primário do governo central e do setor público consolidado por ano (2003-2025 e parcial 2026)

### Takeaway
O setor público consolidado teve superávits primários de ~3% do PIB entre 2003 e 2008, superávits menores em 2009-2013, déficits ininterruptos de 2014 a 2020 (pico de 9,24% do PIB em 2020), superávits em 2021-2022 e voltou ao déficit em 2023 (2,28%, inflado por R$ 92 bi de precatórios), 2024 (0,40%) e 2025 (0,43%); em 12 meses até ago/2026 o déficit é de 0,62% do PIB.

### Cited Findings

**Setor público consolidado — resultado primário em % do PIB (acumulado no ano; sinal: + superávit / − déficit). Fonte: BCB/SGS série 5793 (NFSP primário, fluxo 12 meses, % PIB; a série está em convenção NFSP, aqui invertida para leitura) — [BCB/SGS 5793](https://api.bcb.gov.br/dados/serie/bcdata.sgs.5793/dados?formato=json&dataInicial=01/12/2002)**
| Ano | Primário | Governo |
|---|---|---|
| 2002 | +3,19 | FHC (referência) |
| 2003 | +3,24 | Lula 1 |
| 2004 | +3,69 | Lula 1 |
| 2005 | +3,74 | Lula 1 |
| 2006 | +3,15 | Lula 1 |
| 2007 | +3,24 | Lula 2 |
| 2008 | +3,33 | Lula 2 |
| 2009 | +1,94 | Lula 2 |
| 2010 | +2,62 | Lula 2 |
| 2011 | +2,94 | Dilma 1 |
| 2012 | +2,18 | Dilma 1 |
| 2013 | +1,71 | Dilma 1 |
| 2014 | −0,56 | Dilma 1 (1º déficit da série) |
| 2015 | −1,86 | Dilma 2 |
| 2016 | −2,48 | Dilma 2 / Temer |
| 2017 | −1,68 | Temer |
| 2018 | −1,55 | Temer |
| 2019 | −0,84 | Bolsonaro |
| 2020 | −9,24 | Bolsonaro (pandemia) |
| 2021 | +0,72 | Bolsonaro |
| 2022 | +1,25 | Bolsonaro |
| 2023 | −2,28 | Lula 3 |
| 2024 | −0,40 | Lula 3 |
| 2025 | −0,43 | Lula 3 |
| 12 m até ago/2026 | −0,62 | Lula 3 **[últ.: ago/2026]** |

- Valores em R$ (BCB): 2025 déficit de R$ 55,021 bi (0,43% do PIB), sendo governo central −R$ 58,687 bi, governos regionais +R$ 9,537 bi; 2024 déficit de R$ 47,553 bi (0,40%) — [Agência Brasil, 30/01/2026](https://agenciabrasil.ebc.com.br/economia/noticia/2026-01/contas-publicas-tem-deficit-de-r-55021-bilhoes-em-2025); estatais 2025: déficit de R$ 5,9 bi — [CNN Brasil](https://www.cnnbrasil.com.br/economia/money/macroeconomia/setor-publico-tem-deficit-de-r-55-bilhoes-em-2025-diz-banco-central/)
- 2023: déficit consolidado de R$ 249,1 bi (2,28% do PIB), "primeiro resultado deficitário desde 2020", influenciado pelo pagamento de R$ 92,4 bi em precatórios; 2022: superávit de R$ 126,0 bi (1,25-1,28%); 2021: superávit de R$ 64,7 bi (0,73%) — [Agência Brasil, 31/01/2025](https://agenciabrasil.ebc.com.br/economia/noticia/2025-01/banco-central-setor-publico-registra-deficit-de-04-do-pib-em-2024); [BCB, Nota de Estatísticas Fiscais jan/2024](https://www.bcb.gov.br/content/estatisticas/hist_estatisticasfiscais/202401_Texto_de_estatisticas_fiscais.pdf)
- Agosto/2026 (mensal): consolidado −R$ 10,0 bi (governo central −R$ 14,7 bi; regionais +R$ 2,7 bi; estatais +R$ 2,0 bi); 12 meses: −R$ 82,1 bi (0,62% do PIB) — [Poder360 (BCB, 30/09/2026)](https://www.poder360.com.br/poder-economia/divida-bruta-atinge-829-do-pib-em-agosto-diz-banco-central/)

**Governo central (Tesouro + Previdência + BC) — resultado primário "acima da linha", R$ milhões correntes e % do PIB. Fonte: Tesouro Nacional, Série Histórica RTN, Tabelas 2.1 e 2.1-A — [planilha oficial](https://www.tesourotransparente.gov.br/ckan/dataset/ab56485b-9c40-4efb-8563-9ce3e1973c4b/resource/527ccdb1-3059-42f3-bf23-b5e3ab4c6dc6/download/seriehistoricajul26.xlsx) (dataset [Resultado do Tesouro Nacional](https://www.tesourotransparente.gov.br/ckan/dataset/resultado-do-tesouro-nacional))**
| Ano | R$ milhões | % PIB | Receita líq. % PIB | Despesa % PIB |
|---|---|---|---|---|
| 2003 | +39.080 | +2,27 | 17,42 | 15,14 |
| 2004 | +49.341 | +2,52 | 18,13 | 15,61 |
| 2005 | +52.673 | +2,43 | 18,78 | 16,35 |
| 2006 | +48.748 | +2,02 | 18,78 | 16,76 |
| 2007 | +57.650 | +2,12 | 18,98 | 16,87 |
| 2008 | +71.438 | +2,30 | 18,92 | 16,62 |
| 2009 | +39.436 | +1,18 | 18,56 | 17,37 |
| 2010 | +77.891 | +2,00 | 20,21 | 18,20 |
| 2011 | +91.891 | +2,10 | 18,86 | 16,76 |
| 2012 | +84.988 | +1,77 | 18,71 | 16,95 |
| 2013 | +72.159 | +1,35 | 18,70 | 17,35 |
| 2014 | −23.482 | −0,41 | 17,70 | 18,11 |
| 2015 | −120.502 | −2,01 | 17,42 | 19,43 |
| 2016 | −161.276 | −2,57 | 17,37 | 19,95 |
| 2017 | −124.261 | −1,89 | 17,54 | 19,43 |
| 2018 | −120.221 | −1,72 | 17,59 | 19,31 |
| 2019 | −95.065 | −1,29 | 18,23 | 19,52 |
| 2020 | −743.255 | −9,77 | 15,83 | 25,59 |
| 2021 | −35.068 | −0,39 | 17,52 | 17,91 |
| 2022 | +46.408 | +0,46 | 18,41 | 17,95 |
| 2023 | −228.499 | −2,09 | 17,38 | 19,46 |
| 2024 | −42.924 | −0,36 | 18,35 | 18,72 |
| 2025 | −61.694 | −0,48 | 18,31 | 18,80 |
| jan-jul/2026 | −81.305 (jan-jul/2025: −70.347) | — | — | — |

- Nota: o valor de 2023 na série atual (R$ −228,5 bi) é menor que o divulgado em jan/2024 por revisões posteriores; o Tesouro também reporta a versão "abaixo da linha" (BCB) na Tabela 2.1 (2023: −R$ 264,5 bi; 2020: −R$ 745,3 bi; 2022: +R$ 54,9 bi) — [Tesouro, Série Histórica RTN](https://www.tesourotransparente.gov.br/ckan/dataset/ab56485b-9c40-4efb-8563-9ce3e1973c4b/resource/527ccdb1-3059-42f3-bf23-b5e3ab4c6dc6/download/seriehistoricajul26.xlsx)
- 2025 detalhado (Tesouro): déficit de R$ 61,69 bi (0,48% do PIB), +32,3% real sobre 2024 (R$ 42,92 bi; 0,36%); Tesouro+BC superávit de R$ 255,5 bi; RGPS déficit de R$ 317,2 bi; receita líquida +2,8% real (R$ +64,3 bi), despesa +3,4% real (R$ +79,1 bi); IR +R$ 43,56 bi (+5,2%), IOF +R$ 15,4 bi (+21,3%), dividendos −R$ 26,3 bi (−34,3%); benefícios previdenciários +R$ 41,4 bi (+4,1%), BPC +R$ 10,8 bi (+9,1%), pessoal +R$ 16,9 bi (+4,3%), Fundeb +R$ 10 bi (+19,7%), discricionárias +R$ 11,9 bi (+6,1%), gastos extraordinários −R$ 20,7 bi (fim das ações de calamidade do RS) — [Agência Brasil, 29/01/2026](https://agenciabrasil.ebc.com.br/economia/noticia/2026-01/deficit-primario-do-governo-central-totaliza-r-617-bilhoes-em-2025)
- 2026 parcial (Ipea, com dados do Tesouro): déficit acumulado jan-ago/2026 de R$ 93,7 bi (jan-ago/2025: R$ 87,4 bi; valores a preços de ago/2026); 12 meses: −R$ 68,7 bi (~0,53% do PIB); receita líquida jan-ago +5,7% real, despesa +5,7% real; discricionárias +31,8%; créditos extraordinários +283,5% — [Ipea, Carta de Conjuntura, 08/10/2026](https://www.ipea.gov.br/cartadeconjuntura/index.php/2026/10/panorama-fiscal-evolucao-recente-e-perspectivas-10/); agosto/2026 mensal: déficit de R$ 13,6 bi (ago/2025: R$ 15,5 bi), receita +3,5% real, despesa +1,9% real — [Tesouro, RTN ago/2026 (29/09/2026)](https://www.tesourotransparente.gov.br/publicacoes/boletim-resultado-do-tesouro-nacional-rtn/2026/8) **[últ.: ago/2026]**
- Componentes estruturais (Tesouro, % PIB): benefícios previdenciários 6,24% (2003) → 6,56% (2010) → 8,10% (2016) → 8,72% (2020) → 8,06% (2025); pessoal e encargos 4,46% (2003) → 4,33% (2010) → 4,11% (2016) → 3,16% (2025); sentenças judiciais e precatórios (custeio e capital) R$ 17,3 bi (2022) → R$ 71,4 bi (2023; 0,65% PIB) → R$ 34,3 bi (2024) → R$ 42,8 bi (2025) — [Tesouro, Série Histórica RTN, Tabelas 2.2 e 2.2-A](https://www.tesourotransparente.gov.br/ckan/dataset/ab56485b-9c40-4efb-8563-9ce3e1973c4b/resource/527ccdb1-3059-42f3-bf23-b5e3ab4c6dc6/download/seriehistoricajul26.xlsx)

### Inferences
- Anos de superávit do governo central (Tesouro): 2003-2013 (11 anos seguidos) e 2022; anos de déficit: 2014-2021 e 2023-2025. No consolidado: superávits 2003-2013, 2021 e 2022; déficits 2014-2020 e 2023-2025.
- Fatos favoráveis/desfavoráveis por governo (apenas a partir dos números acima): Lula 1-2 teve o maior superávit médio (~3,2% PIB em 2003-2008), mas o superávit caiu em 2009 (crise global) e a receita de 2010 foi inflada pela capitalização da Petrobras (receita líquida saltou para 20,21% do PIB e recuou para 18,86% em 2011). Dilma herdou superávit de 2,6% e entregou déficit de 2,5% (2016). Temer reduziu o déficit de 2,48% para 1,55%. Bolsonaro reduziu para 0,84% em 2019, teve o maior déficit da série em 2020 (9,24%) e entregou superávit de 1,25% em 2022 (ajudado por inflação, commodities e dividendos). Lula 3 teve déficit de 2,28% em 2023 (com R$ 92 bi de precatórios atrasados), reduziu para 0,40-0,43% em 2024-2025, mas a tendência em 12 meses voltou a piorar em 2026 (0,62% em ago/2026).

### Gaps
- Não encontrei fonte oficial consolidada com as metas de superávit primário fixadas nas LDOs de 2003-2014 (ex.: 4,25%/3,75%/3,1% do PIB e abatimentos do PAC); o artigo dos Cadernos de Finanças Públicas do Tesouro acessado só trata do arcabouço de 2023. Tratar como lacuna.
- As notas mensais do BCB (PDF) não foram lidas diretamente; as revisões de PIB alteram os % do PIB em centésimos entre publicações (ex.: 2024 DBGG 76,1% em jan/2025 e 76,27% na série atual).

## Dívida Bruta do Governo Geral e Dívida Líquida por ano, fim de cada governo, nível atual e projeções

### Takeaway
A DBGG/PIB (BCB, série 13762) caiu de 55,5% (dez/2006) para 51,8% (dez/2010), subiu para 69,8% (dez/2016) e 75,3% (dez/2018), chegou a 86,9% em dez/2020 e recuou para 71,7% em dez/2022; desde então subiu para 78,6% (dez/2025) e 82,9% em ago/2026 — maior nível desde mar/2021 — com projeções de 83,4% (Focus/Prisma) para 2026 e trajetória ascendente até 2030-2036 segundo Focus, IFI e FMI.

### Cited Findings

**DBGG (% PIB, dezembro de cada ano) — [BCB/SGS série 13762](https://api.bcb.gov.br/dados/serie/bcdata.sgs.13762/dados?formato=json&dataInicial=01/12/2006) | DLSP (% PIB, dezembro) — [BCB/SGS série 4513](https://api.bcb.gov.br/dados/serie/bcdata.sgs.4513/dados?formato=json&dataInicial=01/12/2002)**
| Dez de | DBGG | DLSP | Governo |
|---|---|---|---|
| 2002 | n.d. (série começa 2006) | 59,93 | FHC (ref.) |
| 2003 | n.d. | 54,26 | Lula 1 |
| 2004 | n.d. | 50,19 | Lula 1 |
| 2005 | n.d. | 47,92 | Lula 1 |
| 2006 | 55,48 | 46,49 | Lula 1 |
| 2007 | 56,72 | 44,55 | Lula 2 |
| 2008 | 55,98 | 37,57 | Lula 2 |
| 2009 | 59,21 | 40,88 | Lula 2 |
| 2010 | 51,77 | 37,98 | **fim Lula 2** |
| 2011 | 51,27 (mínimo da série) | 34,47 | Dilma 1 |
| 2012 | 53,67 | 32,19 | Dilma 1 |
| 2013 | 51,54 | 30,50 (mínimo DLSP) | Dilma 1 |
| 2014 | 56,28 | 32,59 | Dilma 1 |
| 2015 | 65,50 | 35,64 | Dilma 2 |
| 2016 | 69,84 | 46,14 | **Dilma afastada mai/2016; Temer** |
| 2017 | 73,72 | 51,37 | Temer |
| 2018 | 75,27 | 52,77 | **fim Temer** |
| 2019 | 74,44 | 54,70 | Bolsonaro |
| 2020 | 86,94 | 61,37 | Bolsonaro (pico) |
| 2021 | 77,31 | 55,11 | Bolsonaro |
| 2022 | 71,68 | 56,13 | **fim Bolsonaro** |
| 2023 | 73,83 | 60,43 | Lula 3 |
| 2024 | 76,27 | 61,30 | Lula 3 |
| 2025 | 78,64 | 65,24 | Lula 3 |
| ago/2026 | 82,87 | 69,27 | Lula 3 **[últ.: ago/2026]** |

- Trajetória mensal 2026 da DBGG: mar 79,88%; abr 80,09%; mai 81,04%; jun 81,95%; jul 82,55%; ago 82,87% — [BCB/SGS 13762](https://api.bcb.gov.br/dados/serie/bcdata.sgs.13762/dados?formato=json&dataInicial=01/01/2026)
- Ago/2026 em R$: DBGG R$ 11,1 trilhões (82,9% do PIB), "maior patamar em termos percentuais do PIB desde março de 2021 (85,1%)"; variação no mês +0,3/0,4 p.p.: juros apropriados +0,8 p.p., câmbio +0,1 p.p., PIB nominal −0,5 p.p.; variação acumulada no ano +4,2 p.p.: juros +6,5 p.p., emissões líquidas +1,5 p.p., PIB nominal −3,6 p.p., câmbio −0,2 p.p. — [Poder360](https://www.poder360.com.br/poder-economia/divida-bruta-atinge-829-do-pib-em-agosto-diz-banco-central/); [CNN Brasil](https://www.cnnbrasil.com.br/economia/money/macroeconomia/bc-divida-bruta-do-governo-geral-avanca-para-829-do-pib-em-agosto/); DLSP ago/2026: R$ 9,2 tri (69,3% do PIB) — [Ipea](https://www.ipea.gov.br/cartadeconjuntura/index.php/2026/10/panorama-fiscal-evolucao-recente-e-perspectivas-10/)
- Fim de 2025: DBGG R$ 10,017 tri (78,7%); DLSP R$ 8,311 tri (65,3%), "maior da série histórica"; fim de 2024: DBGG R$ 8,984 tri (76,3%), DLSP R$ 7,220 tri (61,3%); o real valorizou 11,1% em 2025, o que elevou a dívida líquida (reservas valem menos em R$) — [Agência Brasil, 30/01/2026](https://agenciabrasil.ebc.com.br/economia/noticia/2026-01/contas-publicas-tem-deficit-de-r-55021-bilhoes-em-2025)
- Fatores da DLSP em 2024 (p.p. do PIB): juros nominais +8,0; déficit primário +0,4; crescimento do PIB nominal −4,4; privatizações −0,3; ajuste externo −0,3; desvalorização cambial de 27,9% no ano (aumenta) — [Agência Brasil, 31/01/2025](https://agenciabrasil.ebc.com.br/economia/noticia/2025-01/banco-central-setor-publico-registra-deficit-de-04-do-pib-em-2024)
- IFI: em 12 meses até jul/2026, juros nominais e emissões líquidas responderam por +10,5 p.p. do PIB de aumento da DBGG, contra −5,2 p.p. de redução pelo crescimento do PIB — "mesmo quando a política fiscal cumpre formalmente as metas estabelecidas, o serviço da própria dívida pode superar o esforço de consolidação" — [IFI, RAF 116, set/2026, p. 45](https://www12.senado.leg.br/ifi/pdf/raf116_set2026.pdf)
- Marcos históricos citados pelo BCB: DBGG/PIB 74,0% em 2017 x 55,5% em 2006 — [BCB, Nota Técnica 47](https://www.bcb.gov.br/content/publicacoes/notastecnicas/47_notas_tecnicas_julho_2018.pdf); máximo da série 87,66% em out/2020 e mínimo 51,27% em dez/2011 (agregador privado, conferir com SGS) — [Daddus Consultoria](https://www.daddusconsultoria.com/conteudos/indicadores/divida-bruta-pib)
- Dívida Pública Federal (DPF, Tesouro): ~R$ 9,3 tri em ago/2026, ~96% interna (DPMFi), prazo médio ~4 anos; custo implícito 12 meses: LFT ~15,0% a.a., LTN ~12,6%, NTN-B ~10,5%, dívida bruta ~13,0%, líquida ~14,8% — [Ipea, 08/10/2026](https://www.ipea.gov.br/cartadeconjuntura/index.php/2026/10/panorama-fiscal-evolucao-recente-e-perspectivas-10/)

**Projeções para 2026 e além**
- Prisma Fiscal (mediana de analistas privados, Ministério da Fazenda, 15/10/2026): DBGG 83,4% do PIB em 2026 (83,2% em setembro) e 87% em 2027; déficit primário 2026 de R$ 53,0 bi e 2027 de R$ 44,0 bi — [CNN Brasil](https://www.cnnbrasil.com.br/economia/money/macroeconomia/mercado-eleva-projecao-de-deficit-em-2026-para-r-53-bi-diz-prisma-fiscal/)
- Focus (BCB, citado pelo Ipea): DBGG 83,4% em 2026 e 95,1% em 2030 — [Ipea, 08/10/2026](https://www.ipea.gov.br/cartadeconjuntura/index.php/2026/10/panorama-fiscal-evolucao-recente-e-perspectivas-10/)
- IFI (RAF 113, jun/2026): cenário base com DBGG de 80,1% (atual) → 82,5% em 2026 → >100% em 2032 → 115% em 2036; superávit primário necessário para estabilizar a dívida: 2,1% do PIB/ano, inatingível antes de 2029 mesmo no cenário otimista; despesa primária 19,2% do PIB (2026) → 19,9% (2032); receita líquida 18,9% → 18,3% — [Senado Notícias, 25/06/2026](https://www12.senado.leg.br/noticias/materias/2026/06/25/ifi-proximo-presidente-da-republica-tera-de-enfrentar-decisoes-fiscais-dificeis); [Poder360](https://www.poder360.com.br/poder-economia/proximo-presidente-tera-decisoes-fiscais-dificeis-diz-ifi/)
- IFI (RAF 116, set/2026, tabela de projeções): DBGG 82,5% em 2026 e 86,4% em 2027; resultado primário do setor público consolidado −0,5% (2026) e −0,7% (2027); juros nominais líquidos 8,6% (2026) e 8,5% (2027); resultado nominal −9,0% (2026) e −9,2% (2027); Selic 14,0% fim-2026 e 12,0% fim-2027 — [IFI, RAF 116, p. 58](https://www12.senado.leg.br/ifi/pdf/raf116_set2026.pdf)
- Tesouro (citado no fechamento de 2025): dívida de 79,3% do PIB em 2025 com projeção de 88,6% em 2032 — [Gazeta do Povo, 30/01/2026](https://www.gazetadopovo.com.br/economia/governo-cumpre-meta-fiscal-2025-rombo-61-bi/)
- FMI (Artigo IV 2026, divulgado 23/07/2026, metodologia FMI): dívida bruta de 97,8% do PIB em 2026; sem medidas, 106% em 2035; com ajuste de 3 p.p. do PIB em 5 anos (2026-2031), ~85% em 2031 — [Poder360](https://www.poder360.com.br/poder-economia/brasil-crescera-24-em-2026-e-divida-se-aproxima-de-100-do-pib/)
- FMI (Fiscal Monitor abr/2026, Tabela A15, metodologia FMI): Brasil 87,0% (2024), 93,3% (2025), 96,5% (2026), 100,0% (2027), 102,3% (2028), 106,5% (2031) — [FMI](https://www.imf.org/-/media/files/publications/fiscal-monitor/2026/april/english/text.pdf)
- Moody's (jul/2026): sem reformas, dívida sobe de ~80% para 90% do PIB até 2030 — [Seu Dinheiro](https://www.seudinheiro.com/2026/economia/a-moodys-esta-de-olho-no-brasil-e-esses-sao-os-pontos-fortes-e-fracos-para-o-rating-soberano-subir-mlim/)

### Inferences
- Variação da DBGG por mandato (dez a dez, série BCB): Lula 2 (2006→2010) −3,7 p.p.; Dilma (2010→2016) +18,1 p.p.; Temer (2016→2018) +5,4 p.p.; Bolsonaro (2018→2022) −3,6 p.p. (apesar do pico de +11,7 p.p. em 2020); Lula 3 (2022→ago/2026) +11,2 p.p. A queda de 2021-2022 veio em boa parte de inflação alta (PIB nominal) e devolução de recursos do BNDES, não apenas de superávit; a alta de 2023-2026 veio sobretudo de juros (Selic a 15%, ver seção de juros).
- A DLSP caiu de 59,9% (2002) para 30,5% (2013) e voltou a 69,3% (ago/2026): entre 2008 e 2015 a DLSP ficou artificialmente baixa em relação à DBGG por causa dos empréstimos do Tesouro ao BNDES (ativo do governo), razão pela qual o BCB e o FMI privilegiam a DBGG.

### Gaps
- Não obtive o documento original do Artigo IV 2026 do FMI (a página de país do FMI acessada listava como último Artigo IV o de 17/07/2025); os números de 97,8% e do ajuste de 3 p.p. vêm do Poder360. Há divergência não explicada entre 97,8% (Artigo IV) e 96,5% (Fiscal Monitor) para 2026.
- Não foi possível ler o Boletim Focus diretamente; o dado (83,4%/95,1%) é o citado pelo Ipea.

## Regras fiscais: metas de superávit (2003-2014), pedaladas e impeachment, Teto de Gastos (EC 95/2016) e seus furos, PEC da Transição, Arcabouço (LC 200/2023) e cumprimento das metas 2023-2026

### Takeaway
O Brasil trocou três vezes de regra em dez anos: metas de superávit via LDO (até 2014, abandonadas com déficit em 2014 e as "pedaladas" que levaram à rejeição das contas de 2014 pelo TCU), Teto de Gastos (2016-2022, furado por EC 109, 113, 123 e 126, esta última abrindo R$ 145 bi) e Arcabouço (2023-), cujas metas de 2024 e 2025 foram cumpridas "formalmente" apenas com deduções (R$ 48,7 bi em 2025) e a banda de tolerância, e cuja meta de 2026 (superávit de 0,25%) exigiu contingenciamento de R$ 13,6 bi em set/2026.

### Cited Findings

**Pedaladas e impeachment (Dilma)**
- O TCU rejeitou por unanimidade as contas de 2014 do governo Dilma em 07/10/2015 por causa das "pedaladas fiscais" (atrasos de repasses do Tesouro a bancos públicos para inflar o primário) — [Wikipedia "Fiscal pedaling", citando Estadão 07/10/2015](https://en.wikipedia.org/wiki/Fiscal_pedaling)
- Ministério Público de Contas (TCU): atrasos a bancos públicos somaram R$ 40,2 bi no 1º semestre de 2015 (R$ 24,5 bi BNDES, R$ 13,5 bi BB, R$ 2,2 bi Caixa), acima dos R$ 37,5 bi de todo 2014 — [MPC-ES, out/2015](https://www.mpc.es.gov.br/2015/10/relatorio-do-ministerio-publico-de-contas-no-tcu-diz-que-dilma-repetiu-pedaladas-em-2015/)
- Auditoria do TCU (30/06/2016) sobre 2015: R$ 5,63 bi (Banco do Brasil) e R$ 8,04 bi (BNDES) em "empréstimos ilegais", 11 autoridades responsabilizadas, incluindo o ex-ministro Joaquim Levy — [Correio Braziliense](https://www.correiobraziliense.com.br/app/noticia/politica/2016/06/30/interna_politica,538458/auditoria-do-tcu-confirma-pedaladas-fiscais-de-dilma-em-2015.shtml)
- Decretos de crédito suplementar de R$ 2,5 bi (jul-ago/2015) incompatíveis com a meta fiscal integraram a denúncia do impeachment — [PSDB-PE (nota partidária, usar com cautela)](https://www.psdb.org.br/pe/tcu-ve-indicios-de-pedaladas-fiscais-nas-contas-do-governo-dilma-de-2015-petista-tera-30-dias-para-se-explicar/)
- Secretário do TCU Leonardo Albernaz à comissão do impeachment (13/06/2016): pedaladas registradas em 2014 e 2015 foram "violação da responsabilidade fiscal", em "dezenas de bilhões de reais"; a defesa (José Eduardo Cardozo) alegou que a jurisprudência do TCU mudou entre 2009 e 2014 — [Senado Notícias, 14/06/2016](https://www12.senado.leg.br/noticias/materias/2016/06/14/secretario-do-tcu-afirma-que-pedalada-e-violacao-da-responsabilidade-fiscal)
- Resultado fiscal associado: 1º déficit primário da série em 2014 (−0,56% consolidado; −0,41% governo central) e déficits de 1,86% e 2,48% em 2015-2016 — [BCB/SGS 5793](https://api.bcb.gov.br/dados/serie/bcdata.sgs.5793/dados?formato=json&dataInicial=01/12/2013); [Tesouro RTN](https://www.tesourotransparente.gov.br/ckan/dataset/ab56485b-9c40-4efb-8563-9ce3e1973c4b/resource/527ccdb1-3059-42f3-bf23-b5e3ab4c6dc6/download/seriehistoricajul26.xlsx)

**Teto de Gastos — EC 95/2016 (Temer)**
- Promulgada em 15/12/2016; limita despesas primárias dos três Poderes, MPU e DPU ao valor do ano anterior corrigido pelo IPCA por 20 anos, com revisão da regra de correção possível a partir do 10º ano; votos: Câmara 366-111 (1º turno, 10/10/2016) e 359-116 (25/10/2016); Senado 61-14 (29/11/2016) e 53-16 (13/12/2016); crítica de Nelson Barbosa aos gatilhos ("defeito de fabricação") — [Wikipedia pt "Novo Regime Fiscal"](https://pt.wikipedia.org/wiki/Novo_Regime_Fiscal)
- Alterações: EC 109/2021 (PEC Emergencial, mar/2021) acionou gatilhos quando despesas obrigatórias superassem 95% da despesa primária; EC 113/2021 (PEC dos Precatórios, dez/2021) mudou a correção do teto para IPCA jan-dez, abrindo ~R$ 65 bi em 2022; EC 126/2022 revogou a maior parte dos artigos da EC 95 — [Wikipedia pt "Novo Regime Fiscal"](https://pt.wikipedia.org/wiki/Novo_Regime_Fiscal)

**Furos ao teto (Bolsonaro)**
- PEC dos Precatórios (EC 113/2021, promulgada 08/12/2021): espaço fiscal total estimado pela Consultoria de Orçamento da Câmara em R$ 108,4 bi para 2022 — R$ 64,9 bi garantidos pela mudança na correção do teto (uso restrito a saúde, previdência e assistência), R$ 39,485 bi pelo limite de pagamento de precatórios (financiando o Auxílio Brasil) e R$ 4,08 bi por precatórios parcelados fora do limite — [Agência Câmara, 08/12/2021](https://www.camara.leg.br/noticias/836271-pec-dos-precatorios-abre-espaco-de-r-65-bilhoes-no-orcamento-de-2022); Tesouro (Esteves Colnago): espaço de R$ 106,1 bi em 2022, apenas R$ 1,1 bi livre — [Forbes/Reuters, nov/2021](https://forbes.com.br/forbes-money/2021/11/pec-dos-precatorios-abre-espaco-de-r-1061-bilhoes-em-2022-mas-so-r-11-bilhao-esta-livre/)
- "PEC Kamikaze"/PEC das Bondades (EC 123/2022, promulgada 14/07/2022): declarou estado de emergência e autorizou ~R$ 41,2-41,25 bi fora das regras fiscais em ano eleitoral: Auxílio Brasil de R$ 400 → R$ 600 e 1,6 mi de novas famílias (~R$ 26 bi), voucher caminhoneiros R$ 1.000 (~R$ 5,4 bi), crédito etanol (até R$ 3,8 bi), transporte de idosos (R$ 2,5 bi), taxistas (até R$ 2 bi), auxílio-gás (R$ 1,05 bi), Alimenta Brasil (R$ 0,5 bi); votos: Senado 72-1 e 67-1 (30/06/2022), Câmara 393-14 e 469-17 (12/07/2022); único voto contra no Senado: José Serra, que disse que a PEC passava por cima de "todas as regras fiscais" — [Wikipedia pt "PEC Kamikaze" (com referências G1/Estado de Minas)](https://pt.wikipedia.org/wiki/PEC_Kamikaze); texto oficial: [Planalto, EC 123](http://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc123.htm) (servidor retornou erro 503 em 21/10/2026)

**PEC da Transição (EC 126/2022)**
- Promulgada em 21/12/2022: R$ 145 bi de despesas fora do teto por um ano (R$ 70 bi para o Bolsa Família de R$ 600 + R$ 150 por criança até 6 anos; R$ 75 bi para outras áreas, incluindo R$ 16,6 bi saúde/Farmácia Popular e R$ 6,8 bi para o aumento real do salário mínimo); mais R$ 23 bi para investimentos; dispensa da regra de ouro para os R$ 145 bi e exclusão desses valores da meta de primário; obrigou o presidente a enviar PLP de novo regime fiscal até 31/08/2023; redistribuiu as emendas de relator (77,5% Câmara / 22,5% Senado) e elevou o limite de restos a pagar de emendas de 0,6% para 1% da receita — [Agência Brasil, 21/12/2022](https://agenciabrasil.ebc.com.br/politica/noticia/2022-12/congresso-promulga-pec-da-transicao)
- Transparência Brasil: a EC 126/2022 deu ao relator-geral do orçamento de 2023 poder para destinar R$ 9,85 bi em emendas e remanejar recursos para comissões; emendas de comissão saltaram de R$ 329 mi (2022) para R$ 6,9 bi (2023) — [Transparência Brasil, nota técnica jul/2024](https://www.transparencia.org.br/downloads/publicacoes/continuidadedoorcamentosecreto.pdf)

**Arcabouço Fiscal / Regime Fiscal Sustentável (LC 200/2023)**
- Regras: despesa cresce no máximo 70% do crescimento real da receita, com piso de 0,6% e teto de 2,5% reais ao ano; se a meta for descumprida, crescimento cai a 50%; metas originais: 2024 zero, 2025 +0,5%, 2026 +1,0% do PIB; Câmara aprovou por 372-108 em 1º turno; Senado (relator Omar Aziz) 57-17, excluindo Fundeb, FCDF e C&T dos limites; vigência fim de ago/2023 — [Wikipedia pt "Novo arcabouço fiscal"](https://pt.wikipedia.org/wiki/Novo_arcabou%C3%A7o_fiscal); metas no PLP original em R$: 2024 R$ 0; 2025 R$ 61,61 bi; 2026 R$ 130,83 bi; banda de 0,25 p.p.; 70% do excedente acima da banda pode ir para investimento — [Tesouro, Cadernos de Finanças Públicas nº 3](https://publicacoes.tesouro.gov.br/index.php/cadernos/article/download/220/352/1134)
- Metas revisadas: 2025 = resultado zero com banda de ±0,25 p.p. (~R$ 31 bi); 2026 = superávit de 0,25% do PIB (R$ 34,3 bi) com banda de 0,25 p.p.; 2027 = superávit de 0,5% (R$ 73,2 bi; piso R$ 36,6 bi) — [Agência Brasil, 29/01/2026](https://agenciabrasil.ebc.com.br/economia/noticia/2026-01/deficit-primario-do-governo-central-totaliza-r-617-bilhoes-em-2025); [Agência Brasil, ago/2025](https://agenciabrasil.ebc.com.br/economia/noticia/2025-08/orcamento-de-2026-tem-meta-de-superavit-de-r-343-bilhoes); [IFI, RAF 116](https://www12.senado.leg.br/ifi/pdf/raf116_set2026.pdf)
- Cumprimento 2023: déficit efetivo de R$ 228,5-230,5 bi (2,09% do PIB), com R$ 92,4 bi de precatórios pagos após decisão do STF; o arcabouço só vigorou para a meta a partir de 2024 — [Tesouro RTN](https://www.tesourotransparente.gov.br/ckan/dataset/ab56485b-9c40-4efb-8563-9ce3e1973c4b/resource/527ccdb1-3059-42f3-bf23-b5e3ab4c6dc6/download/seriehistoricajul26.xlsx); [Agência Brasil, 31/01/2025](https://agenciabrasil.ebc.com.br/economia/noticia/2025-01/banco-central-setor-publico-registra-deficit-de-04-do-pib-em-2024)
- Cumprimento 2024: déficit efetivo de R$ 42,92 bi (0,36% do PIB), "puxado pelas enchentes no Rio Grande do Sul"; o governo considerou a meta (zero ± 0,25 p.p.) cumprida formalmente — [Agência Brasil, 29/01/2026](https://agenciabrasil.ebc.com.br/economia/noticia/2026-01/deficit-primario-do-governo-central-totaliza-r-617-bilhoes-em-2025); [Metrópoles, 02/02/2026](https://www.metropoles.com/brasil/governo-lula-tirou-r-486-bilhoes-do-calculo-da-meta-fiscal)
- Cumprimento 2025: déficit efetivo R$ 61,69 bi (0,48%); deduções autorizadas de R$ 48,68 bi — precatórios excedentes R$ 41,15 bi, ressarcimento de descontos indevidos do INSS R$ 2,83 bi, defesa R$ 2,5 bi, educação/saúde temporárias R$ 2,2 bi — resultado para a meta: déficit de R$ 13 bi (0,10% do PIB), dentro do piso de −R$ 31 bi; "empoçamento" de R$ 8 bi de emendas não gastas ajudou — [Agência Brasil](https://agenciabrasil.ebc.com.br/economia/noticia/2026-01/deficit-primario-do-governo-central-totaliza-r-617-bilhoes-em-2025); [Gazeta do Povo](https://www.gazetadopovo.com.br/economia/governo-cumpre-meta-fiscal-2025-rombo-61-bi/); IFI: cumprir as metas de 2024 e 2025 "não necessariamente demonstra esforço fiscal"; Jeferson Bittencourt (ASA): metade da melhora prometida se perde em exceções — [Metrópoles](https://www.metropoles.com/brasil/governo-lula-tirou-r-486-bilhoes-do-calculo-da-meta-fiscal); secretário do Tesouro Rogério Ceron: resultado "muito satisfatório"; o ideal seria um limite "sem tantas exceções" — [Gazeta do Povo](https://www.gazetadopovo.com.br/economia/governo-cumpre-meta-fiscal-2025-rombo-61-bi/)
- TCU alertou o governo sobre mirar o piso da banda em 2025 (equivalente a −R$ 31 bi) — [Metrópoles, 29/12/2025](https://www.metropoles.com/brasil/economia-br/entenda-a-situacao-fiscal-que-o-governo-vai-enfrentar-em-2026)
- Cumprimento 2026 (em curso): Relatório de Avaliação do 4º bimestre (24-25/09/2026) elevou o déficit efetivo projetado de R$ 52,0 bi para R$ 80,9 bi; deduções autorizadas R$ 67,29 bi; resultado para a meta: déficit de R$ 13,65 bi, abaixo do piso (zero), exigindo contingenciamento de R$ 13,6 bi (mais bloqueio de R$ 2,5 bi pelo limite de despesa; total congelado R$ 16,1 bi); em julho o mesmo cálculo mostrava superávit de R$ 10,8 bi — [ACIARA/Agência Brasil, 25/09/2026](https://aciara.com.br/governo-eleva-rombo-fiscal-de-2026-para-bilhoes/); [Ipea](https://www.ipea.gov.br/cartadeconjuntura/index.php/2026/10/panorama-fiscal-evolucao-recente-e-perspectivas-10/); IFI (ago/2026): déficit efetivo de 0,4% do PIB em 2026 (governo e IFI); cumprimento formal depende de deduções de R$ 62,8 bi (governo) a R$ 69,8 bi (IFI); déficit primário estrutural de 1,4% do PIB nos 4 trimestres até jun/2026 (0,7% um ano antes) — [CNN Brasil, 20/08/2026](https://www.cnnbrasil.com.br/economia/money/macroeconomia/ifi-alerta-para-despesas-crescendo-acima-das-receitas-e-deficit-estrutural/)
- Haddad (dez/2025): governo "está mirando o centro da meta fiscal", mas trabalha com a banda e conta com "empoçamento"; nota da Fazenda: "o déficit primário acumulado do Governo Lula 3 será 70% menor" que o do governo Bolsonaro — [Metrópoles](https://www.metropoles.com/brasil/economia-br/entenda-a-situacao-fiscal-que-o-governo-vai-enfrentar-em-2026)
- 2027 (PLOA 2027): governo projeta superávit efetivo de R$ 18,6 bi (0,1% PIB) e R$ 83,4 bi após deduções de R$ 64,7 bi (R$ 59,2 bi precatórios/RPV excedentes = 39,4% da despesa com precatórios; R$ 5,0 bi defesa; R$ 0,6 bi Fundo Social); IFI projeta déficit efetivo de R$ 86,1 bi (−0,6% PIB) e superávit apurado de só R$ 0,9 bi, abaixo do piso de R$ 36,6 bi — contingenciamento necessário de R$ 35,7 bi; divergência total R$ 104,8 bi, por premissas (PIB 2,5% governo x 1,8% IFI x 1,5% Focus; IPCA 3,6% x 4,0% x 4,3%; massa salarial +10,1% x +7,3%); receita condicionada de R$ 42 bi do Imposto Seletivo "cujo projeto sequer foi enviado" — [IFI, RAF 116, p. 3-4 e 27](https://www12.senado.leg.br/ifi/pdf/raf116_set2026.pdf)
- Exceções acumuladas: IFI estima deduções da meta de até R$ 157,3 bi em 2024-2026 (Pé-de-Meia, defesa, socorro ao "tarifaço" de R$ 9,5 bi etc.); Correios: até R$ 10 bi fora do resultado das estatais; Novo PAC: até R$ 5 bi; precatórios 2026: R$ 55,1 bi autorizados fora do cálculo; despesa primária +17% real 2023-2026 — [Gazeta do Povo, 22/12/2025](https://www.gazetadopovo.com.br/economia/com-puxadinhos-no-orcamento-governo-lula-legaliza-fracasso-do-arcabouco-fiscal/); "gastos fora do arcabouço podem chegar a R$ 163 bi até 2026" (título de matéria relacionada) — [Metrópoles](https://www.metropoles.com/brasil/economia-br/entenda-a-situacao-fiscal-que-o-governo-vai-enfrentar-em-2026)
- Precatórios (EC 136/2025, promulgada 09/09/2025, origem PEC 66/2023 de Jader Barbalho): precatórios e RPVs saem do limite de despesa primária federal a partir de 2026; a partir de 2027, 10% do estoque é reincorporado por ano às metas; estoque para 2026 ~R$ 70 bi; estados/municípios pagam entre 1% e 5% da RCL conforme endividamento; correção IPCA + 2% a.a. limitada à Selic — [Senado Notícias](https://www12.senado.leg.br/noticias/materias/2025/09/09/promulgada-emenda-que-limita-pagamento-de-precatorios-veja-novas-regras); crítica: "contornando o muro fiscal (de novo)" — [Blog do IBRE/FGV](https://blogdoibre.fgv.br/posts/pec-6623-contornando-o-muro-fiscal-de-novo)
- IFI: o arcabouço perde eficácia a partir de 2028 pela pressão das despesas obrigatórias; ~metade da despesa federal é indexada ao salário mínimo (INSS, BPC, seguro-desemprego) — [Senado Notícias, 25/06/2026](https://www12.senado.leg.br/noticias/materias/2026/06/25/ifi-proximo-presidente-da-republica-tera-de-enfrentar-decisoes-fiscais-dificeis)

### Inferences
- Atores: no período 2015-2016 o ator decisivo foi o TCU (rejeição das contas) e o Congresso (impeachment); em 2016-2022 o Congresso e o Executivo mudaram a Constituição quatro vezes para abrir espaço no teto (EC 109, 113, 123, 126), sempre com maioria ampla; em 2023-2026 Executivo e Congresso criaram deduções por lei complementar (LC 221, 223, 235) e emenda (EC 136), e o STF atuou nos precatórios (2023) e nas emendas (2022-2026).
- Em termos de "cumprimento", todas as metas 2024-2025 foram cumpridas apenas no critério legal (após deduções e banda); no critério "efetivo" nenhuma foi atingida — e 2026 caminha para o mesmo padrão.

### Gaps
- Não encontrei texto oficial da meta da LDO 2023 (frequentemente citada como déficit de até R$ 231,55 bi) nem o detalhamento oficial das deduções da meta de 2024 (valor exato das despesas com a calamidade do RS excluídas).
- Textos legais no Planalto (EC 95, 123, 126; LC 200) retornaram erro 503 em 21/10/2026; as descrições vêm de Agência Brasil, Agência Câmara, Senado e Wikipedia (com referências).

## Gastos: Auxílio Emergencial, Auxílio Brasil/Bolsa Família, emendas parlamentares/orçamento secreto e STF, precatórios, Desenrola, Pé-de-Meia, isenção do IR até R$ 5 mil

### Takeaway
O Auxílio Emergencial custou entre R$ 293 bi (dados do Senado: ~R$ 230 bi em 2020 + ~R$ 63 bi em 2021) e R$ 352-354 bi (Portal da Transparência, bruto) em 2020-2021; o Bolsa Família custa ~R$ 160 bi/ano desde 2023 (R$ 168,2 bi em 2024); as emendas parlamentares empenhadas saltaram de R$ 13,9 bi (2019) para R$ 47,1 bi (2025) e R$ 40,1 bi até out/2026, com o STF (Rosa Weber em 2022, Flávio Dino desde 2024) impondo rastreabilidade; a isenção do IR até R$ 5 mil (Lei 15.270/2025) custa R$ 25,8 bi em 2026, com compensação prevista de R$ 34,1 bi via tributação de dividendos.

### Cited Findings

**Auxílio Emergencial (2020-2021) e Auxílio Brasil (2021-2022)**
- Auxílio Emergencial 2020: ~R$ 230 bi; Auxílio Residual 2021: ~R$ 63 bi; total ~R$ 293 bi (dados do Senado) — [CNN Brasil, checagem 30/03/2022](https://www.cnnbrasil.com.br/politica/fatos-primeiro-verba-do-auxilio-emergencial-nao-equivale-a-15-anos-de-bolsa-familia-como-disse-bolsonaro/); contraditado por total de R$ 352 bi (Portal da Transparência, já descontadas devoluções) — [Poder360, 25/10/2025](https://www.poder360.com.br/poder-governo/governo-federal-deu-r-156-trilhao-em-auxilios-desde-a-pandemia/) e R$ 354 bi — [Poder360, 23/12/2021](https://www.poder360.com.br/governo/custo-do-auxilio-brasil-vai-superar-3-anos-de-bolsa-familia/)
- TCU, Acórdão 2282/2020-Plenário: R$ 167,61 bi pagos até jul/2020; estimativa de R$ 23,7 bi em pagamentos indevidos — [TCU](https://pesquisa.apps.tcu.gov.br/doc/acordao-completo/2282/2020/Plen%C3%A1rio)
- Impacto fiscal: despesa do governo central saltou de 19,52% do PIB (2019) para 25,59% (2020) e o déficit primário para R$ 743,3 bi (9,77%) — [Tesouro RTN](https://www.tesourotransparente.gov.br/ckan/dataset/ab56485b-9c40-4efb-8563-9ce3e1973c4b/resource/527ccdb1-3059-42f3-bf23-b5e3ab4c6dc6/download/seriehistoricajul26.xlsx); gasto total com assistência social: R$ 92,8 bi (2019) → R$ 409,9 bi (2020) — [Poder360, 27/10/2025](https://www.poder360.com.br/poder-governo/gasto-do-governo-com-assistencia-social-triplicou-no-pos-pandemia/)
- Auxílio Brasil 2022: R$ 89,9 bi previstos (benefício de R$ 600 a partir da EC 123) — [Poder360, 23/12/2021](https://www.poder360.com.br/governo/custo-do-auxilio-brasil-vai-superar-3-anos-de-bolsa-familia/); Bolsa Família jan/2004-dez/2019 somou ~R$ 315 bi (MDS) — [CNN Brasil](https://www.cnnbrasil.com.br/politica/fatos-primeiro-verba-do-auxilio-emergencial-nao-equivale-a-15-anos-de-bolsa-familia-como-disse-bolsonaro/)

**Bolsa Família (Lula 3) e outros benefícios**
- Bolsa Família: R$ 168,2 bi pagos em 2024; R$ 158,6 bi reservados para 2025 e R$ 158,6 bi para 2026; ~R$ 13 bi/mês (R$ 12,9 bi em out/2025); BPC: R$ 113,6 bi (2025, estimativa), R$ 9,9 bi em ago/2025; >R$ 30 bi gastos desde 2023 com benefícios concedidos por decisão judicial; Pé-de-Meia: R$ 9,2 bi (2024) e R$ 12,5 bi (2025); total de auxílios 2020-2025: R$ 1,56 tri; assistência social total: R$ 291 bi (2024), R$ 285,8-296 bi (2025), R$ 292,2 bi (2026) — [Poder360, 25/10/2025](https://www.poder360.com.br/poder-governo/governo-federal-deu-r-156-trilhao-em-auxilios-desde-a-pandemia/); [Poder360, 27/10/2025](https://www.poder360.com.br/poder-governo/gasto-do-governo-com-assistencia-social-triplicou-no-pos-pandemia/); contraditado em detalhe por Portal Transparência Brasil (R$ 163,50 bi em 2024; R$ 157,10 bi em 2025) — [busca; página não acessível em 21/10/2026](https://portaltransparenciabrasil.com/beneficios-ao-cidadao/evolucao-historica)
- Reajuste do Bolsa Família (Decreto 13.120) e proibição das bets (MP 1.394) em 2026: deterioração estimada de R$ 27,8 bi frente ao PLOA, antes de compensações — [Ipea, 08/10/2026](https://www.ipea.gov.br/cartadeconjuntura/index.php/2026/10/panorama-fiscal-evolucao-recente-e-perspectivas-10/)
- Pé-de-Meia: após questionamento do TCU (programa financiado por fundo privado fora do orçamento), foi incluído no Orçamento de 2026 e, por LC 235/2026, no piso da educação — [Gazeta do Povo](https://www.gazetadopovo.com.br/economia/com-puxadinhos-no-orcamento-governo-lula-legaliza-fracasso-do-arcabouco-fiscal/); [IFI, RAF 116, p. 4](https://www12.senado.leg.br/ifi/pdf/raf116_set2026.pdf)

**Emendas parlamentares e orçamento secreto**
- Emendas parlamentares por ano (Portal da Transparência/CGU, carregado em 06/10/2026; "pago" inclui restos a pagar), R$ bi: 2014 6,09/4,64; 2015 3,38/2,77; 2016 25,92/23,90; 2017 17,53/15,25; 2018 12,01/10,72; **2019 13,86/12,37; 2020 37,54/33,06; 2021 33,40/28,77; 2022 25,46/23,81; 2023 35,38/29,76; 2024 44,81/39,39; 2025 47,08/36,72; 2026 (parcial) 40,06/25,88**; 2025 por tipo: 52% individuais, 25% bancada, 24% comissão — [Cofre Público/Portal Transparência Brasil (painel)](https://cofrepublico.com.br/emendas-parlamentares/painel)
- Valores no Orçamento aprovado: R$ 53 bi (2025) e R$ 61 bi (2026, recorde; R$ 49,9 bi após vetos/remanejamentos); PLOA 2027 reserva R$ 44,8 bi para impositivas (individuais 2% da RCL — 1,55 p.p. Câmara, 0,45 Senado — e bancada 1% da RCL) mais até R$ 12,9 bi de comissão; pagos R$ 32,5 bi em jan-jun/2026 (+30% vs. 2022) — [Agência Brasil, 31/08/2026](https://agenciabrasil.ebc.com.br/economia/noticia/2026-08/orcamento-de-2027-reserva-r-448-bilhoes-para-emendas-impositivas); 2025: R$ 31,5 bi pagos ("maior valor nominal da história") + R$ 15,5 bi empenhados — [Transparência Internacional Brasil, fev/2026](https://transparenciainternacional.org.br/posts/os-novos-capitulos-do-orcamento-secreto/)
- Orçamento secreto (RP 9): criado nas LDOs 2020 e 2021; ~R$ 16 bi em 2021 e valor semelhante em 2022; Rosa Weber (15/12/2022) votou pela inconstitucionalidade ("à margem da legalidade"), maioria formada em 19/12/2022 — [Wikipedia pt "Orçamento secreto"](https://pt.wikipedia.org/wiki/Or%C3%A7amento_secreto); STF declarou inconstitucionais RP 8 e RP 9 em dez/2022; Dino suspendeu emendas em ago/2024 exigindo rastreabilidade; plano de trabalho Congresso-governo aprovado no STF no início de 2025 liberou pagamentos; em 21/12/2025 Dino suspendeu o art. 10 do PL 128/2025 que revalidaria restos a pagar desde 2019 (~R$ 3 bi, ~R$ 1 bi de RP 9) — [Agência Brasil, 21/12/2025](https://agenciabrasil.ebc.com.br/politica/noticia/2025-12/dino-suspende-trecho-de-pl-que-libera-emendas-do-orcamento-secreto); em ago/2026 Dino anulou emendas indicadas por presidentes de partido ou pessoas sem mandato — [Agência Brasil, 31/08/2026](https://agenciabrasil.ebc.com.br/economia/noticia/2026-08/orcamento-de-2027-reserva-r-448-bilhoes-para-emendas-impositivas)
- Moody's: emendas parlamentares passaram de 2% para 24% da despesa discricionária desde 2015 — [Seu Dinheiro, 30/07/2026](https://www.seudinheiro.com/2026/economia/a-moodys-esta-de-olho-no-brasil-e-esses-sao-os-pontos-fortes-e-fracos-para-o-rating-soberano-subir-mlim/)
- Investigações: >100 inquéritos na PF envolvendo parlamentares; Operação Overclean; PGR denunciou ministro Juscelino Filho (08/04/2025) — [Transparência Internacional Brasil](https://transparenciainternacional.org.br/posts/os-novos-capitulos-do-orcamento-secreto/)

**Precatórios**
- Despesa com sentenças e precatórios (custeio/capital, Tesouro): R$ 17,3 bi (2022) → R$ 71,4 bi (2023) → R$ 34,3 bi (2024) → R$ 42,8 bi (2025); precatórios previdenciários (urbano): R$ 22,2 bi (2022) → R$ 44,5 bi (2023) → R$ 20,9 bi (2024) → R$ 33,2 bi (2025) — [Tesouro RTN, Tabela 2.2](https://www.tesourotransparente.gov.br/ckan/dataset/ab56485b-9c40-4efb-8563-9ce3e1973c4b/resource/527ccdb1-3059-42f3-bf23-b5e3ab4c6dc6/download/seriehistoricajul26.xlsx); R$ 92,4 bi pagos em 2023 após decisão do STF (BCB) — [Agência Brasil](https://agenciabrasil.ebc.com.br/economia/noticia/2025-01/banco-central-setor-publico-registra-deficit-de-04-do-pib-em-2024); R$ 41,15 bi excluídos da meta em 2025 e R$ 59,2 bi previstos para 2027 — [Gazeta do Povo](https://www.gazetadopovo.com.br/economia/governo-cumpre-meta-fiscal-2025-rombo-61-bi/); [IFI RAF 116](https://www12.senado.leg.br/ifi/pdf/raf116_set2026.pdf)

**Desenrola**
- Desenrola Brasil (Lei 14.690/2023): 1ª fase de jul/2023 a mai/2024; ~15 milhões de beneficiados e ~R$ 53 bi em dívidas renegociadas (dados citados em mai/2026 no lançamento do "Novo Desenrola") — [Wikipedia pt "Desenrola Brasil" (ref. Perfil Brasil, 04/05/2026)](https://pt.wikipedia.org/wiki/Desenrola_Brasil)

**Isenção do IR até R$ 5 mil (Lei 15.270/2025)**
- Sancionada em 26/11/2025; isenção até R$ 5 mil/mês e desconto progressivo até R$ 7,3 mil; vale para a renda de 2026 (declarações a partir de 2027); custo R$ 25,8 bi em 2026; compensação: tributação mínima de alta renda (acima de R$ 600 mil/ano, até 10%, ~140 mil contribuintes) e de lucros/dividendos, com arrecadação prevista de R$ 34,1 bi em 2026 — saldo líquido +R$ 8,3 bi; aprovação unânime na Câmara e no Senado; estados/municípios compensados via fundos de participação — [Migalhas](https://www.migalhas.com.br/quentes/445195/lula-sanciona-lei-que-amplia-isencao-do-ir-para-renda-ate-r-5-mil); IFI: perda de R$ 25-30 bi/ano e compensação pela tributação acima de R$ 50 mil/mês "não se materializou" nos dados até maio/2026 (contribuintes operam como PJ) — [Senado Notícias](https://www12.senado.leg.br/noticias/materias/2026/06/25/ifi-proximo-presidente-da-republica-tera-de-enfrentar-decisoes-fiscais-dificeis); [Poder360](https://www.poder360.com.br/poder-economia/proximo-presidente-tera-decisoes-fiscais-dificeis-diz-ifi/)

### Inferences
- A discrepância de ~R$ 60 bi no custo do Auxílio Emergencial decorre de critérios (valores brutos x líquidos de devoluções; "emergencial" 2020 x "residual" 2021); para checagem, cite a faixa R$ 293-354 bi com a fonte de cada ponta.
- As emendas cresceram em todos os governos desde 2016 e os recordes nominais de 2024-2026 ocorreram sob Lula 3, mas a decisão de torná-las impositivas (EC 86/2015, 100/2019) e o orçamento secreto (2020-2022) são de iniciativa do Congresso; a contenção veio do STF, não do Executivo nem do Legislativo.

### Gaps
- Não encontrei valores oficiais do custo do Desenrola para o Tesouro (aporte ao FGO), nem a nota técnica original de Transparência Brasil legível (PDF em imagem) com RP 9 por ano em 2020/2022; os valores de RP 9 em 2020 não foram localizados.
- Não encontrei série oficial anual do Bolsa Família 2023-2025 em fonte primária (Portal da Transparência) — os números vêm de levantamentos do Poder360.

## Receitas: carga tributária por ano, reforma tributária (EC 132/2023, LC 214/2025), IOF 2025 e desonerações

### Takeaway
A carga tributária bruta do governo geral (metodologia do Tesouro, série desde 2010) oscilou entre 29,2% (2020) e 31,2% (2022) e bateu recordes de 32,2% (2024) e 32,4% do PIB (2025), puxada pelo governo central (21,6%); a crise do IOF em 2025 opôs Executivo e Congresso e foi arbitrada pelo STF (Moraes) em 16/07/2025; a reforma tributária (IBS/CBS/IS) está em transição e já afeta o orçamento de 2027.

### Cited Findings
- Carga Tributária Bruta do Governo Geral (% PIB, Tesouro/STN, dados preliminares de 2025 publicados em 10/04/2026): 2010 30,32; 2011 31,00; 2012 30,60; 2013 30,30; 2014 29,53; 2015 29,69; 2016 29,79; 2017 29,93; 2018 30,40; 2019 30,39; 2020 29,15; 2021 30,88; 2022 31,24; 2023 30,26; 2024 32,22; 2025 32,40. Por esfera em 2025: governo central 21,60; estados 8,38; municípios 2,42. Variação 2024→2025: +0,18 p.p. (central +0,26; municípios +0,03; estados −0,10). Comparativo STN x RFB para 2010-2017: a RFB apurava 32-33% (metodologia distinta) — [Tesouro Transparente, CTB 2025](https://www.tesourotransparente.gov.br/publicacoes/carga-tributaria-do-governo-geral/2025/114); [planilha Base CTB GG.xlsx](https://thot-arquivos.tesouro.gov.br/publicacao-anexo/28024)
- Leitura do recorde: 32,4% é "o maior patamar da série histórica iniciada em 2010", puxado por IRRF, IOF e contribuições previdenciárias federais; ICMS recuou — [Contábeis, 23/04/2026](https://www.contabeis.com.br/noticias/76330/carga-tributaria-do-brasil-atinge-recorde-de-32-4-do-pib-em-2025/); IRRF atingiu 5% do PIB em 2025, maior da série — [Contábeis](https://www.contabeis.com.br/noticias/77032/seis-tributos-atingiram-carga-recorde-em-2025-aponta-tesouro-nacional/); atenção: o número de 34,2% para 2024 divulgado em mar/2025 é anterior à revisão metodológica que retirou FGTS e Sistema S — [Impostômetro](https://impostometro.org/artigos/carga-tributaria-brasil/)
- Receita Federal publica o estudo "Carga Tributária no Brasil" anualmente (edições 2015-2024; 2024 atualizada em 02/12/2025) — [RFB, lista de edições](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/estudos/carga-tributaria); [CTB 2024](https://www.gov.br/receitafederal/pt-br/centrais-de-conteudo/publicacoes/estudos/carga-tributaria/carga-tributaria-no-brasil-2024/view)
- Receita líquida do governo central (% PIB, Tesouro): 17,42 (2003) → 20,21 (2010, capitalização Petrobras) → 17,37 (2016) → 15,83 (2020) → 18,41 (2022) → 18,31 (2025) — [Tesouro RTN 2.1-A](https://www.tesourotransparente.gov.br/ckan/dataset/ab56485b-9c40-4efb-8563-9ce3e1973c4b/resource/527ccdb1-3059-42f3-bf23-b5e3ab4c6dc6/download/seriehistoricajul26.xlsx)

**IOF 2025 (crise Executivo x Congresso x STF)**
- Congresso derrubou o decreto do IOF em 25/06/2025 (383 deputados; unanimidade no Senado); PSOL, PL e AGU acionaram o STF; audiência de conciliação sem acordo; Moraes (16/07/2025) restabeleceu quase todo o decreto, mantendo fora o "risco sacado" — [Gazeta do Povo](https://www.gazetadopovo.com.br/republica/moraes-derruba-veto-congresso-iof/); [Agência Brasil, 17/07/2025](https://agenciabrasil.ebc.com.br/economia/noticia/2025-07/entenda-como-fica-iof-apos-decisao-de-ministro-do-stf)
- Impacto: sem o risco sacado, perda de R$ 450 mi (2025) e R$ 3,5 bi (2026); Receita estimou R$ 8,4 bi de arrecadação com IOF no 2º semestre de 2025 — [Jovem Pan](https://jovempan.com.br/economia/macroeconomia/decisao-de-moraes-sobre-o-decreto-do-iof-fara-governo-deixar-de-arrecadar-r-450-milhoes-neste-ano/); [CNN Brasil](https://www.cnnbrasil.com.br/economia/macroeconomia/apos-stf-governo-estima-arrecadar-r-84-bi-com-iof-no-2-semestre/); IOF cresceu R$ 15,4 bi (+21,3%) em 2025 — [Agência Brasil](https://agenciabrasil.ebc.com.br/economia/noticia/2026-01/deficit-primario-do-governo-central-totaliza-r-617-bilhoes-em-2025)

**Reforma tributária**
- PLOA 2027 já traz CBS de R$ 636,8 bi (4,3% do PIB) e Imposto Seletivo de R$ 42,0 bi (0,3% do PIB) como receita condicionada ("projeto sequer foi enviado ao Congresso"); aporte de R$ 33,8 bi (0,2% PIB) ao Fundo de Compensação aos Estados pela substituição do IPI pelo IS, despesa nova fora do limite mas dentro da meta — [IFI, RAF 116, p. 3-4 e 31](https://www12.senado.leg.br/ifi/pdf/raf116_set2026.pdf)
- Moody's: reforma tributária/IVA deve trazer ganhos de eficiência — [Seu Dinheiro](https://www.seudinheiro.com/2026/economia/a-moodys-esta-de-olho-no-brasil-e-esses-sao-os-pontos-fortes-e-fracos-para-o-rating-soberano-subir-mlim/)

**Desonerações**
- Combustíveis 2022 (LC 194/2022, Bolsonaro, sancionada 24/06/2022 com veto à compensação aos estados): fixou ICMS de combustíveis à alíquota modal; estados estimam perda de ~R$ 115 bi/ano (Comsefaz) ou R$ 102 bi em 12 meses (Sérgio Gobetti/Ipea); renúncia federal de PIS/Cofins/Cide estimada em R$ 52,9 bi para manter a desoneração em todo 2023 — [Senado Notícias](https://www12.senado.leg.br/noticias/materias/2022/06/24/bolsonaro-sanciona-limite-para-icms-de-combustiveis-mas-veta-compensacao-a-estados); [Comsefaz](https://comsefaz.org.br/novo/estados-perdem-r-102-bilhoes-apos-lc-194-2022/); [InfoMoney](https://www.infomoney.com.br/consumo/lula-decide-prorrogar-desoneracao-de-combustiveis-mas-preco-deve-subir-em-janeiro-entenda/)
- Desoneração da folha: criada pela Lei 12.546/2011 (Plano Brasil Maior, Dilma), substituindo 20% sobre a folha por 1-4,5% sobre a receita; reduzida de 56 para 17 setores pela Lei 13.670/2018 — [Wikipedia pt](https://pt.wikipedia.org/wiki/Desonera%C3%A7%C3%A3o_da_folha_de_pagamento); custo registrado pelo Tesouro como "Compensação ao RGPS pelas Desonerações da Folha": R$ 1,8 bi (2012), R$ 9,0 bi (2013), R$ 18,1 bi (2014), R$ 25,4 bi (2015, pico = 0,42% PIB), R$ 17,6 bi (2016), R$ 13,9 bi (2017), R$ 13,5 bi (2018), R$ 10,2 bi (2019), R$ 9,4 bi (2020), R$ 7,3 bi (2021), R$ 3,1 bi (2022), zero em 2023-2025 (rubrica descontinuada) — [Tesouro RTN, Tabela 2.2, linha 4.3.08](https://www.tesourotransparente.gov.br/ckan/dataset/ab56485b-9c40-4efb-8563-9ce3e1973c4b/resource/527ccdb1-3059-42f3-bf23-b5e3ab4c6dc6/download/seriehistoricajul26.xlsx)

### Inferences
- A carga tributária caiu durante Dilma 2/Temer e no auge da pandemia e subiu sob Lula 3 (de 30,3% em 2023 para 32,4% em 2025), coerente com a estratégia de reequilíbrio pelo lado da receita (IOF, fim de benefícios, tributação de fundos exclusivos/offshores, JCP etc.) criticada pela IFI como insuficiente para estabilizar a dívida.

### Gaps
- Não encontrei fonte acessível (páginas oficiais da Fazenda exigiram autenticação; Agência Brasil/Wikipedia retornaram 404) para datas e parâmetros da EC 132/2023 e da LC 214/2025 (alíquota de referência, cronograma 2026-2033); tratar como lacuna a ser preenchida com o texto legal.
- Não encontrei o custo anual oficial da desoneração da folha após 2022 nem a Lei 14.973/2024 (reoneração gradual) em fonte acessível.

## Déficit nominal e juros da dívida (% PIB) por ano; custo da Selic alta

### Takeaway
Os juros nominais do setor público consumiram entre 4,1% (2020) e 8,4% do PIB (2015); em 2025 somaram R$ 1 trilhão (7,91% do PIB) e em 12 meses até ago/2026 R$ 1,18 trilhão (8,86%), levando o déficit nominal a 9,48% do PIB — o pior desde a pandemia — com a Selic a 15%.

### Cited Findings

**Resultado nominal (déficit, % PIB, dezembro) — [BCB/SGS 5727](https://api.bcb.gov.br/dados/serie/bcdata.sgs.5727/dados?formato=json&dataInicial=01/12/2002); juros nominais = nominal − primário (séries 5727 e 5793; valores de dez/2015, 2020, 2023, 2025 confirmados diretamente na [série 5760](https://api.bcb.gov.br/dados/serie/bcdata.sgs.5760/dados?formato=json&dataInicial=01/12/2014): 8,37; 4,11; 6,56; 7,91)**
| Ano | Déficit nominal | Juros (derivado) |
|---|---|---|
| 2003 | 5,18 | 8,42 |
| 2004 | 2,88 | 6,57 |
| 2005 | 3,54 | 7,28 |
| 2006 | 3,57 | 6,72 |
| 2007 | 2,74 | 5,98 |
| 2008 | 1,99 | 5,32 |
| 2009 | 3,19 | 5,13 |
| 2010 | 2,41 | 5,03 |
| 2011 | 2,47 | 5,41 |
| 2012 | 2,26 | 4,44 |
| 2013 | 2,96 | 4,67 |
| 2014 | 5,95 | 5,39 |
| 2015 | 10,22 | 8,36 |
| 2016 | 8,98 | 6,50 |
| 2017 | 7,77 | 6,09 |
| 2018 | 6,96 | 5,41 |
| 2019 | 5,81 | 4,97 |
| 2020 | 13,34 | 4,10 |
| 2021 | 4,26 | 4,98 |
| 2022 | 4,57 | 5,82 |
| 2023 | 8,84 | 6,56 |
| 2024 | 8,47 | 8,07 |
| 2025 | 8,34 | 7,91 |
| 12 m até ago/2026 | 9,48 | 8,86 **[últ.: ago/2026]** |

- 2025: juros nominais R$ 1 trilhão (recorde; 7,91% do PIB) x R$ 950,4 bi (8,07%) em 2024; swaps cambiais deram ganho de R$ 105,9 bi em 2025 (reduzindo juros) e perda de R$ 115,9 bi em 2024; déficit nominal R$ 1,062 tri (2025) x R$ 998 bi (2024); Selic 15% a.a., "a mais alta desde julho de 2006" — [Agência Brasil, 30/01/2026](https://agenciabrasil.ebc.com.br/economia/noticia/2026-01/contas-publicas-tem-deficit-de-r-55021-bilhoes-em-2025); 2023: juros R$ 718,3 bi (6,56%), déficit nominal R$ 967,4 bi (8,84%) — [Agência Brasil, 31/01/2025](https://agenciabrasil.ebc.com.br/economia/noticia/2025-01/banco-central-setor-publico-registra-deficit-de-04-do-pib-em-2024)
- Ago/2026: juros no mês R$ 105,9 bi (ago/2025: R$ 74,3 bi; swap passou de ganho de R$ 19,9 bi para perda de R$ 9,3 bi); 12 meses: R$ 1.182,2 bi (8,86% do PIB) x R$ 946,5 bi (7,61%) um ano antes; déficit nominal 12 meses R$ 1.264,2 bi (9,48%) — [Poder360](https://www.poder360.com.br/poder-economia/divida-bruta-atinge-829-do-pib-em-agosto-diz-banco-central/); [Gazeta Mercantil](https://gazetamercantil.com/juros-setor-publico-agosto-1-18-trilhao)
- 2015: juros de R$ 501,8 bi (8,4% do PIB), "valor mais alto da série histórica (junto com 2003)"; 2020: 4,1% — [FGV IBRE, Observatório de Política Fiscal](https://observatorio-politica-fiscal.ibre.fgv.br/politica-economica/pesquisa-academica/decomposicao-de-juros-nominais-liquidos-no-brasil-2002-2024); BNDES: juros líquidos 8,1% (2024) → 7,9% (2025); déficit nominal 8,5% → 8,3% — [BNDES](https://blogdodesenvolvimento.bndes.gov.br/serie/estudos-especiais/pPagamento-liquido-de-juros-nominais-no-Brasil-em-2025-p/)
- Pico de 12 meses do déficit nominal na pandemia: 10,25% do PIB em abr/2021 — [Mais Retorno](https://maisretorno.com/portal/bc-setor-publico-registra-deficit-primario-de-r-65508-bilhoes-em-junho)
- Mecanismo Selic→dívida: ~50% da dívida é indexada à Selic; juros reais ~9%; juros consomem 7,7% do PIB (2025) e 20% da receita (pares: 14%) — Moody's — [Seu Dinheiro](https://www.seudinheiro.com/2026/economia/a-moodys-esta-de-olho-no-brasil-e-esses-sao-os-pontos-fortes-e-fracos-para-o-rating-soberano-subir-mlim/); IFI: sensibilidade do prêmio de risco à DBGG subiu de 2,10 p.p. (2011-2013) para 3,16 p.p. (12 meses até ago/2026) — [IFI, RAF 116](https://www12.senado.leg.br/ifi/pdf/raf116_set2026.pdf); Fitch projeta déficit nominal do governo geral de 8,6% em 2026 (8,1% em 2025), "principalmente por maiores custos de juros", x mediana BB de 3,5% — [Investing.com, 16/06/2026](https://br.investing.com/news/world-news/fitch-mantem-rating-do-brasil-em-bb-com-perspectiva-estavel-93CH-1975122)

### Inferences
- Em 2024-2026 o déficit nominal (~8,3-9,5% do PIB) é quase todo juros: o primário explica só 0,4-0,6 p.p. Isso significa que a dívida cresce principalmente pelo custo de carregamento (Selic 14,25-15%) e não pelo gasto primário corrente — ponto usado tanto pelo governo (culpa o BC) quanto pela IFI/FMI (o prêmio de risco sobe com a dívida, realimentando a Selic).
- Picos de juros coincidem com ciclos de Selic alta: 2003 (Selic 26,5%), 2015-2016 (14,25%) e 2024-2026 (15%).

### Gaps
- Não baixei a série 5760 (juros) para antes de dez/2014; os valores 2003-2013 da coluna "juros" são derivados por diferença e podem divergir em centésimos do dado direto.

## Avaliações independentes: IFI, TCU, FMI, agências de rating e posição da Fazenda

### Takeaway
IFI, FMI, Moody's e Fitch convergem em que a dívida brasileira só se estabiliza com ajuste primário de 2 a 3 p.p. do PIB a ser feito pelo próximo governo (2027-2031); o rating segue em grau especulativo (Fitch BB estável, Moody's Ba1), e a Fazenda sustenta que as metas estão sendo cumpridas e que o déficit acumulado de Lula 3 será 70% menor que o de Bolsonaro.

### Cited Findings
- IFI (RAF 113, jun/2026): "sem reformas no perfil das despesas obrigatórias, nenhuma regra fiscal conterá a trajetória da dívida"; próximo presidente enfrentará "discussões duras" sobre previdência, salários e benefícios (diretor Alexandre Andrade); dívida de 115% do PIB em 2036 é "extremamente elevada" para um emergente — [Senado Notícias](https://www12.senado.leg.br/noticias/materias/2026/06/25/ifi-proximo-presidente-da-republica-tera-de-enfrentar-decisoes-fiscais-dificeis); [Poder360](https://www.poder360.com.br/poder-economia/proximo-presidente-tera-decisoes-fiscais-dificeis-diz-ifi/)
- IFI (RAF 115, ago/2026): quadro fiscal "inalterado"; estoque de restos a pagar de R$ 105,5 bi (~6x o bloqueio oficial) — [CNN Brasil](https://www.cnnbrasil.com.br/economia/money/macroeconomia/ifi-alerta-para-despesas-crescendo-acima-das-receitas-e-deficit-estrutural/); IFI (RAF 116, set/2026): "a realidade estará muito distante do resultado fiscal para estabilizar a relação entre dívida pública e o PIB" — [IFI](https://www12.senado.leg.br/ifi/pdf/raf116_set2026.pdf)
- TCU: rejeitou as contas de 2014 (07/10/2015) e apontou pedaladas em 2015 — [Wikipedia "Fiscal pedaling"](https://en.wikipedia.org/wiki/Fiscal_pedaling); [Correio Braziliense](https://www.correiobraziliense.com.br/app/noticia/politica/2016/06/30/interna_politica,538458/auditoria-do-tcu-confirma-pedaladas-fiscais-de-dilma-em-2015.shtml); questionou o Pé-de-Meia fora do orçamento e alertou sobre mirar o piso da meta em 2025 — [Gazeta do Povo](https://www.gazetadopovo.com.br/economia/com-puxadinhos-no-orcamento-governo-lula-legaliza-fracasso-do-arcabouco-fiscal/); [Metrópoles](https://www.metropoles.com/brasil/economia-br/entenda-a-situacao-fiscal-que-o-governo-vai-enfrentar-em-2026); Acórdão 2282/2020 sobre o Auxílio Emergencial — [TCU](https://pesquisa.apps.tcu.gov.br/doc/acordao-completo/2282/2020/Plen%C3%A1rio)
- FMI (Artigo IV 2026, 23/07/2026): recomenda ajuste de 3 p.p. do PIB em 5 anos, poupar receitas extraordinárias do petróleo, eliminar despesas tributárias ineficientes, desvincular benefícios do salário mínimo, eliminar pisos constitucionais de saúde e educação; PIB 2,4% e IPCA 5,6% em 2026 — [Poder360](https://www.poder360.com.br/poder-economia/brasil-crescera-24-em-2026-e-divida-se-aproxima-de-100-do-pib/); Artigo IV anterior (14-17/07/2025) — [FMI](https://www.imf.org/en/publications/cr/issues/2025/07/16/brazil-2025-article-iv-consultation-press-release-staff-report-and-statement-by-the-568678)
- Fitch (16/06/2026): BB, perspectiva estável; forças: economia grande e diversificada, finanças externas sólidas, câmbio flutuante; fraquezas: dívida alta e crescente, rigidez orçamentária, governança fraca, baixo crescimento potencial; dívida do governo geral 78,6% (2025) → >80% (2026); espera disputa apertada entre Lula e Flávio Bolsonaro em outubro — [Investing.com](https://br.investing.com/news/world-news/fitch-mantem-rating-do-brasil-em-bb-com-perspectiva-estavel-93CH-1975122)
- Moody's (30/07/2026, William Foster): Ba1 (um degrau abaixo do grau de investimento; perfil fiscal isolado B1); "ajustes na política fiscal e econômica após a eleição serão necessários para estabilizar o peso da dívida"; ajuste de 2-2,5% do PIB; gatilhos de alta: reduzir indexação, conter emendas, queda sustentada do juro real — [Seu Dinheiro](https://www.seudinheiro.com/2026/economia/a-moodys-esta-de-olho-no-brasil-e-esses-sao-os-pontos-fortes-e-fracos-para-o-rating-soberano-subir-mlim/); perspectiva da Moody's teria passado de positiva para estável em mai/2025 (fonte secundária) — [Toro Blog](https://blog.toroinvestimentos.com.br/educacao-financeira/rating-do-brasil/)
- Ministério da Fazenda/Haddad: governo não planeja alterar a meta de 2026; "mirando o centro da meta"; déficit acumulado de Lula 3 "70% menor" que o de Bolsonaro; Durigan aposta em projeto que limita benefícios fiscais (R$ 20 bi) — [Metrópoles, 29/12/2025](https://www.metropoles.com/brasil/economia-br/entenda-a-situacao-fiscal-que-o-governo-vai-enfrentar-em-2026); Tesouro (Ceron): meta de 2025 cumprida, resultado "muito satisfatório", 2026 deve ficar mais perto do centro da banda — [Gazeta do Povo](https://www.gazetadopovo.com.br/economia/governo-cumpre-meta-fiscal-2025-rombo-61-bi/)
- Mercado (Prisma Fiscal, out/2026): déficit de R$ 53,0 bi em 2026 (fora da meta efetiva de superávit, mas dentro do piso após deduções) — [CNN Brasil](https://www.cnnbrasil.com.br/economia/money/macroeconomia/mercado-eleva-projecao-de-deficit-em-2026-para-r-53-bi-diz-prisma-fiscal/)

### Inferences
- A afirmação da Fazenda de déficit "70% menor" compara somas nominais dos primários do governo central: Bolsonaro 2019-2022 = −R$ 95,1 −743,3 −35,1 +46,4 = −R$ 827,0 bi; Lula 3 2023-2025 = −228,5 −42,9 −61,7 = −R$ 333,1 bi (−R$ 414 bi se somado o déficit de R$ 81 bi de jan-jul/2026) — aritmética feita a partir da série do Tesouro; 90% do déficit de Bolsonaro é o ano da pandemia (2020).

### Gaps
- Não encontrei comunicado recente da S&P (último conhecido: BB estável, segundo fonte secundária sem data confiável).
- Não acessei o relatório do Artigo IV 2026 nem o relatório do TCU sobre as contas de 2025 (que a IFI diz ter acionado gatilhos da LC 200 por déficit em 2025, RAF 116 nota de rodapé).

## Comparação da dívida/PIB do Brasil com pares emergentes

### Takeaway
Na métrica comparável do FMI (Fiscal Monitor abr/2026), a dívida bruta do Brasil (93,3% do PIB em 2025; 96,5% em 2026) está ~18-20 p.p. acima da média dos emergentes (75,3% e 78,9%), ~20 p.p. acima da América Latina (74,2%) e acima de México (61,8%), África do Sul (78,6%), Índia (84,1%) e Colômbia (59,9%), abaixo apenas da China (99,2%) entre os grandes emergentes.

### Cited Findings
- Dívida bruta do governo geral (% PIB, FMI, Tabela A15; 2025 / 2026 / 2027): Brasil 93,3 / 96,5 / 100,0; média emergentes e renda média 75,3 / 78,9 / 82,2; G20 emergentes 80,5 / 85,2 / 89,2; América Latina 74,2 / 73,2 / 74,1; Ásia 90,6 / 96,1 / 99,8; Europa emergente 33,9 / 37,3 / 40,5; China 99,2 / 106,9 / 112,5; Índia 84,1 / 83,4 / 82,5; África do Sul 78,6 / 78,9 / 79,7; México 61,8 / 62,7 / 63,1; Argentina 80,3 / 70,4 / 68,1; Colômbia 59,9 / 60,9 / 61,3; Chile 41,8 / 42,5 / 44,4; Indonésia 41,0 / 41,5 / 41,8; Turquia 23,5 / 25,5 / 26,9 — [FMI, Fiscal Monitor abr/2026, Tabela A15](https://www.imf.org/-/media/files/publications/fiscal-monitor/2026/april/english/text.pdf)
- Histórico Brasil na métrica FMI: 82,7 (2017), 84,8 (2018), 87,1 (2019), 96,0 (2020), 88,9 (2021), 83,9 (2022), 84,0 (2023), 87,0 (2024) — [FMI, Tabela A15](https://www.imf.org/-/media/files/publications/fiscal-monitor/2026/april/english/text.pdf)
- Resultado nominal do governo geral (% PIB, FMI, Tabela A9; 2024 / 2025 / 2026): Brasil −6,2 / −8,1 / −7,7; média emergentes −5,5 / −6,1 / −6,0; México −5,8 / −4,9 / −4,4; Índia −7,9 / −7,4 / −7,4; África do Sul −5,7 / −5,8 / −4,9; China −8,2 / −8,4 / −8,2 — [FMI, Tabela A9](https://www.imf.org/-/media/files/publications/fiscal-monitor/2026/april/english/text.pdf)
- Resultado primário do governo geral (% PIB, FMI, Tabela A10): Brasil +1,3 (2022), −2,2 (2023), −0,2 (2024), −0,4 (2025), −0,5 (2026), −0,4 (2027), +0,1 (2028); média emergentes −3,5 (2024), −3,9 (2025), −3,6 (2026); México +0,2 (2024), +1,2 (2025); Índia −3,0 (2024), −2,1 (2025) — [FMI, Tabela A10](https://www.imf.org/-/media/files/publications/fiscal-monitor/2026/april/english/text.pdf)
- Leitura jornalística da comparação: emergentes ex-China ~57,5% do PIB; México ~63% com déficit de 4,9% — [CNN Brasil](https://www.cnnbrasil.com.br/blogs/lucinda-pinto/economia/money/macroeconomia/divida-do-brasil-pode-chegar-a-100-do-pib-no-primeiro-ano-do-novo-governo/)
- Fitch: déficit nominal brasileiro projetado de 8,6% do PIB em 2026 x mediana de 3,5% dos soberanos BB — [Investing.com](https://br.investing.com/news/world-news/fitch-mantem-rating-do-brasil-em-bb-com-perspectiva-estavel-93CH-1975122); Moody's: juros consomem 20% da receita no Brasil x 14% nos pares — [Seu Dinheiro](https://www.seudinheiro.com/2026/economia/a-moodys-esta-de-olho-no-brasil-e-esses-sao-os-pontos-fortes-e-fracos-para-o-rating-soberano-subir-mlim/)

### Inferences
- O Brasil não é o emergente com maior déficit primário (a média dos emergentes é pior, −3,9% em 2025), mas tem déficit nominal e dívida muito acima da média porque paga juros 2-3 vezes maiores em proporção da receita; esse é o ponto que distingue o caso brasileiro nas avaliações do FMI e das agências.

### Gaps
- Não extraí a tabela de juros/receita por país (Tabela A24, indicadores estruturais) do Fiscal Monitor; a comparação de juros vem de Moody's/Fitch.
