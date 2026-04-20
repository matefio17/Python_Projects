# 🎰 Python CLI Casino Simulator

Konsolowa aplikacja kasynowa napisana w Pythonie jako projekt edukacyjny
do nauki programowania — logiki aplikacji, walidacji danych oraz budowy większych systemów CLI.

---

## 🎮 Dostępne gry

| Gra                    | Status                   |
| ---------------------- | ------------------------ |
| 🎡 Ruletka             | ✅ Ukończona (end-to-end) |
| 🃏 Poker Texas Hold'em | 🔜 Wkrótce               |
| 🂱 Blackjack           | 🔜 Wkrótce               |

---

## 🎯 Ruletka — funkcjonalności

Ruletka została zaimplementowana w pełni end-to-end:

* ✔️ pełny flow użytkownika (menu → wybór zakładu → spin → wynik → update portfela)
* ✔️ system portfela (saldo, wpłaty, wypłaty)
* ✔️ walidacja danych wejściowych (int, float, listy, zakresy, edge case’y)
* ✔️ animacja spinu ruletki (efekt zwalniania)

### 🟥 Outside bets:

* Red / Black
* Even / Odd
* Low / High (1–18 / 19–36)
* Dozens (1–12 / 13–24 / 25–36)

### 🎯 Inside bets:

* Straight up
* Split
* Street
* Corner
* Six line

---

## 🚀 Uruchomienie

```bash
git clone https://github.com/matefio17/Python_Projects
cd Python_Projects/Python_CLI_Casino_Simulator
python python_cli_casino_simulator.py
```

> Wymagany Python 3.x — projekt korzysta wyłącznie ze standardowych bibliotek (`random`, `time`).

---

## 📚 Czego się nauczyłem

* budowy pełnego flow aplikacji CLI
* zarządzania stanem (wallet, przebieg gry)
* implementacji logiki domenowej (zasady ruletki i typy zakładów)
* walidacji danych wejściowych (defensive programming)
* pracy ze strukturami danych (`dict`, listy, mapowania)
* rozbijania problemu na mniejsze funkcje i modularny kod
* obsługi edge case’ów i debugowania logiki
* refaktoryzacji kodu (przejście od „spaghetti code” do czytelniejszej struktury)

---

## 🔜 Plany rozwoju

* [x] System salda (portfel - doładowania i wypłaty)
* [x] Pełna implementacja ruletki (zakłady, logika, wypłaty)
* [ ] Refaktoryzacja (m.in. lepsza struktura danych, dispatch logic)
* [ ] Poker Texas Hold'em
* [ ] Blackjack
* [ ] Podział projektu na moduły (`roulette.py`, `blackjack.py`, itd.)

---

## 👨‍💻 Autor

**matefio17** — projekt realizowany w ramach nauki Pythona i przygotowania do pracy w IT (Python / IT Support / Sysadmin)
