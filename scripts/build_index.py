#!/usr/bin/env python3
"""Monta data/index.json e data/fontes.json e valida os arquivos de data/.

Uso: python3 -I scripts/build_index.py [--check]
--check  apenas valida e reporta, sem escrever.
"""
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import date
from pathlib import Path
from urllib.parse import urlparse

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

VEREDITOS = {"verdadeiro", "verdadeiro-mas", "falta-contexto", "exagerado",
             "impreciso", "falso", "insustentavel", "opiniao"}
LADOS = {"governo-lula-pt", "oposicao-flavio-pl", "outro", "ambos"}
GOVERNOS = {"lula-1-2", "dilma", "temer", "bolsonaro", "lula-3"}
STATUS_CAT = {"investigado", "denunciado", "reu", "condenado-1a", "condenado-2a",
              "condenado-definitivo", "absolvido", "arquivado", "prescrito", "anulada",
              "cumprindo-pena", "pena-cumprida", "nao-investigado"}
STATUS_MED = {"em-vigor", "proposta", "aprovada-aguarda", "revogada", "caducou",
              "suspensa-stf", "vetada"}
SLUG_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")

COLECOES = ["checagens", "series", "escandalos", "explicadores", "historias",
            "eventos", "falas", "medidas", "simuladores"]
UNICOS = {"governos": "governos.json", "glossario": "glossario.json",
          "candidatos": "candidatos.json", "partidos": "partidos.json",
          "temas": "temas.json", "temas_em_alta": "temas_em_alta.json"}

erros, avisos = [], []


def carregar(p: Path):
    try:
        return json.loads(p.read_text(encoding="utf-8"))
    except Exception as e:  # noqa: BLE001
        erros.append(f"{p.relative_to(DATA)}: JSON inválido ({e})")
        return None


def fontes_de(obj, acc):
    """Percorre recursivamente e coleta objetos com 'url' e 'nome' (fontes)."""
    if isinstance(obj, dict):
        if "url" in obj and isinstance(obj.get("url"), str) and obj["url"].startswith("http"):
            nome = obj.get("nome") or obj.get("veiculo") or obj.get("fonte") or ""
            acc.append((str(nome), obj["url"], obj.get("tier")))
        for v in obj.values():
            fontes_de(v, acc)
    elif isinstance(obj, list):
        for v in obj:
            fontes_de(v, acc)


def validar_checagem(p, d):
    rel = p.relative_to(DATA)
    for campo in ("id", "slug", "frase", "lado", "veredito", "resumo_uma_frase",
                  "explicacao_simples", "numeros", "fontes", "atualizado_em"):
        if campo not in d:
            erros.append(f"{rel}: falta '{campo}'")
    if d.get("veredito") not in VEREDITOS:
        erros.append(f"{rel}: veredito inválido '{d.get('veredito')}'")
    if d.get("lado") not in LADOS:
        erros.append(f"{rel}: lado inválido '{d.get('lado')}'")
    if d.get("slug") and not SLUG_RE.match(d["slug"]):
        erros.append(f"{rel}: slug fora do padrão '{d['slug']}'")
    if d.get("slug") and p.stem != d["slug"]:
        erros.append(f"{rel}: nome do arquivo difere do slug '{d['slug']}'")
    if isinstance(d.get("explicacao_simples"), list) and len(d["explicacao_simples"]) != 3:
        avisos.append(f"{rel}: explicacao_simples tem {len(d['explicacao_simples'])} frases (esperado 3)")
    for n in d.get("numeros", []) or []:
        f = n.get("fonte") or {}
        if not f.get("url"):
            avisos.append(f"{rel}: número '{n.get('rotulo')}' sem URL de fonte")
    if d.get("exemplo") is True:
        avisos.append(f"{rel}: marcado como exemplo")


def validar_serie(p, d):
    rel = p.relative_to(DATA)
    for campo in ("id", "titulo", "unidade", "fonte", "pontos"):
        if campo not in d:
            erros.append(f"{rel}: falta '{campo}'")
    if d.get("id") and p.stem != d["id"]:
        erros.append(f"{rel}: nome do arquivo difere do id '{d['id']}'")
    for pt in d.get("pontos", []) or []:
        if not isinstance(pt.get("valor"), (int, float)) and pt.get("valor") is not None:
            erros.append(f"{rel}: valor não numérico em {pt.get('periodo')}")
    if not (d.get("fonte") or {}).get("url"):
        avisos.append(f"{rel}: série sem URL de fonte")


def validar_escandalo(p, d):
    rel = p.relative_to(DATA)
    for pess in d.get("pessoas", []) or []:
        if pess.get("status_categoria") not in STATUS_CAT:
            erros.append(f"{rel}: status_categoria inválido '{pess.get('status_categoria')}' ({pess.get('nome')})")
    for g in (d.get("governos_em_que_ocorreram_os_fatos") or []) + (d.get("governos_em_que_foi_investigado") or []):
        if g not in GOVERNOS:
            erros.append(f"{rel}: governo inválido '{g}'")


def validar_medida(p, d):
    rel = p.relative_to(DATA)
    if d.get("status") not in STATUS_MED:
        erros.append(f"{rel}: status inválido '{d.get('status')}'")
    if d.get("lado") not in LADOS:
        erros.append(f"{rel}: lado inválido '{d.get('lado')}'")
    if d.get("governo") and d["governo"] not in GOVERNOS | {"congresso", "proposta-2026"}:
        avisos.append(f"{rel}: governo fora da lista '{d.get('governo')}'")


def validar_fala(p, d):
    rel = p.relative_to(DATA)
    if d.get("veredito") not in VEREDITOS:
        erros.append(f"{rel}: veredito inválido '{d.get('veredito')}'")
    if d.get("lado") not in LADOS:
        erros.append(f"{rel}: lado inválido '{d.get('lado')}'")
    if not d.get("evento_id"):
        erros.append(f"{rel}: fala sem evento_id")


VALIDADORES = {"checagens": validar_checagem, "series": validar_serie,
               "escandalos": validar_escandalo, "medidas": validar_medida,
               "falas": validar_fala}


def main():
    check = "--check" in sys.argv
    index = {"versao": "1.0.0", "atualizado_em": date.today().isoformat(), "arquivos": {}}
    todas_fontes = []
    slugs, ids_series = Counter(), Counter()
    stats = defaultdict(Counter)

    for col in COLECOES:
        pasta = DATA / col
        arquivos = sorted(p for p in pasta.glob("*.json") if not p.name.startswith("_")) if pasta.exists() else []
        lista = []
        for p in arquivos:
            d = carregar(p)
            if d is None:
                continue
            lista.append(f"{col}/{p.name}")
            VALIDADORES.get(col, lambda *_: None)(p, d)
            fontes_de(d, todas_fontes)
            if col == "checagens":
                slugs[d.get("slug")] += 1
                stats["checagens_por_lado"][d.get("lado")] += 1
                stats["checagens_por_veredito"][d.get("veredito")] += 1
            if col == "series":
                ids_series[d.get("id")] += 1
            if col == "falas":
                stats["falas_por_candidato"][d.get("candidato")] += 1
                stats["falas_por_veredito"][d.get("veredito")] += 1
        index["arquivos"][col] = lista

    for chave, nome in UNICOS.items():
        p = DATA / nome
        if p.exists():
            d = carregar(p)
            if d is not None:
                index["arquivos"][chave] = nome
                fontes_de(d, todas_fontes)
        else:
            avisos.append(f"{nome}: ausente")
    index["arquivos"]["fontes"] = "fontes.json"

    for s, n in slugs.items():
        if n > 1:
            erros.append(f"slug duplicado em checagens: {s}")
    for s, n in ids_series.items():
        if n > 1:
            erros.append(f"id duplicado em series: {s}")

    # Referências cruzadas: séries citadas em checagens devem existir
    existentes = set(ids_series)
    for arq in index["arquivos"].get("checagens", []):
        d = carregar(DATA / arq) or {}
        for sid in d.get("series", []) or []:
            if sid not in existentes:
                avisos.append(f"{arq}: série referenciada não existe: {sid}")

    # fontes.json
    por_dominio = {}
    for nome, url, tier in todas_fontes:
        dom = urlparse(url).netloc.lower().removeprefix("www.")
        e = por_dominio.setdefault(dom, {"nome": nome or dom, "dominio": dom, "tier": tier, "ocorrencias": 0})
        e["ocorrencias"] += 1
        if not e.get("tier") and tier:
            e["tier"] = tier
        if (not e["nome"] or e["nome"] == dom) and nome:
            e["nome"] = nome
    fontes = sorted(por_dominio.values(), key=lambda x: -x["ocorrencias"])

    index["estatisticas"] = {k: dict(v) for k, v in stats.items()}
    index["estatisticas"]["total_fontes_distintas"] = len(fontes)

    print(f"Coleções: " + ", ".join(f"{k}={len(v) if isinstance(v, list) else 1}" for k, v in index["arquivos"].items()))
    print(f"Fontes distintas (domínios): {len(fontes)}")
    for k, v in index["estatisticas"].items():
        print(f"  {k}: {v}")
    if avisos:
        print(f"\nAVISOS ({len(avisos)}):")
        for a in avisos[:200]:
            print("  -", a)
    if erros:
        print(f"\nERROS ({len(erros)}):")
        for e in erros:
            print("  -", e)

    if not check:
        (DATA / "index.json").write_text(json.dumps(index, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        (DATA / "fontes.json").write_text(json.dumps(fontes, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print("\nindex.json e fontes.json gravados.")
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
