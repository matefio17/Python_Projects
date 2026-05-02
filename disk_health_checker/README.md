
# Disk Health Checker 💾

Prosty, ale rozbudowywany monitor wolnego miejsca na dysku napisany w Pythonie.  
Skrypt działa w pętli, zbiera metryki systemowe i raportuje stan dysku w czasie rzeczywistym do konsoli oraz pliku logów.

Projekt ewoluuje w kierunku lekkiego narzędzia typu **system health monitor / lightweight observability agent**.

---

## 📋 Spis treści
- [Funkcje](#-funkcje)
- [Architektura](#-architektura)
- [Wymagania](#-wymagania)
- [Instalacja i uruchomienie](#-instalacja-i-uruchomienie)
- [Konfiguracja](#-konfiguracja)
- [Struktura logów](#-struktura-logów)
- [Obsługa błędów](#-obsługa-błędów)
- [Plany rozwoju (Roadmap)](#-plany-rozwoju-roadmap)

---

## ✨ Funkcje

- **Monitoring w czasie rzeczywistym**  
  Cycliczne sprawdzanie stanu dysku w zadanym interwale.

- **Rozszerzone metryki systemowe**  
  Zbieranie danych o:
  - użytej przestrzeni
  - całkowitej pojemności
  - wolnym miejscu (GB i %)

- **Wielopoziomowe statusy zdrowia systemu**
  - `OK`
  - `WARNING`
  - `CRITICAL`

- **State tracking (zmiana stanu)**  
  Logowanie tylko przy zmianie statusu systemu (redukcja szumu logów).

- **Podwójne logowanie**
  - terminal (stdout)
  - plik `disk_health.log`

- **Obsługa błędów systemowych**
  Stabilność działania w przypadku problemów OS lub uprawnień.

---

## 🧠 Architektura

Projekt został zbudowany w prostym modelu:

```

main loop
↓
get_disk_usage() → zbiera metryki systemowe
↓
check_status() → ocenia stan dysku
↓
state comparison (previous_status)
↓
logging_process() → zapis logów tylko przy zmianie stanu

````

---

## ⚙️ Wymagania

- Python 3.10+
- Biblioteki standardowe:
  - `shutil`
  - `time`
  - `logging`

---

## 🚀 Instalacja i uruchomienie

1. Sklonuj repozytorium lub pobierz plik:
```bash
git clone <repo-url>
````

2. Sprawdź wersję Pythona:

```bash
python --version
```

3. Uruchom skrypt:

```bash
python disk_health_checker.py
```

---

## 🛠️ Konfiguracja

Główne parametry systemu znajdują się w sekcji konfiguracji:

| Zmienna                  | Opis                           | Domyślnie     |
| ------------------------ | ------------------------------ | ------------- |
| `DISK_PATH`              | Monitorowana ścieżka dysku     | `/` lub `C:\` |
| `MIN_FREE_PCT_WARNING`   | Próg ostrzeżenia (%)           | 20            |
| `MIN_FREE_PCT_CRITICAL`  | Próg krytyczny (%)             | 5             |
| `CHECK_INTERVAL_SECONDS` | Interwał sprawdzania (sekundy) | 120           |

---

## 📄 Struktura logów

Logi zawierają pełny kontekst stanu systemu:

```
YYYY-MM-DD HH:MM:SS,ms - LEVEL - MESSAGE
```

Przykład:

```text
2026-05-02 12:00:00 - INFO - Disk space OK. == Current usage - 12.30GB/100GB. == 45.50% (55.20GB) free.
2026-05-02 12:02:00 - WARNING - Low disk space. == Current usage - 80.10GB/100GB. == 18.20% (18.20GB) free.
```

---

## ⚠️ Obsługa błędów

Skrypt obsługuje następujące klasy problemów:

* `OSError` → problemy systemowe / API OS
* `PermissionError` → brak dostępu do zasobów
* `KeyboardInterrupt` → bezpieczne zatrzymanie procesu
* `Exception` → fallback dla nieprzewidzianych błędów

Każdy błąd jest logowany z odpowiednim poziomem ważności.

---

## 🚀 Plany rozwoju (Roadmap)

### Etap 1: Integracje alertów

* [ ] Email notifications (SMTP)
* [ ] Webhook (Discord)

### Etap 2: Rozszerzenie monitoringu

* [ ] Obsługa wielu dysków / mount pointów
* [ ] Historia zużycia (trend analysis)

### Etap 3: Konfiguracja i skalowanie

* [ ] config.json / .env support
* [ ] CLI arguments (argparse)

### Etap 4: Observability upgrade

* [ ] eksport metryk (np. Prometheus format)
* [ ] dashboard HTML

---

## 👨‍💻 Autor

**Mateusz Markiewicz**
Projekt rozwijany w ramach nauki Python / Linux / System Administration
Cel: przygotowanie do pierwszej pracy w IT (Helpdesk / Junior Sysadmin / IT Ops)

