# Séries de dados (`data/series/`) — notas 01, 02 e 03

Gerado em 2026-10-21 a partir das notas `01_macroeconomia_por_governo.md`, `02_contas_publicas_divida.md` e `03_emprego_renda_pobreza_social.md`. Só constam números, períodos e URLs presentes nas notas; anos ausentes estão em `lacunas`/`notas_metodologicas` de cada arquivo. Itens que as notas marcam como não verificados levam `nao_verificado: true`. Pontos parciais (ano em curso) levam `parcial: true`; projeções, `projecao: true`.

Total de séries desta leva: 57. Outras séries na pasta (saúde, segurança, educação, infraestrutura, energia etc.) foram geradas a partir de outras notas e não estão listadas aqui.

| id | título | unidade | frequência | último período | nota | lacunas |
|---|---|---|---|---|---|---|
| `balanca-comercial` | Balança comercial: saldo e exportações por ano | US$ bilhões | anual | 2026 (jan–ago) | 01 | — |
| `bolsa-familia-custo` | Custo anual do Bolsa Família / Auxílio Brasil | R$ bilhões | anual | 2026 | 02 | Custo anual 2007–2021 não levantado. Custo final auditado do Auxílio Emergencial (Tesouro) não obtido; só a faixa R$ 293–354 bi. |
| `bolsa-familia-familias` | Famílias atendidas pelo Bolsa Família / Auxílio Brasil | milhões de famílias | anual | out/2026 | 03 | Famílias e valor médio ano a ano 2003–2021 não obtidos (dados abertos do MDS não acessados). 2007–2009, 2011 e 2025 sem ponto. |
| `cambio-fim-de-periodo` | Dólar: cotação no fim de cada ano (R$/US$) | R$ por US$ | anual | set/2026 (fim de mês) | 01 | Cotação diária de 21/10/2026 não coletada (apenas o fechamento de set/2026). |
| `cambio-media-anual` | Dólar: cotação média anual (R$/US$) | R$ por US$ | anual | 2026 (jan–set) | 01 | — |
| `carga-tributaria` | Carga tributária bruta do governo geral (% do PIB) | % do PIB | anual | 2025 | 02 | Carga tributária 2003–2009 não disponível na metodologia do Tesouro. |
| `carteira-assinada-pnad` | Empregados do setor privado com carteira (PNAD Contínua) | mil pessoas | trimestral | 2T2026 | 03 | — |
| `desemprego-pme-anual` | Taxa de desemprego média anual (PME, 6 regiões metropolitanas, 2003–2012) | % da população economicamente ativa | anual | 2012 | 03 | — |
| `desemprego-pnad-anual` | Taxa de desocupação média anual (PNAD Contínua) | % da força de trabalho | anual | 2025 | 03 | — |
| `desemprego-pnad-trimestral` | Taxa de desocupação por trimestre (PNAD Contínua) | % da força de trabalho | trimestral | 2T2026 | 03 | Trimestres intermediários de 2012–2024 não transcritos na nota. |
| `desemprego-pnad-trimestre-movel` | Taxa de desocupação, trimestres móveis (últimos 12) | % da força de trabalho | mensal | jun–ago/2026 | 03 | — |
| `desoneracao-folha-custo` | Custo da desoneração da folha (compensação ao RGPS) | R$ bilhões | anual | 2025 | 02 | Custo anual oficial após 2022 e a Lei 14.973/2024 (reoneração gradual) não encontrados. |
| `divida-bruta-fmi` | Dívida bruta do governo geral na metodologia do FMI (% do PIB) | % do PIB | anual | 2031 (projeção) | 02 | Anos 2011–2013 e 2015 não constam na nota. |
| `divida-bruta-pib` | Dívida bruta do governo geral (% do PIB) | % do PIB | anual | ago/2026 | 02 | DBGG de 2002 a 2005 não existe na metodologia atual. |
| `divida-liquida-pib` | Dívida líquida do setor público (% do PIB) | % do PIB | anual | ago/2026 | 02 | — |
| `emendas-parlamentares` | Emendas parlamentares empenhadas e pagas por ano | R$ bilhões | anual | 2026 (parcial, até out/2026) | 02 | Valores de RP 9 em 2020 não localizados. Anos anteriores a 2014 não constam na nota. |
| `emprego-formal-caged-saldo` | Saldo anual de empregos com carteira (CAGED e Novo CAGED) | vínculos (saldo) | anual | 2026 (jan–ago) | 03 | Tabela oficial do MTE com saldos anuais 'com ajustes' 2003–2025 não acessada. |
| `endividamento-familias` | Endividamento das famílias (% da renda acumulada em 12 meses, BCB) | % da renda | mensal | jul/2026 | 03 | Meses anteriores a dez/2022 não transcritos. |
| `extrema-pobreza` | Extrema pobreza segundo o Banco Mundial (US$ 2,15/dia, PPC 2017) | % da população | anual | 2024 | 03 | Anos 2002, 2004, 2005, 2007, 2008, 2010, 2013, 2015 e 2017 não constam na nota. |
| `extrema-pobreza-ibge` | Extrema pobreza segundo o IBGE (linha de US$ 2,15 PPC/dia) | % da população | anual | 2024 | 03 | Anos 2012–2022 do IBGE não acessados. |
| `familias-endividadas-peic` | Famílias com dívidas (CNC/Peic) | % das famílias | mensal | mai/2026 | 03 | Peic de set/out/2026 não lida. Série mensal completa não transcrita. |
| `gini` | Índice de Gini do rendimento domiciliar per capita (IBGE) | índice (0 a 1) | anual | 2025 | 03 | Explicação oficial do IBGE para a revisão 0,506 → 0,504 (2024) não localizada. |
| `gini-banco-mundial` | Índice de Gini segundo o Banco Mundial (renda per capita) | índice (0 a 1) | anual | 2024 | 03 | Anos 2004, 2005, 2007, 2008, 2010, 2013 e 2017 não constam na nota. |
| `ibovespa-fim-de-ano` | Ibovespa no último pregão de cada ano | pontos | anual | 19/10/2026 | 01 | A nota não traz os fechamentos de 2004, 2005 e 2012. |
| `inadimplencia-pf` | Inadimplência das pessoas físicas (BCB) | % da carteira | mensal | ago/2026 | 03 | Meses intermediários não transcritos; série do juro do rotativo não localizada no SGS. |
| `informalidade` | Taxa de informalidade (PNAD Contínua) | % da população ocupada | trimestral | jun–ago/2026 | 03 | Série anual completa 2012–2023 não transcrita na nota. |
| `investimento-direto-pais` | Investimento direto no país (IDP) por ano | US$ bilhões | anual | 2026 (jan–ago) | 01 | — |
| `ipca-12-meses-mensal` | IPCA acumulado em 12 meses, mês a mês (2025–2026) | % em 12 meses | mensal | set/2026 | 01 | — |
| `ipca-anual` | Inflação (IPCA) por ano | % ao ano | anual | 2026 (12 meses até set/2026) | 01 | — |
| `ipca-meta-e-teto` | Meta de inflação, piso e teto por ano | % ao ano | anual | 2026 | 01 | Intervalos de tolerância por ano não verificados na página oficial do BCB. Não verificado se/quando o BC publicou carta aberta de descumprimento referente a 2025. |
| `juros-nominais-pib` | Juros nominais pagos pelo setor público (% do PIB) | % do PIB | anual | 12 meses até ago/2026 | 02 | Série 5760 não baixada antes de dez/2014. |
| `massa-rendimento-real` | Massa de rendimento real habitual | R$ bilhões | mensal | jun–ago/2026 | 03 | Série anual 2012–2024 não obtida (só 2025 e trimestres móveis de 2026). |
| `participacao-forca-trabalho` | Taxa de participação na força de trabalho e nível de ocupação | % da população em idade de trabalhar | trimestral | 2T2026 | 03 | — |
| `pib-anual` | Crescimento real do PIB por ano | % ao ano | anual | 2026 (acum. 4 trim. até 2T2026) | 01 | Datação oficial de recessões do CODACE/FGV não acessada (site retornou 503). |
| `pib-brasil-vs-mundo` | Crescimento do PIB: Brasil, América Latina, emergentes e mundo | % ao ano | anual | 2026 (projeção) | 01 | — |
| `pib-dolares` | PIB nominal em dólares | US$ bilhões | anual | 2026 (projeção FMI) | 01 | — |
| `pib-media-por-governo` | Média anual de crescimento do PIB por governo | % ao ano (média) | anual | Lula 3 (2023–2025) | 01 | — |
| `pib-per-capita-dolares` | PIB per capita em dólares (FMI) | US$ correntes | anual | 2026 (projeção FMI) | 01 | A nota traz apenas anos selecionados (2002, 2003, 2010, 2011, 2014–2016, 2018, 2020, 2022–2026); os demais anos não foram levantados. |
| `pib-per-capita-reais` | PIB per capita em reais correntes | R$ correntes | anual | 2025 | 01 | — |
| `pobreza-banco-mundial` | Pobreza segundo o Banco Mundial (US$ 6,85/dia, PPC 2017) | % da população | anual | 2024 | 03 | Anos 2004, 2005, 2007, 2008, 2010 e 2013 não constam na nota. |
| `pobreza-banco-mundial-ppc-2021` | Pobreza nas novas linhas do Banco Mundial (US$ 3,00 e US$ 8,30/dia, PPC 2021) | % da população | anual | 2024 | 03 | Apenas os anos 2003, 2014, 2019, 2021 e 2024 constam na nota. |
| `pobreza-ibge` | Pobreza segundo o IBGE (linha de US$ 6,85 PPC/dia) | % da população | anual | 2024 | 03 | Série anual completa 2012–2024 do IBGE não acessada (faltam 2012–2020 e 2022). |
| `ranking-pib-mundial` | Posição do Brasil entre as maiores economias (PIB em US$) | posição | anual | 2026 (projeção) | 01 | A nota só traz anos selecionados (2010, 2014, 2020, 2022, 2025, 2026). |
| `rendimento-medio-real` | Rendimento médio real habitual do trabalho (PNAD Contínua) | R$ a preços do último trimestre | trimestral | 2T2026 | 03 | 4T2013, 4T2020 e 4T2021 não constam na nota. |
| `rendimento-medio-real-trimestre-movel` | Rendimento médio real habitual, trimestres móveis de 2026 | R$ a preços do último trimestre | mensal | jun–ago/2026 | 03 | — |
| `reservas-internacionais` | Reservas internacionais (fim de ano) | US$ bilhões | anual | set/2026 | 01 | — |
| `resultado-nominal-pib` | Resultado nominal do setor público (% do PIB) | % do PIB | anual | 12 meses até ago/2026 | 02 | — |
| `resultado-primario-governo-central-pib` | Resultado primário do governo central (% do PIB, Tesouro) | % do PIB | anual | jan–jul/2026 | 02 | Percentual do PIB de 2026 (parcial) não informado na nota. Metas de superávit das LDOs 2003–2014 não localizadas em fonte oficial. |
| `resultado-primario-pib` | Resultado primário do setor público (% do PIB) | % do PIB | anual | 12 meses até ago/2026 | 02 | — |
| `risco-pais-embi` | Risco-país (EMBI+ Brasil) no fim de cada ano | pontos-base | anual | 2024 (até 30/07/2024) | 01 | EMBI+ e CDS após jul/2024 indisponíveis na nota. Histórico de ratings soberanos é dado de memória, não verificado; não convertido em série. |
| `salario-minimo-cestas-basicas` | Quantas cestas básicas o salário mínimo compra | cestas básicas por salário mínimo | anual | jan/2025 | 03 | Anos 2004, 2005, 2007–2009, 2011, 2013, 2015 e 2017 não constam na tabela transcrita. |
| `salario-minimo-ganho-real` | Ganho real do salário mínimo a cada reajuste | % acima da inflação | anual | jan/2026 | 03 | Ganho real do reajuste de mai/2023 (R$ 1.320) não informado. |
| `salario-minimo-nominal` | Salário mínimo nominal a cada reajuste | R$ | anual | jan/2026 | 03 | — |
| `selic-efetiva-acumulada-ano` | Selic efetiva acumulada no ano | % ao ano | anual | 12 meses até set/2026 | 01 | — |
| `selic-fim-de-ano` | Meta da taxa Selic no fim de cada ano | % ao ano | anual | set/2026 (vigente em 21/10/2026) | 01 | Valor de fim de ano não informado na nota para 2004–2009, 2011, 2013, 2014, 2016, 2017, 2019, 2021, 2023 e 2024. |
| `serasa-negativados` | Pessoas com dívidas em atraso (Serasa) | milhões de pessoas | anual | jul–ago/2026 | 03 | — |
| `subutilizacao-pnad` | Taxa composta de subutilização da força de trabalho | % da força de trabalho ampliada | trimestral | 2T2026 | 03 | Série anual completa de desalento e participação não transcrita. |

## Séries pedidas e não criadas

- Nenhuma: todos os ids pedidos (`pib-anual`, `pib-media-por-governo`, `ipca-anual`, `ipca-meta-e-teto`, `selic-fim-de-ano`, `cambio-media-anual`, `reservas-internacionais`, `divida-bruta-pib`, `divida-liquida-pib`, `resultado-primario-pib`, `resultado-nominal-pib`, `juros-nominais-pib`, `carga-tributaria`, `emendas-parlamentares`, `desemprego-pnad-anual`, `desemprego-pnad-trimestral`, `emprego-formal-caged-saldo`, `informalidade`, `rendimento-medio-real`, `salario-minimo-nominal`, `salario-minimo-ganho-real`, `pobreza-ibge`, `pobreza-banco-mundial`, `extrema-pobreza`, `gini`, `bolsa-familia-familias`, `bolsa-familia-custo`, `endividamento-familias`, `inadimplencia-pf`, `balanca-comercial`, `pib-brasil-vs-mundo`, `ranking-pib-mundial`, `risco-pais-embi`, `ibovespa-fim-de-ano`) têm dados nas notas, mas vários são incompletos (ver coluna lacunas).

## Lacunas transversais

- `selic-fim-de-ano`: a nota lista mudanças da meta por data, não o valor de 31/12; só anos legíveis diretamente foram incluídos (complemento em `selic-efetiva-acumulada-ano`).
- `ipca-meta-e-teto`: pisos e tetos não verificados na página oficial do BCB (JavaScript); centros das metas são oficiais.
- `pobreza-ibge` / `extrema-pobreza-ibge`: só 2021 (pico), 2023 e 2024; a série anual longa é do Banco Mundial.
- `informalidade`, `endividamento-familias`, `inadimplencia-pf`, `massa-rendimento-real`: pontos esparsos, sem série anual completa.
- `bolsa-familia-familias` / `bolsa-familia-custo`: valores aproximados e de fontes jornalísticas; dados abertos do MDS não acessados.
- `risco-pais-embi`: série do Ipeadata termina em 30/07/2024. Histórico de ratings soberanos é dado de memória e não virou série.
- `emprego-formal-caged-saldo`: quebra metodológica em 2020 (Novo CAGED); não somar entre governos.
- `desemprego-pnad-anual`: a nota 01 traz médias de quatro trimestres (SIDRA) ligeiramente diferentes da Retrospectiva oficial usada aqui.
- `governos.json`: indicadores de pobreza e Gini de Lula 1-2 usam Banco Mundial (2003→2009; 2010 ausente); desemprego de Lula 1-2 usa PME (não comparável).
