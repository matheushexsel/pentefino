# Esquema dos dados do Pente Fino

Pasta `data/` é a fonte de verdade do site. Todo número tem valor, período de referência, fonte e URL. Nada é inventado: se um dado não está nas notas de `research_notes/`, o campo fica `null` e o item vai para `lacunas`.

## Convenções gerais

- Arquivos JSON, UTF-8, indentação de 2 espaços. Datas em ISO `AAAA-MM-DD`; períodos como texto curto (`"ago/2026"`, `"2T2026"`, `"2025"`).
- Números sempre numéricos (não string). Unidade em campo próprio. Valores monetários em bilhões quando acima de 1 bilhão (`"R$ bilhões"`).
- `slug`: minúsculas, sem acento, hífens, sem stopwords desnecessárias.
- Toda `fonte`: `{ "nome": "...", "url": "https://...", "acesso_em": "2026-10-21", "tier": "oficial|multilateral|academico|checagem|imprensa|partidario" }`.
- Todo registro: `"atualizado_em"`, `"nota_bruta_url"` (link para a nota em `research_notes/` no GitHub, branch master) e, se necessário, `"lacunas": ["..."]`.
- Campos de texto em português do Brasil, linguagem simples, sem palavras de torcida.

## IDs fixos

**Governos** (`governos.json`): `lula-1-2` (2003-2010), `dilma` (2011-2016-08-31), `temer` (2016-08-31 a 2018), `bolsonaro` (2019-2022), `lula-3` (2023-).

**Lados**: `governo-lula-pt`, `oposicao-flavio-pl`, `outro`, `ambos`.

**Candidatos** (`candidatos.json`): `lula`, `flavio-bolsonaro`, `caiado`, `zema`, `renan-santos`, `cury` (demais conforme TSE).

**Vereditos** (ordem fixa e nota para ClaimReview, `bestRating` 6, `worstRating` 1):
`verdadeiro` (6), `verdadeiro-mas` (5), `falta-contexto` (4), `exagerado` (3), `impreciso` (2), `falso` (1), `insustentavel` (sem nota), `opiniao` (sem nota).

**Temas** (`temas.json`): `economia`, `contas-publicas`, `emprego-renda`, `pobreza-programas-sociais`, `impostos`, `pix`, `energia`, `combustiveis`, `seguranca`, `saude`, `educacao`, `infraestrutura`, `meio-ambiente`, `corrupcao`, `justica-stf`, `eleicao-2026`, `ideologias`, `relacoes-exteriores`, `direitos-sociais`.

**status_categoria** (pessoas em escândalos e processos): `investigado`, `denunciado`, `reu`, `condenado-1a`, `condenado-2a`, `condenado-definitivo`, `absolvido`, `arquivado`, `prescrito`, `anulada`, `cumprindo-pena`, `pena-cumprida`, `nao-investigado`.

**status de medidas**: `em-vigor`, `proposta`, `aprovada-aguarda`, `revogada`, `caducou`, `suspensa-stf`, `vetada`.

**tipo de evento**: `debate`, `sabatina`, `entrevista`, `podcast`, `live`, `discurso`, `propaganda`, `rede-social`.

## Arquivos

### `index.json`
```json
{ "versao": "1.0.0", "atualizado_em": "...", "arquivos": { "checagens": [...], "series": [...], "escandalos": [...], "explicadores": [...], "historias": [...], "eventos": [...], "falas": [...], "medidas": [...], "simuladores": [...], "governos": "governos.json", "glossario": "glossario.json", "candidatos": "candidatos.json", "partidos": "partidos.json", "fontes": "fontes.json", "temas": "temas.json", "temas_em_alta": "temas_em_alta.json" } }
```

Arquivos auxiliares (nome começando com `_`, ex.: `escandalos/_resumo_por_partido.json`, `escandalos/_leniencias_cgu.json`, `escandalos/_balancos_lava_jato.json`, `falas/_resumo.json`) não seguem o esquema da coleção e são listados à parte em `index.json`, na chave `auxiliares`.

### `checagens/<slug>.json`
```json
{ "id": "chk-0001", "slug": "...", "frase": "...", "frase_normalizada": "...", "variantes": [], "autor": { "nome": "...", "partido": "...", "cargo": "..." }, "lado": "...", "alvo": { "nome": "...", "partido": "..." }, "data": "...", "onde": "...", "url_declaracao": "...", "temas": [], "tags": [], "veredito": "...", "resumo_uma_frase": "...", "explicacao_simples": ["3 frases"], "explicacao_completa_md": "...", "o_que_e_verdade": [], "o_que_nao_se_sustenta": [], "quem_e_responsavel": [ { "ator": "...", "papel": "...", "peso": "alto|medio|baixo" } ], "numeros": [ { "rotulo": "...", "valor": 0, "unidade": "...", "periodo": "...", "fonte": {}, "comparacao": { "rotulo": "...", "valor": 0 } } ], "series": ["id-da-serie"], "checagens_externas": [ { "veiculo": "...", "veredito_original": "...", "url": "...", "data": "..." } ], "fontes": [], "nota_bruta_url": "...", "perguntas_frequentes": [ { "pergunta": "...", "resposta": "..." } ], "relacionadas": ["slug"], "atualizado_em": "...", "changelog": [ { "data": "...", "o_que_mudou": "publicação" } ], "exemplo": false }
```

### `series/<id>.json`
```json
{ "id": "...", "titulo": "...", "descricao_simples": "...", "unidade": "...", "tipo_grafico": "barra|linha|area", "frequencia": "anual|mensal|trimestral", "fonte": {}, "pontos": [ { "periodo": "2003", "valor": 1.1 } ], "faixas_referencia": [ { "rotulo": "...", "valor": 0 } ], "notas_metodologicas": [], "ultimo_periodo": "...", "temas": [], "atualizado_em": "..." }
```

### `governos.json` (array)
```json
{ "id": "...", "presidente": "...", "partido": "...", "inicio": "...", "fim": null, "vice": "...", "resumo_uma_frase": "...", "contexto_externo": [], "indicadores_inicio_fim": [ { "serie": "divida-bruta-pib", "inicio": { "periodo": "...", "valor": 0 }, "fim": { "periodo": "...", "valor": 0 } } ] }
```

### `escandalos/<id>.json`
```json
{ "id": "...", "nome": "...", "periodo": { "inicio": "...", "fim": null }, "governos_em_que_ocorreram_os_fatos": [], "governos_em_que_foi_investigado": [], "resumo_simples": [], "valores": [ { "rotulo": "...", "valor": 0, "unidade": "...", "fonte": {} } ], "partidos": [ { "partido": "...", "citados": null, "denunciados": null, "condenados_1a_instancia": null, "condenados_definitivo": null, "condenacoes_anuladas": null, "fonte": {} } ], "pessoas": [ { "nome": "...", "partido_na_epoca": "...", "cargo": "...", "crime": "...", "tribunal": "...", "data_condenacao": null, "pena": null, "status_atual": "...", "status_categoria": "...", "url": "..." } ], "linha_do_tempo": [ { "data": "...", "evento": "...", "url": "..." } ], "o_que_dizem_os_dois_lados": { "acusacao": "...", "defesa": "..." }, "status_atual_md": "...", "fontes": [], "nota_bruta_url": "...", "atualizado_em": "..." }
```

### `explicadores/<id>.json` ("Quem decide isso?")
```json
{ "id": "...", "pergunta": "...", "resposta_curta": "...", "temas": [], "cadeia_de_responsabilidade": [ { "ator": "...", "o_que_controla": "...", "o_que_nao_controla": "...", "peso": "alto|medio|baixo", "url": "..." } ], "composicao": [ { "rotulo": "...", "percentual": 0, "fonte": {} } ], "linha_do_tempo": [], "numeros": [], "series": [], "mitos_e_fatos": [ { "mito": "...", "fato": "...", "fontes": [] } ], "perguntas_frequentes": [], "fontes": [], "nota_bruta_url": "...", "atualizado_em": "..." }
```

### `historias/<id>.json`
```json
{ "id": "...", "titulo": "...", "pergunta_principal": "...", "resposta_curta": ["3 frases"], "periodo": { "inicio": "...", "fim": "..." }, "temas": [], "personagens": [ { "id": "...", "nome": "...", "papel_na_historia": "...", "partido_atual": null } ], "capitulos": [ { "id": "1", "titulo": "...", "periodo": "...", "texto_md": "...", "eventos": [ { "data": "...", "fato": "...", "citacao_literal": null, "literal": true, "quem_disse": null, "url": "...", "tipo": "declaracao|decisao|fato|documento" } ], "o_que_a_acusacao_dizia": "...", "o_que_a_defesa_dizia": "...", "numeros": [] } ], "glossario_local": [ { "termo": "...", "definicao_simples": "..." } ], "o_que_cada_lado_diz_hoje": { "lado_a": { "quem": "...", "frase": "...", "veredito": "...", "checagem_slug": null }, "lado_b": { "quem": "...", "frase": "...", "veredito": "...", "checagem_slug": null } }, "perguntas_frequentes": [], "fontes": [], "nota_bruta_url": "...", "atualizado_em": "..." }
```

### `eventos/<id>.json`
```json
{ "id": "...", "tipo": "debate", "nome": "...", "data": "...", "veiculo": "...", "participantes": ["lula", "flavio-bolsonaro"], "url_video": null, "url_transcricao": null, "resumo_uma_frase": "...", "placar": { "lula": { "checadas": 0, "por_veredito": {} }, "flavio-bolsonaro": { "checadas": 0, "por_veredito": {} } }, "falas": ["fala-id"], "checagens_externas": [], "fontes": [], "atualizado_em": "..." }
```

### `falas/<id>.json`
```json
{ "id": "fala-0001", "slug": "...", "evento_id": "...", "candidato": "lula|flavio-bolsonaro|<aliado-slug>", "lado": "...", "minuto": null, "frase_literal": "...", "literal": true, "tema": "...", "veredito": "...", "resumo_uma_frase": "...", "explicacao_simples": [], "o_que_e_verdade": [], "o_que_nao_se_sustenta": [], "numeros": [], "base_legal": [ { "norma": "...", "o_que_diz": "...", "url": "..." } ], "checagens_externas": [], "checagem_slug": null, "historia_id": null, "fontes": [], "atualizado_em": "..." }
```

### `medidas/<id>.json`
```json
{ "id": "...", "nome": "...", "tipo": "imposto|beneficio|lei-trabalhista|tarifa|privatizacao|outro", "governo": "...", "lado": "...", "norma": { "nome": "...", "data": "...", "url": "...", "vigencia": "..." }, "status": "...", "o_que_faz_simples": [], "quem_ganha": { "descricao": "...", "pessoas": null, "faixa_renda": "...", "fonte": {} }, "quem_paga": { "descricao": "...", "pessoas": null, "faixa_renda": "...", "fonte": {} }, "custo_ou_arrecadacao": { "valor": null, "unidade": "...", "fonte": {} }, "regra_simulador": { "tipo": "tabela|percentual|fixo|nenhuma", "parametros": {} }, "mitos": [ { "mito": "...", "fato": "...", "fontes": [] } ], "fontes": [], "nota_bruta_url": "...", "atualizado_em": "..." }
```

### `simuladores/renda.json`
```json
{ "id": "renda", "salario_minimo": { "valor": 1621, "ano": 2026, "fonte": {} }, "distribuicao": [ { "rotulo": "...", "faixa_max": 0, "pessoas": null, "percentual_acumulado": 0, "renda_media_decimo": 0, "fonte": {} } ], "mediana": { "valor": 0, "periodo": "...", "fonte": {} }, "medidas": ["id-em-medidas"], "notas": [] }
```

### `glossario.json` (array)
```json
{ "termo": "...", "slug": "...", "categoria": "ideologia|economia|juridico|eleitoral|energia|outro", "definicao_simples": "...", "definicao_completa_md": "...", "exemplos_historicos": [], "o_que_nao_e": "...", "criterios_academicos": [], "fontes": [] }
```

### `candidatos.json` (array)
```json
{ "slug": "...", "nome": "...", "nome_urna": "...", "partido": "...", "vice": { "nome": "...", "partido": "..." }, "coligacao": [], "resumo_neutro": ["3 frases"], "cargos": [ { "cargo": "...", "inicio": "...", "fim": null } ], "patrimonio_tse": { "total": 0, "ano": 2026, "itens": [ { "descricao": "...", "valor": 0 } ], "url": "..." }, "votacoes": [ { "materia": "...", "data": "...", "voto": "...", "url": "..." } ], "processos": [ { "caso": "...", "status_categoria": "...", "tribunal": "...", "data": "...", "url": "..." } ], "mudancas_de_posicao": [ { "tema": "...", "antes": "...", "depois": "...", "fontes": [] } ], "doacoes": { "total": null, "fundo_eleitoral": null, "maiores_doadores": [], "url": "..." }, "programa": { "url": "...", "eixos": [] }, "resultado_1_turno": { "votos": 0, "percentual": 0, "fonte": {} }, "fontes": [] }
```

### `partidos.json` (array)
```json
{ "sigla": "...", "nome": "...", "fundacao": "...", "posicao_espectro": { "bls_score": null, "ano": null, "fonte": {} }, "presidente": null, "bancada_camara_2023": null, "bancada_camara_2027": null, "bancada_senado_2027": null, "fontes": [] }
```

### `temas.json` (array)
```json
{ "slug": "...", "nome": "...", "descricao": "...", "icone": "lucide-icon-name", "ordem": 1 }
```

### `temas_em_alta.json` (array)
```json
{ "id": "...", "termo": "...", "lado_que_impulsiona": "...", "evidencia": [ { "fonte": "...", "metrica": "...", "data": "...", "url": "..." } ], "o_que_e": "...", "o_que_os_dados_dizem": "...", "checagem_slug": null, "historia_id": null, "atualizado_em": "..." }
```

### `fontes.json` (array, gerado por script a partir de todos os registros)
```json
{ "nome": "...", "dominio": "...", "tier": "...", "ocorrencias": 0 }
```
