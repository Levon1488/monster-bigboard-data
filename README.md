# Monster BigBoard – Reality & Digital Products

Tento repozitář obsahuje kompletní katalog více než 140 digitálních a realitních produktů, rozdělených do kategorií.  
Data jsou připravena ve formátu **JSON**, a lze je použít pro:

- interaktivní vizualizace (mapy, bigboardy, zoom in/out)
- generování katalogů (PDF, web, e-shop)
- propojení s API a SaaS platformami

## Obsah repozitáře

- `final_catalog.json` – čitelná verze se všemi produkty (pro vývoj a úpravy)
- `final_catalog.min.json` – minifikovaná verze pro nasazení (rychlejší načítání)
- `README.md` – tento popis

## Struktura položek v JSON

Každý produkt obsahuje klíče:

- `section` – kategorie (např. Tipy na nemovitosti, Databáze, Šablony…)
- `type` – typ služby (ONLINE / PREMIUM / CUSTOM)
- `audience` – cílová skupina (INVESTOR / MAKLER / BOTH)
- `title` – název produktu
- `short` – krátký popisek (1 řádek)
- `what` – co to je, detailní vysvětlení
- `how` – jak funguje (frekvence, způsob dodání)
- `why` – proč je to užitečné pro klienta
- `icon` – doporučená ikona (Material Design / Eva Icons)
- `url` – odkaz (zatím placeholder `#`)
- `tags` – štítky pro vyhledávání

## Příklad

```json
{
  "section": "A. Tipy na nemovitosti a monitoring",
  "type": "ONLINE",
  "audience": "BOTH",
  "title": "Fresh Pack – Okresní monitoring",
  "short": "Denní sledování nových nabídek v okrese.",
  "what": "Automatický monitoring portálů a úředních zdrojů.",
  "how": "Doručení 7:30 / 16:00 do WhatsApp/Telegram + CSV.",
  "why": "Nesjíždíš ručně inzerci. Příležitosti dřív než ostatní.",
  "icon": "mdi:map-search-outline",
  "url": "#",
  "tags": "monitoring,tipy,okres"
}
```

## Využití

- **Investoři** – rychlý přehled o možnostech investování do nemovitostí a digitálních produktů.
- **Makléři** – moderní nástroje a šablony pro práci s klienty.
- **Firmy** – SaaS řešení, custom služby a databáze.

---

📌 Tento dataset je připravený k okamžitému použití v e-shopech (Shoptet, Shopify, WooCommerce) nebo pro vizualizaci v nástrojích jako Miro, D3.js, nebo vlastní webové aplikace.

