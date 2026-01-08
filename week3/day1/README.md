# 🗓️ Woche 3 – Tag 1

## Pandas Memory & Dtype Engineering

### 🎯 Ziel

Du sollst **belegen**, dass du Pandas **kontrollierst**, nicht umgekehrt:

- Speicherverbrauch verstehen
- Dtypes bewusst wählen
- Entscheidungen **messen und begründen**

---

## 📦 Aufgabe 1 – Synthetisches Dataset (Pflicht)

### Anforderungen

Erzeuge ein DataFrame mit **mindestens 5 Mio Zeilen** und folgenden Spalten:

| Spalte       | Beschreibung                | Erwarteter Typ        |
| ------------ | --------------------------- | --------------------- |
| `event_id`   | fortlaufende ID             | int                   |
| `user_id`    | viele Wiederholungen        | int                   |
| `event_type` | ~10 diskrete Werte          | str → später category |
| `value`      | numerisch mit Ausreißern    | float                 |
| `created_at` | Zeitstempel                 | datetime              |
| `country`    | ISO-Code (z. B. DE, US, FR) | str → category        |
| `is_active`  | Flag                        | bool                  |

**Regeln**

- **Kein CSV-Import**
- Datenerzeugung **primär mit NumPy**
- Zufallsseed setzen
- Code muss deterministisch sein

---

## 🔍 Aufgabe 2 – Memory Audit (Pflicht)

Erstelle eine **saubere Analyse**:

1. Gesamt-RAM des DataFrames
2. RAM pro Spalte
3. Identifikation von:

   - `object`-Spalten
   - überdimensionierten Numerics
   - unnötigem Index

**Erwartung**

- Nutzung von
  `df.info(memory_usage="deep")`
  `df.memory_usage(deep=True)`
- Ergebnisse **nicht nur ausgeben**, sondern **interpretieren**

---

## 🛠️ Aufgabe 3 – Optimierung (Pflicht)

Optimiere den DataFrame gezielt:

- Downcasting:

  - `int64 → int32 / int16`
  - `float64 → float32` (nur wenn vertretbar!)

- `object → category` **nur dort, wo sinnvoll**
- Index bewusst setzen oder entfernen

**Wichtig**

- Jede Optimierung muss:

  - messbar sein
  - begründet werden
  - **nicht blind angewendet**

---

## 📊 Aufgabe 4 – Vorher/Nachher-Vergleich (Pflicht)

Erstelle eine Vergleichstabelle:

| Metrik                    | Vorher | Nachher |
| ------------------------- | ------ | ------- |
| Gesamt-RAM                |        |         |
| Größte Spalte             |        |         |
| Anzahl object-Spalten     |        |         |
| Ladezeit (falls relevant) |        |         |

---

## 📝 Aufgabe 5 – Engineering-Notiz (Pflicht)

Kurzer Report (Markdown, max. 1 Seite):

- Welche Optimierungen haben **am meisten gebracht**?
- Welche waren **riskant**?
- Welche würdest du **in Produktion nicht automatisch** anwenden?
- Wo liegen die **Tradeoffs (CPU vs RAM)**?

---

## ❌ Typische Fehler (werden hart abgestraft)

- `.astype()` ohne Messung
- Kategorien für High-Cardinality-Spalten
- „Pandas macht das schon“
- Kein Seed
- Kein reproduzierbarer Code

---

## ✅ Abgabeformat

Du schickst mir:

1. Code (ein Python-File oder Notebook)
2. Memory-Vergleich (Text oder Tabelle)
3. Engineering-Notiz
