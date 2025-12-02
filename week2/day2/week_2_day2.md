# **Tag 2 OOP Basics, aber richtig (praxisorientiert, nicht akademisch)**

Du bist kein Anfänger → wir gehen OOP auf Data-Engineering-Art an.

### **Themen:**

- `__init__`, `__repr__`
- Klassenmethoden (`@classmethod`)
- Statische Methoden (`@staticmethod`)
- Properties
- Dataclasses (wichtiger!)

### **Aufgaben:**

1. Erstelle eine `Person` Klasse mit:
   - name, age, city
   - `__repr__`
   - `@classmethod from_csv_row`
   - property `is_adult`
2. Nutze `dataclasses.dataclass` für dieselbe Klasse vergleiche.
3. Bonus:
   Schreibe eine Klasse `CSVLoader`, die: - Dateien einliest - Zeilen in `Person`Objekte umwandelt - Methoden wie `.filter_by_city()`, `.average_age()` hat
