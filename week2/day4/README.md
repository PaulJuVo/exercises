# **Tag 4 – Error Handling & Logging (Pro Level)**

### **Themen:**

- eigener Logger (mit log Datei + Konsole)
- Handler: FileHandler, StreamHandler
- Logging Levels
- Eigene Exceptions schreiben

### **Aufgaben:**

1. Schreibe eine eigene Exception:

   ```python
   class CSVFormatError(Exception):
       ...

   ```

2. Löst sie aus, wenn:
   - eine Spalte fehlt
   - ein Datentyp nicht stimmt
3. Setze Logger so auf:
   - INFO → Konsole
   - ERROR → Datei `errors.log`
4. Bonus:
   Schreibe einen Decorator `@log_exceptions`, der automatisch jede Exception loggt und erneut raised.
