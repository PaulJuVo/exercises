# **Tag 4 – Error Handling & Logging (Pro Level)**

getLogger(**name**) erzeugt einen hierarchischen Logger, dessen Log-Meldungen per Propagation an den im main konfigurierten Root-Logger weitergeleitet werden.
Das Logging-Setup erfolgt im Einstiegspunkt der Anwendung, nicht beim Import von Modulen, um Seiteneffekte zu vermeiden und die Kontrolle über die Anwendungskonfiguration zu behalten.

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
