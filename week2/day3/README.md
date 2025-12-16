# 🔥 **Tag 3 – Module, Packages, Architektur**

### **Themen:**

- Projektstruktur für Data Engineering
- `__init__.py`
- relative imports
- eigene Packages bauen

### **Aufgaben:**

Erstelle eine Projektstruktur:

```
my_project/
   data/
   core/
        __init__.py
        csv_loader.py
        transformations.py
        statistics.py
   main.py

```

1. `csv_loader.py` → CSV lesen
2. `transformations.py` → Functions wie:
   - convert_to_int
   - replace_empty_with_none
   - scale_salary()
3. `statistics.py`
   - average
   - count_missing
   - min/max
4. `main.py` → orchestriert alles
   (so wie echte ETL-Skripte)
5. Bonus:
   Schreibe Unit Tests für 2–3 Funktionen (`unittest`).
