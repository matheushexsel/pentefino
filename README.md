# Pente Fino

Base de dados públicos, verificáveis e apartidários sobre política, economia e serviços públicos no Brasil, para alimentar um site didático de checagem de fatos. Estado dos dados: 21 de outubro de 2026 (duas rodadas de pesquisa).

## Estrutura

- `data/` — dados estruturados que o site lê. Esquema em `data/SCHEMA.md`. Manifesto em `data/index.json`.
  - `checagens/` frases checadas (229), `falas/` frases ditas em debates e sabatinas (344), `eventos/` debates, sabatinas e entrevistas (18)
  - `series/` séries temporais (150), `governos.json` fichas dos cinco governos desde 2003
  - `escandalos/` casos de corrupção com pessoas, partidos e situação jurídica (19, mais tabelas auxiliares de leniências da CGU e balanços da Lava Jato), `historias/` linhas do tempo longas (7)
  - `explicadores/` "quem decide isso?" (9), `medidas/` impostos, benefícios e leis com quem ganha e quem paga (40), `simuladores/renda.json`
  - `glossario.json`, `partidos.json`, `candidatos.json`, `temas.json`, `temas_em_alta.json`, `fontes.json`
- `research_notes/` — notas brutas de pesquisa por tema, com número, período de referência e URL da fonte em cada dado.
- `reports/` — relatório consolidado.
- `scripts/build_index.py` — valida todos os arquivos de `data/` e gera `index.json` e `fontes.json`.

## Regras dos dados

Todo número tem valor, período, fonte e URL. Nada é estimado fora do que as fontes dizem: itens sem verificação completa carregam `"nao_verificado": true` e a lista `lacunas` explica o que falta. A escala de vereditos e os ids fixos estão em `data/SCHEMA.md`.

## Validar

```
python3 -I scripts/build_index.py --check
```
