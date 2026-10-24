# Debate da TV Globo, 23/10/2026: checagem com dados oficiais

Data da checagem: 24/10/2026. Transcrição e lista de afirmações: [nota 16](https://github.com/matheushexsel/pentefino/blob/master/research_notes/Pente%20fino%20dados%20pol%C3%ADticos%20Brasil%202026/16_debate_globo_2026-10-23_transcricao.md). Evento no site: `data/eventos/debate-globo-2turno-2026-10-23.json`; falas `fala-0345` a `fala-0557`.

## Método

- As falas vêm das legendas automáticas de 15 clipes oficiais do canal g1 no YouTube, que juntos cobrem os blocos do debate (108 min).
- Por decisão editorial desta edição, os vereditos usam **apenas fontes oficiais**: órgãos federais (IBGE, Banco Central, Tesouro, Receita, ministérios, agências reguladoras, INPE, SINESP, DATASUS, INEP, Portal da Transparência), Legislativo (Câmara, Senado, Planalto, Diário Oficial, TCU), Judiciário (STF, STJ, TSE, TRFs), governos estaduais, organismos intergovernamentais (FMI, Banco Mundial, OMS, FAO) e, quando a fala é sobre outro país, órgãos oficiais desse país. Imprensa, agências de checagem, ONGs e institutos privados não foram usados.
- Quando não existe registro oficial público sobre o fato, o veredito é `insustentavel`. Isso não significa que a fala seja falsa, e sim que não há dado oficial que a confirme ou desminta.
- Escala: verdadeiro · verdadeiro-mas · falta-contexto · exagerado · impreciso · falso · insustentavel · opiniao.

## Placar

| Veredito | Lula | Flávio Bolsonaro |
|---|---|---|
| verdadeiro | 17 | 14 |
| verdadeiro-mas | 28 | 30 |
| impreciso | 11 | 3 |
| exagerado | 8 | 9 |
| falta-contexto | 7 | 25 |
| insustentavel | 19 | 27 |
| falso | 5 | 7 |
| opiniao | 2 | 1 |
| **total** | **97** | **116** |

## Economia, inflação, contas públicas, impostos e emprego

Checagem feita em 24/10/2026 só com dados oficiais (governo federal, Legislativo, BCB, IBGE, órgãos estaduais e organismos intergovernamentais), conforme REGRAS.md. Arquivo completo: `g1_economia_checado.json` (53 afirmações). As falas vêm da legenda automática do YouTube; quando a legenda é ambígua, a leitura checada está no JSON (`leitura_checada`, `leitura_incerta`).

#### Contagem

| Veredito | Lula | Flávio Bolsonaro | Total |
|---|---|---|---|
| verdadeiro | 6 | 3 | 9 |
| verdadeiro-mas | 9 | 6 | 15 |
| falta-contexto | 2 | 6 | 8 |
| exagerado | 1 | 4 | 5 |
| impreciso | 3 | 0 | 3 |
| falso | 1 | 3 | 4 |
| insustentavel | 1 | 7 | 8 |
| opiniao | 0 | 1 | 1 |
| **total** | 23 | 30 | 53 |

#### Tabela

| id | orador | frase (curta) | veredito | dado oficial decisivo |
|---|---|---|---|---|
| [F05](https://youtu.be/26XCkA5BHm8?t=83) | Flávio | Ô Lula, por que que você endividou o povo brasileiro desse jeito? | **falta-contexto** | [Endividamento das famílias / renda 12m: 49,86 % (jul/2026)](https://api.bcb.gov.br/dados/serie/bcdata.sgs.29037/dados?formato=json) |
| [L12](https://youtu.be/26XCkA5BHm8?t=102) | Lula | Se não fosse do governo do PT aumentar o salário mínimo acima da inflação, colocando o PIB no orçamento, o… | **verdadeiro-mas** | [Salário mínimo de abr/2002 (R$ 200) a preços de set/2026: 837,8 R$ de set/2026 (abr/2002)](http://www.ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='GAC12_SALMINRE12')) |
| [L13](https://youtu.be/26XCkA5BHm8?t=111) | Lula | (Paráfrase; legenda truncada: "por conta do seu pai do Tem [Temer] que não aumentaram") Os governos Temer e… (leitura incerta) | **verdadeiro-mas** | [Ganho real do mínimo em 2019 (cálculo próprio): 1,14 % (2019)](https://api.bcb.gov.br/dados/serie/bcdata.sgs.1619/dados?formato=json) |
| [L14](https://youtu.be/26XCkA5BHm8?t=218) | Lula | É por isso que nós chegamos a R$ 1600, porque senão seria 900 | **verdadeiro-mas** | [Salário mínimo de abr/2002 (R$ 200) a preços de set/2026: 837,8 R$ de set/2026 (abr/2002)](http://www.ipeadata.gov.br/api/odata4/ValoresSerie(SERCODIGO='GAC12_SALMINRE12')) |
| [L16](https://youtu.be/26XCkA5BHm8?t=238) | Lula | eu disse que como nós aprovamos o fim da escala por um [6x1], os trabalhadores vão ter dois dias para ficar… (leitura incerta) | **verdadeiro-mas** | [Emenda Constitucional nº 141/2026](https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc141.htm) |
| [F06](https://youtu.be/26XCkA5BHm8?t=288) | Flávio | (Paráfrase; legenda: "não adianta nada, Lulín ser de R$621") O salário mínimo atual é de R$ 1.621 (leitura incerta) | **verdadeiro** | [Salário mínimo vigente: 1.621 R$ (2026)](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/D12797.htm) |
| [F07](https://youtu.be/26XCkA5BHm8?t=296) | Flávio | você implementou a carga tributária mais alta desse país na história | **verdadeiro-mas** | [Carga tributária bruta do governo geral: 32,4 % do PIB (2025 (preliminar))](https://thot-arquivos.tesouro.gov.br/publicacao-anexo/28024) |
| [F08](https://youtu.be/26XCkA5BHm8?t=300) | Flávio | Até agora, com a reforma tributária, ninguém sabe quanto vai ser o valor do imposto de valor agregado. O… (leitura incerta) | **falta-contexto** | [Prazo para o Senado fixar a alíquota de referência da CBS…: data (31/10/2026)](https://www.planalto.gov.br/ccivil_03/leis/lcp/Lcp214.htm) |
| [F09](https://youtu.be/26XCkA5BHm8?t=316) | Flávio | Porque vai ser o maior IVA do mundo. O brasileiro vai pagar o maior imposto do mundo na era Lula | **falta-contexto** | [IVA-padrão da Hungria: 27 % (2024)](https://www.oecd.org/content/dam/oecd/en/topics/policy-sub-issues/consumption-tax-trends/consumption-tax-trends-hungary.pdf) |
| [F11](https://youtu.be/26XCkA5BHm8?t=343) | Flávio | como ele gasta muito mais do que ele arrecada e ele precisa aumentar impostos para cobrir o que ele tá… | **verdadeiro-mas** | [Déficit primário em 12 meses (convenção NFSP: positivo =…: 0,62 % do PIB (12 meses até ago/2026)](https://api.bcb.gov.br/dados/serie/bcdata.sgs.5793/dados?formato=json) |
| [F12](https://youtu.be/26XCkA5BHm8?t=352) | Flávio | A inflação chegou com toda a força | **exagerado** | [IPCA 12 meses: 4,58 % (set/2026)](https://apisidra.ibge.gov.br/values/t/1737/n1/all/v/2265/p/202101-202609) |
| [F13](https://youtu.be/26XCkA5BHm8?t=354) | Flávio | Nós temos uma das maiores taxas de juros do mundo. É a mesma taxa que reajusta a sua dívida | **verdadeiro-mas** | [Posição do Brasil entre bancos centrais com dado de…: 3 posição (set/2026)](https://stats.bis.org/api/v1/data/WS_CBPOL/M./all?lastNObservations=1&format=csv) |
| [F14](https://youtu.be/26XCkA5BHm8?t=367) | Flávio | já tem lá disponível uma caixa de ovo, uma dúia [dúzia] de ovos com 10 ovos. [...] tem um sabão em pó de 1… (leitura incerta) | **insustentavel** | [IPCA – ovo de galinha, acumulado: -0,59 % (jan/2023–set/2026)](https://apisidra.ibge.gov.br/values/t/7060/n1/all/v/63/p/202001-202609/c315/7169,7171,7173,7176,12222,7283,7355) |
| [F15](https://youtu.be/26XCkA5BHm8?t=406) | Flávio | Em quatro anos de governo, você consegue comprar mais ou menos com o seu salário | **falso** | [Rendimento médio real habitual: 3.777 R$ (preços de ago/2026) (jun–ago/2026)](https://apisidra.ibge.gov.br/values/t/6390/n1/all/v/5933/p/201812,202212,202512,202608) |
| [F17](https://youtu.be/Z2AA0h2wr4U?t=31) | Flávio | Quem produz tá sufocado, tá intimidado, não consegue tomar crédito porque tá muito caro | **exagerado** | [Concessões de crédito rural direcionado (PF+PJ): 338,6 R$ bilhões (safra 2023/24)](https://api.bcb.gov.br/dados/serie/bcdata.sgs.20701/dados?formato=json) |
| [L23](https://youtu.be/Z2AA0h2wr4U?t=124) | Lula | E é por isso que o nosso superávit comercial foi para quase 85 bilhões de reais (leitura incerta) | **verdadeiro** | [Saldo comercial (FOB): 84,2 US$ bilhões (out/2025–set/2026)](https://api-comexstat.mdic.gov.br/general) |
| [F21](https://youtu.be/Z2AA0h2wr4U?t=193) | Flávio | (Paráfrase; legenda confusa) No Plano Safra, considerando as garantias exigidas, o juro real chega a ficar… (leitura incerta) | **exagerado** | [Taxa média crédito rural PF: 11,12 % a.a. (ago/2026)](https://api.bcb.gov.br/dados/serie/bcdata.sgs.20771/dados?formato=json) |
| [F22](https://youtu.be/Z2AA0h2wr4U?t=233) | Flávio | você ainda contingencia os recursos do seguro rural e do e do do plano safra, inclusive para os agricultores… (leitura incerta) | **falta-contexto** | [Recursos do PSR destinados ao seguro rural: 565,4 R$ milhões (2025)](https://www.camara.leg.br/noticias/1276942-camara-aprova-projeto-que-reformula-o-seguro-rural/) |
| [L24](https://youtu.be/Z2AA0h2wr4U?t=311) | Lula | Não tem um segmento da agricultura brasileira que não tenha obtido muito mais recursos, muito mais… | **falta-contexto** | [Concessões crédito rural direcionado: 158 R$ bilhões (safra 2019/20)](https://api.bcb.gov.br/dados/serie/bcdata.sgs.20701/dados?formato=json) |
| [L25](https://youtu.be/Z2AA0h2wr4U?t=322) | Lula | o juro que esses bancos pagam na agricultura não é a taxa Selic. Esse juro é subsidiado tanto pelo BNDS… (leitura incerta) | **verdadeiro-mas** | [Taxa média crédito rural PF: 11,12 % a.a. (ago/2026)](https://api.bcb.gov.br/dados/serie/bcdata.sgs.20771/dados?formato=json) |
| [F27](https://youtu.be/FIKMIfvhAkA?t=141) | Flávio | você já gastou mais de R$ 400 bilhões de reais para tentar se reeleger | **insustentavel** | [Limite de gasto da União na compra de dívidas (Desenrola…: 15 R$ bilhões (MP 1.393/2026)](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/Mpv/mpv1393.htm) |
| [L33](https://youtu.be/FIKMIfvhAkA?t=184) | Lula | você inventou um tesouraço que um dia diz que vai, a sua economista diz que vai, você diz que nega (leitura incerta) | **insustentavel** | sem dado oficial localizado |
| [L43](https://youtu.be/vASlNIMp2PM?t=201) | Lula | Nós levamos [indústria] automobilística para Pernambuco. [...] nós levamos outra pra Bahia, levamos pro Ceará (leitura incerta) | **verdadeiro-mas** | [Governo de Pernambuco/ADEPE – 'Fiat inaugura sua fábrica…](https://www.adepe.pe.gov.br/na-rota-do-desenvolvimento-fiat-inaugura-sua-fabrica-da-jeep-em-goiana/) |
| [L53](https://youtu.be/QhluFzoPl30?t=267) | Lula | Milhões de trabalhadores se acidentam por irresponsabilidade patronal | **exagerado** | [Acidentes de trabalho registrados: 732.751 acidentes (2023)](https://www.gov.br/previdencia/pt-br/assuntos/previdencia-social/arquivos/AEAT_2023/secao-i-estatisticas-de-acidentes-do-trabalho/subsecao-a-acidentes-do-trabalho/capitulo-1-brasil-e-grandes-regioes/1-10-quantidade-de-acidentes-do-trabalho-por-situacao-do-registro-e-motivo-segundo-os-subgrupos-da-classificacao-brasileira-de-ocupacoes-cbo-no-brasil-2023) |
| [F47](https://youtu.be/QhluFzoPl30?t=374) | Flávio | tá com a conta atrasada, são mais de 80 milhões de pessoas como você que tão pagando contas além da data de… | **insustentavel** | [Inadimplência PF: 6,03 % (ago/2026)](https://api.bcb.gov.br/dados/serie/bcdata.sgs.21084/dados?formato=json) |
| [F48](https://youtu.be/QhluFzoPl30?t=397) | Flávio | arroz, feijão, carne? Tá tudo mais caro no seu governo | **falta-contexto** | [IPCA arroz: 3,92 % (jan/2023–set/2026)](https://apisidra.ibge.gov.br/values/t/7060/n1/all/v/63/p/202001-202609/c315/7169,7171,7173,7176,12222,7283,7355) |
| [F52](https://youtu.be/jctCsMD2nTE?t=27) | Flávio | O atual governo tá deixando uma dívida aí de R$ 11 trilhões de reais para você trabalhador pagar | **verdadeiro** | [DBGG: 11.054.954 R$ milhões (ago/2026)](https://api.bcb.gov.br/dados/serie/bcdata.sgs.13761/dados?formato=json) |
| [F53](https://youtu.be/jctCsMD2nTE?t=41) | Flávio | A taxa de juro oficial no Brasil hoje está aí em torno de 14% porque é um governo gastador | **verdadeiro-mas** | [Meta Selic: 13,75 % a.a. (desde 17/09/2026)](https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json) |
| [F54](https://youtu.be/jctCsMD2nTE?t=56) | Flávio | uma vez que a dívida do governo cresce, a dívida das famílias cresce junto | **falso** | [DBGG: 82,87 % do PIB (ago/2026)](https://api.bcb.gov.br/dados/serie/bcdata.sgs.13762/dados?formato=json) |
| [L55](https://youtu.be/jctCsMD2nTE?t=80) | Lula | (Paráfrase) Foi o grupo político de Flávio que aprovou a autonomia ("independência") do Banco Central | **verdadeiro** | [Votos 'sim' no Senado (substitutivo): 56 votos (03/11/2020)](https://legis.senado.leg.br/dadosabertos/materia/votacoes/135147) |
| [F55](https://youtu.be/jctCsMD2nTE?t=89) | Flávio | nós [fizemos] o Banco Central Independente [...] esse é um legado do presidente Jair Bolsonaro (leitura incerta) | **verdadeiro** | [Lei Complementar nº 179/2021](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp179.htm) |
| [F56](https://youtu.be/jctCsMD2nTE?t=124) | Flávio | lá em outubro de 2022, nas eleições anteriores, a previsão de taxa de juro, se o presidente Bolsonaro… | **verdadeiro-mas** | [Mediana Focus da Selic para o fim de 2026: 7,75 % a.a. (pesquisa de 28/10/2022)](https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoAnuais?$filter=Indicador%20eq%20'Selic'%20and%20Data%20ge%20'2022-10-01'%20and%20Data%20le%20'2022-10-31'%20and%20baseCalculo%20eq%200&$format=json) |
| [F57](https://youtu.be/jctCsMD2nTE?t=138) | Flávio | hoje nós temos uma taxa em torno de 14. São sete pontos percentuais de diferença com essa dívida pública de… (leitura incerta) | **exagerado** | [7 p.p. × DBGG (teto teórico, cálculo próprio): 774 R$ bilhões/ano (ago/2026)](https://api.bcb.gov.br/dados/serie/bcdata.sgs.13761/dados?formato=json) |
| [F59](https://youtu.be/jctCsMD2nTE?t=212) | Flávio | eu sei que as pratias [prateleiras] estão vazias agora porque as pessoas não tm dinheiro para comprar (leitura incerta) | **falso** | [Índice de volume de vendas do varejo (ajuste sazonal): 108,69 índice (2022=100) (ago/2026)](https://apisidra.ibge.gov.br/values/t/8880/n1/all/v/7170/p/all/c11046/all) |
| [L56](https://youtu.be/jctCsMD2nTE?t=235) | Lula | quando ele fala que vai comprar a dívida dos devedores, ele tá copiando uma coisa que eu já mandei pro… (leitura incerta) | **verdadeiro-mas** | [Deságio mínimo exigido: 90 % (MP 1.393/2026)](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/Mpv/mpv1393.htm) |
| [L57](https://youtu.be/jctCsMD2nTE?t=260) | Lula | nós fizemos [antes] de ontem, sabe, um perdão de quase 15 bilhões, de 4 milhões [e] meio que estava devendo… (leitura incerta) | **impreciso** | [Dívidas de MEIs na proposta de perdão: 12,6 R$ bilhões (out/2026)](https://www.gov.br/fazenda/pt-br/assuntos/noticias/2026/outubro/governo-encaminha-ao-congresso-nacional-proposta-para-trabalhadores-por-conta-propria) |
| [L59](https://youtu.be/jctCsMD2nTE?t=301) | Lula | (Paráfrase; legenda: "nós erdemos com 13% e que tá 13,75%") Lula diz ter herdado juros de 13%–13,75% de um… (leitura incerta) | **verdadeiro** | [Meta Selic: 13,75 % a.a. (31/12/2022)](https://api.bcb.gov.br/dados/serie/bcdata.sgs.432/dados?formato=json) |
| [L60](https://youtu.be/jctCsMD2nTE?t=309) | Lula | eu tive presidente do Banco Central 8 anos, não troquei. Fernando Henrique [trocou] quatro vezes (leitura incerta) | **verdadeiro** | [Presidentes do BC no governo FHC: 5 pessoas (1995–2002)](https://www.bcb.gov.br/historiacontada/) |
| [L61](https://youtu.be/jctCsMD2nTE?t=339) | Lula | É por isso que o salário mínimo cresceu no nosso governo | **verdadeiro** | [Salário mínimo: 1.621 R$ (2026)](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2025/decreto/D12797.htm) |
| [L62](https://youtu.be/jctCsMD2nTE?t=361) | Lula | ninguém nesse país, ninguém em nenhum momento da história fez mais crédito do que nós fizemos | **verdadeiro-mas** | [Crédito / PIB: 56,03 % (dez/2025)](https://api.bcb.gov.br/dados/serie/bcdata.sgs.20622/dados?formato=json) |
| [L63](https://youtu.be/jctCsMD2nTE?t=383) | Lula | a economia não crescia acima de 3% desde que eu deixei a presidência em 2010. E ela voltou a crescer | **falso** | [PIB, variação anual: 4 % (2011)](https://apisidra.ibge.gov.br/values/t/5932/n1/all/v/6563/p/201004,201104,201204,201304,201404,201504,201604,201704,201804,201904,202004,202104,202204,202304,202404,202504,202602/c11255/90707) |
| [F60](https://youtu.be/1FBddn-4QeM?t=84) | Flávio | O tesouraço vai ser nos impostos que você criou. Foram mais de 30 que você criou ou aumentou | **insustentavel** | [Lei nº 14.754/2023](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/L14754.htm) |
| [F71](https://youtu.be/sFjChKegcxs?t=22) | Flávio | Chegou ao ponto de de falar a seguinte frase: "Se a comida tá cara, não compra" | **verdadeiro-mas** | [Planalto, 'Entrevista do presidente Lula às rádios…](https://www.gov.br/planalto/pt-br/acompanhe-o-planalto/entrevistas/entrevista-do-presidente-lula-as-radios-sociedade-e-metropole-da-bahia) |
| [L71](https://youtu.be/sFjChKegcxs?t=44) | Lula | nós, desde o primeiro mês de mandato, nós criamos o primeiro [Desenrola] para resolver o problema da dívida,… (leitura incerta) | **impreciso** | [Data da MP do Desenrola Brasil: data (05/06/2023)](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/Mpv/mpv1176.htm) |
| [F72](https://youtu.be/sFjChKegcxs?t=96) | Flávio | O brasileiro antes parcelava um fogão, parcelava um microondas, parcelava a geladeira, agora parcela o que… | **insustentavel** | [Comprometimento de renda com dívidas: 28,72 % (jul/2026)](https://api.bcb.gov.br/dados/serie/bcdata.sgs.29034/dados?formato=json) |
| [F73](https://youtu.be/sFjChKegcxs?t=125) | Flávio | a Caixa Econômica Federal tem mais de 11 milhões de contratos imobiliários, são mais de 30 milhões de… | **insustentavel** | [Caixa Notícias, ago/2026 – 'CAIXA registra lucro líquido…](https://caixanoticias.caixa.gov.br/Paginas/Not%C3%ADcias/2026/08-AGOSTO/CAIXA-registra-lucro-liquido-recorrente-de-RS-39-bilhoes-no-2T26-e-RS-74-bilhoes-no-1S26.aspx) |
| [F74](https://youtu.be/sFjChKegcxs?t=146) | Flávio | É porque tá tudo atrelado à taxa de juro do seu governo, que é muito cara | **falta-contexto** | [TR acumulada (cálculo próprio): 2,02 % (out/2025–set/2026)](https://api.bcb.gov.br/dados/serie/bcdata.sgs.226/dados?formato=json) |
| [F75](https://youtu.be/sFjChKegcxs?t=151) | Flávio | (Paráfrase; valor ininteligível na legenda: "mais de R5 bilhões") Lula gastou bilhões em medidas para se… (leitura incerta) | **insustentavel** | [Data de envio do PLOA 2027: data (31/08/2026)](https://www.gov.br/fazenda/pt-br/assuntos/noticias/2026/setembro/governo-federal-apresenta-projeto-de-orcamento-de-2027-com-previsao-de-superavit-primario-de-r-18-6-bilhoes) |
| [F76](https://youtu.be/sFjChKegcxs?t=168) | Flávio | como você prometeu a picanha e não entregou a picanha | **opiniao** | [IPCA carnes: 18,5 % (jan/2023–set/2026)](https://apisidra.ibge.gov.br/values/t/7060/n1/all/v/63/p/202001-202609/c315/7169,7171,7173,7176,12222,7283,7355) |
| [L72](https://youtu.be/sFjChKegcxs?t=251) | Lula | nós fizemos dois desenrola. No primeiro atendemos 15 milhões de pessoas, no segundo atendemos quase 16… | **falta-contexto** | [Pessoas beneficiadas no Desenrola Brasil (2023–2024): 15 milhões (encerramento em mai/2024)](https://www.gov.br/fazenda/pt-br/assuntos/noticias/2024/maio/desenrola-brasil-encerra-com-beneficio-a-mais-de-15-milhoes-de-pessoas-e-reducao-da-inadimplencia-entre-a-populacao-mais-vulneravel-do-pais) |
| [L73](https://youtu.be/sFjChKegcxs?t=267) | Lula | Nós já mandamos a medida provisória. Vamos fazer um leilão esse mês, um leilão que pode chegar a mais de R50… (leitura incerta) | **impreciso** | [Limite de gasto da União: 15 R$ bilhões (MP 1.393/2026)](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/Mpv/mpv1393.htm) |
| [L74](https://youtu.be/sFjChKegcxs?t=300) | Lula | (Paráfrase; legenda truncada: "nós fizemos por isso 17 milhões [e] meio") Provável referência a ~17,5… (leitura incerta) | **verdadeiro** | [MEIs cadastrados: 17,6 milhões (out/2026)](https://www.gov.br/fazenda/pt-br/assuntos/noticias/2026/outubro/governo-encaminha-ao-congresso-nacional-proposta-para-trabalhadores-por-conta-propria) |
| [L75](https://youtu.be/sFjChKegcxs?t=306) | Lula | Nós fizemos a lei geral da pequena e média empresa | **verdadeiro-mas** | [Lei Complementar nº 123/2006](https://www.planalto.gov.br/ccivil_03/leis/lcp/lcp123.htm) |

#### Resumo de uma frase por item

- **F05** (falta-contexto): O peso das prestações na renda e a inadimplência das famílias estão em máximas, mas o tamanho da dívida em relação à renda está praticamente estável desde 2021 — o grande salto ocorreu em 2020–2021.
- **L12** (verdadeiro-mas): A ordem de grandeza está certa: corrigido apenas pela inflação desde 2002–2003, o mínimo estaria em torno de R$ 805–840 hoje, até um pouco abaixo dos R$ 900 citados.
- **L13** (verdadeiro-mas): Temer deu reajustes ligeiramente abaixo do INPC; Bolsonaro deu um ganho real pequeno em 2019 (+1,1%, pela regra de 2015) e praticamente zero nos anos seguintes.
- **L14** (verdadeiro-mas): O mínimo é R$ 1.621; sem ganhos reais desde 2002–2003 ele estaria entre R$ 805 e R$ 842 — abaixo até dos R$ 900 citados.
- **L16** (verdadeiro-mas): A Emenda Constitucional 141, promulgada em 16/10/2026, garante dois dias de repouso semanal, mas a regra só vale a partir de dez/2026 e quem aprovou foi o Congresso.
- **F06** (verdadeiro): O salário mínimo em vigor desde janeiro de 2026 é de R$ 1.621.
- **F07** (verdadeiro-mas): Na série oficial do Tesouro (2010–2025), a carga de 2025 (32,4% do PIB) é a maior, mas a série começa em 2010 e o número inclui estados e municípios.
- **F08** (falta-contexto): É verdade que a alíquota ainda não foi fixada, que a CBS começa em 2027 e que há estimativa oficial de ~28%, mas a lei não exige que o Executivo envie um projeto de lei com a alíquota: quem fixa a alíquota de referência é o Senado, por resolução, até 31 de outubro.
- **F09** (falta-contexto): A estimativa de ~28% superaria os 27% da Hungria, o maior IVA-padrão registrado pela OCDE, mas a alíquota ainda não foi fixada e a lei prevê medidas para trazê-la a 26,5%.
- **F11** (verdadeiro-mas): O setor público teve déficit primário em todos os anos do governo Lula e houve aumentos de tributos, mas déficits também ocorreram em 2014–2021 e o resultado de 2023 foi inflado pelo pagamento de precatórios represados.
- **F12** (exagerado): A inflação está acima da meta e encostada no teto (4,58% em 12 meses até setembro), mas longe de 'toda a força': em 2022 chegou a 12,13%.
- **F13** (verdadeiro-mas): A Selic de 13,75% é a 3ª maior entre os ~40 bancos centrais acompanhados pelo BIS, mas os empréstimos das famílias não são 'reajustados' pela Selic: custam em média 38% ao ano.
- **F14** (insustentavel): Não há registro oficial que confirme esses casos específicos nem que os ligue ao governo atual; a regra que obriga avisar a redução de embalagens é de 2021.
- **F15** (falso): A sugestão de queda do poder de compra não se confirma: o rendimento médio real do trabalho subiu cerca de 14% entre o fim de 2022 e meados de 2026.
- **F17** (exagerado): O crédito rural ficou mais caro e as concessões caíram em 2026, mas continuam em cerca de R$ 300 bilhões por safra — 'não consegue tomar crédito' exagera.
- **L23** (verdadeiro): Pelo MDIC, o superávit comercial nos 12 meses até setembro de 2026 foi de US$ 84,2 bilhões — 'quase 85 bilhões', em dólares, não em reais.
- **F21** (exagerado): As taxas médias do crédito rural estão entre 11% e 13,5% ao ano nominais; descontada a inflação de 4,6%, o juro real fica entre ~6% e ~8,5%, bem abaixo de 20%.
- **F22** (falta-contexto): A subvenção ao seguro rural era despesa discricionária sujeita a bloqueio, mas desde 30/09/2026 uma lei sancionada por Lula proíbe contingenciá-la — o que Flávio promete já está na lei.
- **L24** (falta-contexto): O crédito rural concedido nas safras do governo Lula superou o das safras do governo Bolsonaro em valores nominais, mas caiu depois do pico de 2023/24 e não há dado acessível por segmento.
- **L25** (verdadeiro-mas): O crédito rural e o habitacional têm taxas abaixo da Selic graças a subsídios, mas quem paga a equalização é o Tesouro (União), não os bancos.
- **F27** (insustentavel): Não há levantamento oficial que some 'R$ 400 bilhões' em medidas eleitorais; o número não pôde ser reconstruído.
- **L33** (insustentavel): As declarações atribuídas à economista da campanha não constam de fonte oficial consultada; no próprio debate, Flávio disse que reajustará mínimo e aposentadorias acima da inflação.
- **L43** (verdadeiro-mas): Há fábricas recentes nos três estados, mas a de Pernambuco foi inaugurada em 2015 (governo Dilma) e a do Ceará opera em montagem de kits; a negociação de Goiana começou em 2010 com o governo estadual.
- **L53** (exagerado): O Brasil registra cerca de 730–790 mil acidentes de trabalho por ano, não 'milhões' por ano; a atribuição à 'irresponsabilidade patronal' é juízo de valor.
- **F47** (insustentavel): O número de pessoas inadimplentes vem de birôs privados de crédito; não há contagem oficial equivalente, embora a taxa oficial de inadimplência das pessoas físicas esteja no maior nível desde 2011.
- **F48** (falta-contexto): Desde jan/2023, carnes subiram 18,5% (igual à inflação geral), mas arroz (+3,9%) e feijão-carioca (+3,0%) subiram muito menos que a inflação e o feijão-preto ficou mais barato (−3,7%); em 12 meses, porém, o feijão disparou.
- **F52** (verdadeiro): A dívida bruta do governo geral chegou a R$ 11,05 trilhões (82,9% do PIB) em agosto de 2026; era R$ 7,22 trilhões em dezembro de 2022.
- **F53** (verdadeiro-mas): A Selic está em 13,75% e o Copom cita a política fiscal entre os fatores que acompanha, mas o comunicado aponta também expectativas desancoradas, mercado de trabalho aquecido, petróleo e cenário externo.
- **F54** (falso): Os dados do Banco Central não mostram esse movimento conjunto: em 2021–2022 a dívida pública caiu enquanto a das famílias subiu, e em 2023–2026 ocorreu o contrário.
- **L55** (verdadeiro): A autonomia do BC (LC 179/2021) foi sancionada por Jair Bolsonaro; no Senado, Flávio votou a favor e os seis senadores do PT presentes votaram contra.
- **F55** (verdadeiro): A LC 179/2021 foi sancionada por Jair Bolsonaro em 24/02/2021, a partir de projeto do Senado aprovado com apoio do governo.
- **F56** (verdadeiro-mas): O Boletim Focus de out/2022 projetava Selic de 7,5%–7,75% para o fim de 2026, mas essa projeção não dependia de quem venceria a eleição.
- **F57** (exagerado): A conta não fecha: 7 pontos sobre R$ 11 trilhões dariam no máximo ~R$ 774 bilhões, e só parte da dívida é corrigida pela Selic; 'quase R$ 1 trilhão' é a conta total de juros, não a diferença.
- **F59** (falso): O volume de vendas do varejo está perto do recorde: 108,7 pontos em ago/2026 (2022=100), apenas 1,3% abaixo do máximo de mar/2026.
- **L56** (verdadeiro-mas): A MP 1.393/2026 autoriza a União a comprar carteiras de dívidas em procedimento competitivo com deságio mínimo de 90%, mas foi enviada ao Congresso como medida provisória (não 'ao Senado') e o teto de 95% não está no texto.
- **L57** (impreciso): O perdão é uma proposta enviada ao Congresso em 13/10/2026, ainda não aprovada, e os números oficiais são R$ 12,6 bilhões para 3,6 milhões de MEIs; a ampliação do limite e do 2º empregado também depende do Congresso.
- **L59** (verdadeiro): A Selic era 13,75% em 31/12/2022 e voltou a 13,75% em 17/09/2026, depois de chegar a 15% em 2025.
- **L60** (verdadeiro): Henrique Meirelles presidiu o BC durante os oito anos de Lula; no governo FHC houve cinco presidentes (Pérsio Arida, Gustavo Loyola, Gustavo Franco, Francisco Lopes e Armínio Fraga), ou seja, quatro trocas.
- **L61** (verdadeiro): O mínimo teve ganho real todos os anos do governo: cerca de +2,8% (2023), +3,1% (2024), +2,6% (2025) e +2,8% (2026) acima do INPC.
- **L62** (verdadeiro-mas): O crédito chegou ao maior nível da série em proporção do PIB (56,0% em dez/2025) e as concessões são recordes, mas isso é crédito dos bancos (públicos e privados), não 'feito' pelo governo, e a série começa em 2007.
- **L63** (falso): O PIB cresceu acima de 3% em 2011 (4,0%, governo Dilma) e em 2021 (4,8%, governo Bolsonaro); no atual governo cresceu 3,2% (2023), 3,4% (2024) e 2,3% (2025).
- **F60** (insustentavel): Não existe contagem oficial; há uma dezena de leis e decretos de 2023–2026 que criaram ou elevaram tributos, mas o total 'mais de 30' depende do critério de contagem.
- **F71** (verdadeiro-mas): Lula disse em entrevista a rádios da Bahia (06/02/2025) que, se o consumidor desconfia que um produto está caro, não deve comprá-lo, como forma de pressionar preços — a frase de Flávio é uma síntese que omite esse contexto.
- **L71** (impreciso): Há três edições, mas a primeira não foi no primeiro mês: a MP do Desenrola é de 5 de junho de 2023, o sexto mês de mandato.
- **F72** (insustentavel): Não há estatística oficial de parcelamento por tipo de produto nem sobre condições de pagamento de um aplicativo privado.
- **F73** (insustentavel): Não foi localizado dado oficial da Caixa com o número de contratos habitacionais ativos nem ranking da ouvidoria por motivo.
- **F74** (falta-contexto): A maior parte do financiamento imobiliário é corrigida pela TR, que sobe quando a Selic está alta (2,0% em 12 meses até set/2026, contra zero em 2019), mas a Selic é definida pelo Copom do BC autônomo, não pelo governo.
- **F75** (insustentavel): O PLOA 2027 foi enviado em 31/08/2026 (menos de dois meses antes do debate), mas o valor citado é ininteligível e não há levantamento oficial do custo das medidas anunciadas depois.
- **F76** (opiniao): Avaliação de promessa de campanha; os dados oficiais mostram que o preço das carnes subiu 18,5% de jan/2023 a set/2026, praticamente igual à inflação geral (18,9%).
- **L72** (falta-contexto): O primeiro Desenrola (2023–2024) beneficiou cerca de 15 milhões de pessoas, segundo a Fazenda; o número de quase 16 milhões para a segunda edição não foi localizado em fonte oficial.
- **L73** (impreciso): A MP existe (1.393/2026), mas o que foi aberto em outubro é um chamamento para os bancos informarem carteiras até 30/10, não o leilão; e a MP limita o gasto da União a R$ 15 bilhões.
- **L74** (verdadeiro): Segundo o governo, o Brasil tem 17,6 milhões de MEIs cadastrados.
- **L75** (verdadeiro-mas): A Lei Complementar 123/2006 (Estatuto da Microempresa e da Empresa de Pequeno Porte, que criou o Simples Nacional) é de 14/12/2006, no governo Lula — mas trata de micro e pequenas, não de médias empresas.

#### Lacunas

##### Gerais

- A API da Matriz de Dados do Crédito Rural (SICOR/BCB) retornou erro 500: não houve dado oficial por programa ou segmento (Pronaf, Pronamp, BNDES, BB). Os itens F17, F21 e L24 usam só o crédito rural direcionado do SGS.
- Páginas do gov.br com acesso restrito ("Conteúdo Restrito" ou captcha) durante o período eleitoral: Planalto (transcrições e notícias), MAPA (bloqueio do seguro rural), Fazenda (nota técnica das alíquotas e balanços do Desenrola). A Agência Gov e a Agência Brasil estão fora do ar por legislação eleitoral. Nesses casos, o título e o trecho indexado da página oficial foram usados, e o item foi marcado com `nao_verificado: true` quando isso foi decisivo (F71, L72, F73).
- O site do TCU bloqueou consultas automáticas, então não foi possível saber se o Executivo enviou ao TCU a proposta da alíquota de referência da CBS (prazo legal: 31/07/2026) nem se o TCU já mandou os cálculos ao Senado.
- Não há dado oficial para estes números: "80 milhões de inadimplentes" (só birôs privados), "R$ 400 bilhões para se reeleger", "mais de 30 impostos", "11 milhões de contratos da Caixa", parcelamento de comida e pizza, e os casos de reduflação citados.
- Últimos dados disponíveis em 24/10/2026: DBGG e resultado fiscal de ago/2026; endividamento das famílias de jul/2026; IPCA de set/2026 e IPCA-15 de out/2026; PNAD do trimestre jun–ago/2026; PMC de ago/2026; comércio exterior (MDIC) até set/2026.
- Contas próprias estão indicadas no JSON (acumulados de IPCA e INPC, somas de fluxos mensais, ganhos reais do mínimo, deflação do crédito rural, 7 p.p. × DBGG).

##### Por item

- **F05**: A série 29034 não pôde ser baixada para 2005–2015 (erro da API); o 'máximo' foi confirmado só para 2016–2026. Dados de jul–ago/2026 são os mais recentes publicados pelo BCB até 24/10/2026.
- **L12**: O contrafactual depende da base escolhida (2002 ou 2003) e do deflator; não há cálculo oficial único 'sem os governos do PT'. Textos das Leis 12.382/2011 e 13.152/2015 não foram reabertos nesta rodada.
- **L13**: O cálculo usa o INPC de janeiro a dezembro; as leis usam o INPC acumulado até novembro, o que pode mudar os resultados em décimos de ponto.
- **L14**: Mesmo contrafactual de L12 (depende da base e do deflator).
- **F06**: Valor 'R$621' na legenda; conferir no áudio.
- **F07**: Não foi localizada série oficial anterior a 2010 na mesma metodologia do Tesouro.
- **F08**: Não foi possível verificar se o Executivo enviou ao TCU a proposta até 31/07/2026 nem se o TCU já enviou os cálculos ao Senado (site do TCU bloqueou o acesso automatizado). A nota técnica da Fazenda com as estimativas (2024) tem acesso restrito no gov.br; a estimativa de 28% foi tomada da Agência Senado. As alíquotas do Imposto Seletivo (outro tributo) dependem de lei ordinária ainda não aprovada — tema distinto do IVA.
- **F09**: O relatório completo da OCDE (Consumption Tax Trends 2024) com o ranking de todos os países retornou 403; usou-se a nota de país da Hungria. A comparação com países fora da OCDE não foi feita.
- **F11**: Valores anuais em R$ obtidos por soma dos fluxos mensais (cálculo da nota 02 do projeto, conferido com a Nota para a Imprensa do BCB de 30/01/2026); não reconferido mês a mês nesta rodada. A atribuição causal 'aumenta impostos PARA cobrir gastos' é interpretação.
- **F13**: Ranking de juro real (descontada a inflação) não feito com fonte oficial. Argentina aparece no BIS só até jun/2025 (29%).
- **F14**: Sem dado oficial sobre os produtos citados; o texto da portaria foi identificado no repositório do MJ, mas não relido integralmente nesta rodada.
- **F15**: A frase é uma pergunta; a checagem avalia a sugestão implícita. A PNAD do trimestre jul–set/2026 ainda não havia sido divulgada.
- **F17**: A API da Matriz de Dados do Crédito Rural (SICOR) retornou erro 500; os números cobrem só crédito rural com recursos direcionados (SGS), sem segmentação por programa. Valores nominais (somas mensais, cálculo próprio).
- **L23**: A série do BCB (BPM6) dá valores menores (US$ 59,7 bi em 2025); a diferença é metodológica.
- **F21**: As resoluções do CMN com as taxas do Plano Safra 2026/27 não foram consultadas. Custo das garantias não tem medição oficial.
- **F22**: Páginas do MAPA sobre bloqueio do PSR em 2025 exigem autenticação; valor bloqueado não confirmado. Relatórios bimestrais de avaliação (SOF) não consultados para equalização do Plano Safra.
- **L24**: Dados por segmento/programa e por banco (BNDES, BB) não obtidos (SICOR com erro 500). Deflação feita com o IPCA de 12 meses em junho de cada ano (SIDRA 1737), aproximação própria.
- **L25**: Valor anual do subsídio (Orçamento de Subsídios da União) não consultado; normas do FGTS/MCMV não relidas.
- **F27**: Sem dado oficial; pedir a metodologia à campanha.
- **L33**: Programa de governo de Flávio Bolsonaro no TSE (DivulgaCandContas) não consultado.
- **L43**: As páginas do Planalto (BYD) e do governo do Ceará não abriram por acesso automatizado (captcha/erro de certificado/503); os dados de BA e CE vêm dos títulos e trechos dessas páginas oficiais em índice de busca. Papel exato do governo federal (incentivos da Lei 9.440/1997, FDNE) não quantificado.
- **L53**: Total oficial de 2024 (todas as categorias) não confirmado na tabela principal do AEAT; usado o número da notícia do ministério. Dados vieram de páginas oficiais identificadas por índice de busca; a tabela do AEAT não foi baixada integralmente.
- **F47**: Sem dado oficial de número de pessoas inadimplentes (o SCR do BC não publica essa contagem de forma aberta).
- **F48**: Acumulados calculados pela composição das variações mensais (cálculo próprio).
- **F52**: Dado de set/2026 ainda não publicado em 24/10/2026.
- **F53**: Ata completa da 281ª reunião não relida (só o comunicado).
- **L55**: Votação na Câmara (fev/2021) não consultada.
- **F57**: Não há estimativa oficial de sensibilidade da conta de juros a 1 p.p. de Selic consultada nesta rodada.
- **F59**: A frase pode ser figura de linguagem; checou-se a leitura literal sobre consumo.
- **L56**: Tramitação da MP no Congresso não consultada.
- **L57**: Número do PLP e tramitação não consultados na Câmara.
- **L59**: Os valores intermediários (10,50% e 15%) vêm da nota 01 do projeto, que consultou a mesma série SGS 432.
- **L60**: Datas exatas de posse de Francisco Lopes e Armínio Fraga não reconferidas; perfis da 'História Contada' lidos por índice de busca (o PDF de composição histórica do BC retornou 404).
- **L61**: Textos das Leis 14.663/2023 e 15.077/2024 não relidos nesta rodada (o limite de 2,5% vem da nota 03 e do PLOA 2027).
- **L62**: Não há série oficial de crédito/PIB anterior a 2007 na mesma metodologia.
- **F60**: Lista montada a partir das normas já levantadas na nota 12 do projeto (URLs do Planalto); os textos não foram reabertos nesta rodada. Não há inventário oficial de 'tributos criados ou aumentados' por governo.
- **F71**: A página do Planalto exigiu captcha e não pôde ser lida integralmente; o conteúdo foi confirmado pelo título e trecho indexado da página oficial (a Agência Gov/EBC está fora do ar por legislação eleitoral). Conferir a transcrição antes de publicar.
- **F72**: Sem dado oficial.
- **F73**: Release de resultados 2T26 da Caixa (RI) não baixado; página de notícias não exibiu o texto por acesso automatizado. Ranking de reclamações do BC (API Olinda) retornou erro 404.
- **F74**: Composição da carteira habitacional da Caixa por indexador não obtida.
- **F75**: Valor inaudível na legenda; conferir no áudio. Não verificado se as medidas constam ou não do PLOA 2027.
- **F76**: Consumo per capita de carne bovina (Conab) não obtido em tabela oficial nesta rodada.
- **L72**: Corpo das notícias da Fazenda sobre o Desenrola com acesso restrito em 24/10/2026; números tomados dos títulos das páginas oficiais. Balanço final da segunda fase (2026) não localizado.
- **L73**: Valor de face estimado das carteiras não divulgado.
- **L74**: Confirmar no áudio o que foi dito.
- **L75**: O texto compilado no Planalto não exibiu a assinatura presidencial no trecho extraído; a data (14/12/2006) situa a sanção no governo Lula.

## Saúde e programas sociais

Checagem feita em 24/10/2026 só com dados oficiais (governo federal, Congresso, Judiciário, estados) e intergovernamentais (FAO, OMS). As frases vêm da legenda automática do YouTube; quando a legenda é ambígua, a leitura checada está no JSON (`leitura_checada`) e marcada com `leitura_incerta`.

#### Contagem

| Veredito | Lula | Flávio Bolsonaro | Total |
|---|---|---|---|
| verdadeiro | 2 | 4 | 6 |
| verdadeiro-mas | 3 | 5 | 8 |
| falta-contexto | 0 | 4 | 4 |
| exagerado | 2 | 1 | 3 |
| impreciso | 2 | 2 | 4 |
| insustentavel | 7 | 5 | 12 |
| opiniao | 1 | 0 | 1 |
| **total** | 17 | 21 | 38 |

#### Tabela

| id | orador | frase (curta) | veredito | dado oficial decisivo |
|---|---|---|---|---|
| [F10](https://youtu.be/26XCkA5BHm8?t=328) | Flávio | na época do presidente Bolsonaro, você tinha lá os seus R$ 600 do Bolso Família… | **falta-contexto** | Acréscimo extraordinário mensal (EC 123/2022): 200 R$ por família (ago–dez/2022) — [Planalto — Emenda Constitucional 123, de 14/07/2022](https://www.planalto.gov.br/ccivil_03/constituicao/emendas/emc/emc123.htm) |
| [L26](https://youtu.be/Z2AA0h2wr4U?t=369) | Lula | eu tinha acabado com a fome neste país em 2012 | **verdadeiro-mas** | Prevalência de subalimentação (abaixo do limiar): 2.5 % (valor publicado: '<2,5') (2011–2013 a 2018–2020) — [FAO/FAOSTAT — Suite of Food Security Indicators, arquivo co…](https://bulks-faostat.fao.org/production/Food_Security_Data_E_All_Data_%28Normalized%29.zip) |
| [L27](https://youtu.be/Z2AA0h2wr4U?t=374) | Lula | (Paráfrase; legenda diz "33.000") Eu voltei em 2023 com 33 milhões de pessoas p… ⚑ | **exagerado** | Pessoas em insegurança alimentar grave: 17.9 milhões (média 2020–2022) — [FAO/FAOSTAT — Suite of Food Security Indicators, arquivo co…](https://bulks-faostat.fao.org/production/Food_Security_Data_E_All_Data_%28Normalized%29.zip) |
| [L28](https://youtu.be/FIKMIfvhAkA?t=28) | Lula | o sul do país é a região que proporcionalmente tem mais aposentado no Brasil | **verdadeiro** | Benefícios do RGPS por mil habitantes — Sul (aritmética própria): 216.7 por mil hab. (ago/2026 ÷ pop. 2025) — [IBGE/SIDRA — Tabela 6579 (estimativas de população 2025, Gr…](https://apisidra.ibge.gov.br/values/t/6579/n2/all/n1/all/v/9324/p/2025) |
| [L32](https://youtu.be/FIKMIfvhAkA?t=175) | Lula | (Paráfrase; legenda: "26 milhões de aposentados que considerário de mínimo") 26… ⚑ | **impreciso** | Aposentadorias previdenciárias emitidas (todos os valores): 24659976 benefícios (ago/2026) — [Ministério da Previdência Social — Boletim Estatístico da P…](https://www.gov.br/previdencia/pt-br/assuntos/previdencia-social/Dados-estatisticos-previdencia-social-e-inss/boletins-da-previdencia-social/2026/beps082026_final.pdf) |
| [F31](https://youtu.be/K-kGhpDV4zA?t=20) | Flávio | nós fizemos o marco legal do saneamento básico | **verdadeiro** | Votos Sim na Câmara (PL 4.162/2019, texto-base): 276 votos (11/12/2019) — [Câmara dos Deputados — API Dados Abertos, tramitações do PL…](https://dadosabertos.camara.leg.br/api/v2/proposicoes/2213200/tramitacoes) |
| [F32](https://youtu.be/K-kGhpDV4zA?t=23) | Flávio | hoje tem aproximadamente 90 milhões de brasileiros que não tem esgoto tratado n… | **impreciso** | População sem rede de água (aritmética própria: 206,8 mi × 15,9%): 32.9 milhões de hab. (2024) — [Ministério das Cidades — SINISA 2025 (ano de referência 202…](https://www.gov.br/cidades/pt-br/acesso-a-informacao/acoes-e-programas/saneamento/sinisa/resultados-sinisa/008_RELATORIO_SINISA_ABASTECIMENTO_AGUA_2025_defeso.pdf) |
| [F33](https://youtu.be/K-kGhpDV4zA?t=35) | Flávio | E nós fizemos esse marco legal exatamente para que houvesse o investimento e at… | **verdadeiro** | Meta de atendimento com água potável: 99 % da população (até 31/12/2033) — [Planalto — Lei 11.445/2007, texto compilado (art. 11-B, met…](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2007/lei/l11445compilado.htm) |
| [F34](https://youtu.be/K-kGhpDV4zA?t=45) | Flávio | Sabe quem votou contra isso lá no Congresso Nacional? A bancada do PT | **verdadeiro** | Votos do PT contra na Câmara (texto-base): 43 votos (11/12/2019) — [Câmara dos Deputados — Dados Abertos, votos nominais de 201…](https://dadosabertos.camara.leg.br/arquivos/votacoesVotos/csv/votacoesVotos-2019.csv) |
| [L34](https://youtu.be/K-kGhpDV4zA?t=65) | Lula | quando o pai dele apareceu na televisão rindo e imitando a pessoa morrendo asfi… | **verdadeiro-mas** | [Agência Senado (reprodução do relatório final da CPI da Pandemia) — '…](https://www12.senado.leg.br/noticias/materias/2021/10/25/saiba-mais-sobre-os-crimes-listados-pela-cpi-da-pandemia) |
| [F35](https://youtu.be/K-kGhpDV4zA?t=183) | Flávio | Por causa do atual governo, o saneamento já foi para depois de 2050 | **insustentavel** | População com rede coletora de esgoto: 59.7 % (2023) — [Ministério das Cidades — SINISA 2024 (ano de referência 202…](https://www.gov.br/cidades/pt-br/acesso-a-informacao/acoes-e-programas/saneamento/sinisa/resultados-sinisa/014_RELATORIO_SINISA_ESGOTAMENTO_SANITARIO_2024_defeso.pdf) |
| [L39](https://youtu.be/vASlNIMp2PM?t=43) | Lula | Eu quando assumi a presidência da República, o Nordeste era a região que tinha … ⚑ | **verdadeiro** | Taxa de analfabetismo 15+ — Nordeste: 23.4 % (2002) — [IBGE — Síntese de Indicadores Sociais 2003 (PNAD 2002), Tab…](https://ftp.ibge.gov.br/Indicadores_Sociais/Sintese_de_Indicadores_Sociais/Sintese_de_Indicadores_Sociais_2003/educacao.zip) |
| [F38](https://youtu.be/vASlNIMp2PM?t=133) | Flávio | o vídeo real sobre o Bolsonaro, ter aquele vídeo dele suspirando [...] Se você … | **insustentavel** | [Agência Senado (reprodução do relatório final da CPI da Pandemia) — '…](https://www12.senado.leg.br/noticias/materias/2021/10/25/saiba-mais-sobre-os-crimes-listados-pela-cpi-da-pandemia) |
| [L44](https://youtu.be/vASlNIMp2PM?t=214) | Lula | Nós fizemos 14 novos hospitais | **insustentavel** | [Secretaria da Saúde da Bahia — 'Primeiro hospital do Novo PAC entregu…](https://www.saude.ba.gov.br/2026/05/06/primeiro-hospital-do-novo-pac-entregue-no-brasil-sera-inaugurado-em-junho-na-bahia-com-oncologia-uti-pediatrica-e-mais-de-1-000-empregos/) |
| [F42](https://youtu.be/vASlNIMp2PM?t=333) | Flávio | Antigamente, no governo dele, o Bolsa Família era ali R$ 75, R$ 120 que você re… | **impreciso** | Benefício médio em dezembro: 190.79 R$ (dez/2019) — [Ipeadata (origem MDS/Portal da Transparência) — série VAL_P…](http://www.ipeadata.gov.br/api/odata4/ValoresSerie%28SERCODIGO='VAL_PBF'%29) |
| [L48](https://youtu.be/QhluFzoPl30?t=152) | Lula | (Paráfrase; legenda ininteligível no termo) Flávio, como senador, chamou o Bols… ⚑ | **insustentavel** | sem dado oficial localizado |
| [F43](https://youtu.be/QhluFzoPl30?t=300) | Flávio | os moradores de rua que dobraram durante seu governo. [...] Se o Brasil tinha 1… | **exagerado** | Pessoas em situação de rua no CadÚnico: 388855 pessoas (mai/2026) — [Agência Brasil/EBC, reproduzindo dados do CadÚnico — 'Rio d…](https://agenciabrasil.ebc.com.br/direitos-humanos/noticia/2026-08/rio-de-janeiro-tem-segunda-maior-populacao-de-rua-do-pais) |
| [F44](https://youtu.be/QhluFzoPl30?t=322) | Flávio | Você foi esquecido pelo atual governo por quatro anos. Sabe quando ele lembrou … ⚑ | **falta-contexto** | Aumento do piso por dia (aritmética própria: R$ 91 ÷ 30): 3.03 R$/dia (out/2026) — [Planalto — Decreto 13.120, de 17/09/2026 (correção dos bene…](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/decreto/D13120.htm) |
| [L64](https://youtu.be/1FBddn-4QeM?t=21) | Lula | (Paráfrase) Lula diz ter visto na imprensa que o "escolhido" de Flávio (para um… ⚑ | **insustentavel** | [TSE/DivulgaCandContas — plano de governo de Flávio Bolsonaro (doc. 28…](https://divulgacandcontas.tse.jus.br/divulga/rest/arquivo/doc/280017104726) |
| [L65](https://youtu.be/1FBddn-4QeM?t=49) | Lula | o plano de saúde mais importante que tem em qualquer país com mais de 100 milhõ… | **opiniao** | [Planalto — Constituição Federal de 1988 (arts. 196 a 200)](https://www.planalto.gov.br/ccivil_03/constituicao/constituicao.htm) |
| [L66](https://youtu.be/1FBddn-4QeM?t=57) | Lula | (Paráfrase; legenda: "deixar morrer 726.000 do pessoal para COVID") O governo B… ⚑ | **impreciso** | Óbitos acumulados por Covid-19 (dados notificados à OMS): 693734 óbitos (até 31/12/2022) — [OMS — WHO COVID-19 global daily data (CSV, dados notificado…](https://srhdpeuwpubsa.blob.core.windows.net/whdh/COVID/WHO-COVID-19-global-daily-data.csv) |
| [F61](https://youtu.be/1FBddn-4QeM?t=94) | Flávio | Tá faltando até de pirona [dipirona] na unidade básica de saúde ⚑ | **insustentavel** | sem dado oficial localizado |
| [F62](https://youtu.be/1FBddn-4QeM?t=120) | Flávio | Agora o Lula votou contra a Constituição de 88 que criou o SUS. [...] você é um… | **verdadeiro-mas** | Deputados constituintes do PT: 16 deputados (1987–1988) — [Câmara dos Deputados — Discurso de Luiz Inácio Lula da Silv…](https://www2.camara.leg.br/atividade-legislativa/plenario/discursos/escrevendohistoria/25-anos-da-constituicao-de-1988/constituinte-1987-1988/pdf/Luiz%20Inacio%20-%20DISCURSO%20%20REVISADO.pdf) |
| [L67](https://youtu.be/1FBddn-4QeM?t=168) | Lula | no governo do pai dele, sabe, quem tomasse vacina ia virar gay, ia virar jacaré | **verdadeiro-mas** | [Agência Senado (reprodução do relatório final da CPI da Pandemia) — '…](https://www12.senado.leg.br/noticias/materias/2021/10/25/saiba-mais-sobre-os-crimes-listados-pela-cpi-da-pandemia) |
| [L68](https://youtu.be/1FBddn-4QeM?t=175) | Lula | Ele inventou remédio para vender clorquina [cloroquina] | **exagerado** | [Agência Senado (reprodução do relatório final da CPI da Pandemia) — '…](https://www12.senado.leg.br/noticias/materias/2021/10/25/saiba-mais-sobre-os-crimes-listados-pela-cpi-da-pandemia) |
| [L69](https://youtu.be/1FBddn-4QeM?t=224) | Lula | poderia ter salvado pelo menos metade das pessoas que morreram | **insustentavel** | Mortes que não teriam ocorrido com a média mundial (estimativa apresentada à CPI): 400000 óbitos (até jun/2021) — [Agência Senado — 'Pesquisas apontam que 400 mil mortes pode…](https://www12.senado.leg.br/noticias/materias/2021/06/24/pesquisas-apontam-que-400-mil-mortes-poderiam-ser-evitadas-governistas-questionam) |
| [L70](https://youtu.be/1FBddn-4QeM?t=244) | Lula | você tá colocando uma pessoa que não quer colocar dinheiro no SUS, já disse que… | **insustentavel** | [TSE/DivulgaCandContas — plano de governo de Flávio Bolsonaro (doc. 28…](https://divulgacandcontas.tse.jus.br/divulga/rest/arquivo/doc/280017104726) |
| [F63](https://youtu.be/1FBddn-4QeM?t=267) | Flávio | meu pai foi salvo de uma facada que foi dada por um ex-integrante do [PSOL] na … ⚑ | **insustentavel** | [Agência Brasil/EBC, citando a Polícia Militar de MG — 'Jair Bolsonaro…](https://agenciabrasil.ebc.com.br/geral/noticia/2018-09/jair-bolsonaro-e-agredido-durante-campanha-em-juiz-de-fora) |
| [F64](https://youtu.be/1FBddn-4QeM?t=285) | Flávio | a espera para uma cirurgia de câncer de tireoide ultrapassou os 700 dias | **verdadeiro-mas** | Espera mediana — tireoidectomia total em oncologia: 719 dias (2025) — [TCU — Acórdão 1622/2026-Plenário (TC 015.703/2025-8), audit…](https://contas.tcu.gov.br/sagas/SvlVisualizarRelVotoAc?codFiltro=SAGAS-SESSAO-ENCERRADA&seOcultaPagina=S&item0=912227) |
| [F65](https://youtu.be/1FBddn-4QeM?t=305) | Flávio | Aquela emenda que eu coloquei aí para aqueles aparelhos que conservam os rins p… | **insustentavel** | sem dado oficial localizado |
| [F66](https://youtu.be/1FBddn-4QeM?t=324) | Flávio | Hoje vocês [santas casas] estão sufocados, estão devendo. E sabe quem é criedor… ⚑ | **falta-contexto** | Desconto máximo para Santas Casas no edital da PGFN (dívidas de FGTS e CS): 70 % da dívida (edital de out/2026) — [Ministério da Fazenda/PGFN — 'PGFN lança edital para negoci…](https://www.gov.br/fazenda/pt-br/assuntos/noticias/2026/outubro/pgfn-lanca-edital-para-negociar-dividas-de-fgts-e-contribuicoes-sociais-de-ate-r-45-milhoes) |
| [F67](https://youtu.be/1FBddn-4QeM?t=341) | Flávio | a tabela SUS, caso você não saiba, paga R$ 10 para um médico por consulta | **verdadeiro-mas** | Valor SIGTAP — consulta médica em atenção especializada: 10.0 R$ (12/2022 e 08/2026) — [Ministério da Saúde/DATASUS — SIGTAP, procedimento 03.01.01…](http://sigtap.datasus.gov.br/tabela-unificada/app/sec/procedimento/exibir/0301010072/08/2026) |
| [F68](https://youtu.be/1FBddn-4QeM?t=353) | Flávio | Uma médica que uma obstetra que faz um parto, por exemplo, recebe R$ 443 só por… | **verdadeiro-mas** | Valor total hospitalar — parto normal: 443.4 R$ (12/2022 e 08/2026) — [Ministério da Saúde/DATASUS — SIGTAP, procedimento 03.10.01…](http://sigtap.datasus.gov.br/tabela-unificada/app/sec/procedimento/exibir/0310010039/08/2026) |
| [F69](https://youtu.be/1FBddn-4QeM?t=361) | Flávio | Cada vez é menor o percentual que o governo federal coloca para o tratamento da… | **falta-contexto** | Participação da União no gasto com ASPS: 45.3 % (2012) — [Ipea — 'Gasto Público em Saúde' (Beneficiômetro)](https://www.ipea.gov.br/portal/beneficiometro/beneficiometro-artigos/saude/gasto-publico-em-saude) |
| [F70](https://youtu.be/1FBddn-4QeM?t=371) | Flávio | o governador Tarcísio lá em São Paulo, que criou a tabela SUS paulista. Com iss… | **verdadeiro-mas** | Valor do parto normal na Tabela SUS Paulista: 2217 R$ (2025) — [Agência SP (Governo do Estado de São Paulo) — 'Saiba como a…](https://www.agenciasp.sp.gov.br/saiba-como-a-tabela-sus-paulista-acelerou-cirurgias-e-exames/) |
| [F100](https://youtu.be/rUnAbA73RH0?t=449) | Flávio | se essa garrafa tiver 10 copos, cada dose custa R$ 50.000. [...] Isso dá para p… | **verdadeiro** | R$ 50.000 ÷ benefício médio (aritmética própria): 64–74 benefícios (out/2026 e antes) — [Agência Brasil/EBC, reproduzindo dados do MDS/Caixa — 'Bene…](https://agenciabrasil.ebc.com.br/economia/noticia/2026-10/beneficiarios-com-nis-de-final-3-0-recebem-bolsa-familia-de-outubro) |
| [L89](https://youtu.be/rUnAbA73RH0?t=480) | Lula | esse whisky foi tomado por você em julho de 2020, quando o cara veio vencer a v… ⚑ | **insustentavel** | [Agência Senado (reprodução do relatório final da CPI da Pandemia) — '…](https://www12.senado.leg.br/noticias/materias/2021/10/26/veja-a-lista-dos-indiciados-da-cpi-no-relatorio-de-renan-calheiros) |
| [L92](https://youtu.be/rUnAbA73RH0?t=744) | Lula | Ele sabe que ele tava no barco no dia que morreu 100 [mil] pessoas [...] no Bra… | **insustentavel** | Óbitos acumulados notificados à OMS: 100477 óbitos (10/08/2020) — [OMS — WHO COVID-19 global daily data (CSV, dados notificado…](https://srhdpeuwpubsa.blob.core.windows.net/whdh/COVID/WHO-COVID-19-global-daily-data.csv) |

⚑ = leitura incerta da legenda automática (ver `leitura_checada` no JSON).

#### Resumo por afirmação

- **F10** (Flávio, falta-contexto): O mínimo de R$ 600 foi pago no governo Bolsonaro, mas só de agosto a dezembro de 2022, por emenda constitucional temporária; o piso permanente deixado por lei era de R$ 400, e os R$ 600 em 2023 dependeram da EC 126/2022 e da Lei 14.601/2023.
- **L26** (Lula, verdadeiro-mas): Pela série atual da FAO, a subalimentação no Brasil ficou abaixo de 2,5% a partir do triênio 2011–2013 (centrado em 2012), mas isso ocorreu no governo Dilma e não significa fome zero.
- **L27** (Lula, exagerado): Nenhuma fonte oficial chega a 33 milhões: a FAO estima 17,9 milhões em insegurança alimentar grave em 2020–2022 e o IBGE mediu 8,5 milhões no fim de 2023; a direção (alta da fome até 2022) está correta.
- **L28** (Lula, verdadeiro): O Sul tem a maior proporção de benefícios do INSS por habitante (217 por mil, contra 169 no Brasil) e o Rio Grande do Sul lidera entre os estados (249 por mil).
- **L32** (Lula, impreciso): Pelo BEPS de agosto de 2026, há 24,9 milhões de aposentadorias no total e 29,5 milhões de benefícios de valor igual a um salário mínimo (22,9 milhões do RGPS e 6,6 milhões assistenciais); '26 milhões de aposentados no mínimo' não corresponde a nenhum desses números.
- **F31** (Flávio, verdadeiro): O PL 4.162/2019 foi enviado pelo Poder Executivo em agosto de 2019 e sancionado por Jair Bolsonaro como Lei 14.026, em 15/07/2020; Flávio votou a favor no Senado.
- **F32** (Flávio, impreciso): Para o esgoto a ordem de grandeza está certa, mas para a água o número oficial é cerca de 33 milhões sem rede de abastecimento, não 40 milhões (SINISA 2025, dados de 2024).
- **F33** (Flávio, verdadeiro): A Lei 14.026/2020 fixou metas de 99% da população com água potável e 90% com coleta e tratamento de esgoto até 31/12/2033, com prorrogação possível até 2040 em casos específicos.
- **F34** (Flávio, verdadeiro): Na Câmara, os 43 deputados do PT que votaram disseram 'Não' ao texto-base (11/12/2019) e a bancada orientou 'Não'; no Senado (24/06/2020), os 6 senadores do PT votaram 'Não'.
- **L34** (Lula, verdadeiro-mas): O relatório final da CPI da Pandemia (via Agência Senado) registra que o presidente ridicularizou 'os doentes com falta de respiração', mas a ligação direta com os mortos por falta de oxigênio em Manaus é interpretação de Lula.
- **F35** (Flávio, insustentavel): Não há projeção oficial de universalização 'depois de 2050'; o prazo legal continua 2033 (prorrogável até 2040), e o ritmo de expansão não tem estimativa oficial localizada.
- **L39** (Lula, verdadeiro): Nos dois indicadores verificados (pobreza e analfabetismo, PNAD 2002), o Nordeste era de longe a pior região; os demais itens da lista não foram verificados.
- **F38** (Flávio, insustentavel): Não localizei gravação ou transcrição oficial do trecho para conferir o contexto; o único registro oficial encontrado, o relatório final da CPI, classifica o episódio como ridicularização de doentes com falta de ar.
- **L44** (Lula, insustentavel): Não encontrei contagem oficial de novos hospitais federais ou financiados pela União no Nordeste que permita confirmar ou negar o número 14.
- **F42** (Flávio, impreciso): O benefício médio foi de R$ 63 a R$ 97 nos governos Lula (2004–2010) e só chegou a cerca de R$ 190 em 2019–2020, já no governo Bolsonaro; o mínimo de R$ 600 valeu só de agosto a dezembro de 2022.
- **L48** (Lula, insustentavel): O uso do apelido 'bolsa-farelo' por Flávio só aparece em reportagens sobre posts apagados em rede social; não há registro oficial (discurso no Senado, documento) localizado.
- **F43** (Flávio, exagerado): O CadÚnico registrava 236,4 mil pessoas em situação de rua em dez/2022 e 388,9 mil em mai/2026, alta de 64%, não 'quase o dobro', e o ponto de partida oficial não é 199 mil.
- **F44** (Flávio, falta-contexto): O reajuste de 15,04% (piso de R$ 600 para R$ 691, cerca de R$ 3 por dia) é real e é o primeiro desde 2023, mas o decreto saiu em 17/09/2026, 36 dias antes do debate, e o governo criou adicionais em 2023.
- **L64** (Lula, insustentavel): Lula não diz quem fez a declaração nem onde; não há registro oficial localizado, e o plano de governo registrado no TSE não pôde ser aberto (HTTP 403).
- **L65** (Lula, opiniao): 'Mais importante' é juízo de valor; o que é verificável é que a Constituição define a saúde como direito de todos e cria um sistema único de acesso universal.
- **L66** (Lula, impreciso): Nenhum registro oficial chega a 726 mil: o painel do Ministério da Saúde soma 716.626 mortes em toda a pandemia e a OMS registra 693.734 até 31/12/2022, fim do governo Bolsonaro; 'optou por deixar morrer' é acusação política.
- **F61** (Flávio, insustentavel): Não localizei dado oficial de desabastecimento de dipirona nas UBS em 2026; o registro oficial encontrado é o recolhimento de um único lote pela Anvisa, citado só em reportagens.
- **F62** (Flávio, verdadeiro-mas): Lula anunciou em plenário, em 22/09/1988, o voto do PT contra a redação final da Constituição, mas o partido assinou o texto; votar contra o texto final não é votar contra o SUS.
- **L67** (Lula, verdadeiro-mas): A fala do 'jacaré' está registrada no relatório final da CPI; a de 'virar gay' não aparece nos registros oficiais localizados, que citam outra fala falsa, a que associava vacina à Aids.
- **L68** (Lula, exagerado): O relatório da CPI registra que o então presidente incentivou repetidamente o uso de cloroquina, sem eficácia comprovada, mas não há registro oficial de que ele tenha 'inventado' remédio ou o vendido.
- **L69** (Lula, insustentavel): Não há estatística oficial de mortes evitáveis; as estimativas citadas na CPI são de pesquisadores, contestadas por senadores governistas, e vão de cerca de 95 mil a 400 mil mortes.
- **L70** (Lula, insustentavel): Não localizei registro oficial de proposta de privatizar ou cobrar pelo SUS; o plano de governo no TSE não pôde ser aberto e a Constituição garante acesso universal.
- **F63** (Flávio, insustentavel): Uma fonte oficial confirma o atendimento na Santa Casa de Juiz de Fora (Polícia Militar, via Agência Brasil), mas não localizei registro oficial de que o atendimento foi pelo SUS nem da filiação do agressor ao PSOL.
- **F64** (Flávio, verdadeiro-mas): O TCU registrou espera mediana de 719 dias para tireoidectomia oncológica em 2025, mas a série oscila muito (era 1.121 dias em 2022, no governo Bolsonaro, e 75 em 2024) e cobre poucos casos registrados.
- **F65** (Flávio, insustentavel): Não consegui verificar a emenda: a consulta de emendas do Portal da Transparência exige chave de API e não localizei registro oficial alternativo.
- **F66** (Flávio, falta-contexto): Não há dado oficial localizado sobre o tamanho da dívida das Santas Casas com a Caixa, e o governo adotou medidas sobre dívidas tributárias e do FGTS dessas entidades (Lei 15.233/2025 e edital da PGFN de out/2026).
- **F67** (Flávio, verdadeiro-mas): O valor da consulta médica em atenção especializada na tabela SIGTAP é R$ 10,00, igual em 2022 e em 2026, mas é o valor de referência federal pago ao estabelecimento, que pode ser complementado por estados, municípios e programas federais.
- **F68** (Flávio, verdadeiro-mas): O parto normal vale R$ 443,40 na tabela SUS, sem mudança entre 2022 e 2026, mas esse é o total da internação: a parte do profissional é R$ 175,80.
- **F69** (Flávio, falta-contexto): A fatia da União no gasto público com saúde caiu de 45,3% em 2012 para 37,6% em 2022 (Ipea), mas a queda ocorreu sobretudo antes do atual governo, e não localizei dado oficial por esfera para 2023–2025.
- **F70** (Flávio, verdadeiro-mas): A Tabela SUS Paulista existe desde janeiro de 2024 e paga até cinco vezes a tabela federal; o governo paulista relata mais cirurgias e internações, mas não publica série oficial do tamanho ou do tempo das filas.
- **F100** (Flávio, verdadeiro): A conta fecha: R$ 50 mil equivalem a 64 benefícios médios de outubro de 2026 (R$ 782,92) ou 74 benefícios médios anteriores ao reajuste (R$ 675).
- **L89** (Lula, insustentavel): Não há registro oficial localizado de reunião de Flávio num barco em julho de 2020 sobre a Covaxin; o relatório final da CPI pediu o indiciamento de Flávio só por incitação ao crime, não no caso Covaxin.
- **L92** (Lula, insustentavel): Não há registro oficial do encontro no barco; é verdade que o Brasil passou de 100 mil mortes em agosto de 2020 e que nenhuma dose da Covaxin foi entregue.

#### Lacunas

- **F10**: Não consultei o PLOA 2023 enviado pelo governo Bolsonaro para quantificar o valor previsto para o benefício em 2023.
- **L26**: Não consultei o relatório SOFI 2014 original (que usava a série da época); usei a série revisada atual da FAO.
- **L27**: Não há medição do IBGE para 2022; a PNAD de 2023 já é do primeiro ano do governo Lula.
- **L28**: O BEPS publica por UF o total de benefícios do RGPS (aposentadorias, pensões e auxílios), não só aposentadorias; usei esse total como aproximação. A série só de aposentadorias por UF (AEPS) não foi consultada.
- **L32**: O BEPS não cruza espécie (aposentadoria) com faixa de valor, então o número exato de aposentadorias no piso não foi obtido.
- **F32**: O SINISA mede acesso à rede, não a qualidade ('água tratada'); o módulo de esgoto cobre municípios com 81,7% da população, e os percentuais nacionais são estimativas do sistema.
- **L34**: Não localizei gravação ou transcrição oficial (Planalto/EBC) da live com a imitação; o relatório integral da CPI no site do Senado ficou bloqueado por verificação anti-robô.
- **F35**: Não verifiquei o texto dos Decretos 11.598 e 11.599/2023 (regras de comprovação de capacidade econômico-financeira), citados na pauta como causa do atraso.
- **L39**: Desnutrição (POF 2002–2003), evasão escolar (Inep), universidades por região (Censo da Educação Superior/Inep) e mestres e doutores (Capes) não foram verificados; o servidor de download do Inep falhou na verificação TLS.
- **L39**: A PNAD 2002 não cobria a área rural do Norte (exceto Tocantins), o que limita a comparação com essa região.
- **F38**: Íntegra oficial da live (mar/2021) não localizada; relatório integral da CPI bloqueado por verificação anti-robô do Senado.
- **L44**: Faltam a lista oficial de hospitais construídos ou financiados pela União no Nordeste (Ministério da Saúde/SISMOB/Ebserh) e a definição do período.
- **F42**: A série do Ipeadata para 2021–2022 não inclui o benefício extraordinário pago à parte; por isso não usei as médias desses dois anos.
- **L48**: Conferir no áudio qual termo Lula usou e buscar na base de pronunciamentos do Senado; posts em redes sociais não são registro oficial.
- **F43**: O relatório do MDHC exigiu login (período eleitoral) e o número de dez/2022 foi conferido só pelo resumo indexado do documento oficial; o painel do CadÚnico (VIS Data/Observatório) exige JavaScript/login.
- **F43**: Não localizei em que data o CadÚnico teria registrado 199 mil pessoas.
- **F44**: A legenda '17 dias' pode ser erro de reconhecimento (o decreto é de 36 dias antes); conferir no áudio.
- **L64**: Identificar quem é o 'escolhido' e obter a íntegra do plano de governo no TSE.
- **L66**: O serviço do painel do MS não informa a data exata do último dado; a diferença entre o painel do MS e a OMS decorre de revisões e datas de corte.
- **F61**: Faltam dados oficiais de estoque da assistência farmacêutica básica (municípios/Ministério da Saúde).
- **F62**: Não consultei os votos nominais de Lula nos dispositivos da saúde nas votações de 1º e 2º turnos da Constituinte.
- **L67**: Não localizei transcrição oficial dos discursos de Bolsonaro de dez/2020 no site do Planalto.
- **L68**: Não consultei auditorias do TCU sobre a produção de cloroquina pelo Laboratório Químico Farmacêutico do Exército.
- **L69**: Não há cálculo oficial (Ministério da Saúde, IBGE) de mortes evitáveis.
- **L70**: Identificar a pessoa e a declaração; obter o plano de governo no TSE.
- **F63**: Filiação partidária de Adélio Bispo (TSE) e forma de financiamento do atendimento (AIH/SUS) não confirmadas em fonte oficial.
- **F64**: A RNDS registrou só 6,8% das cirurgias de 2024, segundo o TCU; os números refletem os casos registrados, não todo o SUS.
- **F65**: Consultar emendas de autoria de Flávio Bolsonaro (Portal da Transparência/Siga Brasil) com objeto 'máquina de perfusão renal'.
- **F66**: Montante da dívida das Santas Casas e participação da Caixa (só há dados de entidades privadas do setor).
- **F67**: O valor efetivamente pago ao médico depende do contrato local e não aparece no SIGTAP.
- **F68**: Não verifiquei incentivos federais adicionais por parto em estabelecimentos habilitados (ex.: Rede Alyne).
- **F69**: Série do SIOPS por esfera para 2023–2025 não acessada.
- **F70**: Dados da regulação estadual (CROSS) sobre tamanho e tempo de fila antes e depois de 2024.
- **F100**: O valor da garrafa (premissa de outra afirmação) não foi checado aqui.
- **L89**: Relatório integral da CPI bloqueado por verificação anti-robô; não foi possível buscar menções a Flávio no texto completo.
- **L92**: Avisos do Ministério da Saúde de 2021 sobre suspensão e cancelamento do contrato exigiram login (período eleitoral); relatório integral da CPI bloqueado.

#### Bloqueios de acesso nesta sessão

- Relatório final da CPI da Pandemia no site do Senado (`legis.senado.leg.br/sdleg-getter`): verificação anti-robô. Usei as matérias da Agência Senado que reproduzem o relatório.
- Páginas antigas do Ministério da Saúde e do MDHC: 'É necessário autenticar' (período eleitoral).
- Plano de governo no TSE (DivulgaCandContas): HTTP 403. Lista pública de filiados do TSE: deixou de ser publicada em 2021.
- Portal da Transparência e Siga Brasil (emendas): exigem chave de API ou JavaScript. Inep (download): falha na cadeia TLS do servidor. API de agregados do IBGE (servicodados): conexão encerrada; usei apisidra e o FTP do IBGE.

## Justiça, corrupção e eleição

Checagem feita em 24/10/2026 só com dados oficiais (TSE, STF, TRF4, Senado, Câmara, Alerj, MPRJ, MPF, CGU/Portal da Transparência, BCB, Previc). As falas vêm da legenda automática do YouTube; onde a legenda era ambígua, a leitura checada está no JSON (`leitura_incerta: true`). Arquivo completo: `g3_justica_eleicao_checado.json`.

#### Contagem por orador e veredito

| Orador | verdadeiro | verdadeiro-mas | falta-contexto | exagerado | impreciso | falso | insustentavel | opiniao | Total |
|---|---|---|---|---|---|---|---|---|---|
| lula | 0 | 4 | 0 | 1 | 1 | 0 | 5 | 1 | 12 |
| flavio-bolsonaro | 2 | 1 | 6 | 0 | 0 | 0 | 12 | 0 | 21 |

#### Tabela

| id | orador | frase (legenda) | veredito | dado oficial decisivo |
|---|---|---|---|---|
| [F23](https://youtu.be/Z2AA0h2wr4U?t=267) | flavio-bolsonaro | a todos os governadores eleitos na região Centro-Oeste, que são nossos aliados | **falta-contexto** | [TSE: GO Vilela (MDB) 59,17% x Wilder (PL); MT Pivetta (Rep.) 60,77% x Fagundes (PL); MS Riedel (PP, com PL) 67,07%; DF 2º turno](https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_candidato_munzona/votacao_candidato_munzona_2026.zip) |
| [L29](https://youtu.be/FIKMIfvhAkA?t=56) | lula | Eu até no último debate perguntei se você tinha tomado emprestado o motosferra [a motosserra] do do do Milei | **insustentavel** | Sem fonte oficial (debate de emissora privada) |
| [F29](https://youtu.be/FIKMIfvhAkA?t=259) | flavio-bolsonaro | Eu vou ajudar o governador Zuco [Zucco] [...] Você, Moro, governador eleito do Paraná [...] Quero que você, J… | **verdadeiro** | [TSE: Zucco 58,07%, Moro 50,11%, Jorginho 68,98% — todos "ELEITO" no 1º turno](https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_candidato_munzona/votacao_candidato_munzona_2026.zip) |
| [F36](https://youtu.be/K-kGhpDV4zA?t=186) | flavio-bolsonaro | doutor Daniel, governador eleito do Pará | **verdadeiro** | [TSE: Dr. Daniel (PODE) eleito com 51,39%](https://cdn.tse.jus.br/estatistica/sead/odsele/votacao_candidato_munzona/votacao_candidato_munzona_2026.zip) |
| [L51](https://youtu.be/QhluFzoPl30?t=235) | lula | Não vou permitir que um miliciano me chame de nove dedos | **opiniao** | [Nenhuma denúncia/condenação por milícia; Alerj: moção 2003 e Medalha Tiradentes 2005 a Adriano da Nóbrega](http://alerjln1.alerj.rj.gov.br/scpro0307.nsf/e4bb858a5b3d42e383256cee006ab66a/66ed6d7f6f4d035583257021004902c3) |
| [F58](https://youtu.be/jctCsMD2nTE?t=158) | flavio-bolsonaro | assim que passou do primeiro pro segundo turno com o Flávio Bolsonaro na frente, a taxa de juro futuro já cai… | **insustentavel** | [Focus/BCB: Selic esperada p/ fim de 2027 estável em 12,00% (02–16/10); DI futuro não é fonte oficial](https://olinda.bcb.gov.br/olinda/servico/Expectativas/versao/v1/odata/ExpectativasMercadoAnuais) |
| [L84](https://youtu.be/T8oPN6v1L0c?t=81) | lula | por que que um senador da República evita que um policial assassino que era para ser julgado agora dia 21 não… | **insustentavel** | Andamento do júri (TJRJ) e recurso (STJ) não localizados |
| [L85](https://youtu.be/T8oPN6v1L0c?t=299) | lula | Todo mundo assiste os discursos dele na Assembleia Legislativa defendendo miliciano, [limpando a garganta] of… | **verdadeiro-mas** | [Alerj: Moção 2650/2003 e PR 1067/2005 (Res. 931/2005) de Flávio a Adriano; parente era ex-mulher, não irmã](http://alerjln1.alerj.rj.gov.br/scpro0307.nsf/e4bb858a5b3d42e383256cee006ab66a/7c5e3718a895341783256dc9004b6f49?OpenDocument=) |
| [L86](https://youtu.be/rUnAbA73RH0?t=120) | lula | esse pai do bebê [Richarlison] faz uma denúncia de que o meu adversário e o advogado dele apareceram numa ilh… | **insustentavel** | Sem documento oficial da SPU/MGI/DOU localizado |
| [F94](https://youtu.be/rUnAbA73RH0?t=190) | flavio-bolsonaro | A justiça já investigou isso. Essa ação já transitou em julgado, já tem uma desão [decisão] definitiva. Essa… | **insustentavel** | Processo e trânsito em julgado não localizados |
| [F95](https://youtu.be/rUnAbA73RH0?t=199) | flavio-bolsonaro | o Will [Willer] é um amigo, não é meu sócio. O sócio dele é o seu o seu advogado, é o seu, é o ex-ministro da… | **insustentavel** | QSA/CNPJ não consultado; sem fonte oficial |
| [F98](https://youtu.be/rUnAbA73RH0?t=320) | flavio-bolsonaro | O Lula, você ganhou um whisk macalo [uísque Macallan] que vale R$ 500.000 | **insustentavel** | Sem registro oficial do presente ou do valor |
| [L87](https://youtu.be/rUnAbA73RH0?t=392) | lula | O que você não se conforma é que você criou um banqueiro e eu fiz ele prisioneiro | **verdadeiro-mas** | [Agência Senado/CAE: compra aprovada sob Campos Neto; STF: prisão decretada por Mendonça (04/03/2026), mantida 4x0](https://www12.senado.leg.br/noticias/materias/2026/05/19/senadores-questionam-como-bc-negou-e-depois-aprovou-venda-do-master-a-vorcaro) |
| [L90](https://youtu.be/rUnAbA73RH0?t=545) | lula | Quem pegou 30 134 milhões de vocári [Vorcaro] que até agora não apareceu é você | **insustentavel** | [STF: Flávio investigado no Inq 5070 (Havengate/Entre Investimentos); valores sob sigilo](https://portal.stf.jus.br/processos/detalhe.asp?incidente=7661993) |
| [F101](https://youtu.be/rUnAbA73RH0?t=555) | flavio-bolsonaro | A Polícia Federal acabou de fazer um relatório [...] sobre esse filme do presidente Bolsonaro que não tem din… | **insustentavel** | [STF: PF juntou documentos ao Inq 5070 em 16/10/2026; teor sigiloso](https://portal.stf.jus.br/processos/detalhe.asp?incidente=7661993) |
| [F102](https://youtu.be/rUnAbA73RH0?t=592) | flavio-bolsonaro | O seu recebeu R milhões deais [R$ (valor inaudível) milhões de reais] por fora, Lula. explica esses 30 milhõe… | **insustentavel** | Sem registro oficial do áudio ou do repasse |
| [L91](https://youtu.be/rUnAbA73RH0?t=615) | lula | criaram um banqueiro chamado Banco Master chamado VCAR [Vorcaro]. Esse cara corrompeu a república [...] se me… | **verdadeiro-mas** | [STF: fases da Compliance Zero contra senadores Ciro Nogueira (PP) e Jaques Wagner (PT); Flávio, Eduardo e Mario Frias no Inq 5070; sem denúncia](https://noticias.stf.jus.br/postsnoticias/stf-autoriza-9a-fase-da-operacao-compliance-zero-em-sp-ba-e-df/) |
| [F103](https://youtu.be/rUnAbA73RH0?t=654) | flavio-bolsonaro | (pergunta de Lula: "Quantas fotos tem você abraçado com ele?") nenhuma | **insustentavel** | Sem fonte oficial sobre fotos |
| [F104](https://youtu.be/rUnAbA73RH0?t=679) | flavio-bolsonaro | O assessor do Alexandre Padilha, foi a matéria da Veja aí [...] articulou para que o dinheiro dos fundos de p… | **insustentavel** | [Previc (19/11/2025): os 265 fundos de pensão fechados não tinham aplicações no Master](https://www.gov.br/previc/pt-br/noticias/patrimonio-do-setor-de-previdencia-complementar-esta-preservado) |
| [F105](https://youtu.be/rUnAbA73RH0?t=787) | flavio-bolsonaro | o endereço que o seu filho colocou naquela procuração [...] um imóvel em São Paulo que pode valer até R$ 15 m… | **insustentavel** | [MPF (2019): Gamecorp/Gol controlada por Fábio Luís, Bittars e Suassuna; imóvel em SP não conferido](https://combateacorrupcao.mpf.mp.br/mais_noticias) |
| [L93](https://youtu.be/rUnAbA73RH0?t=819) | lula | Ontem os meus advogados e o ministro Camilo e Senador foram no Tribunal Eleitoral entregar toda a minha papel… | **insustentavel** | Sem registro oficial do TSE acessível (portal 403) |
| [F106](https://youtu.be/rUnAbA73RH0?t=868) | flavio-bolsonaro | Não tô devendo nada pra sociedade brasileira, Lula. Quem deve explicações é você. [A] documentação tá toda lá | **insustentavel** | Sem registro oficial do TSE acessível (portal 403) |
| [F107](https://youtu.be/rUnAbA73RH0?t=881) | flavio-bolsonaro | Você foi condenado por ocultação de patrimônio, Lula. Você tirou tudo do seu nome | **falta-contexto** | [TRF4 confirmou condenações (2018, 2019); STF anulou (HC 193726, 8x3, 15/04/2021; suspeição de Moro 7x4)](https://noticias.stf.jus.br/postsnoticias/stf-confirma-anulacao-de-condenacoes-do-ex-presidente-lula-na-lava-jato/) |
| [F108](https://youtu.be/rUnAbA73RH0?t=888) | flavio-bolsonaro | A sua declaração de imposto de renda não existe. Os seus bens. [...] O sítio Atibai [Atibaia] tá lá na sua de… | **falta-contexto** | [TSE: declaração de bens de Lula 2026 existe (18 itens, R$ 4.775.650,64); TRF4: Bittar era proprietário formal do sítio](https://cdn.tse.jus.br/estatistica/sead/odsele/bem_candidato/bem_candidato_2026.zip) |
| [L94](https://youtu.be/rUnAbA73RH0?t=937) | lula | E veja que eu tô dizendo pra justiça com amigo seu que é o André Medonça [Mendonça], que é da sua turma | **verdadeiro-mas** | [Senado: Mendonça indicado por Bolsonaro (MSF 36/2021, então AGU), aprovado 47x32](https://legis.senado.leg.br/dadosabertos/plenario/lista/votacao/20211201.json) |
| [L95](https://youtu.be/rUnAbA73RH0?t=962) | lula | se eu ganho R$ 46.000 igual a você e você consegue comprar uma casa de R$ 10 milhões deais [de reais] | **exagerado** | [DL 172/2022: subsídio de R$ 46.366,19 para os dois; TSE: casa de Flávio declarada por R$ 6.226.043,80](https://cdn.tse.jus.br/estatistica/sead/odsele/bem_candidato/bem_candidato_2026.zip) |
| [F110](https://youtu.be/rUnAbA73RH0?t=987) | flavio-bolsonaro | por que que você, né, não abre o sigilo do cartão corporativo? | **verdadeiro-mas** | [CPGF: ~99% do gasto da Presidência é "sigiloso" em 2023–26 (R$ 83,4 de 84,5 mi) e em 2019–22; LAI art. 24 §2º](https://portaldatransparencia.gov.br/download-de-dados/cpgf) |
| [F111](https://youtu.be/rUnAbA73RH0?t=994) | flavio-bolsonaro | Por que você não tira o sigilo de 100 anos que você prometeu que ia não ia fazer e fez? | **falta-contexto** | [CGU: revisão de 2023 reverteu maioria dos sigilos; desde set/2024, 15 anos para dados pessoais](https://www.gov.br/cgu/pt-br/assuntos/noticias/2023/02/cgu-conclui-revisao-dos-sigilos-impostos-a-documentos-de-acesso-publico) |
| [F112](https://youtu.be/rUnAbA73RH0?t=998) | flavio-bolsonaro | Você prometeu que não ia indicar seus amigos pro Supremo, indicou | **falta-contexto** | [Senado: Zanin (advogado de Lula) 58x18; Dino (ministro da Justiça) 47x31; Messias rejeitado 34x42; promessa sem registro oficial](https://legis.senado.leg.br/dadosabertos/plenario/lista/votacao/20230621.json) |
| [F113](https://youtu.be/rUnAbA73RH0?t=1057) | flavio-bolsonaro | O filho dele tá lá na Europa, tá na Espanha. O Lulinha, ele mora no mesmo bairro lá do Vini Júnior [...] Quem… | **insustentavel** | Sem registro oficial público |
| [F114](https://youtu.be/rUnAbA73RH0?t=1089) | flavio-bolsonaro | ele bota sigilo nas entradas do Palácio do Alvorada. Por qu para esconder a entrada da Roberta Lucinga [Luchs… | **insustentavel** | Sem ato oficial localizado; LAI art. 24 §2º permite reservar dados de segurança até o fim do mandato |
| [L96](https://youtu.be/NnDsZaMp9Vw?t=31) | lula | pedir outra vez pro Google ver quem é que gastava mais no cartão corporativo. Se é o mandato do Lula ou o man… | **impreciso** | [CPGF + IPCA: Bolsonaro +19% real no total e +9,5% por mês (com Abin); sem Abin, Lula gasta +15%/mês](https://portaldatransparencia.gov.br/download-de-dados/cpgf) |
| [F115](https://youtu.be/Q7WHDg643ow?t=11) | flavio-bolsonaro | Eu nunca fui investigado por causa de envolvimento com milícia | **falta-contexto** | [STF (HC 201965): rachadinha era peculato, lavagem, ocultação e organização criminosa — não milícia; omite parentes de Adriano no gabinete](https://portal.stf.jus.br/noticias/verNoticiaDetalhe.asp?idConteudo=477496&ori=1) |

#### Lacunas

- **F23**: Declarações de apoio de Vilela e Pivetta a Flávio no 2º turno não constam de base oficial; só a imprensa as registraria.
- **L29**: Sem fonte oficial para o conteúdo do debate da Band de 18/10/2026; a conferência exige a gravação da emissora (fonte não oficial).
- **L51**: Andamento atual de eventual recurso do MPRJ no caso da rachadinha não confirmado em fonte oficial.
- **F58**: Série diária de taxas do Tesouro Direto (prefixados 2029/2032) não baixada — servidor do Tesouro Transparente devolveu HTTP 429; é a única fonte oficial próxima do "juro futuro". Focus publicado só até 16/10/2026 na consulta; o boletim de 23/10 não constava. Taxas de DI futuro (B3/ANBIMA) não são fonte oficial pelas regras do projeto.
- **L84**: Número do processo do júri (TJRJ, Niterói) e do recurso no STJ não localizados em fonte oficial; necessário para conferir a data de 21/10/2026, o adiamento e a assinatura de Flávio.
- **L85**: Atos de nomeação/exoneração da Alerj (Diário Oficial do Legislativo) de Raimunda Veras Magalhães e Danielle da Nóbrega não acessados — o site da Alerj recusou conexão. Discursos de Flávio em Plenário da Alerj não pesquisados em ata oficial.
- **L86**: Processo administrativo da SPU (certidão autorizativa de transferência, 2022) e requerimento de 2021 não acessados. Ato de nomeação do superintendente da SPU no RJ (DOU) não localizado. A acusação pública de Richarlison não é fato oficial.
- **F94**: Número e andamento da ação possessória (TJRJ, Angra dos Reis) e de eventual recurso ao STJ. Matrícula do imóvel e cadastro na SPU.
- **F95**: QSA/CNPJ da Receita Federal da sociedade "Aragão & Tomaz" (se existir) e de empresas de Willer Tomaz (ex.: Alcazar) não consultados; dado aberto do CNPJ é um arquivo de vários GB. Cadastro Nacional das Sociedades de Advogados (OAB) não é fonte oficial governamental pelas regras.
- **F98**: Relação oficial de presentes recebidos pelo presidente (Presidência/Gabinete Pessoal) não acessada. Pedido de inquérito apresentado pela defesa de Flávio ao STF (set/2026) não localizado no portal do STF.
- **L87**: Data exata e número do ato do BC que aprovou a transferência de controle do Banco Máxima (2018–2019) não localizados no DOU. Autoridade judicial que decretou a 1ª prisão de Vorcaro (17–18/11/2025) não confirmada em fonte oficial lida na íntegra.
- **L90**: Valores (R$ 61 mi / R$ 134 mi / US$ 12,3 mi) e destino dos recursos: autos sigilosos; nenhuma fonte oficial pública.
- **F101**: Teor do documento da PF de 16/10/2026 (sigiloso). Não há nota oficial da PF sobre as conclusões.
- **F102**: Autenticidade e data do áudio atribuído a Vorcaro: sem perícia oficial pública. Nenhum inquérito oficial sobre o Instituto Lula ligado ao caso Master foi localizado.
- **L91**: Menções a "bacanal" e pagamentos a mulheres não têm registro oficial público. Situação de eventual denúncia da PGR no caso Master não confirmada em fonte oficial.
- **F103**: Sem fonte oficial sobre fotos ou encontros públicos registrados entre Flávio e Vorcaro.
- **F104**: Reportagem da Veja não é fonte oficial; não foi localizado inquérito sobre assessor de Padilha. Texto integral da nota da Previc lido via índice do buscador (gov.br exige autenticação ao leitor).
- **F105**: Matrícula do imóvel em São Paulo (cartório de registro de imóveis) e valor de mercado não consultados. Que Suassuna era coproprietário formal do sítio não foi confirmado em fonte oficial lida (só Bittar aparece nominalmente no TRF4). Procuração de Fábio Luís ao TSE não é pública.
- **L93**: Andamento das petições das campanhas no PJe do TSE não acessível sem número do processo; portal de notícias do TSE devolveu 403. O que exatamente cada campanha protocolou, e quando, só aparece em reportagens (não usadas).
- **F106**: Mesma lacuna de L93: sem certidão ou andamento oficial do TSE sobre as autorizações de quebra de sigilo das duas campanhas.
- **F107**: Arquivamento posterior dos casos (prescrição do triplex em 2022; rejeição de nova denúncia de Atibaia) não confirmado em fonte oficial lida nesta rodada.
- **F108**: O registro dos pedalinhos com nomes dos netos não foi localizado em fonte oficial lida.
- **L95**: Valor de compra na escritura (citado pela imprensa como R$ 5,97 mi, 2021) e valor de mercado atual não conferidos em registro oficial.
- **F110**: Em jan/2023 o governo divulgou o detalhamento dos gastos de Bolsonaro, mas essa planilha não foi localizada em fonte oficial nesta rodada. Extratos de set–out/2026 ainda não publicados.
- **F111**: A promessa de campanha de Lula (2022) não tem registro oficial. Decisões da CGU em recursos LAI de 2023–2026 (Fala.BR / Busca de Precedentes) não pesquisadas caso a caso; a plataforma exige JavaScript.
- **F112**: Declaração de Lula de 2022 sobre critérios de indicação ao STF não tem registro oficial (só imprensa).
- **F113**: Andamento oficial dos inquéritos sobre Fábio Luís (STF, relator Mendonça) não localizado com número; conteúdo sigiloso.
- **F114**: Resposta do GSI e eventual recurso à CGU (Fala.BR) não localizados. Nenhum registro oficial (Anac/FAB) sobre os voos citados.
- **L96**: A base é organizada pelo mês do extrato (transações sigilosas não trazem data); há defasagem de cerca de um mês — o recorte com 1 mês de deslocamento dá resultado semelhante (+20% no total, +7,7% ao mês). Extratos de set–out/2026 ainda não publicados, por isso o período Lula tem 44 meses. Não se sabe qual recorte Lula usou; nenhum dá 30%.
- **F115**: Íntegra da denúncia do MPRJ contra Flávio (nov/2020) não acessada em fonte oficial; não foi possível ler como ela descreve o papel dos parentes de Adriano.

##### Lacunas gerais de acesso

- Páginas de notícias do gov.br (PF, CGU, Previc, MPS) devolvem "É necessário autenticar" ao leitor automatizado; o conteúdo foi lido pelo índice do buscador e está marcado como tal no JSON.
- tse.jus.br (notícias, DivulgaCand) devolve HTTP 403; os dados do TSE vieram dos arquivos abertos de cdn.tse.jus.br (gerados em 24/10/2026).
- planalto.gov.br, in.gov.br, tjrj.jus.br e jfpr.jus.br não responderam; o Tesouro Transparente devolveu HTTP 429 (taxas do Tesouro Direto).
- Inquéritos do caso Master/Dark Horse no STF (Inq 5026, Inq 5070) correm sob sigilo: só partes e andamentos são públicos.

## Segurança, relações exteriores e meio ambiente

Grupo g4: 32 afirmações. Só fontes oficiais (governo federal, Congresso, Judiciário, estados, órgãos oficiais estrangeiros e intergovernamentais). Acesso em 2026-10-24. Falas vêm da legenda automática do YouTube; `leitura incerta` indica trecho ambíguo.

#### Contagem

| Veredito | Lula | Flávio Bolsonaro |
|---|---|---|
| verdadeiro | 0 | 1 |
| verdadeiro-mas | 4 | 10 |
| falta-contexto | 2 | 7 |
| exagerado | 0 | 2 |
| falso | 0 | 3 |
| insustentavel | 2 | 1 |
| **total** | 8 | 24 |

#### Afirmações

| id | orador | frase (curta) | veredito | dado oficial decisivo |
|---|---|---|---|---|
| [L20](https://youtu.be/Z2AA0h2wr4U?t=101) | Lula | quando o meu adversário ficou lambendo o Trump para taxar o Brasil | **falta-contexto** | [USTR (EUA) — transcrição da audiência pública da Seção 301 sobre o Br…](https://ustr.gov/sites/default/files/files/Issue_Areas/Enforcement/Section%20301/0707%20USTR%20Brazil%20301%20Day%202_full.pdf) |
| [L21](https://youtu.be/Z2AA0h2wr4U?t=114) | Lula | Abrimos 700 novos mercados nesse país | **verdadeiro-mas** | Aberturas de mercado para o agro desde 2023 (anúncio): 700 aberturas (produto x destino) (jan/2023–out/2026) — [MAPA — 'Vice-presidente Geraldo Alckmin e ministr…](https://www.gov.br/agricultura/pt-br/assuntos/noticias/vice-presidente-geraldo-alckmin-e-ministro-andre-de-paula-anunciam-marca-de-700-novos-mercados-abertos-para-o-agro-brasileiro) |
| [L22](https://youtu.be/Z2AA0h2wr4U?t=120) | Lula | (Paráfrase; legenda confusa: "aumentamos em 57 países uma média de 10,5") Aumen… *(leitura incerta)* | **insustentavel** | Variação das exportações totais: 10.4 % (jan–set/2026 vs jan–set/2025) — [MDIC/Secex — Comex Stat, API (exportações por paí…](https://api-comexstat.mdic.gov.br/general) |
| [F24](https://youtu.be/Z2AA0h2wr4U?t=277) | Flávio | como o atual governo liberou geral nas fronteiras, tá aí, voltou a criminalidad… | **falso** | Mortes violentas (CVLI + mortes por intervenção de agente d…: 41145 vítimas (2025) — [MJSP/SINESP VDE — base de dados nacional 2025 (ba…](https://www.gov.br/mj/pt-br/assuntos/sua-seguranca/seguranca-publica/estatistica/download/dnsp-base-de-dados/bancovde-2025.xlsx/view) |
| [L30](https://youtu.be/FIKMIfvhAkA?t=64) | Lula | na Argentina a pobreza chegou a 40% | **falta-contexto** | Pobreza (pessoas), Argentina: 32.3 % das pessoas (1º sem. 2026) — [INDEC (Argentina) — Incidencia de la pobreza y la…](https://www.indec.gob.ar/uploads/informesdeprensa/eph_pobreza_09_2670733F4C4D.pdf) |
| [L31](https://youtu.be/FIKMIfvhAkA?t=70) | Lula | você disse que que é o modelo igual ao doilei [do Milei] *(leitura incerta)* | **verdadeiro-mas** | [Registro primário do debate: clipe oficial do g1 FIKMIfvhAkA (legenda…](https://youtu.be/FIKMIfvhAkA?t=117) |
| [F25](https://youtu.be/FIKMIfvhAkA?t=117) | Flávio | a esquerda governou por 20 anos [a Argentina] | **exagerado** | Mandatos de Néstor e Cristina Kirchner: 12.5 anos (25/05/2003–09/12/2015) — [Casa Rosada (Presidência da Argentina) — lista of…](https://www.casarosada.gob.ar/la-casa-rosada/historia/93-nuestro-pais/presidentes) |
| [F26](https://youtu.be/FIKMIfvhAkA?t=125) | Flávio | O Milei começou um governo com 211% de inflação. A taxa de juro lá chegou a 100% | **verdadeiro-mas** | Inflação ao consumidor, Argentina: 211.4 % em 12 meses (dez/2023) — [INDEC (Argentina) — Índice de precios al consumid…](https://www.indec.gob.ar/uploads/informesdeprensa/ipc_01_24DBD5D8158C.pdf) |
| [F30](https://youtu.be/FIKMIfvhAkA?t=305) | Flávio | essa rota de tráfico de armas e drogas, por exemplo, que passa pelo porto de Pa… | **verdadeiro-mas** | Cocaína retida pela Receita em Paranaguá: 1.8 toneladas (mais de) (2025 (12 operações)) — [Receita Federal — 'Receita Federal encontra 226 q…](https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2026/marco/receita-federal-encontra-226-quilos-de-cocaina-em-terminal-privado-em-paranagua) |
| [F37](https://youtu.be/K-kGhpDV4zA?t=226) | Flávio | A Transamazônica tá lá aberta, a estrada de terra cortada, mas por causa de dos… | **falta-contexto** | Investimento federal na ponte sobre o rio Xingu (BR-230/PA): 405.6 R$ milhões (Novo PAC, balanço 2025) — [DNIT — 'Região Norte recebeu R$ 3,3 bilhões em ob…](https://www.gov.br/dnit/pt-br/assuntos/noticias/regiao-norte-recebeu-r-3-3-bilhoes-em-obras-de-infraestrutura-em-2025) |
| [L37](https://youtu.be/K-kGhpDV4zA?t=309) | Lula | eles tinham um secretário, um ministro de meio ambiente que dizia que era para… | **verdadeiro-mas** | [STF — decisão na Pet 8.975 (min. Alexandre de Moraes, 13/05/2021), qu…](https://www.stf.jus.br/arquivo/cms/noticiaNoticiaStf/anexo/pet8975decisao.pdf) |
| [L38](https://youtu.be/K-kGhpDV4zA?t=363) | Lula | Aliás, eles anularam o Fundo Amazônia. Fomos nós que entramos e que fazemos o f… | **verdadeiro-mas** | Doações internalizadas ao Fundo Amazônia: 0 R$ (2019–2022) — [BNDES/Fundo Amazônia — Transparência, doações (da…](https://www.fundoamazonia.gov.br/pt/transparencia/doacoes/) |
| [F39](https://youtu.be/vASlNIMp2PM?t=170) | Flávio | o que você levou pro Nordeste foi o comando vermelho que se proliferou, tomou c… | **falta-contexto** | [Ipea — Atlas da Violência 2025: retrato dos municípios e dinâmica reg…](https://repositorio.ipea.gov.br/entities/publication/30af7920-4a88-448f-bc14-db21cb82ee30) |
| [F40](https://youtu.be/vASlNIMp2PM?t=181) | Flávio | os estados Nordeste são administrados pelos pelo PT e pelos seus parceiros. São… | **verdadeiro-mas** | Taxa de mortes violentas (CVLI + MIAE), Amapá: 42.4 por 100 mil hab. (2025) — [MJSP/SINESP VDE — base de dados nacional 2025 (ba…](https://www.gov.br/mj/pt-br/assuntos/sua-seguranca/seguranca-publica/estatistica/download/dnsp-base-de-dados/bancovde-2025.xlsx/view) |
| [F45](https://youtu.be/QhluFzoPl30?t=359) | Flávio | No seu governo, recorde de mulheres assassinadas | **falta-contexto** | Óbitos de mulheres por agressão (SIM): 3622 óbitos (2024 (dado final)) — [Ministério da Saúde/DATASUS — SIM, óbitos por cau…](http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sim/cnv/ext10uf.def) |
| [F46](https://youtu.be/QhluFzoPl30?t=363) | Flávio | E no seu governo, a quantidade de mulheres espancadas só aumenta | **verdadeiro-mas** | Notificações de mulheres agredidas por força corporal/espan…: 175104 notificações (2025 (preliminar)) — [Ministério da Saúde/DATASUS — SINAN, notificações…](http://tabnet.datasus.gov.br/cgi/deftohtm.exe?sinannet/cnv/violebr.def) |
| [F49](https://youtu.be/QhluFzoPl30?t=437) | Flávio | o governador Tarcísio junto com o prefeito Ricardo Nunes e o Guilherme Derrite.… | **verdadeiro-mas** | Usuários concentrados na Rua dos Protestantes antes da deso…: 2000 pessoas (cerca de) (até mai/2025) — [Agência SP (Governo do Estado de São Paulo) — 'Fi…](https://www.agenciasp.sp.gov.br/fim-da-cracolandia-completa-um-ano-com-acoes-integradas-e-melhora-da-seguranca-no-centro/) |
| [F51](https://youtu.be/QhluFzoPl30?t=585) | Flávio | Tem um estudo do FBI que diz que aonde há, na região onde há um grande maus-tra… | **verdadeiro-mas (provisório)** | [FBI — 'Tracking Animal Cruelty' (NIBRS passa a registrar crueldade an…](https://www.fbi.gov/news/stories/-tracking-animal-cruelty) |
| [F84](https://youtu.be/T8oPN6v1L0c?t=20) | Flávio | Lula, você já se colocou a favor de manter as saidinhas, né? | **verdadeiro-mas** | Votos pela derrubada do veto, Câmara: 314 votos (contra 126) (28/05/2024) — [Agência Senado — 'Pela segunda vez, Congresso aca…](https://www12.senado.leg.br/noticias/materias/2024/05/28/pela-segunda-vez-congresso-acaba-com-saidas-temporarias-de-presos-em-feriados) |
| [F85](https://youtu.be/T8oPN6v1L0c?t=30) | Flávio | como aconteceu com o sargento PM Dias lá em Minas Gerais, que tava de serviço e… | **verdadeiro** | [Agência Senado — 'Pela segunda vez, Congresso acaba com saídas tempor…](https://www12.senado.leg.br/noticias/materias/2024/05/28/pela-segunda-vez-congresso-acaba-com-saidas-temporarias-de-presos-em-feriados) |
| [F86](https://youtu.be/T8oPN6v1L0c?t=42) | Flávio | Você é uma pessoa ali que é contra a redução da maioridade penal | **falso** | [Agência Brasil/EBC — 'Lula defende redução da maioridade penal para c…](https://agenciabrasil.ebc.com.br/politica/noticia/2026-10/lula-defende-reducao-da-maioridade-penal-para-crimes-hediondos) |
| [F87](https://youtu.be/T8oPN6v1L0c?t=47) | Flávio | Você é contra classificar comando vermelho, PCC e milícias como organizações te… | **verdadeiro-mas** | Pena do crime de domínio social estruturado: 40 anos (máximo da pena-base; mínimo 20) (Lei 15.358/2026) — [Planalto — Lei nº 15.358, de 24/03/2026 (Marco Le…](https://www.planalto.gov.br/ccivil_03/_Ato2023-2026/2026/Lei/L15358.htm) |
| [F88](https://youtu.be/T8oPN6v1L0c?t=142) | Flávio | Era uma troca de tiros numa comunidade conflagrada. [...] porque eu tenho a con… | **falta-contexto** | [STJ — 'Mantida prisão de PM acusado pela morte de criança de cinco an…](https://www.stj.jus.br/sites/portalp/Paginas/Comunicacao/Noticias/02122021-Mantida-prisao-de-PM-acusado-pela-morte-de-crianca-de-cinco-anos-durante-patrulhamento-em-Niteroi--RJ-.aspx) |
| [F89](https://youtu.be/T8oPN6v1L0c?t=181) | Flávio | como nós já começamos a fazer com a lei antifacção. Os chefes dessas organizaçõ… | **verdadeiro-mas** | Pena máxima com aumento para líderes (40 anos em dobro): 80 anos (Lei 15.358/2026) — [Planalto — Lei nº 15.358, de 24/03/2026 (Marco Le…](https://www.planalto.gov.br/ccivil_03/_Ato2023-2026/2026/Lei/L15358.htm) |
| [F90](https://youtu.be/T8oPN6v1L0c?t=192) | Flávio | porque hoje a sua política é de desencarceramento. O que que é isso? Não tem va… | **falso** | Presos em celas físicas (total do RELIPEN): 727301 pessoas (31/12/2025) — [Senappen/MJSP — RELIPEN, 19º ciclo SISDEPEN, 2º s…](https://www.gov.br/senappen/pt-br/servicos/sisdepen/relatorios/relatorios-de-informacoes-penitenciarias/relatorio-do-2o-semestre-de-2025.pdf/@@display-file/file) |
| [F91](https://youtu.be/T8oPN6v1L0c?t=207) | Flávio | hoje lá no celular não fica preso por causa da audiência de custódia que mais u… | **verdadeiro-mas** | [CNJ — Resolução nº 213, de 15/12/2015 (audiências de custódia), assin…](https://atos.cnj.jus.br/atos/detalhar/2234) |
| [F92](https://youtu.be/T8oPN6v1L0c?t=254) | Flávio | Diferente desse atual governo que fala que o ladrão de celular não tem que ser… | **insustentavel** | sem registro oficial localizado |
| [F93](https://youtu.be/rUnAbA73RH0?t=61) | Flávio | Eu vou criar a casa da mulher brasileira, aonde você vai ser acolhida, o seu fi… | **falta-contexto** | Unidades da Casa da Mulher Brasileira em funcionamento: 13 unidades (ago/2026) — [Ministério das Mulheres — 'Casa da Mulher Brasile…](https://www.gov.br/mulheres/pt-br/central-de-conteudos/noticias/2026/agosto-defeso-eleitoral/casa-da-mulher-brasileira-como-funciona-o-atendimento-e-onde-encontrar-uma-unidade) |
| [F96](https://youtu.be/rUnAbA73RH0?t=208) | Flávio | Agora você falou outro bloco, que você vai acabar com a polícia *(leitura incerta)* | **falta-contexto** | [Registro primário do próprio debate: legenda automática dos clipes of…](https://youtu.be/T8oPN6v1L0c?t=340) |
| [F97](https://youtu.be/rUnAbA73RH0?t=268) | Flávio | Só pec aqui eh que você chamou de segurança era para controlar as polícias e nó… | **exagerado** | Votos a favor do substitutivo, 1º turno na Câmara: 487 votos (contra 15) (04/03/2026) — [Câmara dos Deputados — PEC 18/2025, ficha e votaç…](https://dadosabertos.camara.leg.br/api/v2/proposicoes/2500080/votacoes) |
| [L88](https://youtu.be/rUnAbA73RH0?t=421) | Lula | qual é a tua relação com a polícia que não permite você aceitar [a marcação] da… *(leitura incerta)* | **insustentavel** | Votos a favor do substitutivo do PL 3.723/2019 na Câmara: 283 votos (contra 140) (05/11/2019) — [Câmara dos Deputados — PL 3.723/2019, votações em…](https://dadosabertos.camara.leg.br/api/v2/proposicoes/2209381/votacoes) |
| [F99](https://youtu.be/rUnAbA73RH0?t=432) | Flávio | você tá se referindo a um projeto de lei que andou lá na Câmara, que um deputad… | **falta-contexto** | Votos a favor do substitutivo na Câmara: 283 votos (contra 140) (05/11/2019) — [Câmara dos Deputados — PL 3.723/2019, votações em…](https://dadosabertos.camara.leg.br/api/v2/proposicoes/2209381/votacoes) |

#### Resumo por item

- **L20** (falta-contexto): O registro oficial dos EUA mostra Flávio pedindo que as tarifas NÃO fossem aplicadas, embora endossando críticas americanas ao governo e sugerindo adiar a decisão até depois da eleição; quem foi condenado por buscar sanções foi o irmão, Eduardo.
- **L21** (verdadeiro-mas): O Ministério da Agricultura anunciou em 13/10/2026 a marca de 700 aberturas de mercado desde 2023, mas cada 'mercado' é a autorização de um produto para um país, não um país novo.
- **L22** (insustentavel): As exportações brasileiras cresceram 10,4% em jan–set de 2026, número próximo ao citado, mas não há dado oficial que corresponda a '57 países'.
- **F24** (falso): Os registros oficiais do SINESP mostram queda das mortes violentas e dos roubos de 2022 a 2025, no país e no Centro-Oeste; não há dado oficial que indique 'volta da criminalidade com força'.
- **L30** (falta-contexto): A pobreza argentina passou de 40% (chegou a 52,9% no início do governo Milei), mas hoje está em 32,3%, abaixo dos 41,7% que Milei herdou.
- **L31** (verdadeiro-mas): No próprio debate, Flávio defendeu Milei e disse que terá 'o mesmo trabalho aqui'; a expressão 'modelo igual' em fala anterior não foi verificada em registro oficial.
- **F25** (exagerado): Pelos mandatos oficiais, o kirchnerismo governou cerca de 16 anos (2003–2015 e 2019–2023), não 20.
- **F26** (verdadeiro-mas): A inflação de 211,4% é oficial (12 meses até dez/2023), mas o juro básico chegou a 133% antes de Milei; foi o Banco Central sob Milei que o baixou para 100%.
- **F30** (verdadeiro-mas): A Receita e a PF apreendem cocaína com frequência em contêineres de exportação em Paranaguá, mas não foram achados registros oficiais de rota de armas pelo porto.
- **F37** (falta-contexto): Há trechos da BR-230/PA ainda em licenciamento ambiental, mas o governo federal tem obras e licitações em andamento, e não se achou registro de licença negada.
- **L37** (verdadeiro-mas): Salles disse, na reunião ministerial de 22/04/2020, que era hora de 'ir passando a boiada e mudando todo o regramento'; Lula parafraseou com outras palavras.
- **L38** (verdadeiro-mas): O governo Bolsonaro extinguiu o comitê gestor do fundo e não houve novas doações de 2019 a 2022; o fundo não foi juridicamente anulado, e a reativação foi ordenada pelo STF e feita por decreto de Lula em 2023.
- **F39** (falta-contexto): O Ipea registra a expansão de facções como o CV no Nordeste, mas não há dado oficial que atribua essa expansão ao governo federal, e as expulsões não têm contagem oficial localizada.
- **F40** (verdadeiro-mas): Pelo SINESP de 2025, seis estados do Nordeste estão entre os sete com mais mortes violentas por habitante, mas o primeiro é o Amapá e o quarto é Pernambuco, governado pela oposição ao PT.
- **F45** (falta-contexto): Os feminicídios registrados bateram recorde em 2025, mas o total de mulheres assassinadas caiu e está entre os menores da série.
- **F46** (verdadeiro-mas): As notificações do SUS de mulheres agredidas com força corporal ou espancamento cresceram todo ano desde 2022, mas notificação não mede só violência: também reflete mais registro.
- **F49** (verdadeiro-mas): O governo paulista informa que a concentração de usuários na Rua dos Protestantes acabou em maio de 2025, mas os números são do próprio governo, sem avaliação independente oficial sobre a dispersão.
- **F51** (verdadeiro-mas): O FBI passou a registrar crueldade animal em 2016 e uma publicação do órgão aponta ligação com violência contra pessoas, mas no nível do agressor, não de 'regiões'.
- **F84** (verdadeiro-mas): Lula sancionou o fim da maior parte das saídas temporárias em 2024, mas vetou o fim da saída para visita à família; o Congresso derrubou o veto.
- **F85** (verdadeiro): O sargento Roger Dias da Cunha foi baleado em Belo Horizonte em janeiro de 2024, ao abordar suspeitos, por um preso que não voltou da saída de Natal; a lei que restringiu as saídas leva o nome dele.
- **F86** (falso): Em 15/10/2026, Lula disse ser a favor de reduzir a maioridade penal para 16 anos em crimes hediondos, mas não dentro da PEC da Segurança.
- **F87** (verdadeiro-mas): O governo rejeita equiparar facções a terrorismo e as tratou por lei própria, com penas de 20 a 40 anos; isso não significa defender as facções.
- **F88** (falta-contexto): O policial ainda não foi julgado, mas a 'troca de tiros' é a versão da defesa e dos policiais, contestada por testemunhas citadas no STJ.
- **F89** (verdadeiro-mas): A pena de líderes pode chegar a 80 anos na sentença, mas o Código Penal limita o tempo de prisão a 40 anos; a progressão exige de 75% a 85% da pena.
- **F90** (falso): A população presa cresceu no governo Lula: de 644 mil em celas em junho de 2023 para 727 mil em dezembro de 2025, segundo a Senappen.
- **F91** (verdadeiro-mas): O CNJ criou a audiência de custódia em 2015, sob Lewandowski, mas o CNJ é do Judiciário, a regra vem de tratados internacionais e virou lei em 2019, sancionada por Jair Bolsonaro.
- **F92** (insustentavel): Não foi localizado registro oficial de Lula ou do governo dizendo que ladrão de celular não deve ser preso para 'tomar uma cervejinha'.
- **F93** (falta-contexto): A Casa da Mulher Brasileira já existe desde 2013, tem 13 unidades em funcionamento e foi mantida por todos os governos desde então.
- **F96** (falta-contexto): A legenda tem as palavras 'acabar' e 'polícia' juntas, mas no contexto Lula prometia fortalecer a PF e a PRF e acabar com milícia e narcotráfico.
- **F97** (exagerado): O texto do governo tratava sobretudo de competências e integração e incluía corregedorias e ouvidorias autônomas; a Câmara acrescentou regras penais, com apoio quase unânime, e o Senado ainda não votou.
- **L88** (insustentavel): Existe projeto aprovado na Câmara que acaba com a marcação de munições das forças de segurança, mas não há registro oficial de voto ou ato de Flávio a favor dele.
- **F99** (falta-contexto): O projeto não virou lei, mas a Câmara aprovou o texto em 2019 e ele está parado no Senado, onde Flávio vota.

#### Lacunas

- L20: Não foi possível abrir o portal de comentários do USTR (comments.ustr.gov, em JavaScript) para ler a íntegra da manifestação escrita de Flávio.
- L20: Não se localizou registro oficial de declarações de Flávio em julho de 2025, quando a primeira tarifa foi anunciada.
- L21: O painel interativo de aberturas do MAPA não foi baixado; não se mediu o valor exportado pelas novas aberturas.
- L22: Não se localizou publicação oficial do MDIC ou da ApexBrasil com o número '57 países'; a leitura exata da frase depende do áudio.
- F24: Não foram consultadas séries específicas da PF/PRF sobre apreensões em faixa de fronteira; 'liberou geral nas fronteiras' não tem indicador oficial direto.
- L30: Fonte é órgão oficial estrangeiro (INDEC), não listado nominalmente nas regras; registrado como 'oficial-estrangeiro'.
- L31: A declaração anterior citada por Lula (debate da Band ou entrevista) não tem registro em fonte oficial; só em imprensa, que as regras excluem.
- F25: A lista da Casa Rosada consultada termina em Macri (2015–2019); a data do mandato de Alberto Fernández não foi conferida em página oficial.
- F26: Fontes são órgãos oficiais estrangeiros (INDEC, BCRA), registrados como 'oficial-estrangeiro'.
- F30: O total de 2025 (1,8 t) veio do índice do buscador: a página da Receita exigiu autenticação.
- F30: Não se buscou na base da Portos do Paraná nem no balanço anual consolidado da Receita.
- F37: A página do Ministério dos Transportes devolveu HTTP 401; os dados do edital (125 km, cerca de R$ 1 bilhão, trecho licenciado) vieram só do índice do buscador.
- F37: Não se consultou o sistema de licenciamento do Ibama (SisLic) para ver as licenças vigentes de cada segmento.
- L37: O laudo de degravação da PF divulgado pelo STF (S3) devolveu acesso negado; usou-se a transcrição reproduzida na decisão da Pet 8.975.
- L38: A página de doações do BNDES é carregada por JavaScript e não foi relida nesta rodada; os valores são os registrados nas notas do projeto em 21/10/2026.
- F39: O Atlas é coeditado pelo FBSP (ONG); só a parte do Ipea foi considerada, e o conteúdo foi lido pelo índice do buscador porque o repositório usa JavaScript.
- F39: Não se consultaram relatórios das secretarias de segurança do CE, BA e PE sobre expulsões.
- F40: Taxas calculadas pelo projeto com vítimas do SINESP e população estimada do IBGE (2025); podem diferir das publicadas por outras instituições.
- F40: O partido dos governadores é o da eleição de 2022 (TSE); trocas de partido posteriores não foram conferidas em fonte oficial.
- F45: A cobertura do SINESP nos primeiros anos (2015–2017) pode ser incompleta; por isso o SIM foi usado como série de controle.
- F45: SIM 2025 é preliminar.
- F46: O SINESP não traz lesão corporal dolosa em violência doméstica; não foram consultados dados do Ligue 180 nem das secretarias estaduais.
- F49: Não se consultaram os microdados da SSP-SP nem relatórios da Prefeitura sobre a população em situação de rua no entorno.
- F51: As páginas do FBI devolveram HTTP 403; o conteúdo foi lido só pelo índice do buscador. Veredito provisório até leitura direta.
- F85: Não se consultou o processo criminal no TJMG.
- F86: A fonte é a Agência Brasil reproduzindo a fala do presidente na TV Globo; não há transcrição no Planalto. Posições anteriores de Lula não foram pesquisadas.
- F87: A nota da Secom exige autenticação; o conteúdo foi lido pelo índice do buscador. Não se achou nota do Itamaraty.
- F88: Não se acessou a denúncia do MPRJ nem o andamento no TJRJ; a data do júri (21/10/2026, remarcado) e a perícia só aparecem na imprensa.
- F90: O plano 'Pena Justa' (STF/CNJ, ADPF 347) não foi lido nesta rodada; ele é do Judiciário, não do Executivo.
- F92: O site do TSE devolveu HTTP 403. Segundo a imprensa, em 13/10/2022 a ministra Maria Claudia Bucchianeri suspendeu peça de campanha que montava falas de Lula sobre celular e cerveja; a decisão não foi lida na fonte oficial e não entra no veredito.
- F96: Conferir no áudio original o trecho de 05:50–06:10 do clipe T8oPN6v1L0c.
- F97: A redação final aprovada pela Câmara não foi lida na íntegra; o conteúdo penal foi identificado pela indexação oficial do Senado.
- L88: Não se pesquisaram pronunciamentos e emendas de Flávio no Senado sobre o PL 3.723/2019; reportagens citam apoio dele, mas não são fonte oficial.
- F99: Não se identificou o número da emenda/subemenda específica que incluiu a revogação.

#### Notas de método

- Mortes violentas: soma, a partir dos microdados do SINESP/MJSP, de homicídio doloso, feminicídio, latrocínio e lesão corporal seguida de morte (CVLI), mais mortes por intervenção de agente do Estado; taxas com população estimada do IBGE (tabela 6579). O Anuário do Fórum Brasileiro de Segurança Pública (ONG) não foi usado em nenhum veredito.
- Óbitos por agressão: SIM/DATASUS, CID-10 X85–Y09, por residência; 2025 é preliminar.
- Fontes estrangeiras oficiais (INDEC, BCRA, Casa Rosada, USTR, Federal Register, FBI) foram marcadas com o tier `oficial-estrangeiro`; o registro do próprio debate, com `registro-primario-do-debate`.

## Educação, agro, biografias e apostas

Checagem feita em 24/10/2026 só com fontes oficiais (governo federal, Congresso, TSE, Alerj, ITA, EBC como reprodução de dado oficial). Falas vêm da legenda automática; itens com leitura incerta estão marcados no JSON (`leitura_incerta`).

#### Contagem

| Veredito | Lula | Flávio Bolsonaro |
|---|---|---|
| verdadeiro | 9 | 4 |
| verdadeiro-mas | 4 | 4 |
| falta-contexto | 1 | 2 |
| exagerado | 1 | 2 |
| impreciso | 2 | 0 |
| falso | 1 | 0 |
| insustentavel | 3 | 2 |
| **total** | 21 | 14 |

#### Tabela

| id | orador | frase (legenda) | veredito | dado oficial decisivo |
|---|---|---|---|---|
| [F16](https://youtu.be/Z2AA0h2wr4U?t=20) | Flávio | A região Centro-Oeste é a região que mais produz alimentos no nosso Brasil | **verdadeiro** | Pela Conab, o Centro-Oeste produz metade dos grãos do país (49,9% na safra 2025/26), bem à frente de qualquer outra região. ([fonte](https://www.gov.br/conab/pt-br/atuacao/informacoes-agropecuarias/safras/safra-de-graos/boletim-da-safra-de-graos/12o-levantamento-safra-2025-26/site_previsao_de_safra-por_produto-set-2026.xlsx)) |
| [F18](https://youtu.be/Z2AA0h2wr4U?t=42) | Flávio | Você diz que as pessoas têm que se ajoelhar aos seus pés | **insustentavel** | Não foi localizado registro oficial (Planalto, gov.br) da frase atribuída a Lula de que produtores deveriam 'se ajoelhar' a ele. (sem fonte oficial localizada) |
| [F19](https://youtu.be/Z2AA0h2wr4U?t=47) | Flávio | Por que você chama o agro de fascista? | **insustentavel** | A fala de Lula sobre setores 'fascistas e direitistas' do agro (entrevista de 2022, como candidato) não tem registro oficial de governo; não dá para checá-la só com… (sem fonte oficial localizada) |
| [L17](https://youtu.be/Z2AA0h2wr4U?t=70) | Lula | Eu duvido que em algum momento do governo do pai dele houve investimento no agronegócio… | **verdadeiro-mas** | O crédito rural contratado no governo Lula 3 supera o do governo Bolsonaro em total e na média anual, inclusive descontada a inflação, mas caiu em 2024 e 2025 e ficou… ([fonte](https://olinda.bcb.gov.br/olinda/servico/SICOR/versao/v2/odata/ProgramaSubprograma)) |
| [L18](https://youtu.be/Z2AA0h2wr4U?t=82) | Lula | Eu duvido que houve a quantidade de investimento na agricultura familiar que houve no… | **verdadeiro** | O crédito do Pronaf (agricultura familiar) nos anos de Lula 3 supera o de cada ano do governo Bolsonaro, também em termos reais. ([fonte](https://olinda.bcb.gov.br/olinda/servico/SICOR/versao/v2/odata/ProgramaSubprograma)) |
| [L19](https://youtu.be/Z2AA0h2wr4U?t=97) | Lula | nunca se exportou tanto nesse país | **verdadeiro** | As exportações brasileiras bateram recorde em 2025 (US$ 348,3 bi) e o acumulado de jan–set/2026 (US$ 284,7 bi) é o maior da série para o período. ([fonte](https://api-comexstat.mdic.gov.br/general?language=pt)) |
| [F20](https://youtu.be/Z2AA0h2wr4U?t=146) | Flávio | tenho 45 anos de idade. Fui deputado quatro vezes, sou senador da República | **verdadeiro** | Flávio tem 45 anos (nasceu em 30/04/1981), foi eleito deputado estadual quatro vezes (2002, 2006, 2010, 2014) e é senador desde 2019. ([fonte](https://cdn.tse.jus.br/estatistica/sead/odsele/consulta_cand/consulta_cand_2026.zip)) |
| [L35](https://youtu.be/K-kGhpDV4zA?t=98) | Lula | tudo que nós fizemos na Amazônia nesses últimos 24 anos. Você vai perceber que foi mais… | **insustentavel** | A frase compara investimentos na Amazônia sem dizer com o quê, e não foi possível obter série oficial de investimento federal regionalizado por governo. (sem fonte oficial localizada) |
| [L36](https://youtu.be/K-kGhpDV4zA?t=124) | Lula | Eu quando fiz a minha primeira campanha da minha vida de 89, eu descobri que eu não… (leitura incerta) | **impreciso** | Registro oficial da Câmara dá 30 mil km para as Caravanas da Cidadania nos anos 1990, não 91 mil; e a campanha de 1989 não foi a primeira de Lula (ele disputou em 1982… ([fonte](https://www.camara.leg.br/tv/145715-candidato-do-pt-e-o-primeiro-presidente-da-republica-de-origem-operaria/)) |
| [L45](https://youtu.be/vASlNIMp2PM?t=218) | Lula | levamos o Instituto Tecnológico da Aeronáutica para o Ceará como prêmio ao estado do… | **verdadeiro-mas** | O campus do ITA em Fortaleza foi criado por decreto de Lula em 2024, e o Ceará disputa com São Paulo a liderança de aprovados no vestibular do ITA, mas não é o 1º todos… ([fonte](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2024/decreto/D11887.htm)) |
| [L46](https://youtu.be/vASlNIMp2PM?t=232) | Lula | Ao mesmo tempo, nós fizemos 40 novos institutos federais e novas universidades (leitura incerta) | **insustentavel** | Não foi localizado número oficial de 40 novos institutos federais e universidades no Nordeste; os dados oficiais encontrados são nacionais e se referem, em boa parte, a… ([fonte](https://www25.senado.leg.br/web/atividade/pronunciamentos/-/p/pronunciamento/521662)) |
| [L47](https://youtu.be/QhluFzoPl30?t=67) | Lula | por que que ele foi o único deputado estadual do Rio de Janeiro a votar contra o aumento… | **verdadeiro** | Flávio confirmou no próprio debate que votou contra a ampliação da licença-maternidade na Alerj (Lei Complementar estadual 128/2009); o 'único' voto não foi confirmado… ([fonte](https://www3.alerj.rj.gov.br/lotus_notes/default.asp?id=3&url=L2NvbnRsZWkubnNmL2E5OWUzMTdhOWNmZWMzODMwMzI1Njg2MjAwNzFmNWQyLzc5YzJjNzdmODY5YjZmNjg4MzI1NzVlNDAwNmEwZWVkP09wZW5Eb2N1bWVudA==)) |
| [L49](https://youtu.be/QhluFzoPl30?t=219) | Lula | Ele me chamou de nove dedos | **verdadeiro** | No bloco 1, Flávio disse que Lula 'dá com uma mão e tira com os nove dedos', e depois pediu desculpas 'se eu te chamei de nove dedos'. ([fonte](https://youtu.be/26XCkA5BHm8?t=276)) |
| [L50](https://youtu.be/QhluFzoPl30?t=228) | Lula | Se tem alguém que perdeu o dedo com [...] anos, fui eu. Trabalhando à noite quando não… (leitura incerta) | **verdadeiro** | Registros oficiais do Senado confirmam que Lula perdeu o dedo mínimo da mão esquerda em acidente de trabalho numa metalúrgica, aos 19 anos. ([fonte](https://www12.senado.leg.br/noticias/materias/2002/12/30/do-agreste-ao-planalto-central-a-trajetoria-do-novo-presidente-da-republica)) |
| [L52](https://youtu.be/QhluFzoPl30?t=244) | Lula | Ele nunca trabalhou na vida, não sabe o que é uma carteira profissional. O primeiro… | **insustentavel** | Não há registro oficial acessível de um 'emprego falso' de Flávio com o pai; 'nunca trabalhou' é juízo de valor, e os registros mostram 23 anos de mandatos e… ([fonte](https://cdn.tse.jus.br/estatistica/sead/odsele/consulta_cand/consulta_cand_2002.zip)) |
| [L54](https://youtu.be/QhluFzoPl30?t=493) | Lula | O Brasil só foi ter a primeira universidade 420 anos depois da descoberta | **verdadeiro** | A primeira universidade criada pelo governo federal, a Universidade do Rio de Janeiro, é de 7/9/1920 (Decreto 14.343), exatamente 420 anos depois de 1500. ([fonte](https://www2.camara.leg.br/legin/fed/decret/1920-1929/decreto-14343-7-setembro-1920-570508-publicacaooriginal-93654-pe.html)) |
| [F50](https://youtu.be/QhluFzoPl30?t=570) | Flávio | Nós sancionamos a lei Sansão para aumentar as penas para os maus-tratos a animais | **verdadeiro** | A Lei Sansão (Lei 14.064/2020), que aumentou a pena por maus-tratos a cães e gatos, foi sancionada por Jair Bolsonaro em 29/9/2020; o projeto foi do deputado Fred Costa. ([fonte](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2020/lei/L14064.htm)) |
| [L58](https://youtu.be/jctCsMD2nTE?t=277) | Lula | (Paráfrase; legenda ininteligível) "aumentamos de um para dois [...] e aumentamos também… (leitura incerta) | **verdadeiro** | A Lei Complementar 238, sancionada por Lula em 21/10/2026, passa o MEI de 1 para 2 empregados e o teto de faturamento de R$ 81 mil para R$ 110 mil (2027) e R$ 140 mil… ([fonte](https://www.planalto.gov.br/ccivil_03/leis/lcp/Lcp238.htm)) |
| [L76](https://youtu.be/sFjChKegcxs?t=332) | Lula | E é por isso que eu tive a coragem de acabar com as betas [...] nós acabamos com a Bete… | **verdadeiro-mas** | A MP 1.394, de 25/9/2026, proibiu as apostas de quota fixa (bets) em todo o país, mas é medida provisória ainda não votada pelo Congresso, que pode alterá-la ou… ([fonte](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2026/mpv/mpv1394.htm)) |
| [L77](https://youtu.be/sFjChKegcxs?t=369) | Lula | Eu sei que você, por exemplo, é contra acabar com as bet | **falta-contexto** | Flávio criticou no debate o cancelamento das bets, mas em 2023 votou contra a lei que regulamentou as apostas e a favor de excluir delas os cassinos on-line; não… ([fonte](https://legis.senado.leg.br/dadosabertos/votacao?dataInicio=2023-12-01&dataFim=2023-12-31)) |
| [F77](https://youtu.be/2S2HvBYOk24?t=77) | Flávio | Você zerou o orçamento federal para ensino integral e tentou maquiar numa outra cifra | **falta-contexto** | O financiamento federal do tempo integral foi deslocado para dentro da complementação da União ao Fundeb pela EC 135/2024 (contra a qual Flávio votou); não foi possível… ([fonte](https://www.planalto.gov.br/ccivil_03/constituicao/Emendas/Emc/emc135.htm)) |
| [F78](https://youtu.be/2S2HvBYOk24?t=94) | Flávio | Ele é o pai do Tigrinho, ele é o pai do cassino online, ele criou, ele liberou. Aí… | **verdadeiro-mas** | A lei sancionada por Lula em 2023 autorizou cassinos on-line (jogos on-line) e a MP de 25/9/2026, nove dias antes do 1º turno, os proibiu; mas as bets foram criadas em… ([fonte](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/L13756.htm)) |
| [L79](https://youtu.be/2S2HvBYOk24?t=202) | Lula | Todo mundo sabe que nós criamos o pé de meia | **verdadeiro** | O Pé-de-Meia foi criado no governo Lula: MP 1.198/2023, convertida na Lei 14.818, sancionada por Lula em 16/1/2024. ([fonte](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2024/lei/L14818.htm)) |
| [L80](https://youtu.be/2S2HvBYOk24?t=220) | Lula | Todo mundo sabe que nós encontramos 5.600 creches paralisadas, escolas. E escolas de… | **exagerado** | Em abril de 2023, o governo contava 3.540 obras de educação básica paralisadas ou inacabadas, das quais 1.221 creches e pré-escolas, não 5.600 creches. ([fonte](https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/Exm/Exm-1174-23.pdf)) |
| [L81](https://youtu.be/2S2HvBYOk24?t=243) | Lula | eles inventaram uma uma escola cívico-militar. É isso que eles inventaram e que não… | **falso** | O programa federal de escolas cívico-militares (Pecim) foi criado por decreto de Bolsonaro em 2019 e, segundo o MEC, chegou a 216 escolas antes de ser revogado em 2023;… ([fonte](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2019/decreto/D10004.htm)) |
| [L82](https://youtu.be/2S2HvBYOk24?t=261) | Lula | a gente fez mais universidade, a gente fez mais instituto federal, a gente fez mais… | **verdadeiro-mas** | Comparado ao governo Bolsonaro, Lula 3 criou mais universidades por lei e ampliou o tempo integral; mas parte das 'novas universidades' são Cefets transformados e… ([fonte](https://agenciabrasil.ebc.com.br/educacao/noticia/2026-06/censo-escolar-brasil-reduz-reprovacao-abandono-e-atraso-estudantil)) |
| [L83](https://youtu.be/2S2HvBYOk24?t=277) | Lula | com o pé de meia fazendo com que 66% das crianças não desistissem mais da escola | **impreciso** | O MEC atribui ao Pé-de-Meia uma queda de 43% no abandono do ensino médio (de 6,4% para 3,6%), e de 61% entre 2022 e 2025; 66% é o índice de alfabetização, não de alunos… ([fonte](https://agenciabrasil.ebc.com.br/educacao/noticia/2026-06/censo-escolar-brasil-reduz-reprovacao-abandono-e-atraso-estudantil)) |
| [F79](https://youtu.be/2S2HvBYOk24?t=303) | Flávio | foi no governo do presidente Bolsonaro que nós anistiamos quase 99% das dívidas dos… | **verdadeiro-mas** | A lei do governo Bolsonaro (Lei 14.375/2022) deu desconto de até 99% nas dívidas do Fies, mas só para devedores do CadÚnico ou do Auxílio Emergencial com atraso de mais… ([fonte](https://www.planalto.gov.br/ccivil_03/_ato2019-2022/2022/lei/L14375.htm)) |
| [F80](https://youtu.be/2S2HvBYOk24?t=315) | Flávio | fomos nós que demos o maior reajuste da história para os professores, 33% | **verdadeiro-mas** | O reajuste de 33,24% do piso do magistério em 2022 (governo Bolsonaro) foi o maior desde a criação do piso em 2009, mas decorreu da fórmula da Lei 11.738/2008, e não de… ([fonte](https://www.planalto.gov.br/ccivil_03/_ato2007-2010/2008/lei/l11738.htm)) |
| [F81](https://youtu.be/2S2HvBYOk24?t=322) | Flávio | você é uma dessas mães das mais de 1 milhão de crianças que não tem aonde deixar o seu… | **verdadeiro** | O IBGE estima cerca de 2,3 milhões de crianças de 0 a 3 anos fora da creche por dificuldade de acesso (falta de escola, de vaga ou recusa pela idade), acima do 'mais de… ([fonte](https://agenciabrasil.ebc.com.br/politica/noticia/2024-09/eleicoes-garantir-vaga-em-creche-esta-nos-planos-do-seu-candidato)) |
| [F82](https://youtu.be/2S2HvBYOk24?t=381) | Flávio | eu vou retomar de uma forma integral os jogos estudantis brasileiros, os famosos JEBs,… | **falta-contexto** | Os Jogos Escolares Brasileiros foram de fato retomados em 2021, após 17 anos, no governo Bolsonaro; mas houve edições em 2023 e 2024 no governo Lula, e não há dado… ([fonte](https://agenciabrasil.ebc.com.br/esportes/noticia/2021-10/apos-17-anos-jogos-escolares-brasileiros-voltam-ocorrer-no-rj)) |
| [F83](https://youtu.be/2S2HvBYOk24?t=427) | Flávio | tanto é que a nota do PISA no Brasil é uma das piores da história com o atual governo | **exagerado** | No Pisa 2025 o Brasil ficou estável e em nível baixo (377 em matemática, 408 em leitura, 409 em ciências), mas não teve uma das piores notas da história: em ciências… ([fonte](https://agenciabrasil.ebc.com.br/educacao/noticia/2026-09/brasil-melhora-desempenho-escolar-no-longo-prazo-mas-patamar-e-baixo)) |
| [F109](https://youtu.be/rUnAbA73RH0?t=974) | Flávio | porque eu sou advogado, eu sou empresário há 24 anos. Eu sou deputado e senador (leitura incerta) | **verdadeiro-mas** | Flávio está há quase 24 anos em mandatos (deputado estadual desde 2003, senador desde 2019); como empresário, o TSE só registra participação em empresa a partir de 2018. ([fonte](https://cdn.tse.jus.br/estatistica/sead/odsele/consulta_cand/consulta_cand_2002.zip)) |
| [L97](https://youtu.be/NnDsZaMp9Vw?t=74) | Lula | Comecei a trabalhar com 12 anos de idade. Vendi tapioca, vendi laranja, vendi amendoim,… | **verdadeiro** | Registros oficiais do Senado e da Câmara confirmam que Lula começou a trabalhar aos 12 anos, foi vendedor ambulante e engraxate, formou-se torneiro mecânico no Senai e… ([fonte](https://www12.senado.leg.br/noticias/materias/2002/12/30/do-agreste-ao-planalto-central-a-trajetoria-do-novo-presidente-da-republica)) |
| [F116](https://youtu.be/Q7WHDg643ow?t=116) | Flávio | Eles tiveram oportunidade de fazer por quase 20 anos eles não fizeram | **exagerado** | O PT governou o país por cerca de 17 anos e meio (jan/2003 a mai–ago/2016 e desde jan/2023), não 'quase 20'. ([fonte](https://www12.senado.leg.br/noticias/materias/2016/08/31/dilma-rousseff-perde-o-mandato-de-presidente-da-republica-mas-mantem-direitos-politicos)) |

#### Lacunas por item

- **F16**: IBGE (SIDRA – PAM, PPM, LSPA) bloqueado por Cloudflare nesta sessão: não foi possível comparar valor da produção agropecuária total nem pecuária por região.
- **F18**: Sem registro oficial acessível: ato de campanha não é publicado pelo Planalto; o portal gov.br/planalto (discursos) estava bloqueado por limite de acesso (HTTP 429/captcha) nesta sessão. Há relatos na imprensa (não usados, por regra) de fala de Lula em ato de campanha em Florianópolis no dia 19 (set/2026), com reação de entidades do agro. Conferir no vídeo original do ato antes de publicar.
- **F19**: Fonte primária é uma entrevista de emissora privada (2022); não há registro do Planalto. Os discursos presidenciais posteriores (gov.br/planalto) estavam inacessíveis (HTTP 429/captcha). Relatos de imprensa e de agências de checagem indicam que a frase se referia a 'parte' do agronegócio; não foram usados por regra. Conferir o vídeo original.
- **L17**: Valores anunciados de cada Plano Safra (MAPA) e custo de equalização do Tesouro não foram obtidos: gov.br/agricultura e Tesouro bloqueados por limite de acesso (HTTP 429/captcha). Deflação por média anual do IPCA (cálculo próprio a partir da série SGS 433); ano civil, não ano-safra. Por ano-safra (jul–jun), SICOR: 2022/23 R$ 360,7 bi; 2023/24 R$ 422,0 bi; 2024/25 R$ 383,3 bi; 2025/26 R$ 353,3 bi (nominais).
- **L18**: Programa identificado pelo campo 'nomePrograma' iniciado por 'PRONAF' no SICOR; valores do Plano Safra da Agricultura Familiar anunciados pelo MDA não foram obtidos (gov.br bloqueado).
- **L35**: Despesa federal regionalizada (SIOP, Tesouro Transparente, Portal da Transparência) não consultada: portais gov.br com bloqueio de acesso nesta sessão; a série exigiria recorte por função e UF da Região Norte.
- **L36**: Os 91 mil km podem somar várias caravanas (1993–1996 e posteriores); não há registro oficial com esse total. Arquivos do Instituto Lula/Fundação Perseu Abramo não são fontes permitidas.
- **L45**: As estatísticas do ITA são por local de prova (banca), não por estado de origem do candidato. Situação das obras e início das aulas em Fortaleza não confirmados em fonte oficial acessível (páginas da Agência Gov suspensas pela legislação eleitoral).
- **L46**: Lista oficial de novos campi por UF/região (MEC/Setec) inacessível: gov.br/mec com bloqueio (HTTP 429/captcha). Pode haver mistura entre 'institutos' (instituições) e 'campi'.
- **L47**: Votação nominal do PLC 17/2009 na Alerj (placar e nome dos votantes) não localizada: banco de projetos 2007–2011 da Alerj retornou erro; as atas e o Diário da Alerj de jun/2009 não foram consultados. O placar '45 a 1' circula em agências de checagem (não usadas por regra).
- **L49**: Fonte é o próprio registro do debate (legenda automática); não há fonte governamental aplicável. Conferir o áudio.
- **L50**: Turno da noite não confirmado em fonte oficial; biografia oficial no gov.br/planalto inacessível (captcha).
- **L52**: Histórico de secretários parlamentares/lotação na Câmara dos Deputados antes de 2003 não disponível na API de dados abertos; possível registro em boletins administrativos da Câmara não consultado. 'Carteira profissional' (vínculo CLT) só poderia ser verificada em bases sigilosas (CNIS/RAIS).
- **L54**: As páginas da UFPR (1912) e da Ufam (1909) não puderam ser lidas (erro de certificado/503); a disputa de pioneirismo fica registrada sem fonte oficial lida.
- **L58**: Estimativa oficial do valor perdoado e do número de MEIs beneficiados (Receita/PGFN) não obtida. A legenda é ininteligível em parte; conferir o áudio.
- **L77**: Discursos de Flávio no Senado (2023–2026, API) não mencionam apostas; posição dele sobre a conversão da MP 1.394 ainda não tem voto registrado.
- **F77**: Dotação da ação orçamentária do Programa Escola em Tempo Integral no PLOA 2027 (SIOP/Siga Brasil) não consultada; a nota técnica do Congresso não detalha a ação.
- **F78**: 'Prejudicou os times de futebol' e 'acabou com a segurança jurídica' são avaliações; impacto em patrocínios não medido com dado oficial.
- **L80**: Painel atualizado do FNDE sobre a retomada de obras não acessado (gov.br bloqueado); obras paralisadas de institutos federais sem dado oficial localizado.
- **L81**: Execução orçamentária do Pecim (2020–2022) e número de alunos não obtidos de fonte oficial direta (portais do MEC inacessíveis).
- **L82**: Lei de criação da Universidade Federal do Esporte não localizada no Planalto nesta sessão. A lista de leis de criação 2023–2026 pode não ser exaustiva (índice de leis de 2026 do Planalto retornou 403). Se 'a gente' se refere a todos os governos do PT (2003–2016), a comparação muda; não foi feita aqui.
- **L83**: O comunicado do MEC/Agência Gov sobre o '–43%' (6,4%→3,6%) está suspenso pela legislação eleitoral; o número consta de reprodução da Agência Brasil não lida integralmente. Microdados de fluxo do Inep não consultados.
- **F79**: Número de contratos renegociados e valor efetivamente abatido (FNDE/CG-Fies) não obtidos (gov.br/fnde bloqueado).
- **F80**: Portarias do MEC no DOU (in.gov.br) inacessíveis (403); valores tomados de reprodução da Agência Brasil. O reajuste de 2021 (provavelmente 0%) não foi confirmado.
- **F81**: Tabela original do IBGE (SIDRA/PNAD Educação) inacessível (Cloudflare); número absoluto de 2024/2025 não confirmado.
- **F82**: Páginas da Agência Gov (2023, 2024) suspensas 'em respeito à legislação eleitoral'; gov.br/esporte inacessível. Não se verificou se houve edição em 2025 e 2026 nem o orçamento por ano.
- **F83**: Relatórios da OCDE (oecd.org, 403) e do Inep (download.inep.gov.br, sem conexão) não foram lidos diretamente; números de reprodução da EBC. Nota de ciências de 2000 não conferida. O Pisa mede alunos de 15 anos; redes estaduais respondem pela maior parte do ensino avaliado.
- **F109**: Inscrição na OAB não conferida: o Cadastro Nacional dos Advogados exige reCAPTCHA. Junta Comercial/CNPJ não consultados.
- **L97**: Lista de produtos que vendia não confirmada em fonte oficial; biografia oficial do gov.br/planalto inacessível (captcha).

#### Lacunas gerais da sessão

- Portais gov.br (Planalto/discursos e biografia, MEC, FNDE, MAPA, MDA, Inep, Ministério do Esporte) responderam com limite de acesso (HTTP 429/captcha) durante quase toda a sessão; Agência Gov (EBC) está com páginas suspensas pela legislação eleitoral.
- IBGE (SIDRA e Agência de Notícias) bloqueado por Cloudflare; OCDE (403); download.inep.gov.br e in.gov.br (DOU) inacessíveis; Cadastro Nacional dos Advogados (OAB) exige reCAPTCHA.
- Onde o dado oficial só estava disponível em reprodução da Agência Brasil (EBC), o órgão original está citado no nome da fonte.
- Falas de campanha (F18, F19) e acusações sem registro administrativo acessível (L52) ficaram como `insustentavel` por falta de fonte oficial, não por evidência contrária.

## Infraestrutura

Checagem feita em 24/10/2026 só com fontes oficiais (TCU, Tesouro Nacional, Casa Civil/Novo PAC, DNIT, ANTT, Infra S.A., MIDR, Arquivo Nacional, MCTI/LNCC, Planalto, Câmara/Senado, governos estaduais). Falas tiradas da legenda automática do YouTube. Arquivo completo: `g6_infraestrutura_checado.json`.

- **Lula** (16 falas): exagerado 3, falso 3, falta-contexto 2, impreciso 3, insustentavel 1, verdadeiro-mas 4
- **Flávio Bolsonaro** (6 falas): falso 1, impreciso 1, verdadeiro-mas 4

| id | orador | frase (curta) | veredito | dado oficial decisivo |
|---|---|---|---|---|
| [F01](https://youtu.be/woYkhYICZ2k?t=70) | Flávio | nós pegamos o Brasil lá em 2019 com cerca de 14.000 obras inacabadas. E apesar de todos os problemas, a gente… | **verdadeiro-mas** | TCU: 14.403 contratos paralisados (diagnóstico do Ac. 1.079/2019) e 8.674 em ago/2022; queda atribuída em boa parte a mudança de critério — [TCU — Acórdão 2.555/2022-Plenário (TC 021.731/2019-5,…](https://portal.tcu.gov.br/data/files/88/C3/04/9B/A8AA4810B4FE0FF7E18818A8/021.731-2019-5%20%20VR%20%20acompanhamento%20obras%20paralisadas.pdf) |
| [F02](https://youtu.be/woYkhYICZ2k?t=87) | Flávio | Agora, neste ano, o TCU, o Tribunal de Contas da União, acaba de soltar um relatório que existem mais de… | **impreciso** | TCU: 11.469 paralisadas em abr/2025 (divulgado jul/2025); 4.215 em abr/2026; 77% das de 2025 começaram antes de 2023 — [TCU — 'Metade das obras financiadas com recursos federais…](https://portal.tcu.gov.br/imprensa/noticias/metade-das-obras-financiadas-com-recursos-federais-estao-paradas) |
| [L01](https://youtu.be/woYkhYICZ2k?t=130) | Lula | em nenhum momento da história do país se investiu tanto em obra de infraestrutura como nós investimos nesses… | **falso** | Tesouro/RTN: investimento federal GND 4 de R$ 66-73 bi/ano em 2023-25 vs R$ 110,9 bi em 2014 e R$ 109,5 bi em 2010 (R$ de jul/2026) — [Tesouro Nacional — Resultado do Tesouro Nacional, série…](https://www.tesourotransparente.gov.br/ckan/dataset/ab56485b-9c40-4efb-8563-9ce3e1973c4b/resource/527ccdb1-3059-42f3-bf23-b5e3ab4c6dc6/download/seriehistoricajul26.xlsx) |
| [L02](https://youtu.be/woYkhYICZ2k?t=145) | Lula | nós anunciamos um programa de aceleração do crescimento de 1 trilhão e 700 milhões, do qual quase 800 já… | **impreciso** | Casa Civil/Novo PAC: R$ 1,7 tri anunciado (2023); R$ 1,3 tri executado até jun/2026 (96,9% do previsto 2023-26) — [Casa Civil — Novo PAC, página Transparência ('Execução…](https://www.gov.br/casacivil/pt-br/novopac/transparencia/transparencia/) |
| [L03](https://youtu.be/woYkhYICZ2k?t=176) | Lula | qualquer coisa que ele pensar de infraestrutura nós fizemos três ou quatro vezes mais do que o governo deles | **exagerado** | Tesouro/RTN: média 2023-25 = 1,31x a de 2019-22 (1,51x em transporte) — [Tesouro Nacional — Resultado do Tesouro Nacional, série…](https://www.tesourotransparente.gov.br/ckan/dataset/ab56485b-9c40-4efb-8563-9ce3e1973c4b/resource/527ccdb1-3059-42f3-bf23-b5e3ab4c6dc6/download/seriehistoricajul26.xlsx) |
| [L04](https://youtu.be/woYkhYICZ2k?t=186) | Lula | nós herdamos 6.000 obras paradas | **impreciso** | TCU: 8.674 obras paralisadas em ago/2022; 8.603 em abr/2023 — [TCU — Painel de Obras Paralisadas (Power BI público;…](https://paineis.tcu.gov.br/pub/?workspaceId=8bfbd0cc-f2cd-4e1c-8cde-6abfdffea6a8&reportId=013930b6-b989-41c3-bf00-085dc65109de&painel=ObrasParalisadas) |
| [F03](https://youtu.be/woYkhYICZ2k?t=244) | Flávio | eu vou investir muito aqui na concessão de rodovias, como fez o presidente Bolsonaro e eu vou manter uma… | **verdadeiro-mas** | Portaria MInfra 104/2021: isenção para motos só nas concessões federais então em licitação (10 projetos) — [Ministério da Infraestrutura/Transportes — 'Portaria…](https://www.gov.br/transportes/pt-br/assuntos/noticias/2021/8/portaria-estabelece-diretriz-de-politica-publica-de-isencao-de-cobranca-de-pedagio-para-motocicletas) |
| [F04](https://youtu.be/woYkhYICZ2k?t=263) | Flávio | Nós instalamos mais de 21.300 pontos de internet em vários locais do Brasil, atingindo mais 3.100 cidades e… | **verdadeiro-mas** | MCom (dez/2022): 21,3 mil pontos, >11 milhões de pessoas, ~3,2 mil cidades; programa anterior a 2019 — [Ministério das Comunicações — 'Inclusão digital: mais de…](https://www.gov.br/mcom/pt-br/noticias/2022/dezembro/inclusao-digital-mais-de-21-3-mil-pontos-de-internet-do-wi-fi-brasil-sao-instalados) |
| [L05](https://youtu.be/woYkhYICZ2k?t=360) | Lula | Nós estamos fazendo uma rodovia muito importante que ninguém teve coragem de fazer, que liga Porto Velho a… | **verdadeiro-mas** | DNIT (mai/2026): Lote 1C com ~42%; OS do Lote 4 do Trecho do Meio; LP do Trecho do Meio emitida em 2022 — [DNIT — 'Presidente Lula visita o Amazonas e acompanha…](https://www.gov.br/dnit/pt-br/assuntos/noticias/presidente-lula-visita-o-amazonas-e-acompanha-agendas-em-importantes-empreendimentos-da-br-319-am) |
| [L06](https://youtu.be/woYkhYICZ2k?t=369) | Lula | Nós estamos fazendo a Transnordestina, a Fiol e a Fico. Não é que vão fazer, estamos fazendo | **verdadeiro-mas** | Infra S.A.: obras em 240 km da FICO, 485 km da FIOL 2 e 544 km da Transnordestina; FIOL II iniciada em 2011; FICO I pela Vale — [Infra S.A. — página 'Obras' da FIOL (execução física da…](https://www.infrasa.gov.br/ferrovias-da-infra-s-a/ferrovia-de-integracao-oeste-leste/obras/) |
| [L07](https://youtu.be/woYkhYICZ2k?t=376) | Lula | Nós estamos fazendo a Ferrovia das Araras, sabe? Lá no Rio de Janeiro, que é uma obra quase 12 bilhões de… | **impreciso** | ANTT (abr/2024): Nova Serra das Araras (rodovia) custa R$ 1,5 bi, feita pela concessionária CCR RioSP — [ANTT — 'ANTT supervisiona duplicação do novo traçado da…](https://www.gov.br/antt/pt-br/assuntos/ultimas-noticias/antt-supervisiona-duplicacao-do-novo-tracado-da-serra-das-araras) |
| [L08](https://youtu.be/woYkhYICZ2k?t=382) | Lula | Nós estamos fazendo e fizemos o canal, o contorno de Florianópolis | **verdadeiro-mas** | ANTT: contorno entregue em 09/08/2024; R$ 3,9 bi da concessionária Autopista Litoral Sul — [ANTT — 'ANTT e Governo Federal entregam maior obra…](https://www.gov.br/antt/pt-br/assuntos/ultimas-noticias/antt-e-governo-federal-entregam-maior-obra-rodoviaria-da-america-latina) |
| [L09](https://youtu.be/woYkhYICZ2k?t=387) | Lula | o túnel de Santos, quem está colocando ele para fazer somos nós, tanto do orçamento quanto o financiamento do… | **exagerado** | Gov. SP: PPP estadual; aporte público de R$ 5,1 bi dividido igualmente entre Estado e União; BNDES não confirmado — [Governo do Estado de SP (Agência SP) — 'Grupo Mota-Engil…](https://www.agenciasp.sp.gov.br/grupo-mota-engil-vence-leilao-ppp-do-tunel-santos-guaruja/) |
| [L10](https://youtu.be/woYkhYICZ2k?t=401) | Lula | E estamos fazendo o VLT de Salvador, metrô em São Paulo, Belo Belo Horizonte, VLT no Rio de Janeiro | **falta-contexto** | Gov. BA/MG: VLT de Salvador (Estado, R$ 3,2 bi) e Linha 2 de BH (concessão estadual); parte federal não confirmada — [Governo da Bahia — 'VLT impulsiona transformação urbana...'…](https://www.ba.gov.br/comunicacao/noticias/2026-03/379667/vlt-impulsiona-transformacao-urbana-e-amplia-espacos-de-esporte-e-lazer-no) |
| [L11](https://youtu.be/woYkhYICZ2k?t=408) | Lula | além de estar muito próximo de concluir a tão sonhada transposição de São Francisco, que Dom Pedro tentou… | **falta-contexto** | Arquivo Nacional: eixos originais concluídos em 2022; MIDR: ramais Apodi/Agreste/Salgado em curso — [Arquivo Nacional (MGI) — 'Transposição do rio São…](https://querepublicaeessa.an.gov.br/index.php/que-republica-e-essa/assuntos/achados-e-perdidos/553-transposicao-do-rio-sao-francisco) |
| [L15](https://youtu.be/26XCkA5BHm8?t=234) | Lula | Você recentemente ridicularizou a minha proposta de tarifa zero | **insustentavel** | Sem registro oficial das declarações de campanha de Flávio — [Transcrição do debate no projeto…](https://github.com/matheushexsel/pentefino/blob/master/research_notes/Pente%20fino%20dados%20pol%C3%ADticos%20Brasil%202026/16_debate_globo_2026-10-23_transcricao.md) |
| [F28](https://youtu.be/FIKMIfvhAkA?t=228) | Flávio | esse presidente virou as costas para vocês o momento que vocês mais precisavam, que foram nas tragédias de… | **falso** | TCU (Ac. 1.832/2025): R$ 26,1 bi pagos de R$ 42,7 bi autorizados (~61%) até jul/2024 — [TCU — 'Tribunal avalia execução de créditos extraordinários…](https://portal.tcu.gov.br/imprensa/noticias/tribunal-avalia-execucao-de-creditos-extraordinarios-para-o-rio-grande-do-sul) |
| [L40](https://youtu.be/vASlNIMp2PM?t=64) | Lula | levamos a transposição do rio São Francisco, que é hoje a maior obra hídrica em funcionamento no mundo | **falso** | MIDR: 'maior obra hídrica do país' (477 km); governo da China: transposição Sul–Norte é a maior do mundo (185 mi de beneficiados) — [MIDR — página 'Projeto de Integração do Rio São Francisco'…](https://www.gov.br/mdr/pt-br/assuntos/seguranca-hidrica/projeto-sao-francisco) |
| [L41](https://youtu.be/vASlNIMp2PM?t=71) | Lula | São quase 1700 km de canal e 15.000 km de adutoras | **exagerado** | MIDR: eixos com 477 km; Ramal do Apodi 115,5 km; sem total oficial de 1.700 km/15 mil km — [MIDR — página 'Projeto de Integração do Rio São Francisco'…](https://www.gov.br/mdr/pt-br/assuntos/seguranca-hidrica/projeto-sao-francisco) |
| [L42](https://youtu.be/vASlNIMp2PM?t=88) | Lula | levamos [supercomputador] para Natal, levamos [supercomputador] quântico para a Paraíba, levamos indústria… | **verdadeiro-mas** | LNCC/MCTI: supercomputador de IA em Macaíba anunciado em 20/08/2026 (edital a publicar); CIQUANTA-PB em implantação com o Estado — [LNCC/MCTI — 'LNCC conduz implantação de supercomputador de…](https://www.gov.br/lncc/pt-br/assuntos/noticias/ultimas-noticias-1/lncc-conduz-implantacao-de-supercomputador-de-inteligencia-artificial-que-ampliara-a-capacidade-computacional-do-brasil) |
| [F41](https://youtu.be/vASlNIMp2PM?t=312) | Flávio | Você prometeu que ia entregar a transposição no Rio São Francisco até 2009, não entregou. Depois prometeu que… | **verdadeiro-mas** | Câmara: previsão inicial 2012, depois dez/2014; MIDR: 86,3% executado em abr/2016; Arquivo Nacional: eixos concluídos em 2022 — [Agência Câmara — 'Transposição do São Francisco pode ser…](https://www.camara.leg.br/noticias/463450-transposicao-do-sao-francisco-pode-ser-concluida-antes-do-prazo-diz-deputado/) |
| [L78](https://youtu.be/2S2HvBYOk24?t=117) | Lula | O Tigrinho foi criado por você em 2022. [...] O Tigrinho foi teu pai que criou | **falso** | Lei 13.756/2018 (Temer, só esporte); 'jogo on-line' incluído pela Lei 14.790/2023 (Lula) — [Planalto — Lei nº 13.756, de 12/12/2018 (art. 29: apostas…](https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13756.htm) |

#### Lacunas

- **F01**: Os números de 2018 e 2022 usam bases e critérios diferentes; não há série oficial homogênea.
- **F02**: A mudança de critério de 2026 (canceladas fora do rol; Portaria SEGES/MGI citada pela imprensa não foi lida) torna a série não comparável.
- **F02**: 'Ano de início' é o campo do painel; obras sem data foram mantidas à parte.
- **L01**: A série RTN de investimento começa em 2008; para anos anteriores não há série oficial comparável lida nesta checagem.
- **L01**: Não se usou a série da FGV (não governamental).
- **L01**: 2026 está parcial (jan-jul: R$ 38,7 bi).
- **L02**: O balanço por fonte do valor executado (R$ 1,3 tri) não está aberto na página; só a previsão por fonte.
- **L02**: Durante o período de defeso eleitoral (04/07 a 25/10/2026) várias páginas de notícias do gov.br (Casa Civil, Secom, MCom, Ministério dos Transportes, MCTI, Planalto) e o acervo da Agência BNDES estão com acesso restrito; números dessas páginas só puderam ser lidos via índice de busca e não foram reconfirmados na página.
- **L03**: Concessões e investimento privado (leilões) não entram no investimento público; não há série oficial consolidada por governo lida nesta checagem.
- **L03**: A frase é genérica ('qualquer coisa que ele pensar'); checou-se o investimento federal.
- **L04**: O dado do MEC (5,6 mil obras de educação) aparece em fala de ministro em notícia do TCU de 11/06/2026, sem data de referência; não foi usado para o veredito.
- **F03**: O texto integral da portaria no DOU não foi lido (só a nota oficial do ministério).
- **F03**: Não se verificou se a diretriz foi mantida nos leilões de 2023-2026.
- **F04**: Número de pontos ativos em dez/2018 (linha de base) não localizado em fonte oficial acessível.
- **L05**: Situação da Licença de Instalação do Trecho do Meio em out/2026 não confirmada em fonte oficial acessível.
- **L06**: Avanço físico da FICO I em 2026 não localizado em fonte oficial acessível.
- **L07**: Estágio atual (out/2026) da obra: as notas do Ministério dos Transportes de 2026 estão restritas no defeso eleitoral.
- **L08**: Data do contrato de concessão e participação de cada governo na execução não detalhadas em fonte oficial lida.
- **L09**: Contrato de financiamento do BNDES não localizado (acervo da Agência BNDES retirado do ar no defeso eleitoral).
- **L10**: Valores federais do Novo PAC para VLT/metrô de Salvador (citados pela Casa Civil em 2025-2026) não puderam ser abertos.
- **L10**: Metrô de SP e VLT do Rio: não identificados nem checados.
- **L11**: Estágio dos ramais Apodi e Salgado em 2026 não localizado em fonte oficial acessível.
- **L15**: Declarações de campanha (entrevistas, redes) não são fonte oficial; não foram usadas.
- **L15**: Busca em pronunciamentos do Senado não exaustiva.
- **F28**: 'O que prometeu' não tem medida oficial única; não há painel oficial acessível com 'prometido x entregue'.
- **F28**: Balanços da Secom de 2025-2026 (R$ 111,6 bi destinados; 94% executados) estão com acesso restrito no defeso eleitoral e são autodeclarados.
- **L40**: Fontes do governo chinês não estão na lista de tiers do projeto; registradas como 'oficial-governo-estrangeiro'.
- **L41**: Extensão total oficial de ramais e adutoras associadas ao PISF não localizada.
- **L42**: Notas do MCTI sobre o centro quântico (mar e jun/2026) com acesso restrito no defeso; valores divergem entre fontes (R$ 75 mi a R$ 200 mi).
- **L42**: Indústria automobilística no NE (fábricas e datas) não checada em fonte oficial.
- **F41**: Não se localizou documento oficial com promessa de entrega 'até 2009'.
- **F41**: Percentual de execução em dez/2018 não localizado.
- **L78**: Não se verificou se houve atos infralegais do Ministério da Economia em 2022 sobre o tema.

#### Observações de método

- Investimento público: usada só a série do Tesouro (RTN, Tabelas 1.3-A/2.3/2.3-A, investimento pago do Governo Central, GND 4, corrigido pelo IPCA a preços de jul/2026). A série da FGV não foi usada.
- Obras paralisadas: números consultados diretamente no modelo de dados do Painel de Obras Paralisadas do TCU (extrações ago/2022, abr/2023, abr/2024, abr/2025, abr/2026), incluindo o corte por ano de início da obra.
- Leituras incertas da legenda: L02 ('1 trilhão e 700 milhões' = R$ 1,7 tri; 'quase 800' = R$ 800 bi), L07 ('Ferrovia das Araras' = Nova Serra das Araras, rodovia), L08 ('o canal' = ruído), L11 ('1846'), L41 (totais de canais/adutoras), L42 ('supercutador' = supercomputador).
- Fontes do governo da China (L40) foram registradas com o tier 'oficial-governo-estrangeiro', fora da lista de tiers do projeto.
