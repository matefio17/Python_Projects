# MINI PYTHON CASINO


import random
import time

# Przywitanie i wypisanie dostępnych gier

print("Witaj w mini Python Casino!\n")

games = {1 : "Ruletka",
         2 : "Poker Texas Holdem",
         3 : "Blackjack"
}


for number, game in games.items():
    print(f"{number}. {game}")
print()


# Obsługa wyboru gry

choice = None

while not choice:
    user_input = int(input("Wybierz grę wpisując liczbę do niej przypisaną np '1'. Aby wyjść wpisz '0: "))
    if user_input == 0:
        print("Dziękujemy za wizytę w kasynie!\nZapraszamy ponownie.")
        exit()
    elif 1 <= user_input <= len(games):
        choice = games.get(user_input)
        print(f"\nWybrałeś grę: {choice}.")
    else:
        print("\nWprowadzono nieprawidłowe dane!")



# Gra nr 1 - Ruletka

if choice == games.get(1):

    roulette = {0 : "green",
                32 : "red",
                15 : "black",
                19 : "red",
                4 : "black",
                21 : "red",
                2 : "black",
                25 : "red",
                17 : "black",
                34 : "red",
                6 : "black",
                27 : "red",
                13 : "black",
                36 : "red",
                11 : "black",
                30 : "red",
                8 : "black",
                23 : "red",
                10 : "black",
                5 : "red",
                24 : "black",
                16 : "red",
                33 : "black",
                1 : "red",
                20 : "black",
                14 : "red",
                31 : "black",
                9 : "red",
                22 : "black",
                18 : "red",
                29 : "black",
                7 : "red",
                28 : "black",
                12 : "red",
                35 : "black",
                3 : "red",
                26 : "black",
    }

    outside_bets = ["red_black", "even_odd, low_high", "dozens", "columns"]
    inside_bets = ["straight_up", "split", "street", "corner", "six_line"]

    print("Witaj w Ruletce!\nWybierz rodzaj zakładu:")






# Gra nr 2 - Poker

elif choice == games.get(2):
    print("Dostępne wkrótce")

# Gra nr 3 - Blackjack

else:
    print("Dostępne wkrótce")











