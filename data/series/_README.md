# Séries de dados (`data/series/`) — notas 01, 02 e 03

Gerado em 2026-10-21 a partir das notas `01_macroeconomia_por_governo.md`, `02_contas_publicas_divida.md` e `03_emprego_renda_pobreza_social.md`, incluindo as seções 'Enriquecimento — rodada 2 (21/10/2026)'. Só constam números, períodos e URLs presentes nas notas; anos ausentes estão em `lacunas`/`notas_metodologicas` de cada arquivo. Itens que as notas marcam como não verificados levam `nao_verificado: true`. Pontos parciais (ano em curso) levam `parcial: true`; projeções, `projecao: true`.

Total de séries desta leva: 88 (31 criadas na rodada 2). Outras séries na pasta (saúde, segurança, educação, infraestrutura, energia, renda por faixa etc.) foram geradas a partir de outras notas e não estão listadas aqui.

## Rodada 2 — correções aplicadas

- `pib-per-capita-reais`: 2024 = R$ 55.247,45 e 2025 = R$ 59.687,49 (IBGE/CNT), substituindo estimativas próprias; flags removidos.
- `selic-fim-de-ano`: 23 valores de 31/12 (2003–2025) + 2026; vigência da Selic de 15% corrigida para 20/06/2025.
- `ipca-meta-e-teto`: intervalos confirmados na página oficial do BCB (flags `nao_verificado` removidos), normas do CMN e cartas abertas por ano; carta aberta de 2025 em 10/07/2025.
- `ibovespa-fim-de-ano`: 2004, 2005 e 2012 preenchidos; recorde de 208.296 pontos em 20/10/2026.
- `cambio-fim-de-periodo`: PTAX de 20/10/2026 (5,0140).
- `juros-nominais-pib`: SGS 5760 lida diretamente (2004 6,56; 2015 8,37; 2016 6,49; 2020 4,11; 2002 acrescentado).
- `divida-bruta-pib`: pico de out/2020 (87,66%) confirmado no BCB; fatores de variação 2025–2026; lacuna 2002–2005 coberta por `divida-bruta-metodologia-antiga`.
- `carga-tributaria`: 2022 = 31,24% confirmado; valores em R$ e PIB por ano.
- `emendas-parlamentares`: base oficial do Portal da Transparência (09/10/2026); 2026 = R$ 40,17 bi / R$ 25,91 bi; RP 9 corrigido (2020 R$ 21,23 bi; 2021 16,72; 2022 8,64); detalhamento por tipo.
- `emprego-formal-caged-saldo`: série oficial 'com ajustes' do MTE (2002–2025) com estoque de dezembro; série sem ajustes do Ipeadata mantida em `series_alternativas`.
- `bolsa-familia-familias`: dezembros oficiais 2004–2025 (Portal da Transparência/MDS via Ipeadata) com valor pago e benefício médio.
- `bolsa-familia-custo`: divergência benefícios pagos x despesa orçamentária registrada; Auxílio Emergencial com fonte primária (R$ 293,34 bi em 2020; R$ 56,89 bi em 2021).
- `pobreza-ibge` e `extrema-pobreza-ibge`: série anual completa 2012–2024 (SIS 2025, Tabela 2.18).
- `informalidade`: taxa oficial do IBGE (variável 12466) para os 4º trimestres 2016–2025.
- `massa-rendimento-real`: série anual 2012–2025 (SIDRA 6392) com nota sobre a diferença para a Retrospectiva.
- `serasa-negativados`: abr/2020, jan/2023 e ago/2026 (Lupa).
- `salario-minimo-nominal`: Decreto 12.797/2025 confirmado no texto oficial.
- `risco-pais-embi`, `pib-anual`, `resultado-primario-pib`, `resultado-nominal-pib`, `resultado-primario-governo-central-pib`, `desoneracao-folha-custo`, `divida-bruta-fmi`, `gini`, `salario-minimo-ganho-real`: notas e lacunas atualizadas.
- `governos.json`: tarifas dos EUA (40% → fim em fev/2026 → 25% da Seção 301), ratings com datas, Selic de 31/12, novos indicadores (PIB per capita real, FBCF, juro real ex-ante, CAGED com ajustes, DBGG metodologia antiga), lacunas atualizadas.

## Séries criadas na rodada 2

`auxilio-emergencial-pago`, `bolsa-familia-por-uf`, `bolsa-familia-valor-pago-anual`, `bpc-beneficios`, `caged-com-ajustes-por-governo`, `carga-tributaria-por-esfera`, `cds-brasil-5-anos`, `dbgg-mensal-2023-2026`, `deficit-inss-rgps`, `desocupacao-por-regiao`, `desocupacao-por-sexo-raca-idade`, `desocupacao-por-uf-2026`, `divida-bruta-metodologia-antiga`, `emendas-pagas-por-ano`, `emendas-rp9`, `fbcf-pib`, `greves-dieese`, `informalidade-por-uf`, `inseguranca-alimentar-grave`, `ipca-alimentacao-no-domicilio`, `juro-real-ex-ante`, `juros-nominais-reais`, `ldo-metas-primario`, `nem-nem`, `pib-per-capita-real-variacao`, `precatorios-pagos`, `rating-soberano-eventos`, `renda-per-capita-decimos-2012-2025`, `resultado-primario-por-esfera`, `salario-minimo-dolar`, `transacoes-correntes-pib`

## Todas as séries desta leva

| id | título | unidade | frequência | último período | nota | lacunas |
|---|---|---|---|---|---|---|
| `auxilio-emergencial-pago` | Auxílio Emergencial: valor pago por mês (2020–2021) | R$ bilhões | mensal | out/2021 | 03 | Relatório final/acórdão do TCU com custo total auditado não localizado. |
| `balanca-comercial` | Balança comercial: saldo e exportações por ano | US$ bilhões | anual | 2026 (jan–ago) | 01 | — |
| `bolsa-familia-custo` | Custo anual do Bolsa Família / Auxílio Brasil | R$ bilhões | anual | 2026 | 02 | Custo anual 2007–2021 em despesa orçamentária não levantado (valores pagos de 2013–2021 em bolsa-familia-valor-pago-anual). Série oficial 2023–2025 do Tesouro (RTN) inacessível (HTTP 429). Relatório final do TCU com custo auditado do Auxílio Emergencial não localizado. |
| `bolsa-familia-familias` | Famílias atendidas pelo Bolsa Família / Auxílio Brasil em dezembro de cada ano | milhões de famílias | anual | out/2026 | 03 | Famílias em 2003 (série do Portal começa em 2004). Total oficial de famílias em out/2026 (só 'mais de 19 milhões' via imprensa). |
| `bolsa-familia-por-uf` | Bolsa Família por estado: famílias em dez/2022 e dez/2025 | famílias (dez/2025) | anual | dez/2025 | 03 | — |
| `bolsa-familia-valor-pago-anual` | Bolsa Família / Auxílio Brasil: valor pago por ano (benefícios) | R$ bilhões | anual | 2026 (jan–ago) | 03 | Anos 2004–2012 da série anual não somados na nota (apenas dezembros em bolsa-familia-familias). |
| `bpc-beneficios` | BPC: benefícios em dezembro e valor pago por ano | benefícios (dezembro) | anual | set/2026 | 03 | Anos anteriores a 2019 não transcritos. |
| `caged-com-ajustes-por-governo` | Saldo de empregos formais por governo (CAGED com ajustes) | vínculos (soma dos saldos anuais) | anual | Lula 3 (2023–ago/2026) | 03 | — |
| `cambio-fim-de-periodo` | Dólar: cotação no fim de cada ano (R$/US$) | R$ por US$ | anual | 20/10/2026 (PTAX venda, diária) | 01 | — |
| `cambio-media-anual` | Dólar: cotação média anual (R$/US$) | R$ por US$ | anual | 2026 (jan–set) | 01 | — |
| `carga-tributaria` | Carga tributária bruta do governo geral (% do PIB) | % do PIB | anual | 2025 | 02 | Carga tributária 2003–2009 não disponível na metodologia do Tesouro. |
| `carga-tributaria-por-esfera` | Carga tributária por esfera de governo (% do PIB) | % do PIB | anual | 2025 | 02 | — |
| `carteira-assinada-pnad` | Empregados do setor privado com carteira (PNAD Contínua) | mil pessoas | trimestral | 2T2026 | 03 | — |
| `cds-brasil-5-anos` | CDS do Brasil de 5 anos (pontos selecionados) | pontos-base | mensal | 15/05/2026 | 01 | Nenhum valor de ago–out/2026 localizado; sem fonte oficial gratuita para CDS. |
| `dbgg-mensal-2023-2026` | Dívida bruta e líquida mês a mês, jan/2023–ago/2026 | % do PIB | mensal | 08/2026 | 02 | — |
| `deficit-inss-rgps` | Déficit do INSS (RGPS) e resultado do governo federal sem o INSS | R$ bilhões correntes | anual | 2026 (jan–ago) | 02 | Anos anteriores a 2015 não cobertos pelas tabelas do BCB consultadas; o Tesouro Transparente ficou inacessível (HTTP 429). |
| `desemprego-pme-anual` | Taxa de desemprego média anual (PME, 6 regiões metropolitanas, 2003–2012) | % da população economicamente ativa | anual | 2012 | 03 | — |
| `desemprego-pnad-anual` | Taxa de desocupação média anual (PNAD Contínua) | % da força de trabalho | anual | 2025 | 03 | — |
| `desemprego-pnad-trimestral` | Taxa de desocupação por trimestre (PNAD Contínua) | % da força de trabalho | trimestral | 2T2026 | 03 | Trimestres intermediários de 2012–2024 não transcritos na nota. |
| `desemprego-pnad-trimestre-movel` | Taxa de desocupação, trimestres móveis (últimos 12) | % da força de trabalho | mensal | jun–ago/2026 | 03 | — |
| `desocupacao-por-regiao` | Taxa de desocupação por Grande Região | % da força de trabalho (2T2026) | trimestral | 2T2026 | 03 | — |
| `desocupacao-por-sexo-raca-idade` | Desocupação por sexo, cor ou raça e faixa etária | % da força de trabalho (2T2026) | trimestral | 2T2026 | 03 | — |
| `desocupacao-por-uf-2026` | Taxa de desocupação por estado (2T2026, com 4T2014, 4T2019, 4T2022 e 4T2025) | % da força de trabalho (2T2026) | trimestral | 2T2026 | 03 | — |
| `desoneracao-folha-custo` | Custo da desoneração da folha (compensação ao RGPS) | R$ bilhões | anual | 2025 | 02 | Custo anual oficial da desoneração após 2022 (Demonstrativo de Gastos Tributários da RFB exige autenticação). |
| `divida-bruta-fmi` | Dívida bruta do governo geral na metodologia do FMI (% do PIB) | % do PIB | anual | 2031 (projeção) | 02 | Anos 2011–2013 e 2015 não constam na nota. |
| `divida-bruta-metodologia-antiga` | Dívida bruta do governo geral na metodologia antiga do BCB (% do PIB) | % do PIB | anual | ago/2026 | 01 | Dezembros de 2011 a 2025 não transcritos na nota (apenas 2002–2010 e jun–ago/2026). |
| `divida-bruta-pib` | Dívida bruta do governo geral (% do PIB) | % do PIB | anual | ago/2026 | 02 | DBGG de 2002 a 2005 não existe na metodologia atual (ver divida-bruta-metodologia-antiga). |
| `divida-liquida-pib` | Dívida líquida do setor público (% do PIB) | % do PIB | anual | ago/2026 | 02 | — |
| `emendas-pagas-por-ano` | Emendas parlamentares pagas por ano | R$ bilhões | anual | 2026 (até 09/10/2026) | 02 | — |
| `emendas-parlamentares` | Emendas parlamentares empenhadas e pagas por ano | R$ bilhões | anual | 2026 (parcial, até 09/10/2026) | 02 | Emendas pagas em critério de caixa puro (por ano de desembolso) não disponíveis na base. Anos anteriores a 2014 não constam. |
| `emendas-rp9` | Orçamento secreto: emendas de relator (RP 9) por ano | R$ bilhões | anual | 2022 | 02 | Conciliação de 2022 com o Siga Brasil não feita. |
| `emprego-formal-caged-saldo` | Saldo anual de empregos com carteira (CAGED e Novo CAGED) | vínculos (saldo) | anual | 2026 (jan–ago) | 03 | Estoque anual da RAIS 2003–2021 em fonte primária (PDET/MTE fora do ar); só 2022–2024 obtidos. |
| `endividamento-familias` | Endividamento das famílias (% da renda acumulada em 12 meses, BCB) | % da renda | mensal | jul/2026 | 03 | Meses anteriores a dez/2022 não transcritos. |
| `extrema-pobreza` | Extrema pobreza segundo o Banco Mundial (US$ 2,15/dia, PPC 2017) | % da população | anual | 2024 | 03 | Anos 2002, 2004, 2005, 2007, 2008, 2010, 2013, 2015 e 2017 não constam na nota. |
| `extrema-pobreza-ibge` | Extrema pobreza segundo o IBGE (linha de US$ 2,15 PPC/dia) | % da população | anual | 2024 | 03 | — |
| `familias-endividadas-peic` | Famílias com dívidas (CNC/Peic) | % das famílias | mensal | mai/2026 | 03 | Peic de set/out/2026 não lida. Série mensal completa não transcrita. |
| `fbcf-pib` | Taxa de investimento (FBCF/PIB) | % do PIB | anual | 2026 (1S) | 01 | — |
| `gini` | Índice de Gini do rendimento domiciliar per capita (IBGE) | índice (0 a 1) | anual | 2025 | 03 | Explicação oficial do IBGE para a revisão 0,506 → 0,504 (2024) não localizada. |
| `gini-banco-mundial` | Índice de Gini segundo o Banco Mundial (renda per capita) | índice (0 a 1) | anual | 2024 | 03 | Anos 2004, 2005, 2007, 2008, 2010, 2013 e 2017 não constam na nota. |
| `greves-dieese` | Número de greves por ano (DIEESE/SAG) | greves | anual | 2025 | 03 | Balanços de 2014 e 2015 não localizados no site do DIEESE. |
| `ibovespa-fim-de-ano` | Ibovespa no último pregão de cada ano | pontos | anual | 20/10/2026 | 01 | — |
| `inadimplencia-pf` | Inadimplência das pessoas físicas (BCB) | % da carteira | mensal | ago/2026 | 03 | Meses intermediários não transcritos; série do juro do rotativo não localizada no SGS. |
| `informalidade` | Taxa de informalidade (PNAD Contínua) | % da população ocupada | trimestral | jun–ago/2026 | 03 | Taxa de informalidade não calculada pelo IBGE para 2012–2015; 4T2017 não transcrito. |
| `informalidade-por-uf` | Taxa de informalidade por estado (4T2019, 4T2022, 2T2026) | % da população ocupada (2T2026) | trimestral | 2T2026 | 03 | — |
| `inseguranca-alimentar-grave` | Insegurança alimentar grave (fome) — PNAD Contínua 2023–2024 | % das pessoas | anual | 2024 | 03 | POF 2024/2025: nenhum resultado publicado sobre insegurança alimentar localizado. |
| `investimento-direto-pais` | Investimento direto no país (IDP) por ano | US$ bilhões | anual | 2026 (jan–ago) | 01 | — |
| `ipca-12-meses-mensal` | IPCA acumulado em 12 meses, mês a mês (2025–2026) | % em 12 meses | mensal | set/2026 | 01 | — |
| `ipca-alimentacao-no-domicilio` | Inflação dos alimentos: IPCA geral, 'Alimentação e bebidas' e 'Alimentação no domicílio' por ano | % ao ano (dez/dez) | anual | 2026 (12 meses até set) | 01 | — |
| `ipca-anual` | Inflação (IPCA) por ano | % ao ano | anual | 2026 (12 meses até set/2026) | 01 | — |
| `ipca-meta-e-teto` | Meta de inflação, piso e teto por ano | % ao ano | anual | 2026 | 01 | Texto da carta aberta de 10/07/2025 (PDF) não baixado; existência e data confirmadas pelo RPM de set/2025. |
| `juro-real-ex-ante` | Juro real esperado (ex-ante) no fim de cada ano | % ao ano | anual | 16/10/2026 (Selic fim-2027) | 01 | — |
| `juros-nominais-pib` | Juros nominais pagos pelo setor público (% do PIB) | % do PIB | anual | 12 meses até ago/2026 | 02 | — |
| `juros-nominais-reais` | Juros nominais e déficit nominal em reais (setor público e governo central) | R$ bilhões correntes | anual | 2026 (jan–ago) | 02 | — |
| `ldo-metas-primario` | Metas de resultado primário fixadas nas LDOs (2003–2014 e 2023–2026) | % do PIB (2003–2010) ou R$ bilhões (2011–2014, 2023–2026); ver campos | anual | 2026 | 02 | LDOs 2015–2022 não levantadas. LDO 2005: Anexo IV não está no HTML do Planalto (meta inferida). LDO 2026: Anexo IV.1 (metas 2027–2028) é PDF de imagem, não lido. |
| `massa-rendimento-real` | Massa de rendimento real habitual, 2012–2026 | R$ bilhões | anual | jun–ago/2026 | 03 | — |
| `nem-nem` | Jovens de 15 a 29 anos que não estudam nem trabalham | % dos jovens de 15 a 29 anos | anual | 2025 | 03 | SIS: anos 2025 em diante ainda não publicados. |
| `participacao-forca-trabalho` | Taxa de participação na força de trabalho e nível de ocupação | % da população em idade de trabalhar | trimestral | 2T2026 | 03 | — |
| `pib-anual` | Crescimento real do PIB por ano | % ao ano | anual | 2026 (acum. 4 trim. até 2T2026) | 01 | — |
| `pib-brasil-vs-mundo` | Crescimento do PIB: Brasil, América Latina, emergentes e mundo | % ao ano | anual | 2026 (projeção) | 01 | — |
| `pib-dolares` | PIB nominal em dólares | US$ bilhões | anual | 2026 (projeção FMI) | 01 | — |
| `pib-media-por-governo` | Média anual de crescimento do PIB por governo | % ao ano (média) | anual | Lula 3 (2023–2025) | 01 | — |
| `pib-per-capita-dolares` | PIB per capita em dólares (FMI) | US$ correntes | anual | 2026 (projeção FMI) | 01 | A nota traz apenas anos selecionados (2002, 2003, 2010, 2011, 2014–2016, 2018, 2020, 2022–2026); os demais anos não foram levantados. |
| `pib-per-capita-reais` | PIB per capita em reais correntes | R$ correntes | anual | 2025 | 01 | — |
| `pib-per-capita-real-variacao` | PIB per capita: variação real anual e nível em reais de 2025 | % ao ano | anual | 2025 | 01 | — |
| `pobreza-banco-mundial` | Pobreza segundo o Banco Mundial (US$ 6,85/dia, PPC 2017) | % da população | anual | 2024 | 03 | Anos 2004, 2005, 2007, 2008, 2010 e 2013 não constam na nota. |
| `pobreza-banco-mundial-ppc-2021` | Pobreza nas novas linhas do Banco Mundial (US$ 3,00 e US$ 8,30/dia, PPC 2021) | % da população | anual | 2024 | 03 | Apenas os anos 2003, 2014, 2019, 2021 e 2024 constam na nota. |
| `pobreza-ibge` | Pobreza segundo o IBGE (linha de US$ 6,85 PPC/dia) | % da população | anual | 2024 | 03 | — |
| `precatorios-pagos` | Precatórios federais pagos por ano (% do PIB) | % do PIB | anual | 2026 (até 09/09/2026) | 02 | Série em R$ do Tesouro 2015–2026 inacessível (HTTP 429). |
| `ranking-pib-mundial` | Posição do Brasil entre as maiores economias (PIB em US$) | posição | anual | 2026 (projeção) | 01 | A nota só traz anos selecionados (2010, 2014, 2020, 2022, 2025, 2026). |
| `rating-soberano-eventos` | Mudanças de nota e perspectiva do rating soberano do Brasil | evento (sem valor numérico) | anual | out/2026 (vigente) | 01 | Datas-dia de 2008–2016 em fonte primária (Relatório Anual da Dívida do Tesouro ou press releases das agências). |
| `renda-per-capita-decimos-2012-2025` | Renda domiciliar per capita por décimo da população, 2012–2025 | R$ a preços médios do ano de referência da divulgação (2025) | anual | 2025 | 03 | Anos 2013, 2015 e 2017 não transcritos. Base de preços da tabela 7531 a confirmar na documentação do SIDRA. |
| `rendimento-medio-real` | Rendimento médio real habitual do trabalho (PNAD Contínua) | R$ a preços do último trimestre | trimestral | 2T2026 | 03 | 4T2013, 4T2020 e 4T2021 não constam na nota. |
| `rendimento-medio-real-trimestre-movel` | Rendimento médio real habitual, trimestres móveis de 2026 | R$ a preços do último trimestre | mensal | jun–ago/2026 | 03 | — |
| `reservas-internacionais` | Reservas internacionais (fim de ano) | US$ bilhões | anual | set/2026 | 01 | — |
| `resultado-nominal-pib` | Resultado nominal do setor público (% do PIB) | % do PIB | anual | 12 meses até ago/2026 | 02 | — |
| `resultado-primario-governo-central-pib` | Resultado primário do governo central (% do PIB, Tesouro) | % do PIB | anual | jan–jul/2026 | 02 | Percentual do PIB de 2026 (parcial) não informado. RTN de dez/2024 com o valor exato das deduções da meta de 2024 inacessível (Tesouro Transparente HTTP 429). Relatório de Avaliação do 6º bimestre/2024 (página da SOF retornou 404). |
| `resultado-primario-pib` | Resultado primário do setor público (% do PIB) | % do PIB | anual | 12 meses até ago/2026 | 02 | — |
| `resultado-primario-por-esfera` | Resultado primário por esfera de governo (R$ bilhões) | R$ bilhões correntes | anual | 2026 (jan–ago) | 02 | — |
| `risco-pais-embi` | Risco-país (EMBI+ Brasil) no fim de cada ano | pontos-base | anual | 2024 (até 30/07/2024) | 01 | EMBI+ após 30/07/2024 e CDS de 5 anos em ago–out/2026 sem fonte oficial gratuita. Datas-dia dos movimentos de rating de 2008–2016 continuam sem fonte primária (Tesouro respondeu HTTP 429; agências bloquearam). |
| `salario-minimo-cestas-basicas` | Quantas cestas básicas o salário mínimo compra | cestas básicas por salário mínimo | anual | jan/2025 | 03 | Anos 2004, 2005, 2007–2009, 2011, 2013, 2015 e 2017 não constam na tabela transcrita. |
| `salario-minimo-dolar` | Salário mínimo em dólares (corrente e paridade de poder de compra) | US$ correntes | anual | 2026 | 03 | — |
| `salario-minimo-ganho-real` | Ganho real do salário mínimo a cada reajuste | % acima da inflação | anual | jan/2026 | 03 | Ganho real do reajuste de mai/2023 (R$ 1.320) não informado. |
| `salario-minimo-nominal` | Salário mínimo nominal a cada reajuste | R$ | anual | jan/2026 | 03 | — |
| `selic-efetiva-acumulada-ano` | Selic efetiva acumulada no ano | % ao ano | anual | 12 meses até set/2026 | 01 | — |
| `selic-fim-de-ano` | Meta da taxa Selic em 31 de dezembro de cada ano | % ao ano | anual | 2026 (21/10/2026) | 01 | Datas da 282ª (3–4/11/2026) e 283ª (8–9/12/2026) reuniões do Copom só em fontes secundárias (Investidor10, Toro); calendário oficial não acessível. |
| `serasa-negativados` | Pessoas com dívidas em atraso (Serasa) | milhões de pessoas | anual | ago/2026 | 03 | — |
| `subutilizacao-pnad` | Taxa composta de subutilização da força de trabalho | % da força de trabalho ampliada | trimestral | 2T2026 | 03 | Série anual completa de desalento e participação não transcrita. |
| `transacoes-correntes-pib` | Saldo em transações correntes (% do PIB e US$ bilhões) | % do PIB (12 meses, dezembro) | anual | 2026 (jan–ago; % PIB em 12 meses até ago) | 01 | — |

## Séries pedidas e não criadas

- Nenhuma: todos os ids pedidos (`pib-anual`, `pib-media-por-governo`, `ipca-anual`, `ipca-meta-e-teto`, `selic-fim-de-ano`, `cambio-media-anual`, `reservas-internacionais`, `divida-bruta-pib`, `divida-liquida-pib`, `resultado-primario-pib`, `resultado-nominal-pib`, `juros-nominais-pib`, `carga-tributaria`, `emendas-parlamentares`, `desemprego-pnad-anual`, `desemprego-pnad-trimestral`, `emprego-formal-caged-saldo`, `informalidade`, `rendimento-medio-real`, `salario-minimo-nominal`, `salario-minimo-ganho-real`, `pobreza-ibge`, `pobreza-banco-mundial`, `extrema-pobreza`, `gini`, `bolsa-familia-familias`, `bolsa-familia-custo`, `endividamento-familias`, `inadimplencia-pf`, `balanca-comercial`, `pib-brasil-vs-mundo`, `ranking-pib-mundial`, `risco-pais-embi`, `ibovespa-fim-de-ano`) têm dados nas notas, mas vários são incompletos (ver coluna lacunas).

## Lacunas transversais

- Fechadas na rodada 2: Selic de 31/12 (todos os anos), intervalos da meta de inflação, Ibovespa 2004/2005/2012, PIB per capita 2024–2025, DBGG 2002–2005 (metodologia antiga), metas das LDOs 2003–2014, RP 9 por ano, juros 2003–2013 diretos, série anual de pobreza do IBGE, CAGED com ajustes, Bolsa Família oficial por dezembro, Auxílio Emergencial com fonte primária, datação do CODACE, textos das ordens executivas dos EUA, Decreto 12.797/2025.
- `risco-pais-embi`: série do Ipeadata termina em 30/07/2024; CDS só até mai/2026 via imprensa. `rating-soberano-eventos`: dias exatos de 2008–2016 sem fonte primária (`nao_verificado`).
- `endividamento-familias`, `inadimplencia-pf`, `familias-endividadas-peic`, `cds-brasil-5-anos`: pontos esparsos, sem série completa.
- `bolsa-familia-custo`: despesa orçamentária anual 2007–2021 não levantada (benefícios pagos de 2013–2021 em `bolsa-familia-valor-pago-anual`); série do Tesouro inacessível (HTTP 429).
- `emprego-formal-caged-saldo` / `caged-com-ajustes-por-governo`: quebra metodológica em 2020 (Novo CAGED); não comparar blocos antes e depois.
- `ldo-metas-primario`: LDOs 2015–2022 não levantadas; LDO 2005 inferida.
- `desemprego-pnad-anual`: a nota 01 traz médias de quatro trimestres (SIDRA) ligeiramente diferentes da Retrospectiva oficial usada aqui.
- `renda-per-capita-decimos-2012-2025`: anos 2013, 2015 e 2017 ausentes; base de preços da tabela 7531 a confirmar.
- `nem-nem`: duas definições (SIS x SIDRA 7205) não intercambiáveis.
- `informalidade`: variável oficial não calculada para 2012–2015; 4T2017 ausente.
- `governos.json`: indicadores de pobreza e Gini de Lula 1-2 usam Banco Mundial (2003→2009; 2010 ausente); desemprego de Lula 1-2 usa PME (não comparável); câmbio e reservas em 31/08/2016 não levantados.
- Permanecem sem dados: Artigo IV 2026 do FMI (inexistente na página oficial), custo oficial da desoneração após 2022, Mais Médicos, Farmácia Popular 2004–2022, Pé-de-Meia 2025–2026, checagem da frase literal 'Lula quebrou o Brasil'.
