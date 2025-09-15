# gen_market.py
# Převod final_catalog.json -> market.json (kategorie + karty)
import json, re, sys
from collections import defaultdict

SRC = "final_catalog.json"
DST = "market.json"

def slz(x):  # safe lower string
    return str(x or "").strip()

def first(*keys):
    def pick(d):
        for k in keys:
            if isinstance(k, (list, tuple)):
                for kk in k:
                    if kk in d and d[kk] not in (None, ""):
                        return d[kk]
            else:
                if k in d and d[k] not in (None, ""):
                    return d[k]
        return None
    return pick

# mapování polí z různých zdrojů
GET_ID       = first("id","ID","uid","guid","slug","code")
GET_CODE     = first("number","code","kód","cislo","Číslo","no","num")
GET_TITLE    = first("title","name","název","Nazev")
GET_SUBTITLE = first("subtitle","description","desc","popis")
GET_URL      = first("url","link","href")
GET_ICON     = first("icon","ikonka","iconUrl","icon_url")
GET_TAGS     = first("tags","štítky","stítky","tagy")
GET_ORDER    = first("order","pořadí","poradi","ord","rank")
GET_CAT      = first("category","kategorie","section","sekce","group")

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def flatten_items(data):
    """Vrátí list položek a kategorii (pokud ji víme)"""
    # Podpora různých struktur:
    if isinstance(data, dict):
        if isinstance(data.get("categories"), list):
            items = []
            for cat in data["categories"]:
                cat_title = slz(cat.get("title") or cat.get("key") or "Ostatní")
                for it in (cat.get("items") or []):
                    it = dict(it)
                    it["_category"] = cat_title
                    items.append(it)
            return items
        if isinstance(data.get("items"), list):
            return data["items"]
    if isinstance(data, list):
        return data
    return []

def norm_item(raw):
    i = {}
    i["id"]       = slz(GET_ID(raw) or "")
    i["order"]    = GET_ORDER(raw) or 0
    try:
        i["order"] = int(i["order"])
    except: i["order"]=0
    i["number"]   = slz(GET_CODE(raw) or "")
    i["title"]    = slz(GET_TITLE(raw) or "")
    i["subtitle"] = slz(GET_SUBTITLE(raw) or "")
    i["url"]      = slz(GET_URL(raw) or "")
    i["icon"]     = slz(GET_ICON(raw) or "default.svg")
    tags         = GET_TAGS(raw) or []
    if isinstance(tags, str):
        tags = [t.strip() for t in re.split(r"[;,]", tags) if t.strip()]
    i["tags"]     = tags
    i["layout"]   = {"w": 4}
    i["_category"]= slz(GET_CAT(raw) or raw.get("_category") or "Ostatní")
    return i

def build_market(items):
    cats = defaultdict(lambda: {"key":"","title":"","items":[]})
    for it in items:
        c = it["_category"] or "Ostatní"
        if not cats[c]["key"]:
            cats[c]["key"] = c; cats[c]["title"] = c
        it2 = {k:v for k,v in it.items() if not k.startswith("_")}
        cats[c]["items"].append(it2)
    # seřazení v rámci kategorií
    for c in cats.values():
        c["items"].sort(key=lambda x: x.get("order",0))
    market = {
        "app": {"title":"Digitální Tržiště","public": True},
        "categories": sorted(cats.values(), key=lambda x: 0 if x["title"] in ("Úvod","Aplikace") else 1)
    }
    return market

def main():
    data = load_json(SRC)
    items = flatten_items(data)
    if not items:
        print(f"⚠️  V {SRC} jsem nenašel žádné položky.")
        sys.exit(1)
    norm = [norm_item(x) for x in items if GET_TITLE(x)]
    market = build_market(norm)
    with open(DST,"w",encoding="utf-8") as f:
        json.dump(market, f, ensure_ascii=False, indent=2)
    total = sum(len(c["items"]) for c in market["categories"])
    print(f"✅ Vytvořeno {DST} s {total} položkami.")

if __name__ == "__main__":
    main()
