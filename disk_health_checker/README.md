
# Disk Health Checker 💾

Prosty i skuteczny monitor wolnego miejsca na dysku napisanym w Pythonie. Skrypt działa w pętli, sprawdzając stan zasobów i raportując go do konsoli oraz pliku tekstowego.

## 📋 Spis treści
- [Funkcje](#-funkcje)
- [Wymagania](#-wymagania)
- [Instalacja i uruchomienie](#-instalacja-i-uruchomienie)
- [Konfiguracja](#-konfiguracja)
- [Struktura logów](#-struktura-logów)
- [🚀 Plany rozwoju (Roadmap)](#-plany-rozwoju-roadmap)

## ✨ Funkcje
- **Monitorowanie w czasie rzeczywistym:** Automatyczne sprawdzanie wolnego miejsca w zdefiniowanych odstępach czasu.
- **Wielopoziomowe alerty:** Obsługa statusów `OK`, `WARNING` oraz `CRITICAL` w zależności od procentowego wypełnienia dysku.
- **Podwójne logowanie:** Zapisywanie zdarzeń do pliku `disk_health.log` oraz jednoczesne wyświetlanie ich w terminalu.
- **Obsługa błędów:** Odporność na przerwanie pracy przez użytkownika (Ctrl+C) oraz nieoczekiwane wyjątki.

## ⚙️ Wymagania
- Python 3.10 lub nowszy (ze względu na użycie instrukcji `match-case`).
- Biblioteki standardowe: `shutil`, `time`, `logging`.

## 🚀 Instalacja i uruchomienie

1. Sklonuj repozytorium lub pobierz plik skryptu.
2. Upewnij się, że masz zainstalowanego Pythona:
   
   `python --version`

3. Uruchom skrypt:
   
   `disk_health_checker.py`
   

## 🛠️ Konfiguracja
Możesz dostosować działanie skryptu, edytując stałe na początku pliku:
| Zmienna | Opis | Domyślnie |
|---|---|---|
| DISK_PATH | Ścieżka do monitorowanego partycji/dysku | / |
| MIN_FREE_PCT_WARNING | Próg procentowy dla ostrzeżenia | 20% |
| MIN_FREE_PCT_CRITICAL | Próg procentowy dla stanu krytycznego | 5% |
| CHECK_INTERVAL_SECONDS | Częstotliwość sprawdzania (sekundy) | 120 |
## 📄 Struktura logów
Skrypt generuje logi w następującym formacie:
YYYY-MM-DD HH:MM:SS,ms - LEVEL - WIADOMOŚĆ
Przykład:
```text
2023-10-27 12:00:00,123 - INFO - Disk space OK. 45.50% (220.30GB) of free space left.
2023-10-27 12:02:00,123 - WARNING - Low disk space. Only 18.20% (80.15GB) of free space left.

```
## 🚀 Plany rozwoju (Roadmap)
Projekt będzie rozbudowywany o następujące funkcjonalności:
### Etap 1: Powiadomienia i komunikacja
 * [ ] **System powiadomień:** Wysyłanie alertów e-mail (SMTP) po przekroczeniu progu krytycznego.
 * [ ] **Integracja z Webhookami:** Wysyłanie powiadomień na Slacka lub Discorda.
### Etap 2: Rozszerzona analityka
 * [ ] **Monitorowanie wielu ścieżek:** Możliwość zdefiniowania listy dysków/punktów montowania do jednoczesnego sprawdzania.
 * [ ] **Wykrywanie trendów:** Logika sprawdzająca, jak szybko ubywa miejsca na dysku (np. MB/godzinę).
### Etap 3: Interfejs i konfiguracja
 * [ ] **Zewnętrzny plik konfiguracyjny:** Przeniesienie ustawień do pliku .env lub config.json.
 * [ ] **Prosty Dashboard:** Generowanie statycznego raportu HTML z wykresami zużycia miejsca.
### Etap 4: Automatyzacja
 * [ ] **Czyszczenie dysku:** Automatyczne usuwanie plików tymczasowych po osiągnięciu stanu krytycznego.
 * [ ] **Docker:** Konteneryzacja skryptu dla łatwiejszego wdrażania na serwerach.



---

## 👨‍💻 Autor

**Mateusz Markiewicz** — projekt realizowany w ramach nauki Pythona i przygotowania do pracy w IT (Python / IT Support / Sysadmin)
